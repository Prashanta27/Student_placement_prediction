# Student_placement_prediction
Student Placement Prediction using Machine Learning  This project is a simple Machine Learning web application that predicts whether a student will be placed or not based on their CGPA.  The model is trained using a student placement dataset and deployed as an interactive web application using Streamlit.

🚀 Project Overview

The goal of this project is to build a machine learning model that can predict student placement status using academic performance data.
The trained model is integrated into a user-friendly web application where users can enter a student's CGPA and instantly receive a prediction.

🧠 Machine Learning Model

The classification model is built using Logistic Regression, a widely used algorithm for binary classification problems.
The model learns the relationship between:
Student CGPA and Placement Status (Placed / Not Placed)

📊 Dataset

The dataset used in this project contains student placement information including:

Feature ⏩	Description
CGPA ⏩	Student academic performance
Placement Status ⏩	Whether the student was placed or not

The dataset is used to train a classification model that predicts placement outcomes.

⚙️ Technologies Used

1.Python
2.Pandas
3.NumPy
4.Scikit-learn
5.Streamlit

🖥 Web Application Features

✔ Simple and interactive UI
✔ Real-time placement prediction
✔ Machine learning powered backend
✔ Lightweight and fast web application

Users simply enter a CGPA value and click Predict, and the model instantly returns the predicted placement status.


▶️ How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/Prashanta27/Student_placement_prediction
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Run the Streamlit app
streamlit run .\Student_Placement_streamlit.py --server.port 8080

After running the command, the web application will open in your browser.

📸 Application Demo

The user enters a student's CGPA and the model predicts whether the student is likely to be placed.

Example:

Input: CGPA = 7.5
Prediction: Result: Student Will Be Placed
🎯 Project Objective

This project demonstrates how machine learning models can be deployed as real-world applications, enabling users to interact with predictive models through a simple web interface.

📌 Future Improvements
1.Add more student features (skills, internships, projects)
2.Improve model accuracy
3.Deploy the application online
4.Add interactive data visualization

⭐ If you found this project helpful, please consider giving it a star!

⭐ If you found this project helpful, please consider giving it a star!
