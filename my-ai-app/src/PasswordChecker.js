import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './PasswordChecker.css'; 

const PasswordChecker = () => {
    const [password, setPassword] = useState('');
    const [showPassword, setShowPassword] = useState(false);
    const [isValid, setIsValid] = useState(null);
    const [errorMessage, setErrorMessage] = useState('');
    const navigate = useNavigate();

    const validatePassword = () => {
        const isValid = password.length <= 3; 

        setIsValid(isValid);
        setErrorMessage(isValid ? '' : 'Hint: Password is related to this project!');

        if (isValid) {
            navigate('/showcase'); 
        }
    };

    return (
        <div className="password-checker-container">
            <form className="password-form" onSubmit={(e) => { e.preventDefault(); validatePassword(); }}>
                <div className="input-group">
                    <input
                        type={showPassword ? 'text' : 'password'}
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        className="password-input"
                        placeholder="Enter your password"
                    />
                </div>
                <div className="checkbox-group">
                    <input
                        type="checkbox"
                        className="checkbox"
                        checked={showPassword}
                        onChange={() => setShowPassword(!showPassword)}
                    />
                    <label className="checkbox-label">Show password</label>
                </div>
                <button type="submit" className="submit-button">Check Password</button>
                {errorMessage && <div className="error-message">{errorMessage}</div>}
                {isValid === true && <div className="success-message">Password is valid!</div>}
                {isValid === false && <div className="error-message">Password is invalid!</div>}
            </form>
        </div>
    );
};

export default PasswordChecker;
