# Timetable project
# Intermediate Stage
# Data Entry upto lf#1, lf#2 complete
from tkinter import*
from tkinter import ttk
import tkinter as tk
import pandas as pd
from tt_show_class import TimeTable

def dic1_fun(key_col,val_col):
    keys = df1[key_col]
    values = df1[val_col]
    return(dict(zip(keys,values)))
def dic2_fun(key_col,val_col):
    keys = df2[key_col]
    values = df2[val_col]
    return(dict(zip(keys,values)))
def parent_dept_selection(event): 
    global df2
    data_tt["faculty_dept"] = dept_code.get()
    df2 = pd.read_excel("faculty_data.xlsx",sheet_name=data_tt["faculty_dept"])
    df2["ID2"] = df2.index
    emp_code.set('')
    emp_dict = dic2_fun("ID2","Emp_code")
    dept_dict = dic2_fun("ID2","Dept")
    nick_name_dict = dic2_fun("ID2","Nick_name")
    position_dict = dic2_fun("ID2","Position")  
    emp_list = list(emp_dict.values())
    emp_code.config(values=emp_list)
def emp_code_selection(event):
    data_tt["faculty_code"] = emp_code.get()
    assign_dept_code.config(values=("CE","ME","EE"))
def dept_option_selection(event):
    data_tt["class_dept"] = assign_dept_code.get()
    odd_even_code.config(values=("ODD","EVEN"))
def odd_even_selection(event):
    global odd_even
    odd_even = odd_even_code.get()
    if odd_even == 'ODD':
        odd_even_list = ['s1','s3','s5','s7']
    elif odd_even == 'EVEN':
        odd_even_list = ['s2','s4','s6','s8']
    else:
        pass
    semester_code.set('')
    semester_code.config(values=odd_even_list)
def semester_option_selection(event):
    global df1,odd_even
    data_tt["class_semester"] = semester_code.get()
    df1 = pd.read_excel(f"curiculam_{data_tt['class_dept']}.xlsx",sheet_name=data_tt["class_semester"])
    df1["ID1"] = df1.index
    global code_dict,select_dict,class_count_dict
    global lec_dict,tut_dict,lab_dict,proj_dict
    code_dict = dic1_fun("ID1","Code")
    select_dict = dic1_fun("ID1","Select")
    class_count_dict = dic1_fun("ID1","Number")
    lec_dict = dic1_fun("ID1","L")
    tut_dict = dic1_fun("ID1","T")
    lab_dict = dic1_fun("ID1","P")
    proj_dict = dic1_fun("ID1","R")
    ltp_code.config(values=("Lecture","Tutorial","Practical","Projects"))
def ltp_option_selection(event):
    class_x=ltp_code.get()
    data_tt["class_type"] = class_x
    #print(class_x)
    global df1,code_dict,select_dict,class_count_dict
    global lec_dict,tut_dict,lab_dict,proj_dict
    code_dict = dic1_fun("ID1","Code")
    code_list = list(code_dict.values())
    select_list = list(select_dict.values())
    class_count_list = list(class_count_dict.values())
    match class_x:
        case "Lecture":
            ref_list = list(lec_dict.values())
        case "Tutorial":
            ref_list = list(tut_dict.values())
        case "Practical":
            ref_list = list(lab_dict.values())
        case "Projects":
            ref_list = list(proj_dict.values())
        case _:
            print("Who")       
    updated_dict=code_dict
    keys_list = list(select_dict.keys())
    ref_temp=[]
    for i in range(len(ref_list)):
        if select_list[i] == 0:
            del updated_dict[keys_list[i]]
        else:
            ref_temp.append(ref_list[i])
    updated_list = list(updated_dict.values())
    new_ltp=[]
    for i in range(len(ref_temp)):
        if ref_temp[i] != 0:
            new_ltp.append(updated_list[i])
    sub_code.set('')
    sub_code.config(values=new_ltp)
def sub_option_selection(event):
    data_tt["sub_code"] = sub_code.get()
    action_code.config(values=("PROCEED","CLEAR"))
def action_option_selection(event):
    action_entry=action_code.get()
    #print(data_tt)
    if action_entry == "CLEAR":
        lf1_lf2_clear()
        pass
    elif action_entry == "PROCEED":
        cb1.config(state='normal')
        cb2.config(state='normal')
        TimeTable(root)
    else:
        pass
