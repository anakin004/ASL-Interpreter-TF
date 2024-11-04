import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import PasswordChecker from './PasswordChecker';
import VideoShowcase from './Showcase'; 

const App = () => {
    return (
        <Router>
            <div className="Start-container">
                <Routes>
                    <Route path="/" element={<PasswordChecker />} /> 
                    <Route path="/showcase" element={<VideoShowcase />} /> 
                </Routes>
            </div>
        </Router>
    );
};

export default App;
