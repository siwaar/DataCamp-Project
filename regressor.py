from sklearn.ensemble import RandomForestRegressor
from sklearn.base import BaseEstimator
from sklearn.linear_model import LinearRegression
from sklearn.compose import TransformedTargetRegressor
import numpy as np 

class Regressor(BaseEstimator):
    def __init__(self):
        self.MYReg = TransformedTargetRegressor(
        regressor=RandomForestRegressor(n_estimators=30,max_depth=12),
        func=lambda u: np.log10(np.clip(u, a_min=1, a_max=None)),
        inverse_func=lambda u: np.power(10, u),
        check_inverse=False,
        )

    def fit(self, X, y):
        return self.MYReg.fit(X, y)

    def predict(self, X):
        return self.MYReg.predict(X)