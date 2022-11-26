# Device simulating the operation of a watch with additional functions using Raspberry Pi 3B+
The project combines the hardware implementation of the device using the motherboard and external devices and the software implementation created for it in Python using libraries
threading, cv2, mediapipe

### Developers
- Alyona Bushkina
- Svaykin Ilya
- Stolbov Svyatoslav

### Project
//TODO

![diagram (1)](https://user-images.githubusercontent.com/77066690/204109025-7471008a-0a2e-4d9a-8c22-44c97a398b85.jpg)

### Program

Three threads initially work in parallel in the program. One is responsible for viewing the commands entered, the second for executing the previous command, the third for the camera, which constantly scans the space for the presence of a human hand.

During operation, the program can create more threads, for example, a new thread is created to count down the alarm clock.

Commands in the program:
- help - output of model functionality
- exit - termination of the program
- alarm - setting an alarm
- timer - setting the timer
- clock - time display
- sw - setting the stopwatch

### Block diagram
//TODO

### Main libraries used
With the help of mediapipe and cv2 libraries, it is possible to stop functions using a hand movement.
- #### mediapipe
MediaPipe Hands is a highly accurate solution for tracking hands and fingers. It uses machine learning (ML) to deduce 21 three-dimensional hand landmarks from just one frame.

- #### cv2
OpenCV is a library for computer vision, used when reading images from a camera.

The time and datetime libraries implement working with time (read the current time, use the library functions to count seconds, return the date\time in the usual format, postpone the stream for a certain number of seconds, etc.)
- #### time and datetime
The time and datetime modules provide classes for processing time and date in different ways. The standard way of representing time is also supported, but more emphasis is placed on the ease of manipulating date, time and their parts.


Threading library for working with threads.
- #### threading
Threading is a standard module that comes with the interpreter. It was used to manipulate several threads and determine their behavior.

### Results
The finished model has the following functions:
- Watch
- Stopwatch
- Timer
- Alarm clock 

The operating mode is selected dynamically during the operation of the program, it is possible to stop the called signals using a hand movement recorded by the camera

<img width="573" alt="Model" src="https://user-images.githubusercontent.com/77066690/204108803-c2dfd9d7-72f0-4dc3-8288-27fc201ba913.png">

