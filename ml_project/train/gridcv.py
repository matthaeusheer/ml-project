from pprint import pprint
import math


def print_gridcv_report(grid_cv_obj, neg_sqr_of_score=False):
    """Prints mean_test_score aldong with std_test_score and corresponding param set of grid search.

    Arguments
    ---------
    grid_cv_obj: A trained instance of GridSearchCV
    neg_sqr_of_score: If True, the square root of scores will be printed
    """
    
    print('Best param set: ')
    pprint(grid_cv_obj.best_params_)

    cv_results = grid_cv_obj.cv_results_

    print('\n', 10 * '-')
    print('Mean test scores for parameter combinations...')
    for mean, std, params in zip(cv_results['mean_test_score'], cv_results['std_test_score'], cv_results['params']):
        if neg_sqr_of_score:
            mean = math.sqrt(-1.0 * mean)
            std = math.sqrt(std)
        print("%0.3f (+/- %0.03f) for %r" % (mean, std * 2, params))
    print(10 * '-')
