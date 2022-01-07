from chainconsumer import ChainConsumer
import matplotlib as plt
import tkinter as tk
import seaborn as sns
import plotly.graph_objects as go
from scipy.stats import multivariate_normal as mn
import numpy as np

def chain_consumer(main_notebook, df, font, labels):
    frame = tk.Frame(main_notebook, bg='White', width=600, height=600, bd=5)
    frame.pack(fill='both', expand=1)

    main_notebook.add(frame, text='_Chain Consumer')

    frame1 = tk.LabelFrame(frame, text='Set Input', font=font)
    frame1.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.9)

    tk.Label(frame1, text="Param 1", font=font).place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.1)
    x_entry = tk.Entry(frame1, font=font)
    x_entry.place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.04)

    tk.Label(frame1, text="Param 2", font=font).place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.1)
    y_entry = tk.Entry(frame1, font=font)
    y_entry.place(relx=0.4, rely=0.5, relwidth=0.2, relheight=0.04)

    set_head = tk.Button(frame1, text='View Plot',
                           command=lambda: chain_entry_consumer(df, x_entry, y_entry, labels), font=font, bg='#008080',fg='White')
    set_head.place(relx=0.4, rely=0.6, relwidth=0.2, relheight=0.04)

    close = tk.Button(frame, text='Close', command=frame.destroy, font=font, bg='#008080', fg='White')
    close.place(relx=0.45, rely=0.95, relwidth=0.1, relheight=0.04)

def chain_entry_consumer(df, x, y, labels):
    params = []
    params.append(x.get())
    params.append(y.get())
    m = df[labels[0][1].label] == 1
    label1_ = df.loc[m, params].values
    label0_ = df.loc[-m, params].values
    c = ChainConsumer()
    # chain is a sampling of a population that conforms to some statistical properties
    c.add_chain(label0_, parameters=params, name=labels[1][1].label, kde=1.0, color='b')
    c.add_chain(label1_, parameters=params, name=labels[2][1].label, kde=1.0, color='r')
    c.configure(contour_labels='confidence', usetex=False)
    c.plotter.plot(figsize=3.0)
    plt.pyplot.show()

def scatter_matrix_label1(main_notebook, df, font, labels):
    frame = tk.Frame(main_notebook, bg='White', width=600, height=600, bd=5)
    frame.pack(fill='both', expand=1)

    main_notebook.add(frame, text='_Scatter Matrix 0')

    frame1 = tk.LabelFrame(frame, text='Set Input', font=font)
    frame1.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.9)

    tk.Label(frame1, text="Param 1", font=font).place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.1)
    x_entry = tk.Entry(frame1, font=font)
    x_entry.place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.04)

    tk.Label(frame1, text="Param 2", font=font).place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.1)
    y_entry = tk.Entry(frame1, font=font)
    y_entry.place(relx=0.4, rely=0.5, relwidth=0.2, relheight=0.04)

    tk.Label(frame1, text="Param 3", font=font).place(relx=0.4, rely=0.6, relwidth=0.2, relheight=0.1)
    z_entry = tk.Entry(frame1, font=font)
    z_entry.place(relx=0.4, rely=0.7, relwidth=0.2, relheight=0.04)

    set_head = tk.Button(frame1, text='View Plot',
                           command=lambda: scatter_matrix_entry_label1(df, x_entry, y_entry, z_entry, labels), font=font, bg='#008080',fg='White')
    set_head.place(relx=0.4, rely=0.8, relwidth=0.2, relheight=0.04)

    close = tk.Button(frame, text='Close', command=frame.destroy, font=font, bg='#008080', fg='White')
    close.place(relx=0.45, rely=0.95, relwidth=0.1, relheight=0.04)

def scatter_matrix_entry_label1(df, x, y, z, labels):
    params = []
    params.append(x.get())
    params.append(y.get())
    params.append(z.get())
    df_y = df.loc[df[labels[0][1].label] == 1, params]
    sns.set(style='ticks')
    sns.pairplot(df_y, diag_kind='hist')
    plt.pyplot.show()

def scatter_matrix_label0(main_notebook, df, font, labels):
    frame = tk.Frame(main_notebook, bg='White', width=600, height=600, bd=5)
    frame.pack(fill='both', expand=1)

    main_notebook.add(frame, text='_Scatter Matrix 1')

    frame1 = tk.LabelFrame(frame, text='Set Input', font=font)
    frame1.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.9)

    tk.Label(frame1, text="Param 1", font=font).place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.1)
    x_entry = tk.Entry(frame1, font=font)
    x_entry.place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.04)

    tk.Label(frame1, text="Param 2", font=font).place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.1)
    y_entry = tk.Entry(frame1, font=font)
    y_entry.place(relx=0.4, rely=0.5, relwidth=0.2, relheight=0.04)

    tk.Label(frame1, text="Param 3", font=font).place(relx=0.4, rely=0.6, relwidth=0.2, relheight=0.1)
    z_entry = tk.Entry(frame1, font=font)
    z_entry.place(relx=0.4, rely=0.7, relwidth=0.2, relheight=0.04)

    set_head = tk.Button(frame1, text='View Plot',
                           command=lambda: scatter_matrix_entry_label0(df, x_entry, y_entry, z_entry, labels), font=font, bg='#008080',fg='White')
    set_head.place(relx=0.4, rely=0.8, relwidth=0.2, relheight=0.04)

    close = tk.Button(frame, text='Close', command=frame.destroy, font=font, bg='#008080', fg='White')
    close.place(relx=0.45, rely=0.95, relwidth=0.1, relheight=0.04)

