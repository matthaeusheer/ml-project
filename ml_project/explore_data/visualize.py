import matplotlib.pyplot as plt
import seaborn as sns


def plot_columns_serieses(data_frame, columns=None, y_label='', x_label='Sample index', figsize=(18, 5)):
    """Plots the values of the various feature vec entries vs feature index.

    Line plots for features will be slightly offset for better readability. However, thus, no scale is provided.
    """
    df_plot = data_frame.copy()

    n_cols = 1
    if columns:
        df_plot = df_plot[columns]

    if hasattr(df_plot, 'columns'):
        n_cols = len(df_plot.columns)
        offset_val = 30
        for idx, col in enumerate(df_plot.columns):
            df_plot[col] = df_plot[col] + offset_val * idx

    ax = df_plot.plot(figsize=figsize, legend=False, alpha=0.7)
    sns.despine(left=True, bottom=True, right=True)

    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.get_yaxis().set_ticks([])
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles[::-1], labels[::-1], facecolor='None', frameon=False, ncol=n_cols)
    plt.show()


def sns_correlation_plot(data_frame, figsize=(15, 12), cmap="YlGnBu"):
    """Produces a heatmap correlation plot of the given data frame."""

    plt.figure(figsize=figsize)
    correlation = data_frame.corr()  # corr() method of pandas library calculates correlation between columns
    sns.heatmap(correlation, cmap=cmap, annot=True)
    plt.show()
