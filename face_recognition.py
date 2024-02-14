from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        #first
        img_top = Image.open(r"collapse_Images\faceleft1.png")
        img_top = img_top.resize((650,700),Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image = self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)

        #second
        img_bottom = Image.open(r"collapse_Images\faceright.jpg")
        img_bottom = img_bottom.resize((950,700),Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root,image = self.photoimg_bottom)
        f_lbl.place(x=650,y=55,width=950,height=700)
        
         # button
        b1_1 = Button(f_lbl,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",18,"bold"),bg="dark green",fg="white")
        b1_1.place(x=365,y=620,width=200,height=40)
    #======================attendance======================
    def mark_attendance(self, i, r, n, d):
    # If attendance is already marked for this person, print message and stop
        with open("Ramesh.csv", "r") as f:
            for line in f:
                entry = line.strip().split(",")
                if entry[0] == i and entry[1] == r and entry[2] == n and entry[3] == d:
                    print(f"Attendance already marked for {n} (ID: {i}, Roll: {r}, Department: {d})")
                    return  # Stop the function if attendance is already marked

        # If not marked, proceed to mark attendance
        with open("Ramesh.csv", "a", newline="\n") as f:
            now = datetime.now()
            d1 = now.strftime("%d/%m/%Y")
            dstring = now.strftime("%H:%M:%S")
            f.write(f"\n{i},{r},{n},{d},{dstring},{d1},Present")

        print(f"Attendance marked for {n} (ID: {i}, Roll: {r}, Department: {d})")



                

        #==================Face recognition====================
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbour,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbour)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost",username="root",password="Ramu@2004",database="face_recognizer")
                my_cursor = conn.cursor()
                

                # ... (your existing code)

                my_cursor.execute("SELECT Name FROM student WHERE Student_id="+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("SELECT Roll FROM student WHERE Student_id="+str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute("SELECT Dep FROM student WHERE Student_id="+str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                my_cursor.execute("SELECT Student_id FROM student WHERE Student_id="+str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)

            # ... (continue with the rest of your code)





                if confidence>77:
                    cv2.putText(img,f"ID : {i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll : {r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name : {n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department : {d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                coord=[x,y,w,h]
            return coord
        
        def recognize(img,clf,faceCascade):
            coord = draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img = video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()




if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()