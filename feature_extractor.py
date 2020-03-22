import os
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import Pipeline



class FeatureExtractor(object):
	def __init__(self):
		pass

	def fit(self, X_df, y_array):

		X_encoded = X_df

		def process_date(X):
			date = pd.to_datetime(X['JOUR'], format='%Y-%m-%d')
			return np.c_[date.dt.year, date.dt.month, date.dt.day]
		date_transformer = FunctionTransformer(process_date, validate=False)

		numeric_transformer = Pipeline(steps=[
			('impute', SimpleImputer(strategy='median'))])

		date_cols = ['JOUR']
		num_cols = ['lon','lat','nb_metro','nb_rer','principal','Nbre plateformes','num_inc','est_greve','est_jour_ferie']
		drop_cols = ['duree', 'type_inc', 'res_com', 'mode_','line', 'Segment DRG', 'duree', 'type_inc', 'Jour de la semaine', 
                     'Horaire en jour normal', 'Horaire en jour férié', 'type_jour']


		preprocessor = ColumnTransformer(
			transformers=[
				('date', make_pipeline(date_transformer,
				SimpleImputer(strategy='median')), date_cols),
				('num', numeric_transformer, num_cols),
				('drop cols', 'drop', drop_cols)
				])

		self.preprocessor = preprocessor
		self.preprocessor.fit(X_encoded, y_array)
		return self

	def transform(self, X_df):
		X_encoded = X_df
		return self.preprocessor.transform(X_encoded)
