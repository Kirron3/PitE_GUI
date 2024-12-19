import tkinter as tk
from tkinter import ttk, filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.figure import Figure

class SimpleDataVisualizer:
    def __init__(self,root):
        self.root = root
        self.root.title("Data Visualizer")
        self.df = None
        
        # Make window responsive
        self.root.state('zoomed')
        for i in range(3):
            self.root.grid_columnconfigure(i, weight=1)
            self.root.grid_rowconfigure(i,weight=1)
        
        # File loading section
        load_frame = ttk.Frame(root)
        load_frame.grid(row=0, column=0,columnspan=3, sticky='ew',padx=10,pady=5)
        
        self.load_button = ttk.Button(load_frame,text="Load File",command=self.load_file)
        self.load_button.pack(side='left',padx=5)
        
        ttk.Label(load_frame,text="File Type:").pack(side='left',padx=5)
        self.file_type = ttk.Combobox(load_frame,values=["CSV","TXT", "Excel"],width=10)
        self.file_type.set("CSV")
        self.file_type.pack(side='left',padx=5)

        # Add file path label
        self.file_path_label = ttk.Label(load_frame,text="No file selected")
        self.file_path_label.pack(side='left',padx=20)
        
        # Preview
        preview_frame=ttk.LabelFrame(root,text="Data Preview")
        preview_frame.grid(row=1,column=0,columnspan=3,sticky='nsew',padx=10,pady=5)
        
        self.tree = ttk.Treeview(preview_frame,height=5)
        self.tree.pack(fill='both',expand=True,padx=5,pady=5)
        
        # Plot controls
        controls_frame = ttk.Frame(root)
        controls_frame.grid(row=2,column=0,columnspan=3,sticky='ew',padx=10,pady=5)
        
        ttk.Label(controls_frame,text="X Axis:").pack(side='left',padx=5)
        self.x_axis = ttk.Combobox(controls_frame,width=15)
        self.x_axis.pack(side='left',padx=5)
        
        ttk.Label(controls_frame,text="Y Axis:").pack(side='left',padx=5)
        self.y_axis = ttk.Combobox(controls_frame,width=15)
        self.y_axis.pack(side='left',padx=5)
        
        ttk.Label(controls_frame,text="Plot Type:").pack(side='left',padx=5)
        self.plot_type = ttk.Combobox(controls_frame,values=["scatter","line", "bar"])
        self.plot_type.set("line") 
        self.plot_type.pack(side='left',padx=5)
        
        self.plot_button = ttk.Button(controls_frame,text="Plot",command=self.plot_data)
        self.plot_button.pack(side='left',padx=5)
        
        # Plot area with navigation toolbar
        plot_frame = ttk.Frame(root)
        plot_frame.grid(row=3,column=0,columnspan=3,sticky='nsew',padx=10,pady=5)
        
        self.figure = Figure(figsize=(6,4))
        self.canvas = FigureCanvasTkAgg(self.figure,master=plot_frame)
        self.canvas.get_tk_widget().pack(side='top',fill='both',expand=True)
        
        # Add navigation toolbar
        self.toolbar = NavigationToolbar2Tk(self.canvas,plot_frame)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack(side='bottom',fill='both',expand=True)

    def load_file(self):
        filetypes = {"CSV":"*.csv", "TXT":"*.txt", "Excel":"*.xlsx"}
        filename = filedialog.askopenfilename(
            filetypes=[(self.file_type.get(),filetypes[self.file_type.get()])]
        )
        
        if filename:
            try:
                self.file_path_label.config(text=f"File: {filename}")  # Update file path label
                if self.file_type.get()=="Excel":
                    self.df = pd.read_excel(filename)
                else:
                    self.df=pd.read_csv(filename)
                self.update_preview()
                self.update_columns()
            except Exception as e:
                tk.messagebox.showerror("Error",f"Could not load file: {str(e)}")

    def update_preview(self):
        # Clear tree
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        # Setup columns
        self.tree["columns"]=list(self.df.columns)
        self.tree["show"]="headings"
        
        for col in self.df.columns:
            self.tree.heading(col,text=col)
            
        # Add first 5 rows
        for i,row in self.df.head().iterrows():
            self.tree.insert("","end",values=list(row))

    def update_columns(self):
        columns=list(self.df.columns)
        self.x_axis["values"]=columns
        self.y_axis["values"]=columns
        if len(columns)>=2:
            self.x_axis.set(columns[0])
            self.y_axis.set(columns[1])

    def plot_data(self):
        if self.df is None:
            return
            
        self.figure.clear()
        ax=self.figure.add_subplot(111)
        
        x=self.df[self.x_axis.get()]
        y=self.df[self.y_axis.get()]
        
        if self.plot_type.get()=="scatter":
            ax.scatter(x,y)
        elif self.plot_type.get()=="line":
            ax.plot(x,y)
        elif self.plot_type.get()=="bar":
            ax.bar(x,y)
            
        ax.set_xlabel(self.x_axis.get())
        ax.set_ylabel(self.y_axis.get())
        self.figure.tight_layout()
        self.canvas.draw()

if __name__=="__main__":
    root=tk.Tk()
    app=SimpleDataVisualizer(root)
    root.mainloop()