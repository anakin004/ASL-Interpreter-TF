# ASL-Interpreter

Hey, thanks for checking out my repo!

This project is an **American Sign Language (ASL) Interpreter** that leverages machine learning using TensorFlow, Mediapipe, OpenCV and Numpy to detect and interpret ASL signs. The model has been trained on processed data and can make predictions using OpenCV.

## 🚀 Quick Start

### Downloading the Pre-trained Model
- The trained model file (`model.h5`) is available in this repository.
- Download it and place it in the appropriate directory as specified in the code (root directory)
- It is highly recommended to use a virtual environment to utilize the model, you can using venv ...

## 📊 Dataset Information

The ASL Interpreter model was trained with the following dataset structure:
- **60 videos per action**
- **30 frames per video**
- Each frame contains a NumPy array with the keypoints representing the action.

### Key Notes:
1. **Initial Dataset**:
   - Contained 30 videos per action.
   - Performance degraded when more signs were added to the model.

2. **Current Dataset**:
   - Expanded to 60 videos per action.
   - Improved robustness and required less training time.
   - Overall accuracy remained stable despite the larger dataset.
   - More signs to come ...

### Data Availability:
The processed dataset is intentionally excluded to encourage others to train their own models. If you're interested in obtaining the processed data for reference or further development, feel free to reach out!

### Installing Dependencies
1. Install the required dependencies:
  - I will make a requirements text file that you can run a bash script on

Here is a quick demo of the interpreter
-- just noticed on the 'yes' sign mediapipe had trouble detecting my hand which is why it gave alot of variance
-- going to fix soon with more signs included







https://github.com/user-attachments/assets/e23da4e3-3686-4338-ba54-c3058606c1f0






