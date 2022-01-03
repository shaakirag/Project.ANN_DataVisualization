from all_libs import *

# Count Plot
def count_plot(df, header_list):
    pass

#  Histograms
def count_histogram(df, header_list):
    for h in header_list:
        sns.displot(df[h], rug=True)
        plt.pyplot.show()

#  Scatter Matrix (questionable)
def scatter_matrix(df, label):
    for i, col in enumerate(df.columns[:-1]):
        sns.pairplot(df, hue=label, diag_kind='hist')
        plt.pyplot.show()

