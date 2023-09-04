from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import  mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]

class Attendence:
    def __init__(self,root):
         self.root=root
         self.root.geometry("1530x780+0+0")
         self.root.title("face recognition system")

         #==========variables=================
         self.var_atten_id=StringVar()
         self.var_atten_name=StringVar()
         self.var_atten_division=StringVar()
         
         self.var_atten_dep=StringVar()
         self.var_atten_time=StringVar()
         self.var_atten_date=StringVar()
         self.var_atten_attendence=StringVar()


         #first image
         img =Image.open(r"college_images\smart-attendance.jpg")
         img=img.resize((800,200),Image.ANTIALIAS)
         self.photoimg=ImageTk.PhotoImage(img)

         f_lbl=Label(self.root,image=self.photoimg)
         f_lbl.place(x=0,y=0,width=800,height=200)

         #second image
         img1 =Image.open(r"college_images\iStock-182059956_18390_t12.jpg")
         img1=img1.resize((800,200),Image.ANTIALIAS)
         self.photoimg1=ImageTk.PhotoImage(img1)

         f_lbl=Label(self.root,image=self.photoimg1)
         f_lbl.place(x=800,y=0,width=800,height=200)
         
         #bg image
         img3 =Image.open(r"C:\Users\user\OneDrive\Desktop\machine learning projects\face_regonition\college_images\bg.jpg")
         img3=img3.resize((1530,710),Image.ANTIALIAS)
         self.photoimg3=ImageTk.PhotoImage(img3)

         bg_img=Label(self.root,image=self.photoimg3)
         bg_img.place(x=0,y=200,width=1530,height=710)

         title_lbl=Label(bg_img,text="STUDENT ATTENDENCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
         title_lbl.place(x=0,y=0,width=1530,height=45)

         main_frame = Frame(bg_img,bd=2,bg="white")
         main_frame.place(x=10,y=55,width=1505,height=600)

         Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendence Details",font=("times new roman",12,"bold"))
         Left_frame.place(x=10,y=10,width=730,height=580)

         img_left =Image.open(r"college_images\AdobeStock_303989091.jpeg")
         img_left=img_left.resize((720,130),Image.ANTIALIAS)
         self.photoimg_left=ImageTk.PhotoImage(img_left)

         f_lbl=Label(Left_frame,image=self.photoimg_left)
         f_lbl.place(x=5,y=0,width=720,height=130)

         left_inside_frame = Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
         left_inside_frame.place(x=0,y=135,width=720,height=370)

         #label and entry
         #attendence id
         attendenceId_label=Label(left_inside_frame,text="AttendenceID:",font=("times new roman",13,"bold"),bg="white")
         attendenceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

         attendenceId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",13,"bold"))
         attendenceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

           #date
         nameLabel=Label(left_inside_frame,text="Name:",font="comicsansns 11 bold",bg="white")
         nameLabel.grid(row=0,column=2,padx=4,pady=8)

         atten_name=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_name,font="comicsansns 11 bold")
         atten_name.grid(row=0,column=3,pady=8)

         #division
         rollLabel=Label(left_inside_frame,text="Division:",bg="white",font="comicsansns 11 bold")
         rollLabel.grid(row=1,column=0)

         atten_roll=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_division,font="comicsansns 11 bold")
         atten_roll.grid(row=1,column=1,pady=8)


            #department
         depLabel=Label(left_inside_frame,text="Department:",font="comicsansns 11 bold",bg="white")
         depLabel.grid(row=1,column=2)

         atten_dep=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_dep,font="comicsansns 11 bold")
         atten_dep.grid(row=1,column=3,pady=8)

         #time
         timeLabel=Label(left_inside_frame,text="Time:",font="comicsansns 11 bold",bg="white")
         timeLabel.grid(row=2,column=0)

         atten_time=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_time,font="comicsansns 11 bold")
         atten_time.grid(row=2,column=1,pady=8)

         #date
         dateLabel=Label(left_inside_frame,text="DATE:",font="comicsansns 11 bold",bg="white")
         dateLabel.grid(row=2,column=2)

         atten_date=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_date,font="comicsansns 11 bold")
         atten_date.grid(row=2,column=3,pady=8)

         #ATTENDENCE
         attendenceLabel=Label(left_inside_frame,text="Attendence Status:",font="comicsansns 11 bold",bg="white")
         attendenceLabel.grid(row=3,column=0)

         self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendence,font="comicsansns 11 bold",state="readonly")
         self.atten_status["values"]=("Status","Present","Absent")
         self.atten_status.grid(row=3,column=1,pady=8)
         self.atten_status.current(0)

         btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
         btn_frame.place(x=0,y=300,width=720,height=35)

         save_btn=Button(btn_frame,text="Import Csv",command=self.importCsv,width=18,font=("times new roman",13,"bold"),bg="blue",fg="white")
         save_btn.grid(row=0,column=0)

         update_btn=Button(btn_frame,text="Export Csv",width=18,command=self.exportCsv,font=("times new roman",13,"bold"),bg="blue",fg="white")
         update_btn.grid(row=0,column=1)

         delete_btn=Button(btn_frame,text="Update",width=18,font=("times new roman",13,"bold"),bg="blue",fg="white")
         delete_btn.grid(row=0,column=2)

         reset_btn=Button(btn_frame,text="Reset",width=18,command=self.reset_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
         reset_btn.grid(row=0,column=3)


         Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendence Details",font=("times new roman",12,"bold"))
         Right_frame.place(x=750,y=10,width=720,height=580)

         table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
         table_frame.place(x=5,y=5,width=700,height=455)


        # ======== scroll bar==============
         scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
         scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

         self.AttendenceReportTable=ttk.Treeview(table_frame,column=("id","name","division","department","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

         scroll_x.pack(side=BOTTOM,fill=X)
         scroll_y.pack(side=RIGHT,fill=Y)

         scroll_x.config(command=self.AttendenceReportTable.xview)
         scroll_y.config(command=self.AttendenceReportTable.yview)

         self.AttendenceReportTable.heading("id",text="Attendence ID")
         self.AttendenceReportTable.heading("name",text="Name")
         self.AttendenceReportTable.heading("division",text="Division")
         
         self.AttendenceReportTable.heading("department",text="Department")
         self.AttendenceReportTable.heading("time",text="Time")
         self.AttendenceReportTable.heading("date",text="Date")
         self.AttendenceReportTable.heading("attendence",text="Attendence")

         self.AttendenceReportTable["show"]="headings"
         self.AttendenceReportTable.column("id",width=100)
         self.AttendenceReportTable.column("name",width=100)
         self.AttendenceReportTable.column("division",width=100)
        
         self.AttendenceReportTable.column("department",width=100)
         self.AttendenceReportTable.column("time",width=100)
         self.AttendenceReportTable.column("date",width=100)
         self.AttendenceReportTable.column("attendence",width=100)

         self.AttendenceReportTable.pack(fill=BOTH,expand=1)
         self.AttendenceReportTable.bind("<ButtonRelease>",self.get_cursor)

         #============fetch data==============
    def fetchData(self,rows):
      self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
      for i in rows:
           self.AttendenceReportTable.insert("",END,values=i)

     #import csv
    def importCsv(self):  
         global mydata   
         mydata.clear()
         fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV Fle",".*csv"),("All File","*.*")),parent=self.root)
         with open(fln) as myfile:
              csvread=csv.reader(myfile,delimiter=",")
              for i in csvread:
                   mydata.append(i)
                   self.fetchData(mydata)


       #export csv
    def exportCsv(self):
         try:
              if len(mydata)<1:
                   messagebox.showerror("No data","No data found to export",parent=self.root)  
                   return False
              fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV Fle",".*csv"),("All File","*.*")),parent=self.root)
              with open(fln,mode="w",newline="") as myfile:
                   exp_write=csv.writer(myfile,delimiter=",")
                   for i in mydata:
                        exp_write.writerow(i)
                   messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" successfully")
         except Exception as es:
              messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root) 


    def get_cursor(self,event=""):
         cursor_row=self.AttendenceReportTable.focus()
         content=self.AttendenceReportTable.item(cursor_row)
         row=content["values"]
         self.var_atten_id.set(row[0])
         self.var_atten_name.set(row[1])
         self.var_atten_division.set(row[2])
        
         self.var_atten_dep.set(row[3])
         self.var_atten_time.set(row[4])
         self.var_atten_date.set(row[5])
         self.var_atten_attendence.set(row[6])

    def reset_data (self):
         self.var_atten_id.set("")
         self.var_atten_name.set("")
         self.var_atten_division.set("")
        
         self.var_atten_dep.set("")
         self.var_atten_time.set("")
         self.var_atten_date.set("")
         self.var_atten_attendence.set("")
           



                      
              
                        
             

    





















if __name__ == "__main__":
        root=Tk()
        obj=Attendence(root)
        root.mainloop()         
