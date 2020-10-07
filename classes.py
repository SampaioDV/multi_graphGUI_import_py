from tkinter import filedialog
import os
import ntpath
import pandas as pd
import matplotlib.pyplot as plt
import pickle


class Project(object):
    """A class that contain the project"""

    def __init__(self):
        self.files = []   # each element is a Data_file object
        self.graphs = []  # each element is a Figure object
        self.path_prj = None

    def add_files(self):
        """Function to open file dialog and Create a data file object and add
         to self.data_files """

        # list of data paths
        initdir = os.getcwd()
        l_f_paths = filedialog.askopenfilename(initialdir=initdir,
                                               title='Select File',
                                               filetypes=(('all files', '*.*'),
                                                          ('csv files',
                                                           '*.csv'),
                                                          ('txt files',
                                                           '*.txt'),
                                                          ('dat files',
                                                           '*.dat')),
                                               multiple=True)

        for path in l_f_paths:
            # Create data_file and sotore in files attribute
            self.files.append(Data_file(file_path=path))

    def remove_file(self):
        pass

    def make_graph(self, f_index=[0], *args, **kwargs):
        l_files = [self.files[ii] for ii in f_index]
        # Create graph of selected files, plot, and store at graphs attribute
        graph = Graph(l_files=l_files)
        graph.plot_graph()
        self.graphs.append(graph)

    def save(self):
        if self.path_prj is None:
            initdir = os.getcwd()
            path_prj = filedialog.asksaveasfilename(initialdir=initdir,
                                                    filetypes=[("pickle",
                                                                "*.pickle"),
                                                               ("All files",
                                                                "*.*")])
        if self.path_prj:
            path_prj = self.path_prj

        with open(path_prj, 'wb') as file_w:
            pickle.dump(self.files, file_w)
            pickle.dump(self.graphs, file_w)

        self.path_prj = path_prj

    def load_project(self):
        initdir = os.getcwd()
        path_prj = filedialog.askopenfilename(initialdir=initdir,
                                              filetypes=[("pickle",
                                                          "*.pickle"),
                                                         ("All files",
                                                          "*.*")])
        with open(path_prj, 'rb') as file_r:
            self.files = pickle.load(file_r)
            self.graphs = pickle.load(file_r)

        if self.path_prj is None:
            self.path_prj = path_prj


class Data_file(object):
    """A class that that provides all data file information,
     including the data itself."""

    def __init__(self, file_path):
        self.path = file_path
        self.name = str(ntpath.basename(file_path)[:-4])
        self.df = pd.read_csv(file_path, sep=None, engine='python',
                              header=None, index_col=False)


class Graph(object):
    def __init__(self, l_files, *args, **kwargs):
        self.files = l_files
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)

    def plot_graph(self):
        for data_files in self.files:
            data = data_files
            self.ax.plot(data.df.iloc[:, 0], data.df.iloc[:, 1],
                         label=data.name)

        self.ax.legend()
        self.fig.show()
