# data-enrichment assignment 

## step 1: import needed packages to python (pandas, numpy)
## step 2: covert Atlas dataset from txt to csv and load 
- original txt file used: US_2019_ADI_Census Block Group_v3.1.txt
- rename zip variable 
- get the first three digits of zip varibale and save it as a new variable called "zip_atlas_3"
- convert the new zip variable to string for future merge purpose
- check missing values for all variables
## step 3: save the editted Atlas dataset as a new dataset called "atlas_new"

## step 4: load Sparcs dataset
- rename zip variable as "zip_sparcs_3"
- check missing values for all variables
- drop all rows with missing values - also to decrease dataset size for merge purpose
- (attempt was made to merge without dealing with missing values but failed due to python memory size)
## step 5: save the editted Sparcs dataset as a new dataset called "sparcs_new_noempty"

## step 6: merge "sparcs_new_noempty" and "atlas_new"
- variables used: "zip_sparcs_3" and "zip_atlas_3"

## step 7: save the merged dataset as "sparcs_atlas"

## note: gitignore is set to ignore all .csv files in this repo 
