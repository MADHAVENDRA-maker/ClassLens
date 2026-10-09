# ClassLens — AI-Powered Attendance System

ClassLens is a facial recognition-based attendance system built with Python and Streamlit. It simplifies classroom attendance by identifying registered students and recording their attendance automatically, with separate portals for teachers and students.

**Live Demo:** https://classlens-mainsite.streamlit.app/

## Features

- Facial recognition for automated attendance
- Separate teacher and student portals
- Student registration and facial embedding generation
- SVM-based face classification
- Automatic attendance recording and history management
- Supabase integration for cloud-based data storage
- Simple, interactive web interface

## Tech Stack

- **Frontend:** Streamlit, HTML, CSS
- **Backend:** Python
- **Computer Vision:** OpenCV, dlib, face_recognition_models
- **Machine Learning:** scikit-learn, Support Vector Machine (SVM)
- **Database:** Supabase
- **Data Processing:** NumPy, Pandas, Pillow

## How It Works

1. Teachers register students through the application.
2. The system extracts facial embeddings from student images.
3. An SVM classifier is trained using the stored embeddings.
4. During attendance, the system identifies students from their faces.
5. Attendance records are saved to Supabase for future reference.

## Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/MADHAVENDRA-maker/ClassLens.git
cd ClassLens
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Run the application**

```bash
streamlit run app.py
```

## Author

**Madhavendra Gautam**  
Indian Institute of Technology Jammu
