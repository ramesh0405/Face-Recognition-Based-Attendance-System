from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #==================variables==============
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()
        

        #First Image
        img = Image.open(r"collapse_Images\attendanc01.jpg")
        img = img.resize((770,200),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=770,height=200)

        #Second Image
        img1 = Image.open(r"collapse_Images/multiface.jpg")
        img1 = img1.resize((770,200),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=770,y=0,width=770,height=200)

        #bg Image
        img3 = Image.open(r"C:\Users\Ramesh K N\OneDrive\Desktop\Face Recognition System\collapse_Images\frbg.png")
        img3 = img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)

        title_lbl = Label(bg_img,text="ATTENDANCE MANGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1490,height=600)

        # Left label frame
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left = Image.open(r"C:\Users\Ramesh K N\OneDrive\Desktop\Face Recognition System\collapse_Images\attendance03.jpg")
        img_left = img_left.resize((720,130),Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame,image = self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        left_inside_frame = Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=720,height=400)

        #labels and entries

        #attendace id
        AttendanceID_label = Label(left_inside_frame,text="Attendance ID",font=("comicsansns 11 bold",12,"bold"),bg="white")
        AttendanceID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        AttendanceID_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("comicsansns 11 bold",12,"bold"))
        AttendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #roll no
        Attendance_roll_no_label = Label(left_inside_frame,text="Roll No",font=("comicsansns 11 bold",12,"bold"),bg="white")
        Attendance_roll_no_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        Attendance_roll_no_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("comicsansns 11 bold",12,"bold"))
        Attendance_roll_no_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #name
        Attendance_name_label = Label(left_inside_frame,text="Name",font=("comicsansns 11 bold",12,"bold"),bg="white")
        Attendance_name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        Attendance_name_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("comicsansns 11 bold",12,"bold"))
        Attendance_name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Department
        Attendance_dep_label = Label(left_inside_frame,text="Department",font=("comicsansns 11 bold",12,"bold"),bg="white")
        Attendance_dep_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        Attendance_dep_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("comicsansns 11 bold",12,"bold"))
        Attendance_dep_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Time

        Attendance_Time_label = Label(left_inside_frame,text="Time",font=("comicsansns 11 bold",12,"bold"),bg="white")
        Attendance_Time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        Attendance_Time_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("comicsansns 11 bold",12,"bold"))
        Attendance_Time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Date
        Attendance_Date_label = Label(left_inside_frame,text="Date",font=("comicsansns 11 bold",12,"bold"),bg="white")
        Attendance_Date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        Attendance_Date_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("comicsansns 11 bold",12,"bold"))
        Attendance_Date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #attendance
        attendanceLabel = Label(left_inside_frame,text="Attendance Status",bg="white",font="comicsansns 11 bold")
        attendanceLabel.grid(row=3,column=0)

        year_label_combo = ttk.Combobox(left_inside_frame,font=("comicsansns 11 bold",12,"bold"),state="readonly",width=18)
        year_label_combo["values"]=("Status","Present","Absent")
        year_label_combo.current(0)
        year_label_combo.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #buttons frame
        button_frame = Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=0,y=300,width=715,height=35)


        save_btn = Button(button_frame,text="Import CSV",command=self.importCsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn = Button(button_frame,text="Export CSV",command=self.exportCsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn = Button(button_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn = Button(button_frame,text="Reset",command=self.resest_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        



         # Right label frame
        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)

        table_frame = Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=455)

        #============================Scroll bar===============
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,columns=("id","rollno","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("rollno",text="Roll NO")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("rollno",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #======================
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    #import csv       
    def importCsv(self):
        global mydata
        mydata.clear()
        fln= filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #export csv       
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln= filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"Successfully")
        except Exception as es :
               messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def get_cursor(self,event):
        cursor_row=self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content["values"]

        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def resest_data(self):
        
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        


if __name__ == "__main__":
    root = Tk()
    obj =Attendance(root)
    root.mainloop()