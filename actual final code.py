def find_highest_and_lowest_loan_amnts(data):
    # Split the data into lines
    lines = data.strip().split('\n')
    
    # Extract the header and data rows
    header = lines[0].split(',')
    data_rows = lines[1:]
    
    # Find the index of the loan_amnt column
    loan_amnt_index = header.index('loan_amnt')
    
    # Initialize variables to store the highest and lowest loan amounts
    highest_loan_amnt = float('-inf')
    lowest_loan_amnt = float('inf')
    
    # Iterate over each data row
    for row in data_rows:
        # Split the row into columns
        columns = row.split(',')
        
        # Get the loan_amnt value and convert it to an integer
        loan_amnt = int(columns[loan_amnt_index])
        
        # Update the highest and lowest loan amounts
        if loan_amnt > highest_loan_amnt:
            highest_loan_amnt = loan_amnt
        if loan_amnt < lowest_loan_amnt:
            lowest_loan_amnt = loan_amnt
    
    return highest_loan_amnt, lowest_loan_amnt

# Example usage
data = """customer_id,customer_age,customer_income,home_ownership,employment_duration,loan_intent,loan_grade,loan_amnt,loan_int_rate,term_years,historical_default,cred_hist_length,Current_loan_status
1,22,59000,RENT,123,PERSONAL,C,35000,16.02,10,Y,3,DEFAULT
2,21,9600,OWN,5,EDUCATION,A,1000,11.14,1,,2,NO DEFAULT
3,25,9600,MORTGAGE,1,MEDICAL,B,5500,12.87,5,N,3,DEFAULT
4,23,65500,RENT,4,MEDICAL,B,35000,15.23,10,N,2,DEFAULT
5,24,54400,RENT,8,MEDICAL,B,35000,14.27,10,Y,4,DEFAULT
6,21,9900,OWN,2,VENTURE,A,2500,7.14,1,N,2,DEFAULT
7,26,77100,RENT,8,EDUCATION,A,35000,12.42,10,,3,NO DEFAULT
8,24,78956,RENT,5,MEDICAL,A,35000,11.11,10,,4,NO DEFAULT
9,24,83000,RENT,8,PERSONAL,A,35000,8.9,10,,2,NO DEFAULT
10,21,10000,OWN,6,VENTURE,C,1600,14.74,1,N,3,DEFAULT
11,22,85000,RENT,6,VENTURE,A,35000,10.37,10,,4,NO DEFAULT
12,21,10000,OWN,2,HOMEIMPROVEMENT,A,4500,8.63,1,N,2,DEFAULT
13,23,95000,RENT,2,VENTURE,A,35000,7.9,10,,2,NO DEFAULT
14,26,108160,RENT,4,EDUCATION,D,35000,18.39,10,N,4,DEFAULT
15,23,115000,RENT,2,EDUCATION,A,35000,7.9,10,,4,NO DEFAULT
16,23,500000,MORTGAGE,7,DEBTCONSOLIDATION,A,30000,10.65,10,,3,NO DEFAULT
17,23,120000,RENT,0,EDUCATION,A,35000,7.9,10,,4,NO DEFAULT
18,23,92111,RENT,7,MEDICAL,E,35000,20.25,10,N,4,DEFAULT
19,23,113000,RENT,8,DEBTCONSOLIDATION,C,35000,18.25,10,N,4,DEFAULT
20,24,10800,MORTGAGE,8,EDUCATION,A,1750,10.99,4,N,2,DEFAULT
21,25,162500,RENT,2,VENTURE,A,35000,7.49,10,,4,NO DEFAULT
22,25,137000,RENT,9,PERSONAL,D,34800,16.77,10,Y,2,NO DEFAULT
23,22,65000,RENT,4,EDUCATION,C,34000,17.58,10,N,4,DEFAULT
24,24,10980,OWN,0,PERSONAL,A,1500,7.29,4,Y,3,NO DEFAULT
25,22,80000,RENT,3,PERSONAL,C,33950,14.54,10,Y,4,DEFAULT"""

highest, lowest = find_highest_and_lowest_loan_amnts(data)
print(f"Highest loan amount: {highest}")
print(f"Lowest loan amount: {lowest}")