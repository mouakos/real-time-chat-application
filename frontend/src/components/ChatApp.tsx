import React, { useEffect, useMemo, useRef, useState } from "react";

type Author = "me" | "system" | "other";
type ChatMessage = {
  id: string;
  text: string;
  author: Author;
  ts: number;
};

function genClientId() {
  const rnd = Math.random().toString(36).slice(2, 8);
  return `${Date.now().toString(36)}-${rnd}`;
}

function wsBaseUrl(): string {
  // Prefer env if provided, else fall back to localhost
  const fromEnv = import.meta.env.VITE_WS_URL as string | undefined;
  if (fromEnv) return fromEnv.replace(/\/$/, "");
  const scheme = window.location.protocol === "https:" ? "wss" : "ws";
  return `${scheme}://localhost:8000`;
}

export const ChatApp: React.FC = () => {
  const clientId = useMemo(() => genClientId(), []);
  const [connected, setConnected] = useState(false);
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState("");
  const wsRef = useRef<WebSocket | null>(null);
  const listRef = useRef<HTMLDivElement | null>(null);

  // Auto-scroll to bottom when messages change
  useEffect(() => {
    listRef.current?.scrollTo({ top: listRef.current.scrollHeight, behavior: "smooth" });
  }, [messages]);

  // Open WebSocket on mount
  useEffect(() => {
    const url = `${wsBaseUrl()}/ws/${encodeURIComponent(clientId)}`;
    const ws = new WebSocket(url);
    wsRef.current = ws;

    ws.onopen = () => {
      setConnected(true);
      setMessages((prev) => [
        ...prev,
        { id: crypto.randomUUID(), text: "✅ Connected to WebSocket", author: "system", ts: Date.now() },
      ]);
    };

    ws.onmessage = (event) => {
      const raw = String(event.data);
      const author: Author =
        raw.startsWith("You wrote:") ? "me" : raw.includes("left the chat") || raw.includes("joined") ? "system" : "other";

      setMessages((prev) => [
        ...prev,
        { id: crypto.randomUUID(), text: raw, author, ts: Date.now() },
      ]);
    };

    ws.onclose = () => {
      setConnected(false);
      setMessages((prev) => [
        ...prev,
        { id: crypto.randomUUID(), text: "⚠️ Disconnected", author: "system", ts: Date.now() },
      ]);
    };

    ws.onerror = () => {
      setMessages((prev) => [
        ...prev,
        { id: crypto.randomUUID(), text: "❌ WebSocket error", author: "system", ts: Date.now() },
      ]);
    };

    return () => {
      ws.close();
      wsRef.current = null;
    };
  }, [clientId]);

  const sendMessage = () => {
    const text = input.trim();
    if (!text || !wsRef.current || wsRef.current.readyState !== WebSocket.OPEN) return;
    wsRef.current.send(text);
    setInput("");
  };

  const handleKeyDown: React.KeyboardEventHandler<HTMLInputElement> = (e) => {
    if (e.key === "Enter") {
      e.preventDefault();
      sendMessage();
    }
  };

  const reconnect = () => {
    // Force close (if any) and re-run the effect by toggling a key.
    // Simple approach: if closed, effect on mount already tried. Here we create a new instance.
    if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN) return;
    // Recreate with a new effect by manually opening:
    const url = `${wsBaseUrl()}/ws/${encodeURIComponent(clientId)}`;
    const ws = new WebSocket(url);
    wsRef.current = ws;

    ws.onopen = () => {
      setConnected(true);
      setMessages((prev) => [
        ...prev,
        { id: crypto.randomUUID(), text: "🔁 Reconnected", author: "system", ts: Date.now() },
      ]);
    };
    ws.onmessage = (event) => {
      const raw = String(event.data);
      const author: Author =
        raw.startsWith("You wrote:") ? "me" : raw.includes("left the chat") || raw.includes("joined") ? "system" : "other";
      setMessages((prev) => [
        ...prev,
        { id: crypto.randomUUID(), text: raw, author, ts: Date.now() },
      ]);
    };
    ws.onclose = () => {
      setConnected(false);
      setMessages((prev) => [
        ...prev,
        { id: crypto.randomUUID(), text: "⚠️ Disconnected", author: "system", ts: Date.now() },
      ]);
    };
    ws.onerror = () => {
      setMessages((prev) => [
        ...prev,
        { id: crypto.randomUUID(), text: "❌ WebSocket error", author: "system", ts: Date.now() },
      ]);
    };
  };

  return (
    <div className="chat">
      <header className="chat__header">
        <div className="chat__status">
          <span className={`dot ${connected ? "dot--on" : "dot--off"}`} />
          <span>{connected ? "Connected" : "Disconnected"}</span>
        </div>
        <div className="chat__meta">
          <code className="badge">Client ID: {clientId}</code>
          {!connected && (
            <button className="btn" onClick={reconnect} aria-label="Reconnect">
              Reconnect
            </button>
          )}
        </div>
      </header>

      <div ref={listRef} className="chat__messages" role="log" aria-live="polite">
        {messages.map((m) => (
          <div
            key={m.id}
            className={`msg msg--${m.author}`}
            title={new Date(m.ts).toLocaleTimeString()}
          >
            {m.text}
          </div>
        ))}
      </div>

      <form
        className="chat__input"
        onSubmit={(e) => {
          e.preventDefault();
          sendMessage();
        }}
      >
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Type a message…"
          aria-label="Message"
          autoFocus
        />
        <button className="btn" type="submit" disabled={!connected || !input.trim()}>
          Send
        </button>
      </form>
    </div>
  );
};
