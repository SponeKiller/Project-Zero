import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

import { logout } from '../../utils/logout.js';

import "./Dashboard.css";

const Dashboard = () => {
    const [isMenuOpen, setIsMenuOpen] = useState(false);
    const navigate = useNavigate();

    const toggleMenu = () => setIsMenuOpen(!isMenuOpen);

    return (
        <div className="dashboard-page">
        <header className="dashboard-header">
            <h1>Dashboard</h1>
            <div className="user-menu">
                <div className="user-icon" onClick={toggleMenu}>
                    👤
                </div>
                {isMenuOpen && (
                    <div className="dropdown-menu">
                        <ul>
                            <li onClick={logout}>Logout</li>
                        </ul>
                    </div>
                )}
            </div>
        </header>
        <main className="dashboard-content">
            <section className="dashboard-widgets">
                <div className="widget">
                    <h2>Welcome Back!</h2>
                    <p>Here's a quick overview of your account.</p>
                </div>
                <div className="widget">
                    <h2>Recent Activity</h2>
                    <p>No recent activity.</p>
                </div>
                <div className="widget">
                    <h2>Statistics</h2>
                    <p>Your stats will appear here.</p>
                </div>
            </section>
        </main>

        <div className="start-chat">
            <button className="chat-button" onClick={() => navigate('/chat')}>
                Go to Chat
            </button>  
        </div> 
    </div>
    );
};

export default Dashboard;