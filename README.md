# RAMP starting kit : Prediction of daily validation in Paris public underground transports
Authors : Dina ABED, Siwar ABBES, Philippe de SAINT CHAMAS, Mohamed Skander HELLAL, Gwendal HENGOAT , Jules ZACCARDI


## Introduction 

Paris, as one of the largest European cities and a world center of art, fashion, gastronomy and culture, receives  around 18 million tourist per year and it's an attractive economic destination for workers which increase the number of its residents every year (about 12,21 million in 2019). 
All these factors makes the carriers operating public transport lines in Ile-de-France, such as RATP and SNCF, faces many challenges to manage all the transport traffic and to satisfy the passengers. 

## Challenge goal
The aim of our challenge is to help to solve issues related to station management. In fact, predicting the crowds of a metro/RER station in function of time and other influencing factors could help the transport operators in the parisian region to prevent many problems.  
This could be via a regression task to predicting the number of validation in specific station per day.
Open data is available to make this challenge feasible: Both SNCF and RATP websites's has a large open sourse validation data and other information related to the transort network which make the task more challenging. We are using also other open ource national data to create more features, in particular, the websites: https://data.iledefrance-mobilites.fr/ and https://www.data.gouv.fr/

## Requirements
Some python librairies should be installed before starting the challenge such as: 
- `numpy`
- `pandas`
- `seaborn`
- `scikit-learn`
- `matplolib`
- `folium`
- `calendar`
- `datetime`
- `IPythhon`

## Setting
- Intall the ramp-workflow library

``` pip install git+https://github.com/paris-saclay-cds/ramp-workflow.git```
- Download the data via ```  download_data.py```  file. This will create and archive in your local directory. Unzip to create a folder data/ containing all the required data for this challenge. 
-  Modify the file ``` regressor.py```  with your own regressor and inluding all the data feature engineering that you have done in the ``` feature_extractor.py ``` put them in ``` submissions/my_submission```  folder.

- Test locally in the staring_kit.ipynb notebook with the python command:
``` ramp_test_submission --submission my_submission```
- Once satisfied by the metric result, you can submit your code. 




Data is freely downloadable <a href="https://drive.google.com/open?id=1jHVkvRu-G37tBuE6IFp-y0gi7d3hUm7E">
here  </a>

