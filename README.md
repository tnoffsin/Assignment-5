# Assignment-5
A.)  Write a function that determines the highest loan_amnts and lowest loan_amnts in the dataset.
B.) The input would the loan amounts. All the inputs for the codes were the columns of the data which are, customer_id: Unique identifier for each customer customer_age: Age of the customer customer_income: Annual income of the customer home_ownership: Home ownership status (e.g., RENT, OWN, MORTGAGE) employment_duration: Duration of employment in months loan_intent: Purpose of the loan (e.g., PERSONAL, EDUCATION, MEDICAL, VENTURE) loan_grade: Grade assigned to the loan loan_amnt: Loan amount requested loan_int_rate: Interest rate of the loan term_years: Loan term in years historical_default: Indicates if the customer has a history of default (Y/N) cred_hist_length: Length of the customer's credit history in years Current_loan_status: Current status of the loan (DEFAULT, NO DEFAULT)

Loan dataset columns:
customer_id: Unique identifier for each customer
customer_age: Age of the customer
customer_income: Annual income of the customer
home_ownership: Home ownership status (e.g., RENT, OWN, MORTGAGE)
employment_duration: Duration of employment in months
loan_intent: Purpose of the loan (e.g., PERSONAL, EDUCATION, MEDICAL, VENTURE)
loan_grade: Grade assigned to the loan
loan_amnt: Loan amount requested
loan_int_rate: Interest rate of the loan
term_years: Loan term in years
historical_default: Indicates if the customer has a history of default (Y/N)
cred_hist_length: Length of the customer's credit history in years
Current_loan_status: Current status of the loan (DEFAULT, NO DEFAULT)

What does the code do?
These are the steps: 
1.) find_highest_and_lowest_loan_amnts takes a single argument of data
2.) It then splits the data into lines and then seperates the first line or the header by commas and takes the remain lines as the "data_rows" or column titles
3.) Identifies the index of the loan_amnt in the header and then finds the highest and lowest data amounts and loops throughout the dataset
4.) It then returns the highest and lowest loan amounts

Are there any User Defined Functions?
Yes, The function find_highest_and_lowest_data_amnts is a user defined function. It was made to find the highest and lowest loan amounts from the input data string. 

Why is knowing the highest and lowest loan amounts important? What's the point?
Knowing this data can help a company or someone representing a company that has to do with loans for these reasons:
1.) Data Range Insight: Gives you the range of your data, revealing its spread.
2.) Anomaly Detection: Identifies outliers or anomalies, such as errors or significant data points.
3.) Resource Allocation: Helps in planning resources  if you're working with financials or quantities, such as budgets.
4.) Performance Metrics: In business, knowing these metrics can indicate peak performance or areas needing improvement.


