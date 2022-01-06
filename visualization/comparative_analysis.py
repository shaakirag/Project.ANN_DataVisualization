import matplotlib as plt
import seaborn as sns
import numpy as np
import tkinter as tk

# Correlation Table
def correlation_table(main_notebook, df, font):
    frame = tk.Frame(main_notebook, bg='White', width=600, height=600, bd=5)
    frame.pack(fill='both', expand=1)

    main_notebook.add(frame, text='Correlation')

    frame1 = tk.LabelFrame(frame, text='Correlation Table', font=font)
    frame1.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.9)

    output = tk.Label(frame1, text=df.corr(), font=(font, 8))
    output.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

    set_head = tk.Button(frame1, text='View Plot',
                           command=lambda: correlation_plot(df), font=font, bg='#008080',fg='White')
    set_head.place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.04)

    close = tk.Button(frame, text='Close', command=frame.destroy, font=font, bg='#008080', fg='White')
    close.place(relx=0.45, rely=0.95, relwidth=0.1, relheight=0.04)

# Correlation Plot
def correlation_plot(df):
    sns.heatmap(np.abs(df.corr()), annot=True, cmap='viridis', fmt='0.2f')
    plt.pyplot.show()

# Covariance Table
def covariance_table(main_notebook, df, font):
    frame = tk.Frame(main_notebook, bg='White', width=600, height=600, bd=5)
    frame.pack(fill='both', expand=1)

    main_notebook.add(frame, text='Covariance')

    frame1 = tk.LabelFrame(frame, text='Covariance Table', font=font)
    frame1.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.9)

    output = tk.Label(frame1, text=df.corr(), font=(font, 8))
    output.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

    set_head = tk.Button(frame1, text='View Plot',
                           command=lambda: covariance_plot(df), font=font, bg='#008080',fg='White')
    set_head.place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.04)

    close = tk.Button(frame, text='Close', command=frame.destroy, font=font, bg='#008080', fg='White')
    close.place(relx=0.45, rely=0.95, relwidth=0.1, relheight=0.04)

# Covariance Plot
def covariance_plot(df):
    plt.pyplot.figure(figsize=(9, 9))
    sns.heatmap(np.abs(df.cov()), annot=True, cmap='viridis', fmt='0.2f')
    plt.pyplot.show()

def box_plot(main_notebook, df, font):
    frame = tk.Frame(main_notebook, bg='White', width=600, height=600, bd=5)
    frame.pack(fill='both', expand=1)

    main_notebook.add(frame, text='_Box Plot')

    frame1 = tk.LabelFrame(frame, text='Set Input', font=font)
    frame1.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.9)

    tk.Label(frame1, text="Independent", font=font).place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.1)
    x_entry = tk.Entry(frame1, font=font)
    x_entry.place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.04)

    tk.Label(frame1, text="Dependent", font=font).place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.1)
    y_entry = tk.Entry(frame1, font=font)
    y_entry.place(relx=0.4, rely=0.5, relwidth=0.2, relheight=0.04)

    set_head = tk.Button(frame1, text='View Plot',
                           command=lambda: box_entry_plot(df, x_entry, y_entry), font=font, bg='#008080',fg='White')
    set_head.place(relx=0.4, rely=0.6, relwidth=0.2, relheight=0.04)

    close = tk.Button(frame, text='Close', command=frame.destroy, font=font, bg='#008080', fg='White')
    close.place(relx=0.45, rely=0.95, relwidth=0.1, relheight=0.04)

# Box Plot
def box_entry_plot(df, x, y):
    sns.boxplot(x=x.get(), y=y.get(), data=df, whis=0.3)
    sns.swarmplot(x=x.get(), y=y.get(), data=df, color='k', alpha=0.3)
    plt.pyplot.show()

