# ASL-Interpreter

Hey thanks for checking our my repo!

Since this model is already trained on data, you can download the trained.h5 model and using opencv, you can make predictions using opencv all you need to do is make sure you utilize the mediapipe_detection so that mediapipe can make detection on keypoints, drawing them isn't necesary but it is cool ...

-~ also, I would recommend utilizing the visualization function to see the models output extract the keypoints from the image

note --- if a any landmark we are detecting goes out of scope that its represented by a npy of zeros, this is needed for consistency in how the model recieves data and makes predictions

~= then, using predict with the model and running argmax you get the prediction. A little additional optimization is that when we transition between different signs we dont want to say that we are detection a specific sign so we only predict when the sign currently predicted is the same sign as 10 predictions ago, again each prediciton is happening per 30 frames

-=  here is the structure of data if you want to tweak the model

## Description of Directories

- The `Data/` directory contains three folders: `hello/`, `thanks/`, and `iloveyou/`.
- Each of these folders has subdirectories named from `0` to `29`, representing 30 videos.
- Inside each video directory, there are 30 `.npy` files named from `0.npy` to `29.npy`.

If you want the data that I processed let me know, I wanted to leave it out so if anyone wants train their own model with new data they can, and additionally because the model is already trained so the data is not too important for the scope of this project.


I detected three signs but can work for more, I am working on training the model on aditional data to add more signs, but just takes time
We have 3 actions, that have 30 sequences/videos , each video have 30 frames, each frame have a nmpy array with the keypoints of the action
This really not a large ammount of data, and this model could be improved, but for effiency and timesake --- it works :)

-+~ one more note, the versions of the dependencies can go out of scope, so if any issues arrise downloading them, pip should be able to tell you which versions are invalid/incompatible

-- have fun!

Here is a quick demo of the interpreter





https://github.com/user-attachments/assets/27ee7ce0-ef49-4d6b-a139-fdcc8c723d16








