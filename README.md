# CoreML_Keras
Creating ML powered iOS application - live capture digit recognizer (for AR sudoku solver)

This is a cross platform implementation of a live-capture digit recognizer. Deployed on iOS devices, thus built in Swift (XCode). The model is built in Python, it is a Convolutional Neural Network trained on the MNIST dataset of 60,000 handwritten digits. The model's accuracy is approximately 99%.

Firstly, the model is built with Keras in Python. The model is then saved in h5 format and converted to a CoreML model, ie '.mlmodel', for seamless implementation in Swift.
Lastly, in Swift, we create a video capture application that can dynamically detect the digit and predict its value, from our 10 output classes of 0 to 9.
