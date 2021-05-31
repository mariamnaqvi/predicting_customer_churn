# Classification Project - Predicting Customer Churn

## Project Description 
Perform statistical analysis on a set of Telco datapoints to drive the creation of an accurate model. This model will then be used to predict customer churn - that is, to try and estimate the number of customers who will choose to end their business with the aforementioned Telco company. 
 
 ## Project Goals
1. Perform and document the following processes:
    * Acquisition of Data
    * Preparation and Cleaning of Data
    * Exploratory analysis, statistical testing and model evaluation
    * Presenting of key findings and takeaways in a digestible format
2. Moreover, the code should be written in a clear, concise and reusable manner

## Business Goals
Attempt to discover the leading causes of churn at Telco
Perform modeling, analysis and testing to verify the accuracy of a classification and prediction model
Provide recommendations and suggestions to reduce overall customer churn and increase Telco’s revenue

## Initial Hypotheses
*Hypotheses 1:* I accepted/rejected the null hypotheses; there is a difference in churn based on monthly charges
* Confidence level = 0.99
* Alpha = 1 - Confidence level = 0.01
* H<sub>0</sub>: Mean monthly charges of customers who churned = Mean of monthly charges of all customers
* H<sub>1</sub>: Mean monthly charges of customers who churned > Mean of monthly charges of all customers

*Hypotheses 2:* I accepted/rejected the null hypotheses; there is a difference in churn based on customers using fiber optic internet
* Confidence level = 0.99 
* Alpha = 1 - Confidence level = 0.01
* H<sub>0</sub>: Churn Rate is independent of having fiber optic internet
* H<sub>1</sub>: Churn Rate is dependent on having fiber optic internet

*Hypotheses 3:* I accepted/rejected the null hypotheses; there is a difference in churn based on payment type
* Confidence level = 0.99 
* Alpha = 1 - Confidence level = 0.01
* H<sub>0</sub>: Churn is independent of payment type
* H<sub>1</sub>: Churn is not independent of payment type

*Hypotheses 4:* I accepted/rejected the null hypotheses; there is a difference in churn based on tenure and monthly charges
* Confidence level = 0.99
* Alpha = 1 - Confidence level = 0.01
* H<sub>0</sub>: There is no linear correlation between tenure and monthly charges.
* H<sub>1</sub>: There is a linear correlation between tenure and monthly charges

*Hypotheses 5:* I accepted/rejected the null hypotheses; there is a difference in churn based on contract type 
* Confidence level = 0.99 
* Alpha = 1 - Confidence level = 0.01
* H<sub>0</sub>: Churn is independent of contract type
* H<sub>1</sub>: Churn is not independent of contract type

## Data Dictionary
The following categories were initially collected from the database:

Name | Datatype | Definition | Possible Values 
--- | --- | --- | --- 
payment_type_id|non-null   int64 | Indicates the payment type | 1 = Electronic Check; 2 = Mailed Check; 3 = Bank transfer (automatic); 4 = Credit card (automatic)
internet_service_type_id|non-null   int64 | Numeric indicator of the type of Internet Service provided to the customer | 0 = No Internet Service; 1 = DSL; 2 = Fiber Optic
contract_type_id|non-null   int64 | Numeric indicator of the Contract Type for this customer | 0 = Month-to-Month; 1 = 1 Year, 2 = 2 Year
customer_id|non-null   object |Represents the unique ID for the a customer | Alpha-Numeric string
gender|non-null   object | Represents the gender of the customer | Male or Female
senior_citizen|non-null   int64 | Indicates whether the customer is a Senior Citizen | 0 = No; 1 = Yes
partner|non-null   object | Indicates whether the customer has a partner | Yes/No
dependents|non-null   object | Indicates whether the customer has dependents | Yes/No
tenure|non-null   int64 | Represents the number of months the customer was with Telco | Numeric value 
phone_service|non-null   object | Indicates whether or not Phone Services are provided to the customer | Yes/No
multiple_lines|non-null   object | Indicates whether or not the customer has multiple lines| Yes/No
online_security|non-null   object | Indicates whether or not the customer is enrolled in an online security plan| Yes/No
online_backup|non-null   object | Indicates whether or not the customer is enrolled in an online backup plan| Yes/No
device_protection|non-null   object | Indicates whether or not the customer makes use of a device protection plan| Yes/No
tech_support|non-null   object | Indicates whether or not the customer uses tech support| Yes/No
streaming_tv|non-null   object | Indicates whether or not the customer uses streaming tv| Yes/No
streaming_movies|non-null   object | Indicates whether or not the customer views streaming movies | Yes/No 
paperless_billing|non-null   object | Indicates whether or not the customer uses paperless billing| Yes/No 
monthly_charges|non-null   float64| The monthly charges billed to the customer | Numeric Value 
total_charges|non-null   object | The total charges billed to the customer | Numeric Value (in String form) 
churn|non-null   object | Indicates whether or not the customer has churned | Yes/No
contract_type|non-null   object | String description of the Contract Type for this customer | Month-to-Month; 1 Year,  2 Year
internet_service_type|non-null   object | String description of the type of Internet Service provided to the customer | No Internet Service; DSL;  Fiber Optic
payment_type|non-null   object | String description of the Contract Type for this customer | Month-to-Month; 1 Year,  2 Year

