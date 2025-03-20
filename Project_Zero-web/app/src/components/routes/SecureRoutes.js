import { Navigate } from 'react-router-dom';

import useAuth from '../../hooks/useAuth.js';

function SecureRoute({ children }) {
    const { isAuthenticated, loading } = useAuth();

    
    if (!loading && !isAuthenticated) {
        return <Navigate to="/login" />;  
    }


    return children; 
}

export default SecureRoute;