def cancel_option_selection(event):
    lf1_lf2_clear()
    pass

def lf1_lf2_clear():
    emp_code.set('')
    emp_code['values']=()
    assign_dept_code.set('')
    odd_even_code.set('')
    semester_code.set('')
    ltp_code.set('')
    sub_code.set('')
    cancel_code.set('')

def common_for_cancel_options():
    pass

def clear_day_slot():
    text_box1.delete('1.0','end')
    text_box2.delete('1.0','end')
    sr0.set(0)
    sr1.set(0)
    sr2.set(0)
    sr3.set(0)
    sr4.set(0)
    sr5.set(0)
    sr6.set(0)

def week_click(week_value):
    day_slot["week_slot"]=r3.get()
    day_slot["time_slot0"]=sr0.get()
    day_slot["time_slot1"]=sr1.get()
    day_slot["time_slot2"]=sr2.get()
    day_slot["time_slot3"]=sr3.get()
    day_slot["time_slot4"]=sr4.get()
    day_slot["time_slot5"]=sr5.get()
    day_slot["time_slot6"]=sr6.get()
    #print(day_slot)

def cancel_option(event):
    global clear_status
    cancel_entry = cancel_click.get()
    if cancel_entry == "Assigned Class":
        clear_status = 1
        common_for_cancel_options()
        text_box1.insert('1.0',"All the data entry under 1)Assigned for Dept./Topic 2)semester 3)Class Type 4)Subject Code will be reset for fresh entry.")    
    elif cancel_entry == "Day & Slot":
        clear_status = 2
        common_for_cancel_options()
        text_box1.insert('1.0',"All the data entry under 1)Assigned for Dept./Topic 2)semester 3)Class Type 4)Subject Code will be reset for fresh entry.")
    else:  
        clear_status = 3
        common_for_cancel_options()
        text_box1.insert('1.0',"All the data entry under 1)Assigned for Dept./Topic 2)semester 3)Class Type 4)Subject Code will be reset for fresh entry.")
def confirm_cancel():
    cancel_check.config(text="Clear Data Entry",fg="black")
    cancel_button.config(text="Confirm CLEAR",bg="white",fg="black")
    enter_action.config(bg="white")
    global clear_status
    if clear_status == 0:
        clear_lf1_2()
    elif clear_status == 1:
        clear_lf1_2()
    elif clear_status == 2:
        clear_day_slot()
    else:
        clear_ALL()
def verify_ok():
    pass
def update_tt():
    #print("123")
    TimeTable(root)

root=Tk()
root.title("Data entry by Faculty for TimeTable")
w_width = root.winfo_screenwidth()
w_height = root.winfo_screenheight()
dev_WIDTH = 700
dev_HEIGHT = 550
ref_s_WIDTH = 1920
ref_s_HEIGHT = 1080
s_width = int(dev_WIDTH*w_width/ref_s_WIDTH)
s_height = int(dev_HEIGHT*w_height/ref_s_HEIGHT)
#print(s_width,s_height)
root.geometry("700x550")
root.iconbitmap('Logo.ico')
root.columnconfigure(0,weight=1) #weight= 1 indicates scale of one
root.rowconfigure(0,weight=1)
frame=Frame(root)
frame.grid(row=0,column=0,padx=10,pady=5,sticky="nsew")
x = "Lecture"
data_tt={"faculty_dept":'CE',"faculty_code":1234,"class_dept":'CE',
    "class_semester":'S1',"class_type":'Lecture',"sub_code":'Maths'}
odd_even="odd"
day_slot={"week_slot":3,"time_slot0":0,"time_slot1":1,"time_slot2":2,"time_slot3":3,
    "time_slot4":4,"time_slot5":5,"time_slot6":6}
