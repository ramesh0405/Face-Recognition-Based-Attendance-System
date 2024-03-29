from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #==============varaiables===============
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_search = StringVar()

        #First Image
        img = Image.open(r"collapse_Images\m01.jpg")
        img = img.resize((500,130),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #Second Image
        img1 = Image.open(r"collapse_Images\m02.jpeg")
        img1 = img1.resize((500,130),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #Third Image
        img2 = Image.open(r"collapse_Images\m03.jpeg")
        img2 = img2.resize((500,130),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)


        #bg Image
        img3 = Image.open(r"collapse_Images\bg2.jpg")
        img3 = img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl = Label(bg_img,text="STUDENT MANGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1490,height=600)

        # Left label frame
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        
        img_left = Image.open(r"collapse_Images\studentscls.jpg")
        img_left = img_left.resize((720,130),Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame,image = self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        #current course
        current_course_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=200)

        #department
        dep_label = Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=17)
        dep_combo["values"]=("Select Department","AIML","AIDS","CS","CS(AIML)","CS(AIDS)","ECE","EEE","CIVIL","MECH")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        course_label = Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select Courses","MATHEMATICS","OS","DS","JAVA","SCR","DA")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label = Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_label_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=17)
        year_label_combo["values"]=("Select Year","1","2","3","4")
        year_label_combo.current(0)
        year_label_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        semester_label = Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_label_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=17)
        semester_label_combo["values"]=("Select Semester","I","II","III","IV","V","VI","VII","VII")
        semester_label_combo.current(0)
        semester_label_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        #Class Student information
        class_Student_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_Student_frame.place(x=5,y=260,width=720,height=400)

        #Student ID
        studentID_label = Label(class_Student_frame,text="Student ID",font=("times new roman",12,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Student name
        student_name_label = Label(class_Student_frame,text="Student Name",font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        student_name_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division
        class_division_label = Label(class_Student_frame,text="Section",font=("times new roman",12,"bold"),bg="white")
        class_division_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_label_combo = ttk.Combobox(class_Student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width=18)
        div_label_combo["values"]=("Select Division","A","B","C","D")
        div_label_combo.current(0)
        div_label_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        #Student rollno
        student_rollno_label = Label(class_Student_frame,text="USN",font=("times new roman",12,"bold"),bg="white")
        student_rollno_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        student_rollno_entry = ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        student_rollno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        gender_label = Label(class_Student_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_label_combo = ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=18)
        gender_label_combo["values"]=("Select Gender","Male","Female","Other")
        gender_label_combo.current(0)
        gender_label_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

         #dob
        dob_label = Label(class_Student_frame,text="Date of Birth",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Student Email
        student_email_label = Label(class_Student_frame,text="Student Email",font=("times new roman",12,"bold"),bg="white")
        student_email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        student_email_entry = ttk.Entry(class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        student_email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Phone No
        student_PhoneNo_label = Label(class_Student_frame,text="Student Phone Number",font=("times new roman",12,"bold"),bg="white")
        student_PhoneNo_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        student_PhoneNo_entry = ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        student_PhoneNo_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Address
        student_address_label = Label(class_Student_frame,text="Student Address",font=("times new roman",12,"bold"),bg="white")
        student_address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        student_address_entry = ttk.Entry(class_Student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        student_address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Teacher name
        teacher_label = Label(class_Student_frame,text="Teacher",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry = ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio Buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        #radio Buttons2
        radiobtn2 = ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="NO")
        radiobtn2.grid(row=6,column=1)

        #buttons frame
        button_frame = Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=0,y=200,width=715,height=35)


        save_btn = Button(button_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn = Button(button_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn = Button(button_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn = Button(button_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        button_frame1 = Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        button_frame1.place(x=0,y=235,width=715,height=35)

        take_photo_btn = Button(button_frame1,command=self.generate_dataset,text="Take Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn = Button(button_frame1,text="Update Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)

         # Right label frame
        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)

        img_right = Image.open(r"collapse_Images\studentright.jpg")
        img_right = img_right.resize((720,130),Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame,image = self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)

        #================Search System===========================
        Search_frame = LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=135,width=710,height=70)

        search_label = Label(Search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        serach_combo = ttk.Combobox(Search_frame,font=("times new roman",13,"bold"),state="readonly",width=15)
        serach_combo["values"]=("Select Values","Roll_No","Phone_No")
        serach_combo.current(0)
        serach_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry = ttk.Entry(Search_frame,width=20,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn = Button(Search_frame,text="Search",command=self.search_data,width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn = Button(Search_frame,text="Show All",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        #================table Frame ======================
        tabel_frame = Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        tabel_frame.place(x=5,y=210,width=710,height=350)

        scroll_x = ttk.Scrollbar(tabel_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tabel_frame,orient=VERTICAL)
        
        self.student_table = ttk.Treeview(tabel_frame,columns=("dep","course","year","sem","id","name","div","rollno","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("rollno",text="Rollno")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="Date of Birth")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone Number")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"] = "headings"


        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("rollno",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # ===============================Function Declaration ===========================
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
                messagebox.showerror("Error","All Fields are required",parent =self.root)
        else:
             try:
                conn = mysql.connector.connect(host="localhost",username="root",password="Ramu@2004",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.var_dep.get(),
                                                                                                self.var_course.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_semester.get(),
                                                                                                self.var_std_id.get(),
                                                                                                self.var_std_name.get(),
                                                                                                self.var_div.get(),
                                                                                                self.var_roll.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_dob.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_phone.get(),
                                                                                                self.var_address.get(),
                                                                                                self.var_teacher.get(),
                                                                                                self.var_radio1.get()

                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
             except Exception as es :
                  messagebox.showerror("Error",f"Due To :{str(es)}",parent = self.root)
    

    #=====================Fetch===============
    def fetch_data(self):
         conn = mysql.connector.connect(host="localhost",username="root",password="Ramu@2004",database="face_recognizer")
         my_cursor = conn.cursor()
         my_cursor.execute("select * from student")
         data = my_cursor.fetchall()

         if len(data)!= 0:
              self.student_table.delete(*self.student_table.get_children())
              for i in data:
                   self.student_table.insert("",END,values=i)
              conn.commit()
         conn.close()    


    #===================get cursor================
    def get_cursor(self,event):
         cursor_focus = self.student_table.focus()
         content = self.student_table.item(cursor_focus)
         data = content["values"]

         self.var_dep.set(data[0]),
         self.var_course.set(data[1]),
         self.var_year.set(data[2]),
         self.var_semester.set(data[3]),
         self.var_std_id.set(data[4]),
         self.var_std_name.set(data[5]),
         self.var_div.set(data[6]),
         self.var_roll.set(data[7]),
         self.var_gender.set(data[8]),
         self.var_dob.set(data[9]),
         self.var_email.set(data[10]),
         self.var_phone.set(data[11]),
         self.var_address.set(data[12]),
         self.var_teacher.set(data[13]),
         self.var_radio1.set(data[14])

     #======================update function===================
    def update_data(self):
        if self.var_dep.get() == "Select Department"  or self.var_std_name.get() == "" or self.var_std_id.get() == "" :
                messagebox.showerror("Error","All Fields are required",parent =self.root)     

        else:
          try:
               Update =messagebox.askyesno("update","Do you want to update this student details",parent=self.root)
               if Update>0 :
                    conn = mysql.connector.connect(host="localhost",username="root",password="Ramu@2004",database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                         
                                                                                                                                                                     self.var_dep.get(),
                                                                                                                                                                     self.var_course.get(),
                                                                                                                                                                     self.var_year.get(),
                                                                                                                                                                     self.var_semester.get(),
                                                                                                                                                                     self.var_std_name.get(),
                                                                                                                                                                     self.var_div.get(),
                                                                                                                                                                     self.var_roll.get(),
                                                                                                                                                                     self.var_gender.get(),
                                                                                                                                                                     self.var_dob.get(),
                                                                                                                                                                     self.var_email.get(),
                                                                                                                                                                     self.var_phone.get(),
                                                                                                                                                                     self.var_address.get(),
                                                                                                                                                                     self.var_teacher.get(),
                                                                                                                                                                     self.var_radio1.get(),
                                                                                                                                                                     self.var_std_id.get()

     
                                                                                                                                                                     ))
               else:
                    if  not Update:
                         return
               messagebox.showinfo("Success","Student details successfully update completely",parent=self.root)
               conn.commit()
               self.fetch_data()
               conn.close()
          except Exception as es :
               messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)     

     #========================delete function=====================
    def delete_data(self):
         if self.var_std_id.get()=="":
              messagebox.showerror("Error","Student id must be required",parent=self.root)
         else:
              try:
                   delete = messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                   if delete>0:
                         conn = mysql.connector.connect(host="localhost",username="root",password="Ramu@2004",database="face_recognizer")
                         my_cursor = conn.cursor()
                         sql = "delete from student where Student_id=%s"
                         val = (self.var_std_id.get(),)
                         my_cursor.execute(sql,val)
                   else:
                        if not delete:
                             return
                   conn.commit()
                   self.fetch_data()
                   conn.close()
                   messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
              except Exception as es :
               messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)    


     #=====================Reset======================
    def reset_data(self):
         self.var_dep.set("Select Department")
         self.var_course.set("Select Course")
         self.var_year.set("Select Year")
         self.var_semester.set("Select Semester")
         self.var_std_id.set("")
         self.var_std_name.set("")
         self.var_div.set("Select Division")                             
         self.var_roll.set("")
         self.var_gender.set("Select Gender")
         self.var_dob.set("")
         self.var_email.set("")
         self.var_phone.set("")
         self.var_address.set("")
         self.var_teacher.set("")
         self.var_radio1.set("")

     #------------------------------search data---------------------------------
    def search_data(self):
        if self.var_search.get()=="" or self.var_searchTX.get()=="Select":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition',port=3307)
                my_cursor = conn.cursor()
                sql = "SELECT Student_ID,Name,Department,Course,Year,Semester,Division,Gender,DOB,Mobile_No,Address,Roll_No,Email,Teacher_Name,PhotoSample FROM student where Roll_No='" +str(self.var_search.get()) + "'" 
                my_cursor.execute(sql)
                # my_cursor.execute("select * from student where Roll_No= " +str(self.var_search.get())+" "+str(self.var_searchTX.get())+"")
                rows=my_cursor.fetchall()        
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

     #============== Generate data set or take photo samples ========================
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department"  or self.var_std_name.get() == "" or self.var_std_id.get() == "" :
                messagebox.showerror("Error","All Fields are required",parent =self.root)     

        else:
          try:
                conn = mysql.connector.connect(host="localhost",username="root",password="Ramu@2004",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                print("myresult",myresult)
                id =0
                for x in myresult:
                    id+=1

                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                         
                                                                                                                                                                     self.var_dep.get(),
                                                                                                                                                                     self.var_course.get(),
                                                                                                                                                                     self.var_year.get(),
                                                                                                                                                                     self.var_semester.get(),
                                                                                                                                                                     self.var_std_name.get(),
                                                                                                                                                                     self.var_div.get(),
                                                                                                                                                                     self.var_roll.get(),
                                                                                                                                                                     self.var_gender.get(),
                                                                                                                                                                     self.var_dob.get(),
                                                                                                                                                                     self.var_email.get(),
                                                                                                                                                                     self.var_phone.get(),
                                                                                                                                                                     self.var_address.get(),
                                                                                                                                                                     self.var_teacher.get(),
                                                                                                                                                                     self.var_radio1.get(),
                                                                                                                                                                     self.var_std_id.get()==id+1

     
                                                                                                                                                                ))
                    
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                print("Id at sql",id)
                #==========================Load predefined data on face frontals from opencv=====================
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor = 1.3
                    #Mininmum Neighbour = 5

                    for(x,y,w,h) in faces:
                         face_cropped = img[y:y+h,x:x+w]
                         return face_cropped
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None :
                         img_id += 1
                         face = cv2.resize(face_cropped(my_frame),(450,450))
                         face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                         file_name_path = f"data/user.{id}.{img_id}.jpg"  # Unique filename for each student
                         print("ID in cropped images",id)
                         cv2.imwrite(file_name_path,face)
                         cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                         cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                         break
                cap.release()
                cv2.destroyAllWindows()
                     
                messagebox.showinfo("Result","Generating data sets completed!!!!")

          except Exception as es :
               messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)





if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()