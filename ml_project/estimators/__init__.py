import pandas

from sklearn.base import BaseEstimator, ClassifierMixin


class MeanValueClassifier(BaseEstimator, ClassifierMixin):
    """The prediction will be the mean value of all feature values."""

    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def predict(self, X, y=None):
        return pandas.DataFrame(X).mean(axis=1)
