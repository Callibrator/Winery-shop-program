#Created By Callibrator
#Using python 3.x
#callibrator21@gmail.com


import os;
from tkinter import *
from tkinter.ttk import Combobox
import datetime
from tkinter.messagebox import showerror,showinfo


datapath = os.getcwd() + os.sep + "data" + os.sep
userspath = datapath + "users.dat"
krasiapath = datapath+"krasia.dat"
users_data = datapath+"users_data"+os.sep
new_user_tag = "new user "


class User:
        name = ""
        phone = ""
        balance = 00.00
        note = ""
        paragelies = []

        def __init__(self,name = "",lastname = "",phone = "69",address="",balance = 0.0,note = "",paragelies = []):
                self.name = name
                self.lastname = lastname
                self.phone = phone
                self.address = address
                self.balance = balance
                self.note = note
                self.paragelies = paragelies
        def save(self):
                fuser = open(users_data+self.name +" "+self.lastname,"w")
                fuser.write(self.name+"\n")
                fuser.write(self.lastname+"\n")
                fuser.write(str(self.phone)+"\n")
                fuser.write(str(self.address)+"\n")
                fuser.write(str(self.balance)+"\n")
                fuser.write(str(len(self.paragelies))+"\n")
                for i in self.paragelies:
                        fuser.write(str(i) + "\n")
                fuser.write(str(self.note)+"\n")
                fuser.close()
        def load(self):
                fuser = open(users_data+self.name,"r+")
                data = fuser.read()
                fuser.close()
                n = 0
                data = data.split("\n")
                self.name = data[n]
                n+=1
                self.lastname = data[n]
                n+=1
                self.phone = data[n]
                n+=1
                self.address = data[n]
                n+=1
                self.balance =data[n]
                n+=1
                x = int(data[n])
                n+=1
                for i in range(x):
                        self.paragelies.append(data[n])
                        n+=1
                for i in data[n:]:
                        self.note += i+"\n"
                        
        def to_zero(self):
                self.name = ""
                self.lastname = ""
                self.phone = ""
                self.address = ""
                self.balance = 0.0
                self.note = ""
                self.paragelies = []
                

                
                
        
selected_user = User()


last_selected_user = -1

users = []
krasia = []

fcfg = open(datapath+"config.dat","r")
fcfg_data = fcfg.read().split("\n")
fcfg.close()

new_user_tag = fcfg_data[0]

if(os.path.isfile(datapath+"users.dat")):
        fusers = open(userspath,"r")
        for i in fusers:
                i = i.replace("\n","")
                users.append(i)
else:
        fusers = open(userspath,"w")
fusers.close()

if(os.path.isfile(krasiapath)):
        fkrasia = open(krasiapath,"r")
        for i in fkrasia:
                i = i.replace("\n","")
                krasia.append(i)
else:
        fkrasia = open(krasiapath,"w")
        fkrasia.write(fcfg_data[1]+"\n"+fcfg_data[2])
        krasia.append(fcfg_data[1])
        krasia.append(fcfg_data[2])
fkrasia.close()

def delete_from_list(lst,pos):
        try:
                lst.delete(pos,pos)
        except:
                return 0;
        fl = open(userspath,"w")
        for i in lst.get(0,END):
                fl.write(i +"\n")
        fl.close()

def aferesi_paragelias(lst,pos):
        try:
                lst.delete(pos,pos)
        except:
                return 0;
def prosthiki_paragelias(lst,eidos,posotita):
        #str1 = "Είδος: " + eidos +"          Ποσότητα: "+posotita+"        Ημερομηνία: " + datetime.datetime.now().strftime("%d/%m/%y")
        str1 = "Σε εκκρεμότητα "
        while not len(str1) > 16:
                str1 += " "
        
        str1 += eidos +" "
        
        while not len(str1) > 32:
                str1 += " "
                
        str1 += posotita +" "
        
        while not len(str1) > 48:
                str1 += " "

        str1 += datetime.datetime.now().strftime("%d/%m/%y")+" "

        while not len(str1) > 64:
                str1 += " "

        str1 += "0 "

        while not len(str1) > 80:
                str1 += " "

        str1 += "-"
        while not len(str1) > 112:
                str1+= " "
        
        str1 +="-"
        print(str1)

        

                


        lst.insert(END,str1)

        
        
