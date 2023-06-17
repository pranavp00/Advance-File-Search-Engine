from tkinter import *
from tkinter.filedialog import askdirectory
import customtkinter
import os
import test1


customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("dark-blue")  
app = customtkinter.CTk()  
app.title('File Search Engine')
app.geometry("700x560")
app.resizable(False,False)


def dirButton():
    path = askdirectory(title='Select directory',mustexist=True,initialdir=r'C:')
    path = r'{}'.format(path)
    dir.delete(0,END)
    dir.insert(0,path)


def open_file(k):
    os.startfile(k)

def search_button():
    query = search.get()
    root_dir = dir.get()
    result = test1.preparing_matches(root_dir,query)

    scrollable_frame = customtkinter.CTkScrollableFrame(app,width = 675,height = 210)
    scrollable_frame.place(relx=0, rely=0.6)

    

    for i in result:
        
        file_button = customtkinter.CTkButton(scrollable_frame,
                                 height = 50,
                                 text=i['file_path'],
                                 anchor="w",
                                 fg_color='transparent',
                                 command=lambda k=i['file_path']:open_file(k))
        file_button.pack(fill = 'x')
        
heading = customtkinter.CTkLabel(app, text="Advance Search", fg_color="transparent",font=('Arial',35),pady=10)
heading.pack()

search = customtkinter.CTkEntry(master=app,
                               placeholder_text="Filename or Content",
                               width=520,
                               height=35,
                               border_width=2,
                               corner_radius=10)

dir  = customtkinter.CTkEntry(master=app,
                               placeholder_text="Directory",
                               width=380,
                               height=35,
                               border_width=2,
                               corner_radius=10)

search.place(relx=0.5, rely=0.20, anchor=CENTER)
dir.place(relx=0.4, rely=0.35, anchor=CENTER)

dir_button = customtkinter.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Select Directory",
                                 command=dirButton)
dir_button.place(relx=0.7, rely=0.32)

submit = customtkinter.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Search",
                                 command=search_button)
submit.place(relx=0.5, rely=0.5, anchor=CENTER)

app.mainloop()