def scatter_matrix_entry_label0(df, x, y, z, labels):
    params = []
    params.append(x.get())
    params.append(y.get())
    params.append(z.get())
    df_n = df.loc[df[labels[0][1].label] == 0, params]
    sns.set(style='ticks')
    sns.pairplot(df_n, diag_kind='hist')
    plt.pyplot.show()

# Interactive 3D Plot with Test Point (Multivariate Normal Distribution)
def multivariate_normal_distribution(main_notebook, df, font, labels):
    frame = tk.Frame(main_notebook, bg='White', width=600, height=600, bd=5)
    frame.pack(fill='both', expand=1)

    main_notebook.add(frame, text='_Multivariate Normal Distribution')

    frame1 = tk.LabelFrame(frame, text='Set Input', font=font)
    frame1.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.9)

    tk.Label(frame1, text="Param 1", font=font).place(relx=0.25, rely=0.3, relwidth=0.2, relheight=0.1)
    x = tk.Entry(frame1, font=font)
    x.place(relx=0.45, rely=0.325, relwidth=0.2, relheight=0.04)

    tk.Label(frame1, text="Param 2", font=font).place(relx=0.25, rely=0.4, relwidth=0.2, relheight=0.1)
    y = tk.Entry(frame1, font=font)
    y.place(relx=0.45, rely=0.425, relwidth=0.2, relheight=0.04)

    tk.Label(frame1, text="Param 3", font=font).place(relx=0.25, rely=0.5, relwidth=0.2, relheight=0.1)
    z = tk.Entry(frame1, font=font)
    z.place(relx=0.45, rely=0.525, relwidth=0.2, relheight=0.04)

    tk.Label(frame1, text="Test 1", font=font).place(relx=0.25, rely=0.6, relwidth=0.2, relheight=0.1)
    a = tk.Entry(frame1, font=font)
    a.place(relx=0.45, rely=0.625, relwidth=0.2, relheight=0.04)

    tk.Label(frame1, text="Test 2", font=font).place(relx=0.25, rely=0.7, relwidth=0.2, relheight=0.1)
    b = tk.Entry(frame1, font=font)
    b.place(relx=0.45, rely=0.725, relwidth=0.2, relheight=0.04)

    tk.Label(frame1, text="Test 3", font=font).place(relx=0.25, rely=0.8, relwidth=0.2, relheight=0.1)
    c = tk.Entry(frame1, font=font)
    c.place(relx=0.45, rely=0.825, relwidth=0.2, relheight=0.04)

    set_head = tk.Button(frame1, text='View Plot',
                         command=lambda: multivariate_normal_entry_distribution(df, x, y, z, a, b, c, labels, font, frame1), font=font, bg='#008080',fg='White')
    set_head.place(relx=0.4, rely=0.9, relwidth=0.2, relheight=0.04)

    close = tk.Button(frame, text='Close', command=frame.destroy, font=font, bg='#008080', fg='White')
    close.place(relx=0.45, rely=0.95, relwidth=0.1, relheight=0.04)

def multivariate_normal_entry_distribution(df, x, y, z, a, b, c, labels, font, frame1):
    params = []
    params.append(x.get())
    params.append(y.get())
    params.append(z.get())

    df_y = df.loc[df[labels[0][1].label] == 1, params]
    df_n = df.loc[df[labels[0][1].label] == 0, params]

    test_point = []
    test_point.append(int(a.get()))
    test_point.append(int(b.get()))
    test_point.append(int(c.get()))

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

    prob_diagnosis = num_y * prob_test[0] / (num_y * prob_test[0] + num_n * prob_test[1])
    #         print(f"")
    #list[1] * list[0][0][0] / (list[1] * list[0][0][0] + list[2] * list[0][0][1])

    output_text = f'Number of people with diabetes is: {num_y}.\n' \
                  f'Number of people without diabetes is: {num_n}.\n' \
                  f'Positive diagnosis chance is (weighted probability): {100 * prob_diagnosis:.2f}%.'

    output = tk.Label(frame1, text=output_text, font=font)
    output.place(relx=0, rely=0.05, relwidth=1, relheight=0.2)

    fig = go.Figure()
    fig.add_trace(go.Scatter3d(x=df_y[params[0]], y=df_y[params[1]], z=df_y[params[2]], mode='markers', name=labels[2][1].label))
    fig.add_trace(go.Scatter3d(x=df_n[params[0]], y=df_n[params[1]], z=df_n[params[2]], mode='markers', name=labels[1][1].label))
    fig.add_trace(go.Scatter3d(x=[test_point[0]], y=[test_point[1]], z=[test_point[2]], mode='markers', name='Test'))

    fig.show()



