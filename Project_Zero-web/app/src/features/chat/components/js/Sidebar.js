import { FiPlusCircle, FiTrash2, FiHome } from "react-icons/fi";
import { useEffect } from "react";

import { useChatHandlers } from "../../hooks/useChatHandlers";

import "../css/Sidebar.css";

export const Sidebar = ({ onSelectChat, setSelectedChatId, selectedChatId }) => {
  const { chatIds, addChat, loadChats, deleteChat } = useChatHandlers();

  useEffect(() => {
    const load = async () => {
      await loadChats();
    };
    load();
  }, [loadChats]);

  return (
    <aside className="chat-sidebar">
      <div className="sidebar-header">
        <h2>Chats</h2>
        <button className="add-chat-button" onClick={addChat}>
          <FiPlusCircle size={20} />
        </button>
      </div>
      <div className="sidebar-content">
        <ul>
          {chatIds.map((id, index) => (
            <li 
              key={id} 
              className="chat-item"
              onClick={() => {
                onSelectChat(id);
                setSelectedChatId(id);
              }}
            >
              <span>Chat {index + 1}</span>
              <button 
                className="delete-chat-button" 
                onClick={(e) => {
                  e.stopPropagation();
                  if (id === selectedChatId) {
                    setSelectedChatId(null);
                  }
                  deleteChat(id);
                }}
              >
                <FiTrash2 size={16} />
              </button>
            </li>
          ))}
        </ul>
      </div>
      <div className="sidebar-footer">
        <button onClick={() => window.location.href = "/dashboard"}>
          <FiHome size={20} style={{ marginRight: "8px" }} />
          Dashboard
        </button>
      </div>
    </aside>
  );
};
