import tkinter as tk
import seaborn as sns
import matplotlib as plt
plt.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

# Count Plot
def count_plot(df, labels):
    f, ax = plt.pyplot.subplots(1,2,figsize=(10,5))
    df[labels[0][1].label].value_counts().plot.pie(explode=[0,0.1],autopct='%1.1f%%', ax=ax[0], shadow=True)
    ax[0].set_title(labels[0][1].label)
    ax[0].set_ylabel('')
    sns.countplot(x=labels[0][1].label, data=df, ax=ax[1])
    ax[1].set_title(labels[0][1].label)

    plt.pyplot.show()

    #canvas = FigureCanvasTkAgg(f, master=frame)
    #canvas.draw()
    #canvas.get_tk_widget().place(relx=0.2, rely=0.1, relwidth=0.9, relheight=0.9)
    #toolbar = NavigationToolbar2Tk(canvas, frame)
    #toolbar.update()
    #canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

#  Histograms
def count_histogram(main_notebook, df, font):
    frame = tk.Frame(main_notebook, bg='White', width=600, height=600, bd=5)
    frame.pack(fill='both', expand=1)

    main_notebook.add(frame, text='_Count Histogram')

    frame1 = tk.LabelFrame(frame, text='Set Input', font=font)
    frame1.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.9)

    tk.Label(frame1, text="Header", font=font).place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.1)
    h_entry = tk.Entry(frame1, font=font)
    h_entry.place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.04)

    set_h = tk.Button(frame, text='Set Value',
                           command=lambda: set_h_field(h_entry, df), font=font, bg='#008080',fg='White')
    set_h.place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.04)


    close = tk.Button(frame, text='Close', command=frame.destroy, font=font, bg='#008080', fg='White')
    close.place(relx=0.45, rely=0.95, relwidth=0.1, relheight=0.04)

def set_h_field(h_entry, df):
    sns.histplot(data=df, x=df[h_entry.get()])
    plt.pyplot.show()


#  Scatter Matrix
def scatter_matrix(df,labels):
    for i, col in enumerate(df.columns[:-1]):
        sns.pairplot(df, hue=labels[0][1].label, diag_kind='hist')
        plt.pyplot.show()


