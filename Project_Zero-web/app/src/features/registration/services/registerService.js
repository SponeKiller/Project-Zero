import api from '../../../services/api.js';

const registerUser = async (userData) => {
    try {
        const response = await api.post('/users', userData); 
        return response.data;
    } catch (error) {
        console.error('Registration failed:', error);
        throw error;
    }
};

export default registerUser;