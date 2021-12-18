# Sales-Forecasting using SQL and deployment on Web
This project forecasts Walmart store sales next week and next month. The data is stored in SQLite, and SQL query is used to fetch and create input variables. I applied the Linear Regression algorithm, which takes selected features to predict weekly sales. We also deployed the Model on the web using flask and HTML. We elaborate on how the technique is implemented and evaluate the model performance
# Analysis methods
•	Mathematical and Statistical methods such as Pearson, spearman correlation, hypothesis testing, data distributions are implemented in the Exploratory Data analysis and feature engineering phase to know the factors explaining the sales.
•	Descriptive analysis is applied to analyze past events for deciding future sales.
•	Regression Analysis is implemented to predict the sales using essential features.
•	Model Performance is evaluated by measuring the mean absolute and mean absolute percentage errors on both train and test data sets.
•	Web Deployment is performed using Flask and HTML page.
# Model & Results
Linear Regression algorithm is used for forecasting the weekly sales. After data analysis, it is found the previous week's sale is the only variable explaining the current week's sale. The week number and quarter are used for prediction to handle seasonality in the data.

Train and Test: The data of 2010 and 2011 are used for training the model, and 2012 data is used for testing it.

Performance Matrices: Mean Absolute Error (MAE) and Mean Absolute Error percentage (MAPE) are evaluated to measure the model’s performance

Results: The result for train and test for both next week and next month model is coming close to 90% accuracy.

# Web Design
I have designed a 
b page using HTML, style sheet, and python to make the system more interactive and user- friendly. The flask package is used to interact with the Html page.
Process: The user can key in the store number, week of the sale, the sale on that week, and click on the predict sales button. The predicted sale for the next week and month are displayed to the user. 