sr=IntVar()
#LBELFRAME lf1
frame.columnconfigure(0,weight=1) #weight= 1 indicates scale of one
frame.rowconfigure((0,1,2,3),weight=1)
lf1=LabelFrame(frame,text="Employ Code: Parent Dept: Faculty Initial: Assigned Dept.",padx=5,pady=2,fg="Blue")
lf1.grid(row=0,column=0,padx=10,pady=5,sticky="nsew")
lf1.columnconfigure((0,1,2,3),weight=1,uniform="a") #weight= 1 indicates scale of one
lf1.rowconfigure((0,1),weight=1)
dept_emp_code=Label(lf1,text="Parent Dept.& Emp.Code",width=15)
dept_emp_code.grid(row=0,column=0,columnspan=2,padx=2,pady=2,sticky="nsew")
dept_class=Label(lf1,text="Assigned Department/Semester",width=15)
dept_class.grid(row=0,column=2,columnspan=2,padx=2,pady=2,sticky="nsew")
#lf1 entries
dept_options=StringVar()
dept_code=ttk.Combobox(lf1,textvariable=dept_options,state='raedonly')
dept_code.grid(row=1,column=0,padx=10,pady=2,sticky="nsew")
dept_code['values']=("CE","ME","EE")
dept_code.current()
dept_code.bind("<<ComboboxSelected>>",parent_dept_selection)
emp_options=StringVar()
emp_code=ttk.Combobox(lf1,textvariable=emp_options,state='raedonly')
emp_code.grid(row=1,column=1,padx=10,pady=2,sticky="nsew")
emp_code['values']=()
emp_code.current()
emp_code.bind("<<ComboboxSelected>>",emp_code_selection)
assign_dept_options=StringVar()
assign_dept_code=ttk.Combobox(lf1,textvariable=assign_dept_options,state='raedonly')
assign_dept_code.grid(row=1,column=2,padx=10,pady=2,sticky="nsew")
assign_dept_code['values']=()
assign_dept_code.current()
assign_dept_code.bind("<<ComboboxSelected>>",dept_option_selection)
odd_even_options=StringVar()
odd_even_code=ttk.Combobox(lf1,textvariable=odd_even_options,state='raedonly')
odd_even_code.grid(row=1,column=3,padx=10,pady=2,sticky="nsew")
odd_even_code['values']=()
odd_even_code.current()
odd_even_code.bind("<<ComboboxSelected>>",odd_even_selection)
#LBELFRAME lf2
lf2=LabelFrame(frame,text="Selecting Assigned Classes",padx=5,pady=2,fg="Blue")
lf2.grid(row=1,column=0,padx=10,pady=5,sticky="nsew")
#lf2 options
global semester_options
#lf2 labels
lf2.columnconfigure((0,1,2,3),weight=1,uniform="a") #weight= 1 indicates scale of one
lf2.rowconfigure((0,1,2),weight=1)
text_box1=Text(lf2, width=60,height=3,fg="red",font=("Ariel",11))
text_box1.grid(row=0, column=0,columnspan=4,padx=10,pady=5,sticky="nsew")
semester_class=Label(lf2,text="Semester",width=15)
semester_class.grid(row=1,column=0,padx=2,pady=2,sticky="nsew")
ltp_type=Label(lf2,text="Class type",width=15)
ltp_type.grid(row=1,column=1,padx=2,pady=2,sticky="nsew")
sub_code=Label(lf2,text="Subject Code",width=15)
sub_code.grid(row=1,column=2,padx=2,pady=2,sticky="nsew")
sub_check=Label(lf2,text="ACTION",width=15)
sub_check.grid(row=1,column=3,padx=2,pady=2,sticky="nsew")
#lf2 entries
semester_options=StringVar()
semester_code=ttk.Combobox(lf2,textvariable=semester_options,state='raedonly')
semester_code.grid(row=2,column=0,padx=10,pady=2,sticky="nsew")
semester_code['values']=()
semester_code.current()
semester_code.bind("<<ComboboxSelected>>",semester_option_selection)
ltp_options=StringVar()
ltp_code=ttk.Combobox(lf2,textvariable=ltp_options,state='raedonly')
ltp_code.grid(row=2,column=1,padx=10,pady=2,sticky="nsew")
ltp_code['values']=()
ltp_code.current()
ltp_code.bind("<<ComboboxSelected>>",ltp_option_selection)
sub_options=StringVar()
sub_code=ttk.Combobox(lf2,textvariable=sub_options,state='raedonly')
sub_code.grid(row=2,column=2,padx=10,pady=2,sticky="nsew")
sub_code['values']=()
sub_code.current()
sub_code.bind("<<ComboboxSelected>>",sub_option_selection)
action_options=StringVar()
action_code=ttk.Combobox(lf2,textvariable=action_options,state='raedonly')
action_code.grid(row=2,column=3,padx=10,pady=2,sticky="nsew")
action_code['values']=("CLEAR")
action_code.current()
action_code.bind("<<ComboboxSelected>>",action_option_selection)
#LBELFRAME lf3
lf3=LabelFrame(frame,text="Timetable Weekday and Slot selection",padx=5,pady=2,fg="Blue")
lf3.grid(row=2,column=0,padx=10,pady=5,sticky="nsew")
lf3.columnconfigure((0,1,2,3,4,5,6),weight=1,uniform="a") #weight= 1 indicates scale of one
lf3.rowconfigure((0,1,2),weight=1)
r3=IntVar()
week_day=["Monday","Tuesday","Wednesday","Thursday","Friday"]
for i in range(len(week_day)):
    week=(Radiobutton(lf3,text=week_day[i],variable=r3,value=i,command=lambda:week_click(r3.get())))
    week.grid(row=0,column=i+1,padx=10,pady=2,sticky="nsew")
