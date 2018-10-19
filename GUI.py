import tkinter as tk
import os.path


class FileCreator(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        # tk.Tk.config(self, bg="gray")
        self.geometry("400x400")
        tk.Label(self, text="File Location").grid(row=0)
        tk.Label(self, text="File Name").grid(row=1)
        tk.Label(self, text="File Content").grid(row=2)
        self.loc_error = tk.Label(self, text="", fg='red')
        self.name_error = tk.Label(self, text="", fg='red')
        self.content_error = tk.Label(self, text="", fg='red')
        self.success = tk.Label(self, text="", fg="green")
        self.file_location = tk.Entry(self)
        self.file_name = tk.Entry(self)
        self.file_content = tk.Entry(self)

        self.button = tk.Button(self, text="Create File", command=self.on_button, width=27)
        # self.file_location.pack()
        self.file_location.grid(row=0, column=1)
        # self.file_name.pack()
        self.file_name.grid(row=1, column=1)
        # self.file_content.pack()
        self.file_content.grid(row=2, column=1)

        self.button.grid(row=10, column=10, columnspan=2)
        self.loc_error.grid(row=0, column=2)
        self.name_error.grid(row=1, column=2)
        self.content_error.grid(row=2, column=2)
        self.success.grid(row=3)

    def on_button(self):
        file_loc = self.file_location.get()
        file_n = self.file_name.get()
        file_con = self.file_content.get()

        if file_loc == "":
            self.loc_error['text'] = "Error"
            return
        else:
            self.loc_error['text'] = ""

        if file_n == "":
            self.name_error['text'] = "Error"
            return
        else:
            self.name_error['text'] = ""

        if file_con == "":
            self.content_error['text'] = "Error"
            return
        else:
            self.content_error['text'] = ""

        save_path = r"C:/Users/danie/Desktop/" + str(file_loc)

        if not os.path.exists(save_path):
            os.makedirs(save_path)

        file_name = save_path + "/" + file_n + ".txt"

        file = open(file_name, "w")

        file.write(file_con)

        file.close()

        self.success['text'] = "Success"


w = FileCreator()
w.mainloop()
