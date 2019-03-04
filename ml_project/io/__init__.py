import os

import numpy as np
import pandas as pd

from common import DATA_DIR_PATH

TRAIN_FILE_NAME = 'train.csv'
TEST_FILE_NAME = 'test.csv'


class DataHandler:

    def __init__(self, dir_name):
        self.dir_name = dir_name

    def _load_csv_file_from_data_dir(self, file_name):

        if file_name not in [TRAIN_FILE_NAME, TEST_FILE_NAME]:
            raise ValueError('File name should be {} or {}'.format(TRAIN_FILE_NAME, TEST_FILE_NAME))

        if not os.path.exists(os.path.join(DATA_DIR_PATH, self.dir_name)):
            raise IOError('Your specified folder {} does not exist. '
                          'Place a folder called {} into the main '
                          'data directory located at {} which then '
                          'holds the a {} file.'.format(self.dir_name, self.dir_name, DATA_DIR_PATH, file_name))

        if not os.path.exists(os.path.join(DATA_DIR_PATH, self.dir_name, file_name)):
            print(os.path.join(DATA_DIR_PATH, self.dir_name, file_name))
            raise IOError('Your data directory, {}, has to hold a file named {}'.format(self.dir_name, file_name))

        return pd.read_csv(os.path.join(DATA_DIR_PATH, self.dir_name, file_name)).set_index('Id')

    def load_test_data(self):
        """Loads the test data in the specified data directory into pandas data frame.

        Returns
        -------
            Pandas Data Frame holding the test data.
        """

        return self._load_csv_file_from_data_dir(TEST_FILE_NAME)

    def load_train_data(self):
        """Loads the train data in the specified data directory into pandas data frame.

        Returns
        -------
            Pandas Data Frame holding the train data.
        """

        return self._load_csv_file_from_data_dir(TRAIN_FILE_NAME)

    def store_prediction_file(self, predictions, out_file_name='predictions.csv'):
        """Given a pandas series of predictions for samples, store those to a csv file in the data directory.

        Arguments
        ---------
        predictions: Pandas Series holding predicted values for given a set of samples.
        out_file_name: Name of the file which will be placed in output directory.
        """

        predictions.to_csv(os.path.join(DATA_DIR_PATH, self.dir_name, out_file_name))

    def store_results_task1a(self, avg_rms_errors, out_file_name='results_task1a.txt'):
        
        np.savetxt(os.path.join(DATA_DIR_PATH, self.dir_name, out_file_name), avg_rms_errors, fmt='%f')

    def store_results_task1b(self, weight_vector, out_file_name='results_task1b.txt'):

        np.savetxt(os.path.join(DATA_DIR_PATH, self.dir_name, out_file_name), weight_vector, fmt='%f')

