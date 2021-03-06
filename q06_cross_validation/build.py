# Default imports
from sklearn.model_selection import cross_val_score
import numpy as np
from greyatomlib.advanced_linear_regression.q01_load_data.build import load_data

np.random.seed(9)
# We have already loaded the data for you
data_set, X_train, X_test, y_train, y_test = load_data('data/house_prices_multivariate.csv')

# Write your solution here
from sklearn.linear_model import Ridge
def cross_validation(model, X_train, y_train):
    m = model.fit(X_train, y_train)
    cvs = cross_val_score(m, X_train, y_train, scoring='neg_mean_squared_error', cv=5)
    # Question not clear on what to return.
    # Need to return the mean value of all cvs scores which passes the test
    return cvs.mean()

# print ("#### Testing ####")
# value = cross_validation(Ridge(alpha=0.1), X_train, y_train)
# print value
