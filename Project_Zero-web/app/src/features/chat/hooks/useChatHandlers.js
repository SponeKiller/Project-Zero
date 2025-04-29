import { useState, useCallback } from "react";

import { ChatService } from "../services/chatService"; 

export const useChatHandlers = () => {
    const [chatIds, setChatIds] = useState([]);           

    const loadChats = useCallback(async () => {
      const response = await ChatService.getAllChats();
      setChatIds(response.data.chats);
    }, []);
  
  
    const addChat = async () => {
      const response = await ChatService.createChat();
      setChatIds((prev) => [...prev, response.data.id]);
    };
  
    const deleteChat = async (delChatId) => {
      await ChatService.deleteChat(delChatId);
      setChatIds((prev) => prev.filter((chatId) => chatId !== delChatId));

    };
  
    return {
      chatIds,
      loadChats,
      addChat,
      deleteChat,
    };
  };
  