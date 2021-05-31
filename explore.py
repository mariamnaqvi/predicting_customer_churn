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



def explore_univariate(df, cat_vars, quant_vars):
    '''
    This function takes in categorical and quantitative variables from a dataframe.
    It returns a bar plot for categorical variables.
    It returns a histogram for quantitative variables.
    '''
    
    # plot frequencies for each categorical variable
    for var in cat_vars: 
        print('Bar Plot of ' + var)
        bp = df[var].hist()
        bp.grid(False)
        plt.show()
        
    # print histogram for each quantitative variable
    for var in quant_vars:
        generate_hist(df, var)
     


def generate_barplot(df, target, var):
    '''
    Helper function to generate barplots. Given a dataframe df, a target column and a 
    variable, this will generate and draw a barplot for that data set.
    '''
    overall_mean = df[target].mean()
    sns.barplot(var, target, data=df, palette="twilight_shifted")
    plt.xlabel('')
    plt.ylabel('Churn Rate')
    plt.title('Bar plot of ' + var + ' vs ' + target)
    plt.axhline(overall_mean, ls = '--', color = 'grey')
    plt.show()

def generate_hist(df, var):
    '''
    Helper function. Given a dataframe DF and a variable to plot, this function will 
    generate and display a histogram for that variable.
    '''
    print ('Distribution of ' + var)
    df[var].hist()
    plt.grid(False)
    plt.xlabel(var)
    plt.ylabel('Customer count')
    plt.show()

def generate_boxplot(df,target, var):
    '''
    Given a dataframe df, a target column and a variable to plot, this helper function
    will generate and display a boxplot comparing the given data elements.
    '''
    plt.figure(figsize=(10,5))
    sns.boxplot(y=var, x=target, data=df,  palette="twilight_shifted")
    plt.title('Boxplot of ' + var)
    plt.show()

def generate_countplot(df, target, var):
    '''
    Another helper function used to display a plot. Given a dataframe df, a target
    column and a variable, this function will create and display a countplot.
    '''
    sns.countplot(data=df, x=var, hue=target,  palette="twilight_shifted")
    plt.tight_layout()
    plt.show()

def explore_bivariate(df, target, cat_vars, quant_vars):
    '''
    This function takes in takes in a dataframe, the name of the binary target variable, a list of 
    the names of the categorical variables and a list of the names of the quantitative variables.
    For each categorical variable, a crosstab of frequencies is returned along with the results 
    from a chi-square test that is run, and a barplot. .
    '''
    
    for var in cat_vars:
        # bar plot with overall horizontal line
        generate_barplot(df, target, var)
        # create countplot for categorcial variables and churn
        generate_countplot(df, target, var)
    for var in quant_vars:
        # creates boxplot
        generate_boxplot(df,target, var)
        
     
def explore_multivariate(train, target, cat_vars, quant_vars):
    '''
    
    '''
    for cat in cat_vars:
        for quant in quant_vars:
            sns.boxplot(x=train[cat], y=quant, data=train, hue=target, palette="twilight_shifted")
            plt.xlabel('')
            plt.ylabel(quant)
            plt.title(cat + ' vs ' + quant)
            plt.show()
       
        