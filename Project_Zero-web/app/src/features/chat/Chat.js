
import { useState } from "react";
import { FiRotateCcw } from 'react-icons/fi';

import { useMessageHandlers } from "./hooks/useMessageHandlers.js";
import { Sidebar } from "./components/js/Sidebar.js";
import "./Chat.css";

export default function ChatApp() {

  const [selectedChatId, setSelectedChatId] = useState(null);
  const { messages, userMessage, handleChange, handleSubmit, getMessages, regenMessage } = 
  useMessageHandlers(
    [
      {
        role: "system",
        content: "You are a helpful assistant."
      },
      {
        role: "user",
        content: ""
      }
    ]
  )

  const chat = Array.isArray(messages)
    ? messages.filter(msg => msg.role === 'user' || msg.role === 'assistant')
    : [];

  return (
    <div className="chat-container">
      <Sidebar 
        onSelectChat={ getMessages }
        setSelectedChatId={ setSelectedChatId } 
        selectedChatId={ selectedChatId } 
      />
      {selectedChatId !== null && ( 
        <div className="chat-wrapper">
          <div className="chat-messages">
          {chat.map((msg, i) => {
            const isLastAssistant =
            msg.role === 'assistant' && i === chat.length - 1;

            return (
              <div key={i} className={`message-wrapper ${msg.role}`}>
                <div className={`message ${msg.role}`}>
                  {msg.content}
                  {isLastAssistant && (
                    <button
                      className="reload-button"
                      onClick={(e) => regenMessage(e, selectedChatId)}
                      aria-label="Reload assistant response"
                    >
                      <FiRotateCcw size={16} />
                    </button>
                  )}
                </div>
              </div>
            );
          })}            
          <div className="input-container">
            <input
              value={userMessage[1].content}
              onChange={handleChange}
              placeholder="Napiš zprávu..."
              onKeyDown={(e) => e.key === "Enter" && handleSubmit(e, selectedChatId, userMessage)}
            />
            <button onClick={(e) => handleSubmit(e, selectedChatId, userMessage)}>📩</button>
          </div>
        </div>
      </div>
      )}
    </div>
  );
}
