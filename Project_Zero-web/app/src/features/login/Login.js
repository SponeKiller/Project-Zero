import React from 'react';
import './Login.css';
import { useHandlers } from "./hooks/useHandlers";
import DashboardLoader from '../../components/routes/DashboardLoader.js';
const Login = () => {
  const { formData, errorMessage, message, verified, handleChange, handleSubmit } = useHandlers({
    username: '',
    password: '',
    errorMessage: '',
    message: '',
    verified: false
  });

    return (     
        <div className="login-page">
        {verified && <DashboardLoader />}
        <form onSubmit={handleSubmit} className="form-container">
            <h2>Login</h2>
            <div className="form-group">
                <label htmlFor="username">E-mail</label>
                <input 
                    type="text" 
                    id="username" 
                    name="username"
                    value={formData.username}
                    onChange={handleChange}
                    placeholder='Enter your e-mail' 
                    required 
                />
            </div>
            <div className="form-group">
                <label htmlFor="password">Password</label>
                <input
                    type="password" 
                    id="password" 
                    name="password"
                    value={formData.password}
                    onChange={handleChange}
                    placeholder='Enter your password' 
                    required />
            </div>
            <button type="submit" className="submit-btn">Login</button>
            {message && <p className="message">{message}</p>}
            {errorMessage && <p className="error-message">{errorMessage}</p>}
        </form>
    </div>
    );
};

export default Login;
