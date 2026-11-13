# Student Performance Prediction Using Machine Learning

## Project Overview
The Student Performance Prediction System is a Machine Learning-based web application that predicts students' final academic grades using personal, family, academic, and lifestyle-related information.

The application uses a trained Linear Regression model and provides an interactive interface built with Streamlit.

## Objectives
- Analyze factors related to student academic performance.
- Perform Exploratory Data Analysis (EDA).
- Train and evaluate Machine Learning models.
- Predict students' final grades.
- Build an interactive web application using Streamlit.

## Dataset
- **Dataset:** UCI Student Performance Dataset
- **File:** `student-mat.csv`
- **Target Variable:** `G3` (Final Grade)
- **Records:** 395 students
- **Features:** 30 input features

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib
- Jupyter Notebook
- Git & GitHub

## Machine Learning Models
The following models were evaluated:
1. Linear Regression
2. Decision Tree Regressor

**Selected Model:** Linear Regression

## Model Evaluation
The Linear Regression model achieved:

- MAE: 3.395
- RMSE: 4.196
- R² Score: 0.141

## Project Structure
- `Student_Performance_Prediction.ipynb` – Data analysis and model training
- `app.py` – Streamlit web application
- `student-mat.csv` – Dataset
- `best_model.pkl` – Trained ML model
- `preprocessor.pkl` – Data preprocessing object
- `Project_Screenshots/` – Application screenshots

## How to Run the Project

1. Clone the repository:
   `git clone https://github.com/Seniha27/Student-Performance-Prediction.git`

2. Open the project folder.

3. Install the required libraries:
   `pip install pandas numpy matplotlib seaborn scikit-learn streamlit joblib`

4. Run the application:
   `python -m streamlit run app.py`

## Project Screenshots
Screenshots of the application are available in the `Project_Screenshots` folder.

## Future Improvements
- Improve model performance.
- Explore additional Machine Learning algorithms.
- Deploy the application using AWS.

## Author
**Seniha S.**

GitHub: [Seniha27](https://github.com/Seniha27)
