import api from '../services/api.js';

export const toSnakeCase = (data) => {
    // Transforming indexes from camelCase to snake_case
    if (Array.isArray(data)) {
      return data.map(toSnakeCase);
    } else if (typeof data === "object" && data !== null) {
      return Object.fromEntries(
        Object.entries(data).map(([key, value]) => [
          key.replace(/([A-Z])/g, "_$1").toLowerCase(),
          toSnakeCase(value),
        ])
      );
    }
    return data;
  };

export const verifyToken = async () => {

    const token = sessionStorage.getItem('accessToken');

    if (!token) return false;

    try {
      await api.get('/token/me',{
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      
      return true
  } catch (error) {
      return false;
  }
};

export const refreshToken = async () => {
  const refreshToken = localStorage.getItem('refreshToken');
  if (!refreshToken) return null;

  try {
      const response = await api.post('/token/refresh-token', { refresh_token: refreshToken });

      sessionStorage.setItem('accessToken', response.data.access_token);

      return true;
  } catch (error) {
      return false;
  }
};