#  Violin Plot
def violin_plot(main_notebook, df, font):
    frame = tk.Frame(main_notebook, bg='White', width=600, height=600, bd=5)
    frame.pack(fill='both', expand=1)

    main_notebook.add(frame, text='_Violin Plot')

    frame1 = tk.LabelFrame(frame, text='Set Input', font=font)
    frame1.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.9)

    tk.Label(frame1, text="Independent", font=font).place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.1)
    x_entry = tk.Entry(frame1, font=font)
    x_entry.place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.04)

    tk.Label(frame1, text="Dependent", font=font).place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.1)
    y_entry = tk.Entry(frame1, font=font)
    y_entry.place(relx=0.4, rely=0.5, relwidth=0.2, relheight=0.04)

    set_head = tk.Button(frame1, text='View Plot',
                           command=lambda: violin_entry_plot(df, x_entry, y_entry), font=font, bg='#008080',fg='White')
    set_head.place(relx=0.4, rely=0.6, relwidth=0.2, relheight=0.04)

    close = tk.Button(frame, text='Close', command=frame.destroy, font=font, bg='#008080', fg='White')
    close.place(relx=0.45, rely=0.95, relwidth=0.1, relheight=0.04)

def violin_entry_plot(df, x, y):
    sns.violinplot(x=x.get(), y=y.get(), data=df)
    sns.swarmplot(x=x.get(), y=y.get(), data=df, color='k', alpha=0.3)
    plt.pyplot.show()

#  2D Histogram
def twoD_histogram(main_notebook, df, font):
    frame = tk.Frame(main_notebook, bg='White', width=600, height=600, bd=5)
    frame.pack(fill='both', expand=1)

    main_notebook.add(frame, text='_2D Histogram')

    frame1 = tk.LabelFrame(frame, text='Set Input', font=font)
    frame1.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.9)

    tk.Label(frame1, text="Independent", font=font).place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.1)
    x_entry = tk.Entry(frame1, font=font)
    x_entry.place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.04)

    tk.Label(frame1, text="Dependent", font=font).place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.1)
    y_entry = tk.Entry(frame1, font=font)
    y_entry.place(relx=0.4, rely=0.5, relwidth=0.2, relheight=0.04)

    set_head = tk.Button(frame1, text='View Plot',
                           command=lambda: twoD_entry_histogram(df, x_entry, y_entry), font=font, bg='#008080',fg='White')
    set_head.place(relx=0.4, rely=0.6, relwidth=0.2, relheight=0.04)

    close = tk.Button(frame, text='Close', command=frame.destroy, font=font, bg='#008080', fg='White')
    close.place(relx=0.45, rely=0.95, relwidth=0.1, relheight=0.04)

def twoD_entry_histogram(df, x, y):
    plt.pyplot.figure(figsize=(9,9))
    plt.pyplot.hist2d(df[x.get()], df[y.get()], bins=(20,20), cmap='magma')
    plt.pyplot.xlabel(x.get())
    plt.pyplot.ylabel(y.get())
    plt.pyplot.colorbar()
    plt.pyplot.show()

#  Contour Plot
# bin_no recommended is 20
def contour_plot(main_notebook, df, font):
    frame = tk.Frame(main_notebook, bg='White', width=600, height=600, bd=5)
    frame.pack(fill='both', expand=1)

    main_notebook.add(frame, text='_Contour Plot')

    frame1 = tk.LabelFrame(frame, text='Set Input', font=font)
    frame1.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.9)

    tk.Label(frame1, text="Independent", font=font).place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.1)
    x_entry = tk.Entry(frame1, font=font)
    x_entry.place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.04)

    tk.Label(frame1, text="Dependent", font=font).place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.1)
    y_entry = tk.Entry(frame1, font=font)
    y_entry.place(relx=0.4, rely=0.5, relwidth=0.2, relheight=0.04)

    set_head = tk.Button(frame1, text='View Plot',
                           command=lambda: twoD_entry_histogram(df, x_entry, y_entry), font=font, bg='#008080',fg='White')
    set_head.place(relx=0.4, rely=0.6, relwidth=0.2, relheight=0.04)

    close = tk.Button(frame, text='Close', command=frame.destroy, font=font, bg='#008080', fg='White')
    close.place(relx=0.45, rely=0.95, relwidth=0.1, relheight=0.04)

