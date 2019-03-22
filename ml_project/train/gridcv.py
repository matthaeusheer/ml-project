from pprint import pprint
import math


def print_gridcv_report(grid_cv_obj, neg_sqr_of_score=False):
    """Prints mean_test_score aldong with std_test_score and corresponding param set of grid search.

    Arguments
    ---------
    grid_cv_obj: A trained instance of GridSearchCV
    neg_sqr_of_score: If True, the square root of scores will be printed
    """
    best_score = grid_cv_obj.best_score_

    print('Best score: {}'.format(best_score if not neg_sqr_of_score else math.sqrt(-grid_cv_obj.best_score_)))
    print('With params: {}'.format(grid_cv_obj.best_params_))

    cv_results = grid_cv_obj.cv_results_

    print('\n', 10 * '-')
    print('Mean test scores for parameter combinations...')
    for mean, std, params in zip(cv_results['mean_test_score'], cv_results['std_test_score'], cv_results['params']):
        if neg_sqr_of_score:
            mean = math.sqrt(-1.0 * mean)
            std = math.sqrt(std)
        print("%0.6f (+/- %0.06f) for %r" % (mean, std, params))
    print(10 * '-')


def get_score_vs_one_param(grid_cv_obj, param, neg_sqr_of_score=False):
    cv_results = grid_cv_obj.cv_results_

    results = {'score': [], param: []}
    for mean, params in zip(cv_results['mean_test_score'], cv_results['params']):
        if neg_sqr_of_score:
            mean = math.sqrt(-1.0 * mean)

        alpha = params['regr__selected_model'][1][param]

        results['score'].append(mean)
        results[param].append(alpha)

    return results




def get_best_score_with_params(grid_cv_obj, neg_sqr_of_score=False):
    best_score = grid_cv_obj.best_score_ if not neg_sqr_of_score else math.sqrt(-grid_cv_obj.best_score_)
    best_params = grid_cv_obj.best_params_

    return best_score, best_params
