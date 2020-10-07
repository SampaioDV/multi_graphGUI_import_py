import tkinter as tk
from classes import Project


class App:

    def __init__(self, master=None):

        self.master = master

        #####################################################

        self.project = Project()  # Instanciate Project Object

        # ############################### App_Frames ######################
        # list box
        self.frm_lbx = tk.Frame(master)
        self.scroll = tk.Scrollbar(self.frm_lbx, orient='vertical')
        self.lbx = tk.Listbox(self.frm_lbx, heigh=20,
                              width=30, yscrollcommand=self.scroll.set,
                              selectmode='extended')
        self.scroll.config(command=self.lbx.yview)

        self.scroll.pack(side='right', fill='y')
        self.lbx.pack(pady=15)
        self.frm_lbx.pack()

        # buttons
        self.frm_btns = tk.Frame(master)
        self.btn_insert_file = tk.Button(master, text='Insert File(s)',
                                         command=self.select_files)
        self.btn_select_all = tk.Button(master, text='Select All',
                                        command=self.select_all)
        self.btn_graph = tk.Button(master=master, text='Make graph',
                                   command=self.func_graph)

        self.btn_insert_file.pack()
        self.btn_select_all.pack()
        self.btn_graph.pack()

        # Menu bar
        menu_bar = tk.Menu(master=self.master)
        self.master.config(menu=menu_bar)

        project_menu = tk.Menu(menu_bar)  # A submenu
        menu_bar.add_cascade(label='Project', menu=project_menu)

        project_menu.add_command(label='Load Project', command=self.func_load)
        project_menu.add_command(label='Save',
                                 command=self.project.save)
        project_menu.add_command(label='Save as',
                                 command=self.project.save)
        project_menu.add_separator()  # add a separador
        project_menu.add_command(label='Exit', command=self.master.destroy)
        # ########################### Functions ###############

    def select_files(self):
        project = self.project
        project.add_files()
        # Update list box
        self.lbx.delete(0, 'end')
        for item in project.files:
            self.lbx.insert('end', item.name)
        return

    def select_all(self):
        self.lbx.select_set(0, 'end')
        return

    def func_graph(self):
        self.project.make_graph(f_index=self.lbx.curselection())
        # funcs.plot_one_ax(project=self.project,
        #                   f_index=self.lbx.curselection())
        return

    def func_load(self):
        project = self.project
        project.load_project()
        for item in project.files:
            self.lbx.insert('end', item.name)
        for graph in project.graphs:
            graph.fig.show()
