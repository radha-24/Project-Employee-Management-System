from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
import tkinter as tk  

class Employee:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title('Employee Management System')
        
        # Variables
        self.var_dep = StringVar()
        self.var_name = StringVar()
        self.var_designation = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_married = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_idproofcombo = StringVar()
        self.var_idproof = StringVar()
        self.var_gender = StringVar()
        self.var_phone = StringVar()
        self.var_country = StringVar()
        self.var_salary = StringVar()
    
        lbl_title=Label(self.root,text='EMPLOYEE MANAGEMENT SYSTEM', font=('times new roman',37,'bold'),fg='darkblue',bg='white')
        lbl_title.place(x=0,y=0,width=1530,height=50)
        
        #logo
        img_logo=Image.open('images/logo.png')
        img_logo=img_logo.resize((50,50),Image.LANCZOS)        
        self.photo_logo =ImageTk.PhotoImage(img_logo)
        
        self.logo=Label(self.root,image= self.photo_logo)
        self.logo.place(x=270,y=0,width=50,height=50)
        
        #frame
        img_frame=Frame(self.root,bd= 2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1530,height=160)
        
        #frame 1
        img1=Image.open('images/frame.png')
        img1=img1.resize((800,150),Image.LANCZOS)        
        self.photo1 =ImageTk.PhotoImage(img1)
        
        self.img_1=Label(img_frame,image= self.photo1)
        self.img_1.place(x=0,y=0,width=800,height=150)
        
        #frame 2
        img2=Image.open('images/frame2.png')
        img2=img2.resize((800,150),Image.LANCZOS)        
        self.photo2=ImageTk.PhotoImage(img2)
        
        self.img_2=Label(img_frame,image= self.photo2)
        self.img_2.place(x=750,y=0,width=800,height=150)
        
        #Main frame
        Main_frame = Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=5,y=210,width=1520,height=580)
        
        #upper frame
        self.upper_frame = LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information',font=('times new roman',11,'bold'),fg='dark blue')
        self.upper_frame.place(x=10,y=10,width=1500,height=270)
        
        #Labels and Entry fields
     # Department
        lbl_dep = Label(self.upper_frame, text='Department', font=('arial', 12, 'bold'), bg='white')
        lbl_dep.grid(row=0, column=0, padx=10, sticky=W)

        combo_dep = ttk.Combobox(self.upper_frame,textvariable=self.var_dep, font=('Rockwell', 12), width=17, state='readonly')
        combo_dep['value'] = ('Select Department', 'HR', 'Store Dept', 'Product Development', 'Account Dept','Admin Dept')
        combo_dep.current(0)
        combo_dep.grid(row=0, column=1, padx=10, pady=10, sticky=W)
        
     # Name
        lbl_Name = Label(self.upper_frame,font=('arial',12,"bold"),text="Name:",bg="white")
        lbl_Name.grid(row=0,column=2,sticky=W,padx=12,pady=10)
        
        self.txt_name=ttk.Entry(self.upper_frame,textvariable=self.var_name,font=("Rockwell",11))
        
        def valid_nam(value):
            # Allow alphabetical characters and spacess
            return all(c.isalpha() or c.isspace() for c in value)

        # Set the validation criteria for the entry field Email.
        validation = self.upper_frame.register(valid_nam)
        self.txt_name.config(validate="key",validatecommand = (validation,"%P"))
        self.txt_name.grid(row=0,column=3,padx=10,pady=10)
        
     # lbl_Designation
        lbl_Designation=Label(self.upper_frame,font=('arial',11,'bold'),text='Designation:',bg='white')
        lbl_Designation.grid(row=1,column=0,sticky=W,padx=10,pady=10)
        
        self.txt_Designation=ttk.Entry(self.upper_frame,textvariable=self.var_designation,width=22,font=("Rockwell",11))
       
        def valid_designation(value):
            # Allow alphabetical characters and spaces
            return all(c.isalpha() or c.isspace() for c in value)

        # Set the validation criteria for the entry field Designation.
        validation = self.upper_frame.register(valid_designation)
        self.txt_Designation.config(validate="key",validatecommand = (validation,"%P"))
        self.txt_Designation.grid(row=1,column=1,sticky=W,padx=10,pady=10)
        
     # Email
        lbl_email=Label(self.upper_frame,font=('arial',12,'bold'),text='Email:',bg='white')
        lbl_email.grid(row=1,column=2,sticky=W,padx=12,pady=10)
        
        self.txt_email=ttk.Entry(self.upper_frame,textvariable=self.var_email,width=22,font=("Rockwell",11))
        
        def valid_email_ad(value):
            return all(char.isalnum() or char in {'@','_','-','.'} for char in value)

        # Set the validation criteria for the entry field Email.
        validation = self.upper_frame.register(valid_email_ad)
        self.txt_email.config(validate="key",validatecommand = (validation,"%P"))
        self.txt_email.grid(row=1,column=3,padx=10,pady=10)
        
     # Address
        lbl_address= Label(self.upper_frame,font=("arial",12,"bold"),text="Address:",bg='white')
        lbl_address.grid(row=2,column=0,sticky=W,padx=10,pady=10)
        
        self.txt_address=ttk.Entry(self.upper_frame,textvariable=self.var_address,width=22,font=("Rockwell",11))
        
        def valid_Address(value):
            # Allow alphabets ,numbers,special charc  and spaces
            return all(char.isalnum() or char.isspace() or char in {',','@','_','-','.'} for char in value)

        # Set the validation criteria for the entry field Address.
        validation = self.upper_frame.register(valid_Address)
        self.txt_address.config(validate="key",validatecommand = (validation,"%P"))
        self.txt_address.grid(row=2,column=1,padx=10,pady=10)
        
     # Married
        lbl_married_status= Label(self.upper_frame,font=("arial",12,"bold"),text="Married_status:",bg='white')
        lbl_married_status.grid(row=2,column=2,sticky=W,padx=12,pady=10)

        com_txt_married=ttk.Combobox(self.upper_frame,textvariable=self.var_married,state="readonly",font=("Rockwell",12),width=18)
        com_txt_married['value']=("Married","Unmarried")
        com_txt_married.current(0)
        com_txt_married.grid(row=2,column=3,sticky=W,padx=10,pady=10)
        
     # DOB
        lbl_dob= Label(self.upper_frame,font=("arial",12,"bold"),text="DOB:",bg='white')
        lbl_dob.grid(row=3,column=0,sticky=W,padx=10,pady=10)
        
        self.txt_dob=ttk.Entry(self.upper_frame,textvariable=self.var_dob,width=22,font=("Rockwell",11))
        
        def valid_dob(value):
            return all(char.isdigit() or char in {'/', '-'} for char in value)

        # Set the validation criteria for the entry field DOB.
        validation = self.upper_frame.register(valid_dob)
        self.txt_dob.config(validate="key",validatecommand = (validation,"%P"))
        self.txt_dob.grid(row=3,column=1,padx=10,pady=10)
        
     # DOJ
        lbl_doj= Label(self.upper_frame,font=("arial",12,"bold"),text="DOJ:",bg='white')
        lbl_doj.grid(row=3,column=2,sticky=W,padx=12,pady=10)
        
        self.txt_doj=ttk.Entry(self.upper_frame,textvariable=self.var_doj,width=22,font=("Rockwell",11))
        def valid_doj(value):
            return all(char.isdigit() or char in {'/', '-'} for char in value)

        # Set the validation criteria for the entry field DOJ.
        validation = self.upper_frame.register(valid_doj)
        self.txt_doj.config(validate="key",validatecommand = (validation,"%P"))
        self.txt_doj.grid(row=3,column=3,padx=10,pady=10)
        
     # Id Proof
        com_txt_proof=ttk.Combobox(self.upper_frame,textvariable=self.var_idproofcombo,state="readonly",font=("arial",12,"bold"),width=18)
        com_txt_proof['value']=("Select ID Proof","PAN CARD","ADHAR CARD")
        com_txt_proof.current(0)
        com_txt_proof.grid(row=4,column=0,sticky=W,padx=10,pady=10)
        
        self.txt_proof = ttk.Entry(self.upper_frame, textvariable=self.var_idproof, width=22, font=("Rockwell", 11))

        
        def validate_ID(value, Select):
         if Select.get() == "PAN CARD":
             if value.isalnum() and len(value) <= 10 or value == "":
                 return True
             else:
                  return False
             
                 
         elif Select.get() == "ADHAR CARD":
             if value.isdigit() and len(value) <= 12 or value == "":
                   return True
             else:
                 return False   
         else:
             return True
      
        # Set the validation criteria for the entry field based on the selected ID Proof
        validation = self.upper_frame.register(lambda P, Select=com_txt_proof: validate_ID(P, Select))
        self.txt_proof.config(validate="key", validatecommand=(validation, "%P"))
        self.txt_proof.grid(row=4, column=1, padx=2, pady=7)
        

         # Message Entry Field for id proof
        self.message_entry = ttk.Entry(self.upper_frame, textvariable=tk.StringVar(), state="readonly", width=50,
                                       font=("Rockwell", 10))
        self.message_entry.grid(row=5, column=0,columnspan=2 ,padx=10, pady=6,sticky=tk.W)

        # Function to update the message entry field based on the selected ID Proof
        def update_message(*args):
            selected_id_proof = com_txt_proof.get()
            if selected_id_proof == "PAN CARD":
                self.message_entry.config(state="normal")
                self.message_entry.delete(0, tk.END)
                self.message_entry.insert(0, "Enter 10 digit PAN CARD number eg:ABCTY1234D")
                self.message_entry.config(state="readonly")
            elif selected_id_proof == "ADHAR CARD":
                self.message_entry.config(state="normal")
                self.message_entry.delete(0, tk.END)
                self.message_entry.insert(0, "Enter 12 digit ADHAR CARD number")
                self.message_entry.config(state="readonly")
            else:
                self.message_entry.config(state="normal")
                self.message_entry.delete(0, tk.END)
                self.message_entry.config(state="readonly")

        com_txt_proof.bind("<<ComboboxSelected>>", update_message)
        
     # Gender
        lbl_gender= Label(self.upper_frame,font=("arial",12,"bold"),text="Gender:",bg='white')
        lbl_gender.grid(row=4,column=2,sticky=W,padx=12,pady=10)

        com_txt_gender=ttk.Combobox(self.upper_frame,textvariable=self.var_gender,state="readonly",font=("Rockwell",12),width=18)
        com_txt_gender['value']=("Male","Female","Other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=4,column=3,sticky=W,padx=12,pady=10)
        
     # Phone
        lbl_phone= Label(self.upper_frame,font=("arial",12,"bold"),text="Phone No:",bg='white')
        lbl_phone.grid(row=0,column=4,sticky=W,padx=12,pady=10)
        
        self.txt_phone = ttk.Entry(self.upper_frame,textvariable=self.var_phone, width=22, font=("Rockwell", 11))
        def valid_in(value):
            return value.isdigit() and len(value) <= 10 or value == ""

        # Set the validation criteria for the entry field phone.
        validation = self.upper_frame.register(valid_in)
        self.txt_phone.config(validate="key",validatecommand = (validation,"%P"))
        self.txt_phone.grid(row=0, column=5, padx=2, pady=7)
        
     # Country
        lbl_country= Label(self.upper_frame,font=("arial",12,"bold"),text="Country:",bg='white')
        lbl_country.grid(row=1,column=4,sticky=W,padx=12,pady=10)
        
        self.txt_country=ttk.Entry(self.upper_frame,textvariable=self.var_country,width=22,font=("Rockwell",11))
        
        def valid_con(value):
            # Allow alphabetical characters and spaces
            return all(c.isalpha() or c.isspace() for c in value)

        # Set the validation criteria for the entry field Country.
        validation = self.upper_frame.register(valid_con)
        self.txt_country.config(validate="key",validatecommand = (validation,"%P"))
        self.txt_country.grid(row=1,column=5,padx=12,pady=10)
        
     # CTC
        lbl_ctc= Label(self.upper_frame,font=("arial",12,"bold"),text="Salary(CTC):",bg='white')
        lbl_ctc.grid(row=2,column=4,sticky=W,padx=12,pady=10)
        
        self.txt_ctc=ttk.Entry(self.upper_frame,textvariable=self.var_salary,width=22,font=("Rockwell",11))
        def valid_sal(value):
            return value.isdigit() or value == ""

        # Set the validation criteria for the entry field CTC.
        validation = self.upper_frame.register(valid_sal)
        self.txt_ctc.config(validate="key",validatecommand = (validation,"%P"))
        self.txt_ctc.grid(row=2,column=5,padx=12,pady=10)
        
    
         
     # Button Frame
        button_frame = Frame(self.upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=1180,y=10,width=170,height=210) 
         
        btn_add = Button(button_frame,text="Save",command = self.add_data,font=("arial",15,"bold"),width=13,bg="grey",fg="white")
        btn_add.grid(row=0,column=0,padx=0,pady=0)
        
        btn_update = Button(button_frame,text="Update",command = self.update_data,font=("arial",15,"bold"),width=13,bg="grey",fg="white")
        btn_update.grid(row=1,column=0,padx=0,pady=12)
        
        btn_delete = Button(button_frame,text="Delete",command = self.delete_data,font=("arial",15,"bold"),width=13,bg="grey",fg="white")
        btn_delete.grid(row=2,column=0,padx=0,pady=7)
        
        btn_clear = Button(button_frame,text="Clear",command = self.reset_data,font=("arial",15,"bold"),width=13,bg="grey",fg="white")
        btn_clear.grid(row=3,column=0,padx=0,pady=8)
        
     # down frame
        down_frame = LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information Table',font=('times new roman',11,'bold'),fg='dark blue')
        down_frame.place(x=5,y=290,width=1500,height=270)

        #Search Frame
        search_frame = LabelFrame(down_frame,bd=2,relief=RIDGE,bg='white',text='Search Employee Information',font=('Bahnschrift',11,'bold'),fg='navy')
        search_frame.place(x=2,y=0,width=1330,height=50)
        
        search_by=Label(search_frame,font=("arial",11,"bold"),text="Search By:",fg="white",bg="grey")
        search_by.grid(row=0,column=0,sticky=W,padx=5)
        
     # Search
        self.var_com_search = StringVar()
        com_txt_search = ttk.Combobox(search_frame,textvariable=self.var_com_search,state="readonly",font=("arial",12,"bold"),width=18)
        com_txt_search ['value']=("Search Option","phone","idproof")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5)
        
        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,textvariable = self.var_search,width=22,font=("arial",11,"bold"))
        txt_search.grid(row=0,column=2,padx=5)
        
        btn__search=Button(search_frame,text="Search",command = self.search_data,font=("arial",11,"bold"),width=14,bg="light blue",fg="white")
        btn__search.grid(row=0,column=3,padx=5)
        
        btn_showAll=Button(search_frame,text="Show All",command = self.fetch_data,font=("arial",11,"bold"),width=14,fg="white",bg="grey")
        btn_showAll.grid(row=0,column=4,padx=5)
        
        #=========================== Employee table =================================
        #Table frame
        table_frame = Frame(down_frame,bd=3,relief=RIDGE,)
        table_frame.place(x=0,y=60,width=1490,height=170)
    
        scroll_x=ttk.Scrollbar(table_frame,orient= HORIZONTAL) 
        scroll_y=ttk.Scrollbar(table_frame,orient= VERTICAL) 
        
        self.employee_table=ttk.Treeview(table_frame,column=('dep','name','degi','email','address','married','dob','doj','idproofcombo','idproof','gender','phone','country','salary',),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
         
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)
        
        self.employee_table.heading('dep',text='Department')
        self.employee_table.heading('name',text='Name')
        self.employee_table.heading('degi',text='Designation')
        self.employee_table.heading('email',text='Email')
        self.employee_table.heading('address',text='Address')
        self.employee_table.heading('married',text='Married_status')
        self.employee_table.heading('dob',text='DOB')
        self.employee_table.heading('doj',text='DOJ')
        self.employee_table.heading('idproofcombo',text='ID Type')
        self.employee_table.heading('idproof',text='Id_Proof')
        self.employee_table.heading('gender',text='Gender')
        self.employee_table.heading('phone',text='Phone')
        self.employee_table.heading('country',text='Country')
        self.employee_table.heading('salary',text='Salary')
        
        self.employee_table['show']='headings'
        
        self.employee_table.column("dep",width=100)
        self.employee_table.column("name",width=100)
        self.employee_table.column("degi",width=100)
        self.employee_table.column("email",width=100)
        self.employee_table.column("address",width=100)
        self.employee_table.column("married",width=100)
        self.employee_table.column("dob",width=100)
        self.employee_table.column("doj",width=100)
        self.employee_table.column("idproofcombo",width=100)
        self.employee_table.column("idproof",width=100)
        self.employee_table.column("gender",width=100)
        self.employee_table.column("phone",width=100)
        self.employee_table.column("country",width=100)
        self.employee_table.column("salary",width=100)
        
        
        
        
        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    # ====================== Function Declaration ====================
        
    def add_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="" :   
             messagebox.showerror('Error','All Fields are required')
        else:
            try:
                conn = mysql.connector.connect(host='localhost',username='root',password='R1224@sql', database = 'empdata')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into employee2 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                    
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_name.get(), 
                                                                                                                self.var_designation.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_married.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_doj.get(),
                                                                                                                self.var_idproofcombo.get(),
                                                                                                                self.var_idproof.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_country.get(),
                                                                                                                self.var_salary.get()
                                                                                                               ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Employee has been added!',parent = self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)
        
    # fetch data   
    def fetch_data(self): 
           conn = mysql.connector.connect(host='localhost',username='root',password='R1224@sql', database = 'empdata')
           my_cursor=conn.cursor()
           my_cursor.execute('select* from employee2')
           data = my_cursor.fetchall()
           if len(data)!=0:
               self.employee_table.delete(*self.employee_table.get_children())
               for i in data:
                   self.employee_table.insert("",END,values=i)
               conn.commit
           conn.close()        
        
    def get_cursor(self,event =""):
        cursor_row=self.employee_table.focus()
        content = self.employee_table.item(cursor_row)
        data = content['values']
        
        self.var_dep.set(data[0]) 
        self.var_name.set(data[1]) 
        self.var_designation.set(data[2]) 
        self.var_email.set(data[3]) 
        self.var_address.set(data[4]) 
        self.var_married.set(data[5])
        self.var_dob.set(data[6]) 
        self.var_doj.set(data[7]) 
        self.var_idproofcombo.set(data[8]) 
        self.var_idproof.set(data[9]) 
        self.var_gender.set(data[10]) 
        self.var_phone.set(data[11]) 
        self.var_country.set(data[12])
        self.var_salary.set(data[13])
   
    def update_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="" :   
             messagebox.showerror('Error','All Fields are required')
        else:
            try:
                update = messagebox.askyesno('update','Are You Sure Update this Employee data')
                if update>0:    
                    conn = mysql.connector.connect(host='localhost',username='root',password='R1224@sql', database = 'empdata')
                    my_cursor=conn.cursor()
                    my_cursor.execute('UPDATE employee2 SET Department = %s, Name = %s, Designation = %s, Email = %s, Address = %s, Married = %s, DOB = %s, DOJ = %s, IdProofType = %s, Gender = %s, Phone = %s, Country = %s, Salary = %s WHERE IdProof = %s',(
                        
                                                                                                                                                                                                                                                 self.var_dep.get(),
                                                                                                                                                                                                                                                 self.var_name.get(), 
                                                                                                                                                                                                                                                 self.var_designation.get(),
                                                                                                                                                                                                                                                 self.var_email.get(),
                                                                                                                                                                                                                                                 self.var_address.get(),
                                                                                                                                                                                                                                                 self.var_married.get(),
                                                                                                                                                                                                                                                 self.var_dob.get(),
                                                                                                                                                                                                                                                 self.var_doj.get(),
                                                                                                                                                                                                                                                 self.var_idproofcombo.get(),
                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                 self.var_gender.get(),
                                                                                                                                                                                                                                                 self.var_phone.get(),
                                                                                                                                                                                                                                                 self.var_country.get(),
                                                                                                                                                                                                                                                 self.var_salary.get(),
                                                                                                                                                                                                                                                 self.var_idproof.get()
                        
                                                                                                                                                                                                                                                  ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('success','Employee Successfully updated',parent = self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)

            
     # Delete
    def delete_data(self):
        if self.var_idproof.get()=="":
             messagebox.showerror('Error','All fields are Required')
        else:
            try:
                Delete = messagebox.askyesno('Delete','Are you sure to delete this Employee',parent = self.root) 
                if Delete > 0:
                     conn = mysql.connector.connect(host='localhost',username='root',password='R1224@sql', database = 'empdata')
                     my_cursor=conn.cursor()
                     sql = 'delete from employee2 where IdProof =%s'
                     value = (self.var_idproof.get(),)
                     my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                    #conn.autocommit = True
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Delete','Employee Successfully deleted',parent = self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)

    # Reset
    def reset_data(self):
        self.var_dep.set("Select Depertment")
        self.var_name.set("")
        self.var_designation.set("") 
        self.var_email.set("") 
        self.var_address.set("")
        self.var_married.set("Married")
        self.var_dob.set("") 
        self.var_doj.set("") 
        self.var_idproofcombo.set("Select ID Proof") 
        self.var_idproof.set("") 
        self.var_gender.set("") 
        self.var_phone.set("") 
        self.var_country.set("")
        self.var_salary.set("")
        
    #Search
    def search_data(self):
        if self.var_com_search.get()=='' or self.var_search.get()=='':
            messagebox.showerror('Error','Please select option')
        else:
            try:
                conn = mysql.connector.connect(host='localhost',username='root',password='R1224@sql', database = 'empdata')   
                my_cursor = conn.cursor()
                my_cursor.execute('select * from employee2 where ' +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("",END,values=i)
                conn.commit
                conn.close()
            except Exception as es:
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)                 
                      
if __name__=="__main__":
      root=Tk()
      obj=Employee(root) 
      root.mainloop()