def add_new_user_save(name,lastname,til,address,data,win,lst):
        u = User()
        save_name = name+ " "+lastname
        save_name = save_name.lower()
        for i in data:
                if save_name == i.lower():
                        showerror("Error","Αυτό το όνομας υπάρχει ήδη")
                        return 0
        
        check_name = name + " " +lastname
        check_name = check_name.replace(" ","")

        if check_name == "":
                showerror("Error","Πληκτρολογήστε ενα όνομα")
                return 0


        
        lst.insert(END,name+" "+lastname)
        u.name = name
        u.lastname = lastname
        u.phone = til
        u.address = address
        u.save()
        fl = open(userspath,"w")
        for i in lst.get(0,END):
                fl.write(i +"\n")
        fl.close()

        win.destroy()

def add_new_user(lst):
        data = lst.get(0,END)

        add_user_window =Toplevel()
        add_user_window.title = "Add User"
        add_user_window.Topmost = True
        add_user_window.grid = True

        main_frame = Frame(add_user_window)
        main_frame.pack(side=TOP,fill=BOTH)

        nameFrame1 = Frame(main_frame)
        nameFrame1.pack(fill=X,side=TOP)

        Label(nameFrame1,text="Όνομα: ").pack(side=LEFT)
        
        nametext = Entry(nameFrame1)
        nametext.pack(side=LEFT,fill=X,expand=YES)
        
        Label(nameFrame1,text="Επίθετο: ").pack(side=LEFT)
        lastnametext = Entry(nameFrame1)
        lastnametext.pack(side=LEFT,fill=X,expand=YES)

        Label(nameFrame1,text="Τηλέφωνο: ").pack(side=LEFT)
        tiltext = Entry(nameFrame1)
        tiltext.pack(side=LEFT,fill=X,expand=YES)

        addressFrame = Frame(main_frame)
        addressFrame.pack(side=TOP,fill=X)

        Label(addressFrame,text="Διεύθυνση: ").pack(side=LEFT)
        addresstext = Entry(addressFrame)
        addresstext.pack(side=LEFT,fill=X,expand=YES)

        Button(main_frame,text="Προσθήκη(+)",command=lambda:add_new_user_save(nametext.get(),lastnametext.get(),tiltext.get(),addresstext.get(),data,add_user_window,lst) ).pack(side=BOTTOM,fill=X)


        add_user_window.mainloop()
        




def sort_list(lst):
        data =lst.get(0,END)
        items = []
        for i in data:
                items.append(i)


        items.sort()
        lst.delete(0,END)
        for i in items:
                lst.insert(END,i)
        fl = open(userspath,"w")
        for i in lst.get(0,END):
                fl.write(i +"\n")
        fl.close()
def load_user(listbox,name="",lastname="",phone="69",address="",balance=0.0,note="",paragelies= []):
        x = listbox.curselection()
        global last_selected_user
        global selected_user
        if x == ():
                #print("None")
                return 0
        #print(x)
        u = User()
        u.to_zero()
        u.name = listbox.get(0,END)[int(x[0])]
        u.load()

        if u.name == selected_user.name and u.lastname == selected_user.lastname:
                return 0;

        selected_user = u
        
        last_selected_user = int(x[0])
        name.config(state="normal")
        name.delete(0,END)
        lastname.config(state="normal")
        lastname.delete(0,END)
        phone.config(state="normal")
        phone.delete(0,END)
        address.config(state="normal")
        address.delete(0,END)
        balance.config(state="normal")
        balance.delete(0,END)
        note.delete(0.0,END)
        
        
        

        name.insert(END,u.name)
        name.config(state="disabled")
        lastname.insert(END,u.lastname)
        lastname.config(state="disabled")
        phone.insert(END,u.phone)
        phone.config(state="disabled")
        address.insert(END,u.address)
        address.config(state="disabled")
        balance.insert(END,u.balance)
        balance.config(state="disabled")
        note.insert(END,u.note)
        
        paragelies.delete(0,END)
        
        for i in u.paragelies:
                paragelies.insert(END,i)
        
