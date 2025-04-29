import { useState } from 'react';
import { MessageService } from '../services/messageService.js';


export const useMessageHandlers = (initialValues) => {
    const [userMessage, setUserMessage] = useState(initialValues);
    const [regenUsrMessage, setRegenUsrMessage] = useState(initialValues);
    const [messages, setMessages] = useState([]);
    const [errorMessage, setErrorMessage] = useState('');

    const handleChange = (e) => {
        const newContent = e.target.value;
        setUserMessage((prev) =>
            prev.map((msg) =>
                msg.role === "user" ? { ...msg, content: newContent } : msg
            )
        );
    };

    const getMessages = async (id) => {
        const response = await MessageService.getMessages(id);
        setMessages(response.data.messages);
    };

    const handleSubmit = async (e, selectedChatId, message, regenerate) => {
        e.preventDefault();

        try {
            const response = await MessageService.sendMessage(selectedChatId, message);

            if (regenerate) {
                setMessages(prev => {
                    const msgs = response.data.messages;
                    const lastMsg = msgs[msgs.length - 1];
                    if (!lastMsg) return prev;
                    return [...prev, lastMsg];
                });
                  
            } else {
                setMessages((prev) => [...prev, ...response.data.messages]);
                setUserMessage(initialValues);
                setErrorMessage('');
            }
            
            
            
        } catch (error) {
            const status = error?.response?.status ?? 0;
            let errorMessage = 'Something went wrong';

            if (status === 500) errorMessage = "Server error, try again later";

            setErrorMessage(errorMessage);
        }
    };

    const regenMessage = async (e, selectedChatId) => {
        const messageId = 
            messages.findLast(msg => msg.role === 'assistant')?.id ?? '';

        const response = await MessageService.deleteMessage(selectedChatId, messageId)

        if (response.status === 204) {
            // Delete previous assistant message
            setMessages(prevMessages =>
                prevMessages.filter(msg => msg.id !== messageId)
            );

            const lastUserContent = 
                messages.findLast(msg => msg.role === 'user')?.content ?? '';
            setRegenUsrMessage(prev =>
                prev.map(msg =>
                  msg.role === 'user'
                    ? { ...msg, content: lastUserContent }
                    : msg
                )
            );
            handleSubmit(e, selectedChatId, regenUsrMessage, true);
        }
    }



    return { userMessage, messages, errorMessage, handleChange, handleSubmit, getMessages, regenMessage };
};