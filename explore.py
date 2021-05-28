import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pydataset import data
import acquire as aq
import prepare as pr
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
import scipy.stats as stats

def train_validate_test_split(df, target, seed=123):
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

def explore_univariate(train, cat_vars, quant_vars):
    '''
    This function takes in categorical and quantitative variables from the train dataset.
    It returns a frequency table and bar plot for categorical variables.
    It returns a histogram, boxplot and summary statistics for quantitative variables.
    '''
    
    # print frequency table for each categorical variable
    
    for var in cat_vars: 
        print('Frequency table of ' + var)
        labels = list(train[var].unique())
        frequency_table = (
         pd.DataFrame({var: labels,
                      'Count': train[var].value_counts(normalize=False), 
                      'Percent': round(train[var].value_counts(normalize=True)*100,2)}))
        print(frequency_table)
        print('\n')
    
    # plot frequencies for each categorical variable
    for var in cat_vars: 
        print('Bar Plot of ' + var)
        ft = train[var].hist()
        ft.grid(False)
        plt.show()
        
    # print boxplot for each quantitative variable
    for var in quant_vars:
        plt.boxplot(train[var])
        plt.ylabel(var)
        plt.title('Boxplot of ' + var)
        plt.show()
        plt.tight_layout()
        
    # print histogram for each quantitative variable
    for var in quant_vars:
        h = train[var].hist()
        h.grid(False)
        plt.ylabel(var)
        plt.title('Distribution of ' + var)
        plt.show()
     
    # print summary statistics for each quantitative variable
    for var in quant_vars:
        print ('Summary Statistics of ' + var)
        print(train[var].describe())
        print('\n')


def generate_freq_table(train, var):
    print ('Frequency Table of ' + var )
    labels = train[var].unique()
    freq_table = pd.DataFrame({var: labels,
                              'count': train[var].value_counts(),
                               'percent': (round(train[var].value_counts(normalize=True) * 100,2))
    })
    print (freq_table)
    print('-------------------------------')


def generate_barplot(train, target, var):
    overall_mean = train[target].mean()
    sns.barplot(var, target, data=train, alpha =0.5)
    plt.xlabel('')
    plt.ylabel('Churn Rate')
    plt.title('Bar plot of ' + var + ' vs ' + target)
    plt.axhline(overall_mean, ls = '--', color = 'grey')
    plt.show()


def generate_hist(train, var):
    print ('Distribution of ' + var)
    ax = train[var].hist()
    ax.grid(False)
    plt.show()


def generate_desc_stats(train, var):
    print ('Summary Statistics for ' + var)
    print(train[var].describe())


def generate_boxplot(train,target, var):
    plt.figure(figsize=(10,5))
    sns.boxplot(y=var, x=target, data=train)
    plt.title('Boxplot of ' + var)
    plt.show()


# def get_mann_whitney(train, target, quant_var, alternative_h):
#     x = train[train[target] == 0][quant_var]
#     y = train[train[target] == 1][quant_var]
#     statistic, pvalue = stats.mannwhitneyu(x, y, alternative_h)
#     return statistic, pvalue


def explore_bivariate(train, target, cat_vars, quant_vars, alternative_h):
    '''
    This function takes in takes in a dataframe, the name of the binary target variable, a list of 
    the names of the categorical variables and a list of the names of the quantitative variables.
    For each categorical variable, a crosstab of frequencies is returned along with the results 
    from a chi-square test that is run, and a barplot. For each quantitative variable, descriptive
    statistics are computed with respect to the target variable. Difference in means of the quant
    variable are tested between each class in the target using Mann-Whitney. Finally, a boxplot
    and a swarmplot of the target with the quantitative variable are returned.
    '''
    
    for var in cat_vars:
        # produces the frequency table
        generate_freq_table(train, var)
        # bar plot with overall horizontal line
        generate_barplot(train, target, var)
    for var in quant_vars:
        # creates a histogram
        generate_hist(train, var)
        # provides summary statistics
        generate_desc_stats(train, var)
        # creates boxplot
        generate_boxplot(train,target, var)
        # performs mann whitney test -  options are 'two-sided' or 'one-sided'
#         s, p = get_mann_whitney(train, target, var, alternative_h)
#         print (f'Mann Whitney for {var}: statistic = {s}, p-value = {p}')

        