def save_cur_user(listbox,name,lastname,phone,address,balance,note,paragelies):
        #print(listbox.curselection())
        global last_selected_user
        global selected_user
        
        x =last_selected_user
        u = User()
        u.to_zero()

        name_test_save = name.get()+lastname.get()
        name_test_save = name_test_save.replace(" ","")
        
        if(name_test_save == ""):
                showerror("Error","Πληκτρολογήστε ενα όνομα")
                return 0

        name_save = name.get() + " " + lastname.get()
        prev_save_name = selected_user.name + " " + selected_user.lastname
        prev_save_name = prev_save_name.lower()

        delete_name = selected_user.name + " " +selected_user.lastname

        #find position of the name to delete

        delete_var = 0
        for i in listbox.get(0,END):
                if i.lower() == delete_name.lower():
                        break
                delete_var += 1
        
        if(x != -1):
                u.name = listbox.get(0,END)[x]

                if (name_save.lower() != prev_save_name):
                        if (name_save in listbox.get(0,END)) == True:
                                showerror("Error","Αυτό το όνομας υπάρχει ήδη")
                                return 0
                        else:
                                os.remove(users_data+ delete_name)
                                listbox.delete(str(delete_var),str(delete_var))
                                listbox.insert(str(delete_var),name_save)
                else:
                        os.remove(users_data+delete_name)
                        listbox.delete(str(delete_var),str(delete_var))
                        listbox.insert(str(delete_var),name_save)

                        
        else:
                if(name_save in listbox.get(0,END)) == True:
                                showerror("Error","Αυτό το όνομας υπάρχει ήδη")
                                return 0
                else:
                        listbox.insert(END,(u.name +" "+u.lastname))
                        
        u.name = name.get()
        u.lastname = lastname.get()
        u.phone = phone.get()
        u.address = address.get()
        balance.config(state="normal")
        u.balance = balance.get()
        balance.config(state="disabled")
        u.note = note.get(0.0,END)
        for i in paragelies.get(0,END):
                u.paragelies.append(i)
        

        fl = open(userspath,"w")
        for i in listbox.get(0,END):
                fl.write(i +"\n")
        fl.close()

        
        u.save()
        
                        



def add_balance(balance,value):
        b = balance.get()
        try:
                b = float(b)
        except:
                b = 0
        
        v = value.get().replace(",",".")
        try:
                v = float(v)
                balance.config(state="normal")
                b += v
                balance.delete(0,END)
                balance.insert(END,b)
                balance.config(state="disabled")
        except:
                showerror("Error","Κάτι δεν πήγε καλά\nΕλέγξτε τη βάλατε στο πεδίο τίμης")
                return 0
        value.delete(0,END)
        value.insert(END,0)
        
def min_balance(balance,value):
        b = balance.get()
        try:
                b = float(b)
        except:
                b = 0
                
        v = value.get().replace(",",".")
        try:
                v = float(v)
                balance.config(state="normal")
                b -= v
                balance.delete(0,END)
                balance.insert(END,b)
                balance.config(state="disabled")
        except:
                showerror("Error","Κάτι δεν πήγε καλά\nΕλέγξτε τη βάλατε στο πεδίο τίμης")
                return 0
        value.delete(0,END)
        value.insert(END,0)
