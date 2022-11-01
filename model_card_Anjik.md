# Model Card
For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf
## Model Details
Gradient Boosting Classifier was used with some default estimators 
## Intended Use
Predict the target variable which is salary based on some features 
## Training Data
https://archive.ics.uci.edu/ml/datasets/census+income is the source of data. Train:Test split is 80:20
## Evaluation Data
Evaulation is done on census data. 20% of the whole data is used for testing. 
## Metrics
Evaluation Metric was Accuracy. Accuracy of the testing set of data was around 0.83 
## Ethical Considerations
Since lot of features have been mentioned in the data there can be bias in the data. Proper care should be taken to overcome bias
## Caveats and Recommendations
Feature engineering can be done in more detail. Other models like adaboost can also checked for performance
