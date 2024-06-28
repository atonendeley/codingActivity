# Table Of Contents
# Overview 

## [Data Description](Data_Description/Data_Description.md)

## [Exploratory Data Analysis](Exploratory_Data_Analysis/Exploratory_Data_Analysis.md)

## [Summary Performance of the Model](Models/Models.md)

## [Conclusion](Conclusion/Conclusion.md)

### HOTEL BOOKING CANCELLATION 

### This project is based on Predicting the cancellation of hotel booking?

### Introduction
The rate of cancellation for bookings in the hospitality industry is quite alarming as it is high in the competitive market offering no deposit for bookings. Once the booking has been cancelled, there is almost nothing the hotel can do. This kind of setting creates issues and monetary losses for many hotels and creates a demand to take prior precautions for high number of cancellations. Therefore, predicting bookings that can be cancelled and preventing these cancellations will create value for the hospitality industry. This project aims to ascertain how future cancelled hotel bookings can be predicted in advance with the help of machine learning methods. Includimg the measures and steps that can be implemented to reduce their impact on the industry’s revenue.

### Project Objectives
The aim of the project is to predict whether a booking made in a hotel can be cancelled in future or not. Machine models have been developed for this to help identify and flag bookings with probability of high cancellation rates by analysing the trends and features associated with it. To prevent the resulting income losses, hotels can take action on these bookings. With the aid of this form of prediction, hotels can adopt better net demand projections, better overbooking/cancellation policies, and more forceful pricing and inventory allocation tactics. Additionally, hotels can use this technique to determine which of their regular clients never cancel their reservations and are eligible for loyalty rewards.

### The process involved in dealing with the data involves the following steps with details shown in other sections.
* 1. Import Libraries 
* 2. Import the data
* 3. Preprocess the data
* 4. Split the data into training and test sets.
* 5. Fit the models and evaluate performance
* 
### Steps to create a hotel booking cancellation prediction model using logistic regression and decision tree:

* Import necessary libraries like pandas, numpy, seaborn, matplotlib, scikit-learn, etc.

* Load the dataset into a pandas dataframe.

* Perform exploratory data analysis (EDA) to understand the data and identify any data quality issues like missing values, outliers, or inconsistent data.

* Perform data pre-processing, which may include feature selection, feature engineering, data cleaning, data transformation, and data normalization.

* Split the dataset into training and testing sets.

* Build a logistic regression model to predict whether a booking will be canceled or not. Use scikit-learn's LogisticRegression function to create the model.

* Evaluate the model's performance on the testing set using metrics like accuracy, precision, recall, and F1-score.

* Check for multicollinearity among the independent variables, and if present, remove the highly correlated variables to avoid overfitting.

* Determine the optimal threshold using the AUC-ROC curve.

* Build a decision tree model to predict hotel booking cancellations using scikit-learn's DecisionTreeClassifier function.

* Evaluate the decision tree model's performance on the testing set using metrics like accuracy, precision, recall, and F1-score.

* Apply pruning to the decision tree model to reduce overfitting and improve generalization.

* Compare the performance of the logistic regression and decision tree models and select the best model.

* Use the optimised model to predict hotel booking cancellations.

### Main References
* N. Antonio, A. de Almeida, and L. Nunes, “Predicting hotel bookings cancellation with a machine learning
classification model,” in 2017 16th IEEE International Conference on Machine Learning and Applications
(ICMLA), 2017, pp. 1049–1054.
* A. J. Sánchez-Medina, C. Eleazar et al., “Using machine learning and big data for efficient forecasting of
hotel booking cancellations,” International Journal of Hospitality Management, vol. 89, p. 102546, 2020.
* C. Robert, “Machine learning, a probabilistic perspective,” 2014.

### Libraries Used
Python
* [Python Standard Library](https://docs.python.org/2/library/): Built in python modules.
* [Numpy](http://www.numpy.org/): Scientific computing with python.
* [Pandas](http://pandas.pydata.org/): Data analysis tools.
* [matplotlib](https://matplotlib.org/): Static, animated, and interactive visualizations.
* [Seaborn](https://seaborn.pydata.org/): Python data visualization library.

