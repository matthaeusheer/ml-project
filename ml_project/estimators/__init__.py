import pandas

from sklearn.base import BaseEstimator, RegressorMixin


class MeanValueClassifier(BaseEstimator, RegressorMixin):
    """The prediction will be the mean value of all feature values."""

    def fit(self, X, y=None):
        self.means_ = X.mean(axis=1)
        return self

    def predict(self, X, y=None):
        try:
            getattr(self, "means_")
        except AttributeError:
            raise RuntimeError("You must train classifer before predicting data!")

        return self.means_