In addition to the above data, the following columns were added:
Name | Datatype | Definition | Possible Values 
--- | --- | --- | --- 
en_contract_type | int64 | encoded representation of the contract type | 0 = Month-to-Month; 1 = 1 Year, 2 = 2 Year
en_monthly_contract | int64 | encoded representation of whether or not the customer has a monthly contract | 0 = No; 1 = Yes
en_multiple_lines | int64 | encoded representation of whether or not the customer has multiple lines | 0 = No; 1 = Yes
en_has_fiber | int64 | encoded representation of whether or not the customer has fiber optic internet  | 0 = No; 1 = Yes
en_has_DSL | int64 | encoded representation of whether or not the customer has DSL internet | 0 = No; 1 = Yes
has_internet | int64 | encoded representation of the whether or not the customer has internet | 0 = No; 1 = Fiber Optic or DSL

## Project Planning

The overall process followed in this project, is as follows:
1. Plan
2. Acquire
3. Prepare
4. Explore
5. Model
6. Deliver

### 1. Plan
* List of tasks in this Trello Board
* Perform preliminary examination of the dataset
* Collect database details (connection information and credentials)

### 2. Acquire: Create a reusable component to acquire data from the CodeUp database
* This is accomplished using a python script named “acquire.py”. It makes use of stored credentials (via env.py) to connect to the CodeUp database, and collects data using a SQL query from the following tables:
1. Customers
2. Contract_types
3. Internet_Service_Types
4. Payment_Types
* Once the data is collected, store it in a CSV (Comma Separated Value) file as a sort of cache; that way, if the file is present on disk, there is no need to query the CodeUp database.
* Finally, this component will compute & present a set of superficial statistics, including:
    * The number of records collected
    * The number of missing/empty values
    * Information for the overall structure of the retrieved data
    * A description of the retrieved data
    * A list of the collected categories, and the proportional size of each

### 3. Prepare: Create a reusable component to prepare the data for processing and statistical analysis
* Most of the code was written into the file named “prepare.py”, which performs the following processes:
	* Look for (and remove) duplicate records from the incoming data set
	* Replace null or empty values (primarily for the monthly_charges column, which contained empty values)
	* Convert data to an optimal format. 
    		* For example, total_charges was stored as an object - however, this column represents a dollar amount, and converting it to a float will eliminate issues during analysis
	* Create a number of new features (“columns”) representing the existing data in encoded form
	* The encoded data format will make analysis more straightforward, and eliminates redundant values, resulting in clear binary values

### 4. Explore: Create a reusable component to explore the data set and derive key conclusions and takeaways
* This code was saved in the "explore.py" script, which performs the following processes:
	* aid in univariate analysis, by generating bar plot and histograms of certain variabls
	* aid in bivariate analysis, by generating barplots, countplots and boxplots of certain variables
	* aid in multivariate analysis, by generating box plots of combinations of certain varibales 
* Examine churn rate as a function of the tenure of Telco's customers
* Perform statistical analysis of the plots generated in this phase
* Form different hypotheses, execute tests and examine resulting plots
	* Compute the t-statistic and p-value, using these to validate (or invalidate) our hypotheses  
	
### 5. Model
* Generate a baseline, against which all models will be evaluated
* Explore the set of variables and deduce which has the highest level of correlation to churn
	* use these selections to generate multiple models to help predict churn
* Execute each model, tune, validate, and compare to the baseline

### 6. Deliver 
* Output findings to a csv file - in this case, "predictions.csv"

## To recreate
Simply clone the project locally and create an env.py file in the same folder as the cloned code. The format should be as follows:

```host = ‘DB_HOST_IP’
user =  ‘USERNAME’
password = ‘PASSWORD’

def get_db_url(db, user=user, host=host, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
```
    
In the above code, replace the `host`, `user` and `password` values with the correct Database Host IP address, Username and Password.

Next, open the Jupyter notebook titled “final_report_telco” and execute the code within. 

## Key findings
* Overall churn rate is at 27%
* Monthly charges for customers who churn are 21% higher than customers who don't churn
* Month to month contracts had the highest number of churning customers

## Recommendations
* All my models predicted churn with an accuracy higher than the baseline model
* My best model used Logistic Regression and can predict customers who will churn with 80% accuracy
* Use this model to identify customers at risk of churning and provide them incentives to stay

## Takeaways
During the analysis process, I made use of the following classification models:
1. Decision Tree
2. Random Forest
3. KNN
4. Logistic Regression
My validation results indicated that the Logistic Regression model provided 80% accuracy in terms of churn prediction. It provided an overall accuracy of 80% and recall score of 50%, which outperformed the baseline of 73.47%.

## Next Steps
If i had more time, I would:
* explore the outliers in more detail
* examine factors leading to customers with higher monthly charges staying for longer tenures
* explore premium services and their effect on churn more
