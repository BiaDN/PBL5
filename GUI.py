import tkinter as tk                
from tkinter import BOTH, BOTTOM, CENTER, DISABLED, NO, NW, RIGHT, TOP, W, X, Y, Image, Scrollbar, Tk, font as tkfont
from tkinter import messagebox as msg
from tkinter import ttk, Canvas
from PIL import Image, ImageTk
from Management import *

management = Management()

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, CheckPage, DatabasePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Phần mềm quản lý xe ra vào", fg="#289DD2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=30)
        	
        self.img = Image.open("App code\media\home-page.png")
        self.tatras = ImageTk.PhotoImage(self.img)
        canvas = Canvas(self, width=self.img.size[0]+20, height=self.img.size[1]+20)
        canvas.create_image(10, 10, anchor=NW, image=self.tatras)
        canvas.place(x=20, y =80)

        button1 = tk.Button(self, text="Đến trang Theo Dõi Xe Ra Vào", fg="#FFFFFF", font=("Arial", 13), bg="#41C1BA", highlightbackground="#FFFFFF",
                            command=lambda: controller.show_frame("CheckPage"))
        button2 = tk.Button(self, text="Đến trang Quản Lý Dữ Liệu", fg="#FFFFFF", font=("Arial", 13), bg="#41C1BA", highlightbackground="#FFFFFF",
                            command=lambda: controller.show_frame("DatabasePage"))
        button1.place(x=700, y=250)
        button2.place(x=710, y=350)

class CheckPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.label_title = tk.Label(self, text="NHẬN DIỆN BIỂN SỐ", fg="#289DD2", font=("Arial", 20))
        self.label_title.grid(column=1, columnspan=2, row=1)

        self.lb_name = tk.Label(self, text="Họ và tên: ", fg="#365B6D", font=("Arial", 13))
        self.lb_name.grid(column=2, row=2, sticky='w', padx=20)
        self.entry_txt_name = tk.StringVar()
        self.txt_name = tk.Entry(self, width=40, textvariable=self.entry_txt_name, font=("Arial", 11))
        self.txt_name.grid(column=2, row=3, sticky='w', padx=20)

        self.lb_dob = tk.Label(self, text="Ngày sinh: ", fg="#365B6D", font=("Arial", 13))
        self.lb_dob.grid(column=2, row=4, sticky='w', padx=20)
        self.entry_txt_dob = tk.StringVar()
        self.txt_dob = tk.Entry(self, width=40, textvariable=self.entry_txt_dob, font=("Arial", 11))
        self.txt_dob.grid(column=2, row=5, sticky='w', padx=20)

        self.lb_department = tk.Label(self, text="Phòng: ", fg="#365B6D", font=("Arial", 13))
        self.lb_department.grid(column=2, row=6, sticky='w', padx=20)
        self.entry_txt_depart = tk.StringVar()
        self.txt_department = tk.Entry(self, width=40, textvariable=self.entry_txt_depart, font=("Arial", 11))
        self.txt_department.grid(column=2, row=7, sticky='w', padx=20)

        self.lb_license = tk.Label(self, text="Biển số xe: ", fg="#365B6D", font=("Arial", 13))
        self.lb_license.grid(column=2, row=8, sticky='w', padx=20)
        self.entry_txt_license = tk.StringVar()
        self.txt_license = tk.Entry(self, width=40, textvariable=self.entry_txt_license, font=("Arial", 11))
        self.txt_license.grid(column=2, row=9, sticky='w', padx=20)

        self.lb_in = tk.Label(self, text="Giờ vào: ", fg="#365B6D", font=("Arial", 13))
        self.lb_in.grid(column=2, row=10, sticky='w', padx=20)
        self.entry_txt_in = tk.StringVar()
        self.txt_in = tk.Entry(self, width=40, textvariable=self.entry_txt_in, font=("Arial", 11))
        self.txt_in.grid(column=2, row=11, sticky='w', padx=20)

        self.lb_out = tk.Label(self, text="Giờ ra: ", fg="#365B6D", font=("Arial", 13))
        self.lb_out.grid(column=2, row=12, sticky='w', padx=20)
        self.entry_txt_out = tk.StringVar()
        self.txt_out = tk.Entry(self, width=40, textvariable=self.entry_txt_out, font=("Arial", 11))
        self.txt_out.grid(column=2, row=13, sticky='w', padx=20)

        # # Create a canvas that can fit the above video source size
        self.imgtest = Image.open("App code/media/img-test.png")
        self.test = ImageTk.PhotoImage(self.imgtest)
        canvas = Canvas(self, width=550, height=330)
        canvas.create_image(10, 10, anchor=NW, image=self.test)
        canvas.grid(column=1, row=2, rowspan=12, sticky='we', padx=15, pady=15)
        # self.lb_temp = tk.Label(self, text="Chỗ này để cái hình", font=("Arial", 53)).grid(column=1, row=2, rowspan=12, sticky='we', padx=15, pady=15)

        self.entry_txt_db = tk.StringVar()
        self.txt_db = tk.Entry(self, width=40, textvariable=self.entry_txt_db, font=("Arial", 11))
        self.txt_db.grid(column=1, row=15)

        self.btn_test = tk.Button(self, text="Test", command=self.btn_on_click, width=10)
        self.btn_test.grid(column=2, row=15)

        self.btn_home = tk.Button(self, text="Về trang chủ", fg="#FFFFFF", font=("Arial", 13), bg="#41C1BA",
                           command=lambda: controller.show_frame("StartPage"))
        self.btn_home.grid(column=1, row=17, rowspan=2, pady=25)
        self.btn_db = tk.Button(self, text="Đến trang Quản Lý Dữ Liệu", fg="#FFFFFF", font=("Arial", 13), bg="#41C1BA",
                           command=lambda: controller.show_frame("DatabasePage"))
        self.btn_db.grid(column=2, row=17, rowspan=2, pady=25)

    def btn_on_click(self):
        self.entry_txt_name.set("")
        self.entry_txt_dob.set("")
        self.entry_txt_depart.set("")
        self.entry_txt_license.set("")
        self.entry_txt_in.set("")
        self.entry_txt_out.set("")
        license = self.txt_db.get()
        x = management.check_license(license)
        if x:
            self.entry_txt_name.set(x["name"])
            self.entry_txt_dob.set(x["dob"])
            self.entry_txt_depart.set(x["room"])
            self.entry_txt_license.set(x["license_number"])
            self.entry_txt_in.set(x["time_in"])
            self.entry_txt_out.set(x["time_out"])
        else:
            msg.showwarning("Cơ sở dữ liệu", "XE LẠ!!!")

class DatabasePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label_title = tk.Label(self, text="DỮ LIỆU", fg="#289DD2", font=("Arial", 20))
        label_title.pack(side=TOP)

        tree_frame = tk.Frame(self)
        tree_frame.pack(pady=20)
        #scrollbar
        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)
        #create table to display data
        self.table = ttk.Treeview(tree_frame, yscrollcommand = tree_scroll.set)
        self.table.pack(pady=20)
        #configure scrollbar
        tree_scroll.config(command=self.table.yview)
        #define columns
        self.table['columns'] = ("Name", "DoB", "Room", "License Number", "Time in", "Time out")
        #format columns
        self.table.column("#0", width=35, minwidth=15)
        self.table.column("Name", anchor=W, width=150)
        self.table.column("DoB", anchor=W, width=80)
        self.table.column("Room", anchor=W, width=80)
        self.table.column("License Number", anchor=CENTER, width=100)
        self.table.column("Time in", anchor=CENTER, width=120)
        self.table.column("Time out", anchor=CENTER, width=120)
        #create headings
        self.table.heading("#0", text="STT", anchor=CENTER)
        self.table.heading("Name", text="Name", anchor=CENTER)
        self.table.heading("DoB", text="Date of birth", anchor=CENTER)
        self.table.heading("Room", text="Room", anchor=CENTER)
        self.table.heading("License Number", text="License Number", anchor=CENTER)
        self.table.heading("Time in", text="Coming in (time)", anchor=CENTER)
        self.table.heading("Time out", text="Going out (time)", anchor=CENTER)

        data = management.get_all_licenses()
        count = 0
        for record in data:
            self.table.insert(parent='', index='end', iid=count, text=count+1, values=(record['name'], record['dob'], record['room'], record['license_number'], record['time_in'], record['time_out']))
            count += 1

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=20)
        btn_refresh = tk.Button(btn_frame, text="Refresh", fg="#FFFFFF", font=("Arial", 13), bg="#365B6D", command=self.btn_refresh, width=10)
        btn_refresh.grid(row=0, column=0, padx=20)
        btn_register = tk.Button(btn_frame, text="Đăng ký", fg="#FFFFFF", font=("Arial", 13), bg="#365B6D", command=self.btn_register, width=10)
        btn_register.grid(row=0, column=1, padx=20)
        btn_update = tk.Button(btn_frame, text="Chỉnh sửa", fg="#FFFFFF", font=("Arial", 13), bg="#365B6D", command=self.btn_update, width=10)
        btn_update.grid(row=0, column=2, padx=20)
        btn_delete = tk.Button(btn_frame, text="Xoá", fg="#FFFFFF", font=("Arial", 13), bg="#365B6D", command=self.btn_delete, width=10)
        btn_delete.grid(row=0, column=3, padx=20)

        btn_home = tk.Button(btn_frame, text="Về trang chủ", fg="#FFFFFF", font=("Arial", 13), bg="#41C1BA",
                           command=lambda: controller.show_frame("StartPage"))
        btn_home.grid(row=1, column=0, columnspan=2, pady=10)
        btn_check = tk.Button(btn_frame, text="Đến trang Theo Dõi Xe Ra Vào", fg="#FFFFFF", font=("Arial", 13), bg="#41C1BA",
                           command=lambda: controller.show_frame("CheckPage"))
        btn_check.grid(row=1, column=2, columnspan=2, pady=10)
    
    def btn_refresh(self):
        self.data = management.get_all_licenses()
        for record in self.table.get_children():
            self.table.delete(record)
        count = 0
        for record in self.data:
            self.table.insert(parent='', index='end', iid=count, text=count+1, values=(record['name'], record['dob'], record['room'], record['license_number'], record['time_in'], record['time_out']))
            count += 1

    def btn_register(self):
        register_window = Register(self, 0, ())
        register_window.grab_set()

    def btn_update(self):
        try:
            selected = self.table.focus()
            values = self.table.item(selected, 'values')
            update_window = Register(self, 1, values)
            update_window.grab_set()
        except:
            msg.showerror("Cơ sở dữ liệu", "Hãy chọn một bản ghi!")

    def btn_delete(self):
        try:
            selected = self.table.focus()
            values = self.table.item(selected, 'values')
            management.delete_user(values[3]) #license_number
        except:
            msg.showerror("Cơ sở dữ liệu", "Hãy chọn một bản ghi!")

