from all_libs import *

# Correlation Table
def correlation_table(df):
    return df.corr()

# Correlation Plot
def correlation_plot(df):
    sns.heatmap(np.abs(df.corr()), annot=True, cmap='viridis', fmt='0.2f')
    plt.pyplot.show()

# Covariance Table
def covariance_table(df):
    return df.cov()

# Covariance Plot
def covariance_plot(df):
    plt.pyplot.figure(figsize=(9, 9))
    sns.heatmap(np.abs(df.cov()), annot=True, cmap='viridis', fmt='0.2f')
    plt.pyplot.show()

# Scatter Matrix for diabetic and non diabetic

# Box Plot
def box_plot(df, x, y):
    sns.boxplot(x=x, y=y, data=df, whis=0.3)
    sns.swarmplot(x=x, y=y, data=df, color='k', alpha=0.3)
    plt.pyplot.show()

#  Violin Plot
def violin_plot(df, x, y):
    sns.violinplot(x=x, y=y, data=df)
    sns.swarmplot(x=x, y=y, data=df, color='k', alpha=0.3)
    plt.pyplot.show()

#  2D Histogram
def twoD_histogram(df, x, y):
    plt.pyplot.figure(figsize=(9,9))
    plt.pyplot.hist2d(df[x], df[y], bins=(20,20), cmap='magma')
    plt.pyplot.xlabel(x)
    plt.pyplot.ylabel(y)
    plt.pyplot.colorbar()
    plt.pyplot.show()

#  Contour Plot
# bin_no recommended is 20
def contour_plot(df, x, y, bin_no):
    hist, x_edge, y_edge = np.histogram2d(df[x], df[y], bins=bin_no)

    # centre of bins
    x_centre = 0.5*(x_edge[1:] + x_edge[:-1])
    y_centre = 0.5*(y_edge[1:] + y_edge[:-1])

    plt.pyplot.contour(x_centre, y_centre, hist, levels=6)
    plt.pyplot.xlabel(x)
    plt.pyplot.ylabel(y)
    plt.pyplot.colorbar()
    plt.pyplot.show()

#  KDE Plot
def kde_plot(df, x, y):
    plt.pyplot.figure(figsize=(9,9))
    #sns.kdeplot(x=df[x], y=df[y], cmap='viridis', bw_method=0.5)
    sns.kdeplot(x=df[x], y=df[y], cmap='magma', shade=True, cbar=True);
    plt.pyplot.hist2d(df[x], df[y], bins=20, cmap='magma', alpha=0.5)
    plt.pyplot.colorbar()
    plt.pyplot.show()

#  Simple Scatter Plot
def scatter_plot(df, x, y, label, labels):
    plt.pyplot.figure(figsize=(9,9))
    m = df[label] == 1
    plt.pyplot.scatter(df.loc[m, x], df.loc[m, y], c='r', s=15, label=labels[0])
    plt.pyplot.scatter(df.loc[-m, x], df.loc[-m, y], c='b', s=15, label=labels[1])
    plt.pyplot.xlabel(x)
    plt.pyplot.ylabel(y)
    plt.pyplot.legend(loc=2)
    plt.pyplot.show()