#print(week.r3)
show_msg=Label(lf3,text="-----------Slot 1 to Slot 6 for Lecture & Tutorial and Slot X optional-------------",fg="Blue")
show_msg.grid(row=1, column=0, columnspan=7,padx=2,pady=2,sticky="nsew")
slots=["Slot 1","Slot 2","Slot 3","Slot 4","Slot 5","Slot 6","Slot X"]
sr0 = IntVar()
sr1 = IntVar()
sr2 = IntVar()
sr3 = IntVar()
sr4 = IntVar()
sr5 = IntVar()
sr6 = IntVar()
global cb1
cb1=Checkbutton(lf3, text=slots[0], variable=sr0,state='disabled')
cb1.grid(row=3, column=0,sticky="nsew")
cb2=Checkbutton(lf3, text=slots[1], variable=sr1,state='disabled')
cb2.grid(row=3, column=1,sticky="nsew")
cb3=Checkbutton(lf3, text=slots[2], variable=sr2,state='disabled')
cb3.grid(row=3, column=2,sticky="nsew")
cb4=Checkbutton(lf3, text=slots[3], variable=sr3,state='disabled')
cb4.grid(row=3, column=3,sticky="nsew")
cb5=Checkbutton(lf3, text=slots[4], variable=sr4,state='disabled')
cb5.grid(row=3, column=4,sticky="nsew")
cb6=Checkbutton(lf3, text=slots[5], variable=sr5,state='disabled')
cb6.grid(row=3, column=5,sticky="nsew")
cb7=Checkbutton(lf3, text=slots[6], variable=sr6,state='disabled')
cb7.grid(row=3, column=6,sticky="nsew")
#LBELFRAME lf4
#lf4 options
lf4=LabelFrame(frame,text="Timetable Data Entry Commands",padx=5,pady=2,fg="Blue")
lf4.grid(row=3,column=0,padx=10,pady=5,sticky="nsew")
lf4.columnconfigure((0,1,2,3),weight=1,uniform="a") #weight= 1 indicates scale of one
lf4.rowconfigure((0,1),weight=1)
text_box2=Text(lf4, width=60,height=3,fg="red",font=("Ariel",11))
text_box2.grid(row=0,column=0,columnspan=4,padx=10,pady=5,sticky="nsew")
cancel_check=Label(lf4,text="Cancel Data Entry",width=15)
cancel_check.grid(row=1,column=0,columnspan=2, padx=2,pady=2,sticky="nsew")
cancel_options=StringVar()
cancel_code=ttk.Combobox(lf4,textvariable=cancel_options,state='raedonly')
cancel_code.grid(row=2,column=0,padx=10,pady=2,sticky="nsew")
cancel_code['values']=("Clear Day & Slot ","Clear All Data","Clear Data from Time Table")
cancel_code.current()
cancel_code.bind("<<ComboboxSelected>>",cancel_option_selection)

cancel_button=Button(lf4,text="Confirm CANCEL",bg="white",command=confirm_cancel)
cancel_button.grid(row=2,column=1,padx=2,pady=2,sticky="nsew")
verify_data=Label(lf4,text="Verify & Update TimeTable",width=15)
verify_data.grid(row=1,column=2,columnspan=2, padx=2,pady=2,sticky="nsew")
verify_button=Button(lf4,text="Verified OK",bg="white",command=verify_ok)
verify_button.grid(row=2,column=2,padx=2,pady=2,sticky="nsew")
update_button=Button(lf4,text="Update TimeTable",bg="white",command=update_tt)
update_button.grid(row=2,column=3,padx=2,pady=2,sticky="nsew")
root.mainloop()