

'''Install xgboost
Python package site : https://www.lfd.uci.edu/~gohlke/pythonlibs/
Find xgboost : xgboost‑1.2.1‑cp37‑cp37m‑win_amd64.whl
Download it here : C:\Users\Administrator\Anaconda3\Lib\site-packages

Start Anaconda Prompt
wrtie1) conda activate base
write2) pip install C:\Users\Administrator\Anaconda3\Lib\site-packages\xgboost-1.2.1-cp37-cp37m-win_amd64.whl
If error occurs : 제어판 > 시스템 및 보안 > 시스템 > 고급 시스템 설정 > 환경변수
시스템 변수 path double click - 새로 만들기 - C:\Users\Administrator\Anaconda3\Lib\site-packages 입력
'''

# To draw the tree, install graphviz
# Anaconda Prompt
# 1) conda activate base
# 2) conda install graphviz python-graphviz

# conda update --all
# conda update -c conda-forge scikit-learn
# pip install --upgrade scikit-learn

# =========================================================================
# XGBoost from A to Z
# =========================================================================

# Import the modules that will do all the work
import pandas as pd   # load and manipulate data and for One-Hot Encoding
import numpy as np    # calculate the mean and standard deviation
import xgboost as xgb # XGBoost stuff

from sklearn.model_selection import train_test_split
from sklearn.metrics import balanced_accuracy_score, roc_auc_score, make_scorer
from sklearn.model_selection import GridSearchCV   # cross validation
from sklearn.metrics import confusion_matrix       # create a confusion matrix


# =========================================================================
# 1. Importing Data from a File
# =========================================================================

df = pd.read_csv('Telco_customer_churn.csv')
df.head()
# set axis=0 to remove rows, axis=1 to remove columns
df.drop(['Churn Label', 'Churn Score', 'CLTV', 'Churn Reason'],
        axis=1, inplace=True)
df.head()

# Unique values in the column
df['Count'].unique()
# array([1]) → This column only contains 1
df['Country'].unique()
df['State'].unique()
df['City'].unique()

df.drop(['CustomerID', 'Count', 'Country', 'State', 'Lat Long'],
        axis=1, inplace=True)
df.head()

# Although it is OK to have whitespace for XGBoost and classification,
# we can't have any whitespace if we want to draw a tree
# So, let's replace white space in the city names with an underscore character _
df['City'].replace(' ','-', regex=True, inplace=True)
df.head()

# First 10 unique city names to verify we have underscore
df.['City'].unique()[0:10]

# Eliminate the whitespace in the column names
df.columns = df.columns.str.replace(' ','_')
df.head()


# =========================================================================
# 2. Missing Data
# =========================================================================
# Blank space, NA, etc.
# XGBoost has default behavior for missing data
# So all we have to do is identify missing values and make sure they are set to 0

# See what sort of data is in each columns
df.dtypes
df.['Phone_Service'].unique()
df.['Total_Charges'].unique()

# 1) Identifying Missing Data
# Let's see how many rows are missing data
# If it's a lot, then we might have a problem on our hands
# that is bigger than what XGBoost can deal with on its own
# If it's not many, we can just set them to 0
len(df.loc[df['Total_Charges']==' '])
# Since only 11 rows have missing values, let's look at them
df.loc[df['Total_Charges']==' ']

# 2) Dealing with Missing Data

# Since all 11 people with Total_Charges = ' ' have Tenure_Months = 0
# We can know that they just signed up
# Thus, we can set Total_Charges to 0
df.loc[(df['Total_Charges'] == ' '), 'Total_Charges'] = 0

# Now let's verify that we modified Total Charges correctly
# by looking at everyone who had Tenure_Months set to 0
df.loc[df['Tenure_Months'] == 0]

# Problem : Total_Charges still has the 'object' data type
# This is no good because XGBoost only allows 'int', 'float' or 'boolean' data type
# Fix this by converting it with to_numeric()
df['Total_Charges'] = pd.to_numeric(df['Total_Charges'])
df.dtypes

# To draw a picture of the one of the XGBoost trees,
# replace all of the other whitespaces in all of the columnes with underscores
df.replace[' ', '_', regex=True, inplace=True]
df.head()


# =========================================================================
# 3. Formatting the Data for XGBoost
# =========================================================================
# 1) Splitting data into Dependent and Independent Variables
# 2) One-Hot-Encoding
# 3) Converting all columns to Int, Float or Bool


# =========================================================================
# 4. Building a Preliminary XGBoost Model
# =========================================================================


# =========================================================================
# 5. Optimizing Parameters with Cross Validatino and GridSearch()
# =========================================================================
# Optimizing the learning rate, tree depth, number of trees, gamma (for pruning) and lambda (for regularization)


# =========================================================================
# 6. Building, Drawing, Interpreting and Evaluating the Optimized XGBoost Model
# =========================================================================









