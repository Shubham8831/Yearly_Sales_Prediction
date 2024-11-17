# Regression-Based Machine Learning Model for Predicting Yearly Amount Spent

This project is a regression-based machine learning model designed to predict the **yearly amount spent by a user** based on their average session length, time spent on the app, and membership length. The project leverages data preprocessing, machine learning algorithms, and a Streamlit web app for user interaction.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Directory Structure](#directory-structure)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Technologies Used](#technologies-used)
6. [Future Enhancements](#future-enhancements)
7. [License](#license)

---

## Project Overview

E-commerce businesses can benefit significantly from insights into user spending patterns. This project uses a regression model to predict **yearly customer spending**. The model is built using Python and integrated into a Streamlit application for an interactive user experience.  

The dataset includes:
- **Average Session Length**
- **Time Spent on App**
- **Length of Membership**  
Using these features, the model predicts the **Yearly Amount Spent**.

---

## Directory Structure

├── Ecommerce Customers.csv # Dataset used for model training and testing 
├── Notebook.ipynb # Jupyter notebook for data analysis and model development 
├── README.md # Project documentation 
├── app.py # Streamlit app for user interaction 
├── model.pkl # Trained regression model 
├── scaler.pkl # Scaler used for feature normalization 
├── requirements.txt # List of required libraries for the project



---

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/shubham8831/Yearly_Sales_Prediction.git
   cd project-name
   
2. **Set Up Virtual Environment**

  bash
    python -m venv env
    source env/bin/activate   # On Windows: env\Scripts\activate

3. **Install Dependencies**
  bash
    pip install -r requirements.txt

4. **Run the App**
   bash
    streamlit run app.py

   
## Usage
Open the Streamlit app in your browser after running the above command.
Input values for:
  Average Session Length
  Time on App
  Length of Membership
  The app will predict the Yearly Amount Spent based on the input values.
  
## Technologies Used
  Python: Core programming language.
  Pandas, Numpy: Data manipulation and analysis.
  Scikit-learn: Model training and evaluation.
  Streamlit: Web application framework for deployment.
  Matplotlib, Seaborn: Data visualization in Jupyter notebook.

## Future Enhancements
  Add more features to improve model accuracy.
  Experiment with other regression techniques (e.g., Ridge, Lasso, or Polynomial Regression).
  Enhance the Streamlit app UI for better user experience.
  
## Author
Shubham
Passionate about leveraging data science and machine learning to solve real-world problems.



