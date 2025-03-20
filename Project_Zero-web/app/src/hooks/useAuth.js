import { useState, useEffect } from 'react';
import { verifyToken, refreshToken } from '../utils/rqUtils.js';

const useAuth = () => {
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const checkAuth = async () => {
            let isValid = await verifyToken(); 
            if (!isValid) {
                isValid = await refreshToken();
                setIsAuthenticated(isValid);
            } 

            setIsAuthenticated(isValid);
            setLoading(false);
        };
        checkAuth();
    }, []);

    return { isAuthenticated, loading };
};

export default useAuth;