# cleaning the df
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
# function to clean original df

def prep_telco_data(df):
    # check for duplicates 
    num_dups = df.duplicated().sum()
    # returns 22 rows
    if num_dups > 0:
        print(f'There are {num_dups} duplicate rows in your dataset - these will be dropped.')
        df = df.drop_duplicates()
    else:
        print(f'There are no duplicate rows in your dataset.')

        
    # drop customer id column
    columns_to_drop = ['customer_id']
    print(f'Removing the following columns: {columns_to_drop}')
    df = df.drop(columns=columns_to_drop)
    df.columns.to_list()
    
    # replace empty values with null values 
    df['total_charges'] = df.total_charges.replace(" ", np.nan)
    # changing total charges of new customers to their monthly charges
    df['total_charges'] = df.total_charges.fillna(value=df.monthly_charges)    # new_customers = df['total_charges'].value_counts(dropna=False) # 11 customers who have not been charged and so total charges is empty

    # change total charges to float 
    df.total_charges = df.total_charges.astype(float)

    # encode binary categorical variables: gender, sr citizen, parnter, depens, phone ser, multiple lines, online sec, 
    # online backup, device protection, tech support, streaming tv, streaming movies, paperless blling
    dummy_df=pd.get_dummies(df[['gender', 'partner', 'dependents','phone_service', 'multiple_lines',
                                  'online_security','online_backup','device_protection','tech_support','streaming_tv',
                                   'streaming_movies', 'paperless_billing', 'churn', 'contract_type', 'internet_service_type', 'payment_type']], dummy_na=False, 
                            drop_first=[True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True])


    # rename columns
    dummy_df = dummy_df.rename(columns={'partner_Yes': 'has_partner', 'dependents_Yes': 'has_dependents', 'phone_service_Yes': 'has_phone_service',
                            'multiple_lines_No phone service': 'has_single_line', 'multiple_lines_Yes': 'has_multiple_lines', 
                             'online_security_Yes': 'has_online_security', 'online_backup_Yes': 'has_online_backup', 
                             'contract_type_One year': 'has_1yr_contract','contract_type_Two year': 'has_2yr_contract',
                             'internet_service_type_Fiber optic': 'has_fiber', 'internet_service_type_None': 'has_internet_service',
                             'payment_type_Credit card (automatic)': 'pay_by_card', 'payment_type_Electronic check':'pay_echeck',
                             'payment_type_Mailed check':'pay_mailcheck' 
                            })

    # join dummy df to original df
    df = pd.concat([df, dummy_df], axis=1)

    # drop encoded columns
    cols_to_drop = ['gender', 'partner', 'dependents','phone_service', 'multiple_lines',
                                  'online_security','online_backup','device_protection','tech_support','streaming_tv',
                                   'streaming_movies', 'paperless_billing', 'churn', 'contract_type', 'internet_service_type', 'payment_type']
    df = df.drop(columns = cols_to_drop)
    return df
          



# split df into train, validate and split

def train_validate_test_split(df, target, seed = 123):
    '''
    This function takes in a dataframe, the target variable to stratify and a random seed. 
    It splits the original df into train, validate and test dataframes.
    Test dataset is 20% of the original dataset
    Train is 56% (0.7 * 0.8 = .56) of the original dataset
    Validate is 24% (0.3 * 0.7 = 0.24) of the original dataset
    '''
    train, test = train_test_split(df, test_size = 0.2, random_state = seed,
                                  stratify = df[target])
    train, validate = train_test_split(train, train_size = 0.7, random_state = seed,
                                  stratify = train[target])
    return train, validate, test
