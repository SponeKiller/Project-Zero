import "./Dashboard.css";
import React, { useState } from 'react';

const Dashboard = () => {
    const [isMenuOpen, setIsMenuOpen] = useState(false);

    const toggleMenu = () => setIsMenuOpen(!isMenuOpen);
    const logout = () => {
        console.log('User logged out');
        // Přidej zde logiku pro odhlášení
    };

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
                            <li>User Profile</li>
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
    </div>
    );
};

export default Dashboard;