def return_edited_data(name,lastname,phone,address,newName,newLastname,newPhone,newAddress,win):
        name.config(state="normal")
        lastname.config(state="normal")
        phone.config(state="normal")
        address.config(state="normal")
        
        name.delete(0,END)
        lastname.delete(0,END)
        phone.delete(0,END)
        address.delete(0,END)

        name.insert(END,newName)
        lastname.insert(END,newLastname)
        phone.insert(END,newPhone)
        address.insert(END,newAddress)

        name.config(state="disabled")
        lastname.config(state="disabled")
        phone.config(state="disabled")
        address.config(state="disabled")

        win.destroy()
        

def edit_user_data(name,lastname,phone,address):

        edit_window = Toplevel()
        edit_window.title("Edit user")
        edit_window.Topmost = True
        edit_window.grid = True

        main_frame = Frame(edit_window)
        main_frame.pack(fill=BOTH)

        button_frame = Frame(main_frame)
        button_frame.pack(side=BOTTOM,fill=X,expand=YES)

        frame1 = Frame(main_frame)
        frame1.pack(side=LEFT,fill=Y)
        
        frame1a = Frame(frame1)
        frame1a.pack(side=TOP,fill=X)
        frame1b= Frame(frame1)
        frame1b.pack(side=TOP,fill=X)
        frame1c= Frame(frame1)
        frame1c.pack(side=TOP,fill=X)
        frame1d= Frame(frame1)
        frame1d.pack(side=TOP,fill=X)
        

        frame2 = Frame(main_frame)
        frame2.pack(side=LEFT,fill=BOTH,expand=YES)
        
        frame2a = Frame(frame2)
        frame2a.pack(side=TOP,fill=X)
        frame2b = Frame(frame2)
        frame2b.pack(side=TOP,fill=X)
        frame2c = Frame(frame2)
        frame2c.pack(side=TOP,fill=X)
        frame2d = Frame(frame2)
        frame2d.pack(side=TOP,fill=X)

        Label(frame1a,text="Όνομα: ").pack(side=LEFT,fill=X)
        Label(frame1b,text="Επίθετο: ").pack(side=LEFT,fill=X)
        Label(frame1c,text="Τηλέφωνο: ").pack(side=LEFT,fill=X)
        Label(frame1d,text="Διεύθυνση: ").pack(side=LEFT,fill=X)

        nameText= Entry(frame2a)
        nameText.pack(fill=X,expand=YES)
        lastnameText = Entry(frame2b)
        lastnameText.pack(fill=X,expand=YES)
        phoneText = Entry(frame2c)
        phoneText.pack(fill=X,expand=YES)
        addressText = Entry(frame2d)
        addressText.pack(fill=X,expand=YES)

        #inserting data

        nameText.delete(0,END)
        nameText.insert(END,name.get())
        lastnameText.delete(0,END)
        lastnameText.insert(END,lastname.get())
        phoneText.delete(0,END)
        phoneText.insert(END,phone.get())
        addressText.delete(0,END)
        addressText.insert(END,address.get())

        Button(button_frame,text= "Τελος",command=lambda:return_edited_data(name,lastname,phone,address,nameText.get(),lastnameText.get(),phoneText.get(),addressText.get(),edit_window)).pack(side=LEFT,fill=X,expand=YES)

        edit_window.mainloop()
def remove_wine_from_list(lst,select):
        try:
                lst.delete(str(select[0]),str(select[0]))
        except:
                pass
def save_edited_wine(items,win):
        global krasia
        krasia = items
        fl = open(krasiapath,"w")
        for i in krasia:
                fl.write(str(i) + "\n")
        fl.close()
        showinfo("INFO","Aπαιτείται επανεκκίνηση του προγράμματος για να πραγματοποιηθούν οι αλλαγές")
        win.destroy()
def add_wine_list(lst,item):
        items = lst.get(0,END)
        if item in items:
                return 0
        if item.replace(" ","") == "":
                return 0
        lst.insert(END,item)
        
        
