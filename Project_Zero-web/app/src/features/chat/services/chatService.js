import apiSecure from '../../../services/apiSecure.js';
import { handleApiCall } from '../../../utils/handleApiCall.js';

export class ChatService {
   
    static async getAllChats() {
        return await handleApiCall(() =>
            apiSecure.get('/chats')
        );
    }
  
    static async createChat() {
        return await handleApiCall(() =>
            apiSecure.post('/chats')
        );
    }
  
    static async deleteChat(chatId) {
        return await handleApiCall(() =>
            apiSecure.delete(`/chats/${chatId}`)
        );
    }
}