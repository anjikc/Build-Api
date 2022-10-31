# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
Gradient Boosting Classifier was used with sum default estimators 
## Intended Use
Predict the target variable which is salary based on some features 
## Training Data
https://archive.ics.uci.edu/ml/datasets/census+income is the source of data. Train:Test split is 80:20
## Evaluation Data
Evaulation is done on 20% of remaining data after training 
## Metrics
Evaluation Metric was Accuracy 
## Ethical Considerations
Since lot of features have 
## Caveats and Recommendations
Feature engineering can be done in more detail. Other models like adaboost can also checked for performance