def edit_wines(items):
        wine_win = Toplevel()
        wine_win.title("Eπεξεργασία κρασιών")
        wine_win.Topmost = True

        main_frame = Frame(wine_win)
        main_frame.pack(expand=YES,fill=BOTH)

        frame1 = Frame(main_frame)
        frame1.pack(expand=YES,fill=BOTH)

        item_list = Listbox(frame1)
        item_list.pack(expand=YES,fill=BOTH)
        
        for i in items:
                item_list.insert(END,i)
        

        frame2 = Frame(main_frame)
        frame2.pack(fill=X,expand=YES)

        product = Entry(frame2)
        product.pack(side=LEFT,fill=X,expand=YES)

        Button(frame2,text="Προσθήκη στην λίστα",command=lambda:add_wine_list(item_list,product.get())).pack(side=RIGHT)

        frame3 = Frame(main_frame)
        frame3.pack(fill=X,expand=YES)

        Button(frame3,text="Αφαίρεση από την λίστα",command=lambda:remove_wine_from_list(item_list,item_list.curselection())).pack(side=LEFT,expand=YES,fill=X)

        Button(frame3,text="Αποθήκευση & Έξοδος",command=lambda:save_edited_wine(item_list.get(0,END),wine_win)).pack(side=LEFT,expand=YES,fill=X)
        


        wine_win.mainloop()
        

root = Tk()
root.title("Programa")
mn = Menu(root)

filemenu = Menu(mn,tearoff=0)

#filemenu.add_command(label="Αποθηκευση")
filemenu.add_command(label="Εξωδός",command=root.quit)
filemenu.add_command(label="Eπεξεργασία προϊόντων",command=lambda:edit_wines(krasia))

mn.add_cascade(label="Αρχείο",menu=filemenu)

root.config(menu=mn)

frame1 = Frame(root)
frame1.pack(side=LEFT,fill=Y)

Label(frame1,text="Λογαριασμοι: ").pack()

frame1_1 = Frame(frame1)
frame1_1.pack(fill=BOTH,expand=YES)

listbox = Listbox(frame1_1)
listbox.pack(fill=BOTH,expand=YES,side=LEFT)

listbox_scrollbar = Scrollbar(frame1_1)
listbox_scrollbar.pack(side=RIGHT,fill=Y)

listbox.config(yscrollcommand=listbox_scrollbar.set)
listbox_scrollbar.config(command=listbox.yview)

for i in users:
        listbox.insert(END,i)


Button(frame1,text="Προσθήκη(+)",command=lambda:add_new_user(listbox)).pack(side=LEFT)
Button(frame1,text="Aφαιρεση(-)",command = lambda:delete_from_list(listbox,listbox.curselection())).pack(side=LEFT)
Button(frame1,text="Ταξινόμηση",command = lambda:sort_list(listbox)).pack(side=LEFT)

frame2 = Frame(root)
frame2.pack(side=TOP)

Label(frame2,text="Δεδομένα: ").pack(side=TOP)

nameframe = Frame(frame2)
nameframe.pack(side=TOP,fill=X)

Label(nameframe,text="Όνομα: ").pack(side=LEFT)
name = Entry(nameframe)
name.pack(side=LEFT,fill=X,expand=YES)
name.config(state="disabled")

Label(nameframe,text="Επίθετο: ").pack(side=LEFT)
lastname = Entry(nameframe)
lastname.pack(side=LEFT,fill=X,expand=YES)
lastname.config(state="disabled")

Label(nameframe,text="Τηλέφωνο: ").pack(side=LEFT)
til = Entry(nameframe)
til.pack(side=LEFT,fill=X,expand=YES)
til.config(state="disabled")

addressFrame = Frame(frame2)
addressFrame.pack(side=TOP,fill=X)

Label(addressFrame,text="Διεύθυνση: ").pack(side=LEFT)
address = Entry(addressFrame)
address.pack(side=LEFT,fill=X,expand=YES)
address.config(state="disabled")

