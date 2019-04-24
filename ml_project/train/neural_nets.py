from datetime import datetime

import matplotlib.pyplot as plt


def plot_history(trained_models, key='acc'):
    """Given a list of [(name, trained_model), ...] tuples plot the training and validation accuracy."""
    plt.figure(figsize=(16, 10))

    for name, model in trained_models:
        history = model.history
        val = plt.plot(history.epoch, history.history['val_'+key],
                       '--', label=name.title()+' Validation')

        plt.plot(history.epoch, history.history[key], color=val[0].get_color(),
                 label=name.title()+' Training')
        plt.xlim([0, max(history.epoch)])

    plt.xlabel('Epochs')
    plt.ylabel(key.replace('_', ' ').title())
    plt.legend()


def get_date_time_tag():
    """Returns a datetime tag in the following example format '2019-04-01_20-24-13-535342'."""
    curr_time = datetime.now()
    return curr_time.strftime('%Y-%m-%d_%H-%M-%S-%f')

