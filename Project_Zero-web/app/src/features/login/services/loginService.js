import api from '../../../services/api.js';

const loginUser = async (userData) => {
    const formData = new URLSearchParams();
    formData.append('username', userData.username);
    formData.append('password', userData.password);
    
    try {
        const response = await api.post('/token', formData, {
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        }); 
        return response.data;
    } catch (error) {
        throw error;
    }
};

export default loginUser;