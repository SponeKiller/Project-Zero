export const handleApiCall = async (fn) => {
    try {
      const response = await fn();
      return response;
    } catch (error) {
      throw error;
    }
};