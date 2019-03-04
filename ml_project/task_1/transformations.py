from math import exp, cos
import sys

import pandas as pd


def get_phi_callables(n_functions=21, func_name_templ='phi_{}'):
    """Creates a dictionary of callable functions of this module if the function agrees with the given
    function name template.

    Arguments
    ---------
    n_functions: How many functions (up to which scalar index) should be found and returned
    func_name_templ: The callables must have names which agree with this template

    Returns
    -------
    functions: Dict (ordered after function index name) with keys being function names and values being the callable
    """

    this_module = sys.modules[__name__]

    functions = {}

    for func_idx in range(1, n_functions + 1):
        func_name = func_name_templ.format(func_idx)
        callable_func = getattr(this_module, func_name)
        functions[func_name] = callable_func

    return functions


def aggregate_feature_matrix(train_X, callable_func_dict):
    """Runs each transformer function in callable_function_dict on every sample in train_X creation a feature matrix."""

    train_X = train_X.as_matrix()

    feature_mat = []
    for sample in train_X:

        feature_vec = []
        for transformer in callable_func_dict.values():
            feature_vec.append(transformer(sample))

        feature_mat.append(feature_vec)

    feature_mat = pd.DataFrame(feature_mat, columns=callable_func_dict.keys())
    print('Aggregated feature matrix of shape: {}'.format(feature_mat.shape))

    return feature_mat


def phi_1(feature):
    return feature[0]


def phi_2(feature):
    return feature[1]


def phi_3(feature):
    return feature[2]


def phi_4(feature):
    return feature[3]


def phi_5(feature):
    return feature[4]


def phi_6(feature):
    return feature[0] ** 2


def phi_7(feature):
    return feature[1] ** 2


def phi_8(feature):
    return feature[2] ** 2


def phi_9(feature):
    return feature[3] ** 2


def phi_10(feature):
    return feature[4] ** 2


def phi_11(feature):
    return exp(feature[0])


def phi_12(feature):
    return exp(feature[1])


def phi_13(feature):
    return exp(feature[2])


def phi_14(feature):
    return exp(feature[3])


def phi_15(feature):
    return exp(feature[4])


def phi_16(feature):
    return cos(feature[0])


def phi_17(feature):
    return cos(feature[1])


def phi_18(feature):
    return cos(feature[2])


def phi_19(feature):
    return cos(feature[3])


def phi_20(feature):
    return cos(feature[4])


def phi_21(feature):
    return 1


