from sklearn.metrics import mean_squared_error


def rmse_scoring_func(y_true, y_predicted):
    """Sklearn only provides MSE scoring functions. This func provides the RMSE scoring function."""

    return mean_squared_error(y_true, y_predicted)**0.5
