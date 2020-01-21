# Python Sklearn Pipeline

This example works on *VDMML 8.5*, it requires the following packages:

- sklearn
- sasctl

## Data

This example is not dependant on a specific dataset, it uses only Model Studio macros.
It works on [HMEQ data](https://github.com/sassoftware/sas-viya-dmml-pipelines/tree/master/data/hmeq.csv).

## Steps

### Define the inputs: 

setting the variable Matrix and target vector

### Define the pipeline

1. Preprocessing:
 - Numerical variables
    - Imputation with the median

 - Categorical variables:
    - Imputation with the most frequent value
    - One Hot encoding

2. Modeling:
    - Gradient Boosting Classifier

### Register the model

User must complete the code with the following information:

 - server URL
 - username
 - password
 - Model Manager Project Name