Button(addressFrame,text="Επεξεργασία δεδομένων",command=lambda:edit_user_data(name,lastname,til,address)).pack(side=LEFT)




balanceframe = Frame(frame2)
balanceframe.pack(side=TOP,fill=X)

Label(balanceframe,text="Yπόλοιπο").pack(side=LEFT)
balance = Entry(balanceframe)
balance.config(state="disabled")
balance.pack(side=LEFT,fill=X,expand=YES)

Label(frame2,text="Εισαγωγή/Εξαγωγή Χρηματων").pack(side=TOP)

moneyframe = Frame(frame2)
moneyframe.pack(side=TOP)

inmoney = Entry(moneyframe)
inmoney.insert(0,"0")
inmoney.pack(side=LEFT)

Button(moneyframe,text="Προσθήκη(+)",command=lambda:add_balance(balance,inmoney)).pack(side=LEFT)

outmoney = Entry(moneyframe)
outmoney.insert(0,"0")
outmoney.pack(side=LEFT)

Button(moneyframe,text="Aφαιρεση(-)",command=lambda:min_balance(balance,outmoney)).pack(side=LEFT)



paraframe1 = Frame(frame2)
paraframe1.pack(side=TOP,fill=X)

Label(paraframe1,text="Παραγγελίες").pack(side=LEFT)

paraframe2 = Frame(frame2)
paraframe2.pack(side=TOP,fill=X)

Label(paraframe2,text="Είδος: ").pack(side=LEFT)
eidos = Combobox(paraframe2,value = krasia)
eidos.set(krasia[0])
eidos.pack(side=LEFT)

Label(paraframe2,text="Ποσότητα: ").pack(side=LEFT)

amount = Entry(paraframe2)
amount.insert(0,"1")
amount.pack(side=LEFT)


paraframe3 = Frame(frame2)
paraframe3.pack(side=TOP,fill=X)

Label(paraframe3,text="Τρεχόν παραγγελίες: ").pack(side=LEFT)

paraframe3b = Frame(frame2)
paraframe3b.pack(side=TOP,fill=X)

Label(paraframe3b,text="Κατάσταση           Είδος           Ποσότητα        Ημερομηνία      Έχουν παραδοθεί Ημερομηνία τελευταίας παράδοσης Τρόπος πληρωμής").pack(side=LEFT)


paraframe4 = Frame(frame2)
paraframe4.pack(side=TOP,fill=X)

paraframe4a = Frame(paraframe4)
paraframe4a.pack(side=LEFT,fill=Y)

paralist = Listbox(paraframe4)
paralist.pack(side=LEFT,fill=X,expand=YES)


paralist_bar = Scrollbar(paraframe4)
paralist_bar.pack(side=LEFT,fill=Y)

paralist.config(yscrollcommand=paralist_bar.set)


paralist_bar.config(command=paralist.yview)


paraframe5 = Frame(frame2)
paraframe5.pack(side=TOP,fill =X)

Button(paraframe2,text="Προσθήκη(+)",command=lambda:prosthiki_paragelias(paralist,eidos.get(),amount.get())).pack(side=LEFT,fill=X,expand=YES)

Button(paraframe5,text="Αφαιρεση παραγγελίας",command=lambda:aferesi_paragelias(paralist,paralist.curselection())).pack(side=LEFT)

noteframe = Frame(frame2)
noteframe.pack(side=TOP,fill=X)
Label(noteframe,text="Σημείωση: ").pack(side=LEFT)

note = Text(frame2,height=5)
note.pack(side=TOP,fill=X)


saveframe = Frame(frame2)
saveframe.pack(side=TOP,fill=X)

Button(saveframe,text = "Αποθηκευση",fg="red",command=lambda:save_cur_user(listbox,name,lastname,til,address,balance,note,paralist)).pack(side=LEFT,fill=X,expand=YES)

listbox.bind("<<ListboxSelect>>",lambda j:load_user(listbox,name,lastname,til,address,balance,note,paralist))
root.mainloop()
