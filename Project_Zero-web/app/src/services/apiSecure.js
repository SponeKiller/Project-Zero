import axios from 'axios';
import decamelizeKeys from 'decamelize-keys';
import camelizeKeys from 'camelcase-keys';

import { refreshToken } from '../utils/rqUtils.js';
import { logout } from '../utils/logout.js';

const apiSecure = axios.create({
  baseURL: process.env.REACT_APP_API_URL+process.env.REACT_APP_API_ROUTER,
});

// Request interceptor – přidání tokenu
apiSecure.interceptors.request.use((config) => {
  const token = sessionStorage.getItem('accessToken');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  const contentType = config.headers?.['Content-Type'];
  
  if (contentType === 'application/json' && typeof config.data === 'object') {
    config.data = decamelizeKeys(config.data, { separator: '_', deep: true });
  }
    
  return config;
});

apiSecure.interceptors.response.use(
  (response) => {
        const contentType = response.headers?.['Content-Type'];
      
        if (contentType === 'application/json' && typeof response.data === 'object') {
          response.data = camelizeKeys(response.data, { deep: true });
        }
      
        return response;
  },
  async (error) => {
    const originalRequest = error.config;

    
    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;

      try {
        const refreshResponse = await refreshToken(); 

        if (!refreshResponse) {
          logout();
          return Promise.reject(error);
        }

        const newToken = sessionStorage.getItem('accessToken');
        originalRequest.headers.Authorization = `Bearer ${newToken}`;

        const response = await apiSecure(originalRequest);
        
        const contentType = response.headers?.['Content-Type'];
            
        if (contentType === 'application/json' && typeof response.data === 'object') {
          response.data = camelizeKeys(response.data, { deep: true });
        }

        return response;
      } catch {
        if (error.response?.status === 401) {
          logout();
        }
        
        return Promise.reject(error);
      }
    }

    if (error.response?.status === 401) {
      logout();
    }

    return Promise.reject(error);
  }
);

export default apiSecure;
