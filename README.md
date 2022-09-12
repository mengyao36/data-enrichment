# data-enrichment assignment 

## import needed packages to python (pandas, numpy)
## covert Atlas dataset from txt to csv and load 
 rename zip variable 
 get the first three digits of zip varibale and save it as a new variable called "zip_atlas_3"
 convert the new zip variable to string for future merge purpose
 check missing values for all variables
## save the editted Atlas dataset as a new dataset called "atlas_new"

## load Sparcs dataset
 rename zip variable as "zip_sparcs_3"
 check missing values for all variables
 drop all rows with missing values - also to decrease dataset size for merge purpose
## save the editted Sparcs dataset as a new dataset called "sparcs_new_noempty"

## merge "sparcs_new_noempty" and "atlas_new"
variables used: "zip_sparcs_3" and "zip_atlas_3"

## save the merged dataset as "sparcs_atlas"

## note: gitignore is set to ignore all .csv files in this repo 
