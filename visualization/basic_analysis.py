import matplotlib as plt
import seaborn as sns

# Count Plot
def count_plot(df, labels):
    f, ax = plt.pyplot.subplots(1,2,figsize=(10,5))
    df[labels[0][1].label].value_counts().plot.pie(explode=[0,0.1],autopct='%1.1f%%', ax=ax[0], shadow=True)
    ax[0].set_title(labels[0][1].label)
    ax[0].set_ylabel('')
    sns.countplot(labels[0][1].label, data=df, ax=ax[1])
    ax[1].set_title(labels[0][1].label)
    N,P = df[labels[0][1].label].value_counts()
    plt.pyplot.grid()
    plt.pyplot.show()

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


