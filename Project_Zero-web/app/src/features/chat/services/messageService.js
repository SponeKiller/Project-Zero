import apiSecure from '../../../services/apiSecure.js';
import { handleApiCall } from '../../../utils/handleApiCall.js';


export class MessageService {

    static async sendMessage(chat_id, messages) {
        return await handleApiCall(() =>
            apiSecure.post(`/chats/${chat_id}/messages`, {
                messages: messages
            }, {
                headers: {
                    'Content-Type': 'application/json'
                }
            })
        );
    }

    static async getMessages(chat_id) {
        return await handleApiCall(() =>
            apiSecure.get(`/chats/${chat_id}/messages`)
        );
    }
    
    static async deleteMessage(chat_id, message_ids) {
        return await handleApiCall(() =>
            apiSecure.delete(`/chats/${chat_id}/messages/${message_ids}`)
        );
    }
}
