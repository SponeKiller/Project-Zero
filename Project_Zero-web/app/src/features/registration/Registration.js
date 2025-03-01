import React from "react";
import "./Registration.css";
import { useHandlers } from "./hooks/useHandlers";

const Registration = () => {
  const { formData, errorMessage, message, handleChange, handleSubmit } = useHandlers({
    username: '',
    email: '',
    phoneNumber: '',
    password: '',
  });



  return (
    <div className="registration-page">
      <div className="form-container">
        <form onSubmit={handleSubmit} className="registration-form">
          <h2>Register</h2>
          <div className="form-group">
            <label htmlFor="username">Username</label>
              <input
                type="text"
                id="username"
                name="username"
                value={formData.username}
                onChange={handleChange}
                placeholder="Enter your username"
                required
              />
          </div>
          <div className="form-group">
            <label htmlFor="email">Email</label>
            <input
              type="email"
              id="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              placeholder="Enter your email"
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="phoneNumber">Phone Number</label>
            <input
              type="phoneNumber"
              id="phoneNumber"
              name="phoneNumber"
              value={formData.phoneNumber}
              onChange={handleChange}
              placeholder="Enter your phone number"
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
              placeholder="Enter your password"
              required
            />
          </div>
          <button type="submit" className="submit-btn">Sign Up</button>
          {errorMessage && <p className="error-message">{errorMessage}</p>}
          {message && <p className="message">{message}</p>}
        </form>
      </div>
    </div>
  );
};

export default Registration;
