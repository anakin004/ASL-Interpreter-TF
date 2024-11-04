import React, { useState, useEffect } from 'react';
import './Showcase.css';

const VideoShowcase = () => {
    const [currentVideo, setCurrentVideo] = useState(null);
    const [isTextVisible, setIsTextVisible] = useState(false);
    const [isDescriptionVisible, setIsDescriptionVisible] = useState(false);
    const [fadeClass, setFadeClass] = useState('');

    const videos = {
        hello: '/videos/hello.mp4',
        thanks: '/videos/thanks.mp4',
        iloveyou: '/videos/love.mp4',
    };

    const handleVideoClick = (videoKey) => {
        setCurrentVideo(videos[videoKey]);
    };

    useEffect(() => {
        const timer = setTimeout(() => {
            setIsTextVisible(true);
        }, 1000);

        return () => clearTimeout(timer);
    }, []);

    const toggleDescription = () => {
        setFadeClass('fade-out');

        setTimeout(() => {
            setIsDescriptionVisible(!isDescriptionVisible);
            setFadeClass('');
        }, 500);
    };

    return (
        <div className="video-showcase">
            <div className="menu-icon" onClick={toggleDescription}>
                <div className="line"></div>
                <div className="line"></div>
                <div className="line"></div>
            </div>

            {isDescriptionVisible ? (
                <div className={`description ${fadeClass}`}>
                    <div className={`description-text ${isTextVisible ? 'fade-in' : ''}`}>
                    <div className={`description-text ${isTextVisible ? 'fade-in' : ''}`}>
                    This project is a demo of an ASL interpreter, <br />
                    I used TensorFlow-CPU because my GPU is not supported. <br />
                    Any questions/recommendations on improvements are appreciated! <br />
                    <br />
                     - - Click again on the hamburger menu to go back - -
                    </div>

                    </div>
                </div>
            ) : (
                <>
                    <div className={`video-buttons ${fadeClass}`}>
                        <button onClick={() => handleVideoClick('hello')}>Hello</button>
                        <button onClick={() => handleVideoClick('thanks')}>Thanks</button>
                        <button onClick={() => handleVideoClick('iloveyou')}>I Love You</button>
                    </div>

                    {currentVideo && (
                        <div className={`video-container ${fadeClass}`}>
                            <video 
                                src={currentVideo} 
                                controls 
                                autoPlay 
                                style={{ width: '100%', maxHeight: '400px' }} 
                            />
                        </div>
                    )}
                </>
            )}
        </div>
    );
};

export default VideoShowcase;
