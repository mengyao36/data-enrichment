### import needed packages to python
import pandas as pd
import numpy as np

### convert atlas dataset from txt to csv 
atlas = pd.read_csv('Data/Atlas/US_2019_ADI_Census Block Group_v3.1.txt')
atlas.to_csv ('Data/Atlas/atlas.csv', index=None)

### read the atlas csv file
atlas = pd.read_csv('Data/Atlas/atlas.csv')
# change var names into lower case
atlas.columns = atlas.columns.str.lower()
# show all var names in atlas
atlas.columns
# check all var types within atlas dataset
atlas.dtypes
# reaname some vars
atlas = atlas.rename(columns={
    'unnamed: 0':'unnamed_0',
    'unnamed: 0.1':'unnamed_0.1',
    'fips':'zip_atlas',
    })
# check missing values for each var - no missing values detected
atlas.isnull().sum()


### get the first three numbers from 'zip_atlas' and save it as a new var called "zip_atlas_3"
atlas['zip_atlas_3'] = atlas.zip_atlas.astype(str).str[:3]
# show how the new var looks like
atlas['zip_atlas_3'].head(5)


### save the editted data
atlas.to_csv('Data/Atlas/atlas_new.csv')
# load editted dataset
atlas_new = pd.read_csv('Data/Atlas/atlas_new.csv')
# change zip_atlas_3 into str var
atlas_new['zip_atlas_3'] = atlas_new['zip_atlas_3'].astype(str)
# check var type
atlas_new.dtypes
# drop var "unnamed: 0"
atlas_new = atlas_new.drop(columns=['Unnamed: 0', 'unnamed_0', 'unnamed_0.1', 'zip_atlas'])
# check missing values for each var - no missing values detected
atlas_new.isnull().sum()
# save the new dataset
atlas_new.to_csv('Data/Atlas/atlas_new.csv')


### load sparcs dataset
sparcs = pd.read_csv('C:/Users/36men/OneDrive/Documents/Fall 2022/HHA 507 Data/Assignment_Data/sparcs.csv', low_memory=False)
# save sparcs dataset to repo
sparcs.to_csv('Data/sparcs.csv')
# load sparcs dataset 
sparcs = pd.read_csv('Data/sparcs.csv', low_memory=False)
# show all var names in sparcs
sparcs.columns
# check all var types within sparcs dataset
sparcs.dtypes

### format var names
# change all var names into lowercase
sparcs.columns = sparcs.columns.str.lower()
# remove white spaces in var names 
sparcs.columns = sparcs.columns.str.replace('[^A-Za-z0-9]+', '_')
# rename some vars
sparcs = sparcs.rename(columns={
    'zip_code_3_digits':'zip_sparcs_3',
    'unnamed_0':'unnamed_0_sparcs',
    })
# save editted dataset
sparcs.to_csv('Data\sparcs_new.csv')


### load editted dataset
sparcs_new = pd.read_csv('Data\sparcs_new.csv', low_memory=False)
# show all var types
sparcs_new.dtypes
# show all missing values 
sparcs_new.isnull().sum()
# drop some unnecessary vars
sparcs_new = sparcs_new.drop(columns=['Unnamed: 0', 'unnamed_0_sparcs'])
# drop all rows with missing values - also to decrease dataset size for merge or merge cannot be processed
sparcs_new_noempty = sparcs_new.dropna(inplace=True)
# save dataset with changes
sparcs_new.to_csv('Data\sparcs_new_noempty.csv')

### load dataset
sparcs_new_noempty = pd.read_csv('Data\sparcs_new_noempty.csv')
# check missing values in this dataset - should be none
sparcs_new_noempty.isnull().sum()
# check all vars types 
sparcs_new_noempty.dtypes


### use sparcs_new as base dataset anb merge it with atlas_new dataset
sparcs_atlas = sparcs_new_noempty.merge(atlas_new, how='left', left_on='zip_sparcs_3', right_on='zip_atlas_3')
# show first 5 rows of the merged dataset
print(sparcs_atlas.head(5).to_markdown)
# save the merged dataset
sparcs_atlas.to_csv('Data\sparcs_atlas.csv')