import os

import pandas as pd

from common import DATA_DIR_PATH

TRAIN_FILE_NAME = 'train.csv'
TEST_FILE_NAME = 'test.csv'


class DataHandler:

    def __init__(self, dir_name):
        self.dir_name = dir_name

    def load_train_and_test_data(self):
        """Loads the training and test data in the specified data directory into pandas data frames.

        Returns
        -------
            data: A dict with keys 'train_data' and 'test_data' while entries hold corresponding pandas data frames.
        """

        if not os.path.exists(os.path.join(DATA_DIR_PATH, self.dir_name)):
            raise IOError('Your specified folder {} does not exist. '
                          'Place a folder called {} into the main '
                          'data directory located at {} which then '
                          'holds the a {} and {} file.'.format(self.dir_name, self.dir_name, DATA_DIR_PATH,
                                                               TEST_FILE_NAME, TRAIN_FILE_NAME))

        for file_name in [TRAIN_FILE_NAME, TEST_FILE_NAME]:
            if not os.path.exists(os.path.join(DATA_DIR_PATH, self.dir_name, file_name)):
                raise IOError('Your data directory, {}, has to hold a file named {}'.format(self.dir_name, file_name))

        train_data = pd.read_csv(os.path.join(DATA_DIR_PATH, self.dir_name, TRAIN_FILE_NAME)).set_index('Id')
        test_data = pd.read_csv(os.path.join(DATA_DIR_PATH, self.dir_name, TEST_FILE_NAME)).set_index('Id')

        data = {'train_data': train_data,
                'test_data': test_data}

        return data

    def store_prediction_file(self, predictions, header='Id,y', out_file_name='predictions.csv'):
        """Given a pandas series of predictions for samples, store those to a csv file in the data directory.

        Arguments
        ---------
        predictions: Pandas Series holding predicted values for given a set of samples.
        header: To be conform with the required data format.
        out_file_name: Name of the file which will be placed in output directory.
        """

        predictions.to_csv(os.path.join(DATA_DIR_PATH, self.dir_name, out_file_name), header=header)

