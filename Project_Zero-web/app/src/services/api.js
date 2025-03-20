import axios from 'axios';



const api = axios.create({
    baseURL: process.env.REACT_APP_API_URL+process.env.REACT_APP_API_ROUTER,
    withCredentials: true,
    headers: {
        'Content-Type': 'application/json',
    }
    
});


api.interceptors.response.use(
    (response) => response,
    (error) => {
        console.error('API error:', error);
        return Promise.reject(error);
    }
);

export default api;
