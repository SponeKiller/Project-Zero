import axios from 'axios';
import decamelizeKeys from 'decamelize-keys';
import camelizeKeys from 'camelcase-keys';



const api = axios.create({
    baseURL: process.env.REACT_APP_API_URL+process.env.REACT_APP_API_ROUTER,
    withCredentials: true,
    headers: {
        'Content-Type': 'application/json',
    }
    
});

api.interceptors.request.use(config => {
  const contentType = config.headers?.['Content-Type'];
  if (contentType === 'application/json' && typeof config.data === 'object') {
    config.data = decamelizeKeys(config.data, { separator: '_', deep: true });
  }

  return config;
});


api.interceptors.response.use(
    (response) => {
      const contentType = response.headers?.['Content-Type'];
    
      if (contentType === 'application/json' && typeof response.data === 'object') {
        response.data = camelizeKeys(response.data, { deep: true });
      }
    
      return response;
    },
    (error) => {
        return Promise.reject(error);
    }
);

export default api;
