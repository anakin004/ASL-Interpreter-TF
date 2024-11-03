# ASL-Interpreter

Hey thanks for checking our my repo!

I did not feel comfortable putting all of the videos from my React front-end if requested I can show it! Same for the collected frame data, I decided not to publish it here, but the model is available if you want to download it

Sine this model is already trained on data, you can download the trained.h5 model and using opencv, you can make predictions using opencv all you need to do is make sure you utilize the mediapipe_detection so that mediapipe can make detection on keypoints, drawing them isn't necesary but it is cool ...

-~ also, I would recommend utilizing the prob_viz function to visualize the models output extract the keypoints from the image, and MAKE SURE --- !! if a hand goes out of frame that its a npy of zeros !! then, using predict with the model and running argmax you ge tthe prediction a little additional optimization is that when we transition between different signs we dont want to say that we are detection a specific sign so we only predict when the sign currently predicted is the same sign as 10 predictions ago, again each prediciton is happening per frame

-- have fun!!!!!!!

Here is a quick demo of the interpreter

https://github.com/user-attachments/assets/0a1989d9-5c38-45a5-9054-a55d27f5c4cd

