# ASL-Interpreter

Hey thanks for checking our my repo!

Since this model is already trained on data, you can download model.h5 and make predictions using opencv. 

If you want the data that I processed let me know, I wanted to leave it out so if anyone wants train their own model with new data they can, and additionally because the model is already trained so the data is not too important for the scope of this project.


I detected 6 signs but can work for more, I am working on training the model on aditional data to add more signs, but just takes time
I have 6 actions, previous had 3, that have 30 sequences/ 60 videos , each video have 30 frames, each frame have a nmpy array with the keypoints of the action

-- I previously had 30 videos and 30 frames per video, but the model did not perform well when I added more signs, however with more data the model's accuracy did not undergo noticable change,
  and I had to go through less training to achieve similar accuracy, I now have 60 videos per action, with 30 frames each

-+~ one more note, the versions of the dependencies can go out of scope, so if any issues arrise downloading them, pip should be able to tell you which versions are invalid/incompatible

-- have fun!

Here is a quick demo of the interpreter
-- just noticed on the 'yes' sign mediapipe had trouble detecting my hand which is why it gave alot of variance
-- going to fix soon with more signs included







https://github.com/user-attachments/assets/e23da4e3-3686-4338-ba54-c3058606c1f0






