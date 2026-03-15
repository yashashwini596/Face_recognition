Face Recognition System

##  Project Overview

This project implements a simple **Face Recognition System** using Python and computer vision techniques. The system compares a test image with images stored in a dataset and identifies the most similar face.

The project demonstrates the basic workflow of face recognition including **image preprocessing, feature extraction, and identity matching**.

---

##  Technologies Used

* Python
* OpenCV
* NumPy

---

## Project Structure

```
Face_recognition
│
├── dataset/                # Contains images of different persons
│
├── src/
│   └── face_recognition.py # Feature extraction and face comparison logic
│
├── app.py                  # Main program to run the recognition system
├── test.jpg                # Test image used for recognition
├── requirements.txt        # Project dependencies
└── README.md
```

---

##  How the System Works

1. The system loads a **test image**.
2. Each image is **resized and converted into feature vectors**.
3. The system compares the test image with dataset images.
4. The **most similar face** is identified using similarity comparison.

---

##  How to Run the Project

### 1️. Install dependencies

```
pip install -r requirements.txt
```

### 2️. Run the application

```
python app.py
```

### 3️. Output

The program will display the **recognized person's name** in the terminal.

---

##  Future Improvements

* Real-time face recognition using webcam
* Deep learning based face embeddings
* Larger dataset support
* Improved face detection accuracy

---

##  Learning Outcome

This project helped in understanding:

* Image processing using OpenCV
* Feature extraction techniques
* Similarity-based recognition systems
* Basic computer vision pipeline
