from chainconsumer import ChainConsumer
import matplotlib as plt
import seaborn as sns

def chain_consumer(df, label, label0, label1, params):
    m = df[label] == 1
    label0_ = df.loc[m, params].values
    label1_ = df.loc[-m, params].values
    c = ChainConsumer()
    # chain is a sampling of a population that conforms to some statistical properties
    c.add_chain(label0_, parameters=params, name=label0, kde=1.0, color='b')
    c.add_chain(label1_, parameters=params, name=label1, kde=1.0, color='r')
    c.configure(contour_labels='confidence', usetex=False)
    c.plotter.plot(figsize=3.0)
    plt.pyplot.show()

# Interactive 3D Plot with Test Point (Multivariate Normal Distribution)
def get_df_y_df_n(df, columns, label):
    data_pa = df[columns]
    # Split data into two dataframes (datasets) for each label
    df_y = df.loc[data_pa[label] == 1, columns[:-1]]
    df_n = df.loc[data_pa[label] == 0, columns[:-1]]
    return (df_y, df_n)

def multivariate_normal_distribution(df_y, df_n, columns, label0, label1, test_point):
    fig = go.Figure()
    fig.add_trace(go.Scatter3d(x=df_y[columns[0]], y=df_y[columns[1]], z=df_y[columns[2]], mode='markers', name=label0))
    fig.add_trace(go.Scatter3d(x=df_n[columns[0]], y=df_n[columns[1]], z=df_n[columns[2]], mode='markers', name=label1))
    fig.add_trace(go.Scatter3d(x=[test_point[0]], y=[test_point[1]], z=[test_point[2]], mode='markers', name='Test'))

    fig.show()

def scatter_matrix_label0(df_y):
    sns.set(style='ticks')
    sns.pairplot(df_y, diag_kind='hist')
    plt.pyplot.show()

def scatter_matrix_label1(df_n):
    sns.set(style='ticks')
    sns.pairplot(df_n, diag_kind='hist')
    plt.pyplot.show()

# Test point probability
def test_point_prob(df_y, df_n, test_point):
    prob_test = []
    for d in [df_y, df_n]:
        mean = np.mean(d)  # compute the mean of our dataset
        cov = np.cov(d, rowvar=0)  # compute the covariance of our dataset

        # Here we evaluate the probabilities at all the points we have prepared previously
        # We pass the points to the pdf and say evaluate it using this mean and covariance
        prob = mn.pdf(test_point, mean, cov)
        prob_test.append(prob)

    num_y = df_y.shape[0]
    num_n = df_n.shape[0]

    return [[prob_test], num_y, num_n]

        # print("Number of people with diabetes is: ", num_y)
        #         print("Number of people without diabetes is: ", num_n)
        #         prob_diagnosis = num_y * prob_test[0] / (num_y * prob_test[0] + num_n * prob_test[1])
        #         print(f"Positive diagnosis chance is {100 * prob_diagnosis:.2f}%")
        # print(list[1] * list[0][0][0] / (list[1] * list[0][0][0] + list[2] * list[0][0][1]))

