# ASL-Interpreter

Hey thanks for checking our my repo!

Since this model is already trained on data, you can download the trained.h5 model and using opencv, you can make predictions using opencv all you need to do is make sure you utilize the mediapipe_detection so that mediapipe can make detection on keypoints, drawing them isn't necesary but it is cool ...

-~ also, I would recommend utilizing the prob_viz function to visualize the models output extract the keypoints from the image, and MAKE SURE --- !! if a any landmark we are detecting goes out of scope that its represented by a npy of zeros !! then, using predict with the model and running argmax you ge tthe prediction a little additional optimization is that when we transition between different signs we dont want to say that we are detection a specific sign so we only predict when the sign currently predicted is the same sign as 10 predictions ago, again each prediciton is happening per frame

-= note , I trained my model on limited data, essentially this was the structure of my data

## Description of Directories

- The `Data/` directory contains three folders: `hello/`, `thanks/`, and `iloveyou/`.
- Each of these folders has subdirectories named from `0` to `29`, representing 30 videos.
- Inside each video directory, there are 30 `.npy` files named from `0.npy` to `29.npy`.

If you want the data that I processed let me know


We have 3 signs we are detecting, I am working on training the model on aditional data to add more signs, but just takes time
We have 3 actions, that have 30 sequences/videos , each video have 30 frames, each frame have a nmpy array with the keypoints of the action
This really not a large ammount of data, and this model could be improved, but for effiency and timesake --- it works :)

-- have fun!

Here is a quick demo of the interpreter
 - I make a prediction by parsing 30 frames at a time so it fits the model





https://github.com/user-attachments/assets/f0c8776e-4398-4460-b95e-96e048fadfdf




