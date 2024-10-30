#Sharpeye: Incentive Calculation for Employees

Project Overview
The "Sharpeye" project is designed to automate the incentive calculation process for employees, enhancing accuracy and efficiency in financial management. This system integrates various data sources to evaluate employee performance and determine corresponding incentives.

Key Features
Data Manipulation: Utilizes the data_m_store module to handle data manipulation tasks, ensuring that all relevant employee and sales data is processed effectively.
Data Fetching: Employs methods to retrieve essential data, including employee details, sales figures, and performance metrics.
Update Mechanism: Incorporates a CDC (Change Data Capture) approach to keep the data current by updating sales, employee, and performance data daily.
Incentive Calculation: Implements logic to calculate employee incentives based on their performance metrics and sales achievements.
Modular Design: Features a modular architecture, separating data loading, connection management, and incentive calculation functionalities for better maintainability.
Technology Stack
Python
PyODBC for database connectivity
Pandas for data manipulation
Usage
To run the project, ensure you have the necessary Python packages installed. Execute the script, and it will:

Load and manipulate employee and sales data.
Update the current day's data.
Calculate and print the incentive amount based on defined criteria.
