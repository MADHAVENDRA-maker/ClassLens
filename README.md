ClassLens

ClassLens is an AI-powered attendance management system that automates classroom attendance using facial recognition. Built with Streamlit, Python, and computer vision techniques, it provides an intuitive interface for teachers and students while eliminating the need for manual attendance.

Live Demo: https://classlens-mainsite.streamlit.app/

Features
AI-based facial recognition for attendance
Separate teacher and student portals
Student registration with facial embeddings
Automatic attendance marking
Attendance history and record management
Secure authentication
Supabase-backed cloud database
Responsive web interface built with Streamlit
Technology Stack

Frontend

Streamlit
HTML/CSS

Backend

Python

Machine Learning

dlib
face_recognition_models
scikit-learn
Support Vector Machine (SVM)

Database

Supabase

Libraries

OpenCV
NumPy
Pandas
Pillow
System Workflow
Register students through the teacher portal.
Capture and generate facial embeddings.
Train an SVM classifier using the stored embeddings.
Detect and recognize students during attendance.
Record attendance automatically in the database.
Installation

Clone the repository:

git clone https://github.com/<your-username>/ClassLens.git

Navigate to the project directory:

cd ClassLens

Install the required dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py
Author

Madhavendra Gautam

B.Tech, Indian Institute of Technology Jammu

Interested in Artificial Intelligence, Machine Learning, Computer Vision, and Data Science.
