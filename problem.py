import os
import numpy as np
import pandas as pd
import rampwf as rw
from rampwf.workflows import FeatureExtractorRegressor
from rampwf.score_types.base import BaseScoreType
from sklearn.model_selection import GroupShuffleSplit
# from sklearn.metrics import mean_squared_error, mean_absolute_error


problem_title = 'Prediction of daily validation in Paris public underground transports'
_target_column_name = 'NB_VALD'
# A type (class) which will be used to create wrapper objects for y_pred
Predictions = rw.prediction_types.make_regression()
# An object implementing the workflow

class VALID(FeatureExtractorRegressor):
    def __init__(self, workflow_element_names=[
            'feature_extractor', 'regressor']):  #, 'award_notices_RAMP.csv']):
        super(VALID, self).__init__(workflow_element_names[:2])
        self.element_names = workflow_element_names

workflow = VALID()

# define the score (specific score for the VALID problem)
class VALID_error(BaseScoreType):
    is_lower_the_better = True
    minimum = 0.0
    maximum = float('inf')

    def __init__(self, name='ratp error', precision=3):
        self.name = name
        self.precision = precision

    def __call__(self, y_true, y_pred):
        if isinstance(y_true, pd.Series):
            y_true = y_true.values
        max_true = np.maximum(3., np.log10(np.maximum(5., y_true)))
        max_pred = np.maximum(3., np.log10(np.maximum(5., y_pred)))

        loss = np.mean(np.abs(max_true - max_pred))
        return loss

score_types = [
    VALID_error(name='ratp error', precision=3),
]

def get_cv(X, y):
    cv = GroupShuffleSplit(n_splits=8, test_size=0.20, random_state=42)
    return cv.split(X,y, groups=X['LIBELLE_ARRET'])

def _read_data(path, f_name):
    data = pd.read_csv(os.path.join(path, 'data/data challenge', f_name), low_memory=False)
    y_array = data[_target_column_name].values
    X_df = data.drop(_target_column_name, axis=1)
    return X_df, y_array

def get_train_data(path='./'):
    f_name = 'data_challenge_TRAIN.csv'
    return _read_data(path, f_name)

def get_test_data(path='./'):
    f_name = 'data_challenge_TEST.csv'
    return _read_data(path, f_name)
