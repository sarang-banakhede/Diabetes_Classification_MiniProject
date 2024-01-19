------------------------------------------------------------ MINI PROJECT ---------------------------------------------------------------
# Diabetes Prediction Model

This repository contains a classification model that predicts whether a female patient has diabetes based on diagnostic measurements.
The dataset used for training and evaluating the model is originally from the National Institute of Diabetes and Digestive and Kidney Diseases. 
The objective of the model is to assist in early diabetes detection and provide valuable insights to healthcare professionals.

## Dataset

The dataset consists of several diagnostic measurements for each patient:

1. **Pregnancies**: Number of times pregnant
2. **Glucose**: Plasma glucose concentration 2 hours after an oral glucose tolerance test
3. **BloodPressure**: Diastolic blood pressure (mm Hg)
4. **SkinThickness**: Triceps skin fold thickness (mm)
5. **Insulin**: 2-Hour serum insulin (mu U/ml)
6. **BMI**: Body mass index (weight in kg / (height in m)^2)
7. **DiabetesPedigreeFunction**: Diabetes pedigree function
8. **Age**: Age in years
9. **Outcome**: Class variable (0 indicates no diabetes, 1 indicates diabetes)

## Model Selection

Initially, several machine learning algorithms were evaluated for a classification problem aimed at diabetes prediction. The algorithms considered included logistic regression, decision tree, naive Bayes, and Support Vector Machine (SVM). Following a comprehensive assessment, the SVM algorithm exhibited the highest accuracy and recall rates. Thus, the SVM model was selected for deployment.
However, subsequent model refinement was conducted by implementing a bagging technique with the Gaussian Naive Bayes (GaussianNB) estimator. This decision was made after observing improved recall and accuracy metrics compared to the original SVM model. Consequently, the updated model choice was to employ the bagged GaussianNB model for the diabetes prediction task.

## Deployment

The chosen SVM model has been deployed using Flask, a micro web framework for Python. 
Flask provides a simple and efficient way to create a web application to interact with the prediction model. 
The deployed application allows users to input diagnostic measurements and receive predictions regarding the likelihood of diabetes.

## Getting Started

To run the deployed application locally:

1. Clone this repository to your local machine.
2. Navigate to the project directory and set up a virtual environment.
3. Install the required dependencies.
4. Run the Flask application:
5. Access the application in your web browser at `http://127.0.0.1:5000`.

## Contribution

If you would like to contribute to this project, you can:

- Improve the model's performance by experimenting with hyperparameters.
- Expand the dataset or implement data augmentation techniques.
- Enhance the user interface of the Flask application.
- Refactor and optimize the codebase for better maintainability.

Feel free to fork this repository, make changes, and submit pull requests.