class Register(tk.Toplevel):
    def __init__(self, parent, status, value):
        super().__init__(parent)

        self.geometry('400x400')
        self.title('Đăng ký')

        # A Label widget to show in toplevel
        tk.Label(self, text="Nhập thông tin", fg="#289DD2", font=("Arial", 13)).grid(row=0, column=0)

        self.lb_name = tk.Label(self, text="Họ và tên:", font=("Arial", 13)).grid(row=1, column=0, sticky='w', padx=20)
        self.entry_txt_name = tk.StringVar()
        self.txt_name = tk.Entry(self, width=40, textvariable=self.entry_txt_name)
        self.txt_name.grid(column=0, row=2, sticky='w', padx=20)

        self.lb_dob = tk.Label(self, text="Ngày sinh: ", font=("Arial", 13)).grid(column=0, row=4, sticky='w', padx=20)
        self.entry_txt_dob = tk.StringVar()
        self.txt_dob = tk.Entry(self, width=40, textvariable=self.entry_txt_dob)
        self.txt_dob.grid(column=0, row=5, sticky='w', padx=20)

        self.lb_department = tk.Label(self, text="Phòng: ", font=("Arial", 13)).grid(column=0, row=7, sticky='w', padx=20)
        self.entry_txt_depart = tk.StringVar()
        self.txt_department = tk.Entry(self, width=40, textvariable=self.entry_txt_depart)
        self.txt_department.grid(column=0, row=8, sticky='w', padx=20)

        self.lb_license = tk.Label(self, text="Biển số xe: ", font=("Arial", 13)).grid(column=0, row=10, sticky='w', padx=20)
        self.entry_txt_license = tk.StringVar()
        self.txt_license = tk.Entry(self, width=40, textvariable=self.entry_txt_license)
        self.txt_license.grid(column=0, row=11, sticky='w', padx=20)
        self.btn_regis = tk.Button(self, text="OK", width=10)
        self.btn_regis.grid(column=0, row=20)

        if status == 1:
            self.entry_txt_name.set(value[0]) #name
            self.entry_txt_dob.set(value[1]) #date of birth
            self.entry_txt_depart.set(value[2]) #room
            self.entry_txt_license.set(value[3]) #license_number           
            self.txt_license.config(state=DISABLED)
            self.btn_regis.config(command=self.btn_update)
        else: 
            self.btn_regis.config(command=self.btn_register)

    def btn_register(self):
        name = self.txt_name.get()
        dob = self.txt_dob.get()
        room = self.txt_department.get()
        license_number = self.txt_license.get()
        message = management.add_new_user(name, dob, room, license_number)
        msg.showinfo("Cơ sở dữ liệu", message)
    
    def btn_update(self):
        name = self.txt_name.get()
        dob = self.txt_dob.get()
        room = self.txt_department.get()
        license_number = self.txt_license.get()
        message = management.update_user(name, dob, room, license_number)
        msg.showinfo("Cơ sở dữ liệu", message)
            
if __name__ == "__main__":
    app = App()
    app.geometry("1000x600")
    app.title("Nhận diện biển số")
    app.mainloop()