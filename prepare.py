# cleaning the df



# check for duplicates 
df[df.duplicated() == True]
# returns 0 rows so no duplicate rows in the df

# drop customer id column
columns_to_drop = ['customer_id']
df = df.drop(columns=columns_to_drop)
df.columns.to_list()


# drop customers with tenure = 0
df['total_charges'].value_counts(dropna=False) # customers who have not been charged

# encode binary categorical variables: gender, sr citizen, parnter, depens, phone ser, multiple lines, online sec, 
# online backup, device protection, tech support, streaming tv, streaming movies, paperless blling
dummy_df=pd.get_dummies(df[['gender', 'partner', 'dependents','phone_service', 'multiple_lines',
                              'online_security','online_backup','device_protection','tech_support','streaming_tv',
                               'streaming_movies', 'paperless_billing', 'churn', 'contract_type', 'internet_service_type', 'payment_type']], dummy_na=False, 
                        drop_first=[True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True])

# encode payment type, contract type and internet service type to numeric

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


# change total charges to float


