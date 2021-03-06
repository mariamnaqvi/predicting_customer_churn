# cleaning the df
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
# function to clean original df

def prep_telco_data(df):
    '''
    Initial data preparation function. Given a dataframe df, this function performs a
    number of clean-up tasks in preparation for further analysis, including:
    * detecting and removing duplicate records
    * converting columns to the most appropriate datatype
    * combining similar columns to remove redundant/duplicate data
    * one-hot encoding columns to reduce the column count
    Finally, this function will call the split_telco function to split the data into
    three sets - train, test and validate. It returns the train, validate and test splits and also 
    prints the shape of each.
    '''
    # check for duplicates 
    num_dups = df.duplicated().sum()
    # if we found duplicate rows, we will remove them, log accordingly and proceed
    if num_dups > 0:
        print(f'There are {num_dups} duplicate rows in your dataset - these will be dropped.')

        print ('----------------')
        # remove duplicates if found
        df = df.drop_duplicates()
    else:
        # otherwise, we log that there are no dupes, and proceed with our process
        print(f'There are no duplicate rows in your dataset.')

        print('----------------')

    
    
    # replace empty values in total charges with null values 
    df['total_charges'] = df.total_charges.replace(" ", np.nan)
    # changing total charges of new customers to their monthly charges
    df['total_charges'] = df.total_charges.fillna(value=df.monthly_charges)    # new_customers = df['total_charges'].value_counts(dropna=False) # 11 customers who have not been charged and so total charges is empty
    print(f'The empty string values have been filled with monthly_charges values')
    
    # change total charges to float 
    df.total_charges = df.total_charges.astype(float)
    print(f'Total charges has been converted from object to a float data type.')

    print('----------------')


    #----------------------#
    #      New Features    #
    #----------------------#

    # encode contract type column 
    # 0 is month to month 
    # 1 is 1 year contract
    # 2 is 2 year contract
    df['en_contract_type'] = df.contract_type_id.map({1:0, 2:1, 3:2})

    # separate column for month to month contracts
    df['en_monthly_contract'] = df.contract_type_id.map({1:1, 2:0, 3:0})

    df['en_multiple_lines'] = df.multiple_lines.map({'Yes':1, 'No':0, 'No phone service':0})

    df['en_has_fiber'] = df.internet_service_type.map({'Fiber optic':1, 'DSL':0, 'None':0})    

    df['en_has_DSL'] = df.internet_service_type.map({'Fiber optic':0, 'DSL':1, 'None':0})  

    df['has_internet'] = df.internet_service_type.map({'Fiber optic':1, 'DSL':1, 'None':0})  

    # encoding both no and no internet service categories as 0`
    encode_nointernet_cols = ['online_security','online_backup','device_protection','tech_support','streaming_tv','streaming_movies']
    for x in encode_nointernet_cols:
        newcol = "en_"+ x 
        df[newcol] = df[x].map({'Yes':1, 'No':0, 'No internet service':0})
    

    #----------------------#
    #  One hot encoding    #
    #----------------------#

    # encode binary categorical variables: gender, sr citizen, parnter, depens, phone ser, multiple lines, online sec, 
    # online backup, device protection, tech support, streaming tv, streaming movies, paperless blling to numeric
    dummy_df=pd.get_dummies(df[['gender', 'partner', 'dependents','phone_service',
                                'paperless_billing', 'churn']], dummy_na=False, 
                            drop_first=[True, True, True, True, True, True])


    # rename columns that have been one hot encoded
    dummy_df = dummy_df.rename(columns={'partner_Yes': 'has_partner', 'dependents_Yes': 'has_dependents', 'phone_service_Yes': 'has_phone_service', 
                                        'paperless_billing_Yes': 'has_paperless_billing','churn_Yes': 'churned',
                                        'gender_Male': 'gender_female'
                            })

    # join dummy df to original df
    df = pd.concat([df, dummy_df], axis=1)

    # drop encoded columns
    cols_to_drop = ['gender', 'partner', 'dependents','phone_service',  'paperless_billing', 'churn',
                    'internet_service_type_id', 'multiple_lines',
                    'contract_type_id', 'payment_type', 'online_security',
 'online_backup',
 'device_protection',
 'tech_support',
 'streaming_tv',
 'streaming_movies',
 'contract_type',
 'internet_service_type']

    df = df.drop(columns = cols_to_drop)
    
    #----------------------#
    #     Split Data       #
    #----------------------#

    # split data into train, validate, test dataframes, stratified on the churn variable by calling the split telco function
    train, validate, test = split_telco(df, 'churned', seed=123)

    # Now that we have our 3 dataframes, print their shapes and return them    
    train.info()

    print ('----------------')

    print(f'Shape of train split: {train.shape}')

    print ('----------------')

    print(f'Shape of test split: {validate.shape}')

    print ('----------------')

    print(f'Shape of validate split: {test.shape}')

    print ('----------------')
    
    return train, validate, test
          



# split df into train, validate and split

def split_telco(df, target, seed = 123):
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