def contour_entry_plot(df, x, y):
    hist, x_edge, y_edge = np.histogram2d(df[x.get()], df[y.get()], bins=20)

    # centre of bins
    x_centre = 0.5*(x_edge[1:] + x_edge[:-1])
    y_centre = 0.5*(y_edge[1:] + y_edge[:-1])

    plt.pyplot.contour(x_centre, y_centre, hist, levels=6)
    plt.pyplot.xlabel(x.get())
    plt.pyplot.ylabel(y.get())
    plt.pyplot.colorbar()
    plt.pyplot.show()

#  KDE Plot
def kde_plot(main_notebook, df, font):
    frame = tk.Frame(main_notebook, bg='White', width=600, height=600, bd=5)
    frame.pack(fill='both', expand=1)

    main_notebook.add(frame, text='_KDE Plot')

    frame1 = tk.LabelFrame(frame, text='Set Input', font=font)
    frame1.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.9)

    tk.Label(frame1, text="Independent", font=font).place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.1)
    x_entry = tk.Entry(frame1, font=font)
    x_entry.place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.04)

    tk.Label(frame1, text="Dependent", font=font).place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.1)
    y_entry = tk.Entry(frame1, font=font)
    y_entry.place(relx=0.4, rely=0.5, relwidth=0.2, relheight=0.04)

    set_head = tk.Button(frame1, text='View Plot',
                           command=lambda: kde_entry_plot(df, x_entry, y_entry), font=font, bg='#008080',fg='White')
    set_head.place(relx=0.4, rely=0.6, relwidth=0.2, relheight=0.04)

    close = tk.Button(frame, text='Close', command=frame.destroy, font=font, bg='#008080', fg='White')
    close.place(relx=0.45, rely=0.95, relwidth=0.1, relheight=0.04)

def kde_entry_plot(df, x, y):
    plt.pyplot.figure(figsize=(9,9))
    #sns.kdeplot(x=df[x], y=df[y], cmap='viridis', bw_method=0.5)
    sns.kdeplot(x=df[x.get()], y=df[y.get()], cmap='magma', shade=True, cbar=True);
    plt.pyplot.hist2d(df[x.get()], df[y.get()], bins=20, cmap='magma', alpha=0.5)
    plt.pyplot.colorbar()
    plt.pyplot.show()

#  Simple Scatter Plot
def scatter_plot(main_notebook, df, font, labels):
    frame = tk.Frame(main_notebook, bg='White', width=600, height=600, bd=5)
    frame.pack(fill='both', expand=1)

    main_notebook.add(frame, text='_Scatter Plot')

    frame1 = tk.LabelFrame(frame, text='Set Input', font=font)
    frame1.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.9)

    tk.Label(frame1, text="Independent", font=font).place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.1)
    x_entry = tk.Entry(frame1, font=font)
    x_entry.place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.04)

    tk.Label(frame1, text="Dependent", font=font).place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.1)
    y_entry = tk.Entry(frame1, font=font)
    y_entry.place(relx=0.4, rely=0.5, relwidth=0.2, relheight=0.04)

    set_head = tk.Button(frame1, text='View Plot',
                           command=lambda: scatter_entry_plot(df, x_entry, y_entry, labels), font=font, bg='#008080',fg='White')
    set_head.place(relx=0.4, rely=0.6, relwidth=0.2, relheight=0.04)

    close = tk.Button(frame, text='Close', command=frame.destroy, font=font, bg='#008080', fg='White')
    close.place(relx=0.45, rely=0.95, relwidth=0.1, relheight=0.04)

def scatter_entry_plot(df, x, y, labels):
    plt.pyplot.figure(figsize=(9,9))
    m = df[labels[0][1].label] == 1
    plt.pyplot.scatter(df.loc[m, x.get()], df.loc[m, y.get()], c='r', s=15, label=labels[1][1].label)
    plt.pyplot.scatter(df.loc[-m, x.get()], df.loc[-m, y.get()], c='b', s=15, label=labels[2][1].label)
    plt.pyplot.xlabel(x.get())
    plt.pyplot.ylabel(y.get())
    plt.pyplot.legend(loc=2)
    plt.pyplot.show()
