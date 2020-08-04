from tkinter import *
import sqlite3

root = Tk()
root.geometry("300x400")
root.configure(bg='red4')
root.title("SOS GAME")

global fname
global lname
global uname
global pword

conn = sqlite3.connect('people.db')
c = conn.cursor()

'''
#admin executed
c.execute("INSERT INTO mypeople VALUES('admin','admin','admin','123456','0','0')")
'''	

#delete 
#c.execute("DELETE from mypeople WHERE rowid=2")
#conn.commit()

#print all information
all_people = c.execute("SELECT rowid, * FROM mypeople")
for person in all_people:
    print(person[0],person[1],person[2],person[3],person[4])
conn.close()



def play():
    info_frame.pack_forget()
    

def change_info():
    info_frame.pack_forget()
    


def information_manager_signup():
    root.title("Your Information")
    global info_frame
    info_frame = Frame(root, bg='red4', height=400, width=300)
    info_frame.pack()

    register_label = Label(info_frame,text="Your Profile Information!", bg='red4', fg='white', font="Helvetica 12 bold")
    register_label.pack(pady=(50,20))

    #information labels
    iname_l = Label(info_frame,text="Name: \n"+fname, bg='red4', fg='white', font="Helvetica 12").pack()
    ilname_l = Label(info_frame,text="Last Name:\n"+lname, bg='red4', fg='white', font="Helvetica 12").pack()
    iuname_l = Label(info_frame,text="Username:\n"+uname, bg='red4', fg='white', font="Helvetica 12").pack()
    itplayed_l = Label(info_frame,text="Times Played:\n 0", bg='red4', fg='white', font="Helvetica 12").pack()
    itwon_l = Label(info_frame,text="Times Won:\n 0", bg='red4', fg='white', font="Helvetica 12").pack()

    i_changeinfo_btn = Button(info_frame, text="Change Info", bg='black', fg='red4', width=20, command=play).pack(pady=(10,5))
    i_play_btn = Button(info_frame, text="PLAY", bg='black', fg='red4', width=20, command=change_info).pack(pady=(0,5))


def information_manager_login():
    global fname
    global lname
    global uname
    global pword
    global tplayed
    global twon

    #title and frame and information label
    global info_frame
    root.title("Your Information")
    info_frame = Frame(root, bg='red4', height=400, width=300)
    info_frame.pack()
    register_label = Label(info_frame,text="Your Profile Information!", bg='red4', fg='white', font="Helvetica 12 bold")
    register_label.pack(pady=(50,20))

    conn = sqlite3.connect('people.db')
    c = conn.cursor()
    c.execute("SELECT * FROM mypeople WHERE user_name=? AND pass_word=?",(uname,pword,))
    myuser = c.fetchall()

    myusers_fname = myuser[0][0]
    myusers_lname = myuser[0][1]
    myusers_uname = myuser[0][2]
    myusers_tplayed = str(myuser[0][4])
    myusers_twon = str(myuser[0][5])

    #information labels
    iname_l = Label(info_frame, text="Name: \n"+myusers_fname, bg='red4', fg='white', font="Helvetica 12").pack()
    ilname_l = Label(info_frame, text="Last Name:\n"+myusers_lname, bg='red4', fg='white', font="Helvetica 12").pack()
    iuname_l = Label(info_frame, text="Username:\n"+myusers_uname, bg='red4', fg='white', font="Helvetica 12").pack()
    itplayed_l = Label(info_frame, text="Times Played:\n"+myusers_tplayed, bg='red4', fg='white', font="Helvetica 12").pack()
    itwon_l = Label(info_frame, text="Times Won:\n"+myusers_twon, bg='red4', fg='white', font="Helvetica 12").pack()

    i_changeinfo_btn = Button(info_frame, text="Change Info", bg='black', fg='red4', width=20, command=play).pack(pady=(10,5))
    i_play_btn = Button(info_frame, text="PLAY", bg='black', fg='red4', width=20, command=change_info).pack(pady=(0,5))




def login():
    global fname
    global lname
    global uname
    global pword
    global tplayed
    global twon


    def login_database():
        global fname
        global lname
        global uname
        global pword
        global tplayed
        global twon

        uname = uname_e_l.get()
        pword = pword_e_l.get()

        


        if uname == 'admin' and pword=='123456':
            def admin_pass_changer():
                new_pass = admin_e.get()
                conn = sqlite3.connect('people.db')
                c = conn.cursor()
                c.execute("UPDATE mypeople SET pass_word=? WHERE user_name='admin'", (new_pass,))

            login_frame.pack_forget()
            admin_change_pword_f = Frame(login_frame, bg='red4', height=400, width=300).pack()
            
            pword_text = StringVar()
            admin_change_pword_l = Label(admin_change_pword_f, text='Please Change Your Password!!', bg='red4', fg='white', font="Helvetica 12 bold").pack(pady=(80,40))
            admin_e = Entry(admin_change_pword_f,textvariable=StringVar()).pack()
            admin_change_pword_btn = Button(admin_change_pword_f, text='change password',bg='black', fg='red4', borderwidth=2, width=20,command=admin_pass_changer).pack()

            
            
        else:
            conn = sqlite3.connect('people.db')
            c = conn.cursor()
            c.execute("SELECT * FROM mypeople WHERE user_name=? AND pass_word=?",(uname,pword,))
            user = c.fetchall()
        
            if uname=='' or pword=='':
                information_missing_label = Label(login_frame,text='Please enter all the information',bg='red4',fg='white').pack()
                uname = uname_e_l.get()
                pword = pword_e_l.get()

            elif user == []:
                pword_e_l.delete(0,END)
                pword = pword_e_l.get()
                wrong_uorp = Label(login_frame,text="Wrong Username or Password!",bg='red4',fg='white').pack()
                
            
            else:
                login_frame.pack_forget()
                information_manager_login()


    welcome_label.pack_forget()
    login_btn.pack_forget()
    signup_btn.pack_forget()

    #creating a frame for entries
    login_frame = Frame(root,height=400,width=300,bg='red4')
    login_frame.pack()

    login_label = Label(login_frame,text="Please Enter Your Username And Password!", bg='red4', fg='white', font="Helvetica 12")
    login_label.pack(pady=(50,20))


    uname_text=StringVar()
    pword_text=StringVar()

    #labels and entries
    uname_label_l = Label(login_frame,text="User Name*", bg='red4', fg='white', font="Helvetica 12")
    uname_label_l.pack()
    uname_e_l = Entry(login_frame,textvariable=uname_text,borderwidth=2,width=40)
    uname_e_l.pack()
    

    pword_label_l = Label(login_frame,text="Pass Word*", bg='red4', fg='white', font="Helvetica 12")
    pword_label_l.pack()
    pword_e_l = Entry(login_frame,textvariable=pword_text,borderwidth=2,width=40)
    pword_e_l.pack()

    #login button
    login_btn_2 = Button(login_frame,text="Login", width=20, command=login_database)
    login_btn_2.pack(pady=30)



def signup():
    root.title("SignUp")
    global fname
    global lname
    global uname
    global pword
    global tplayed
    global twon

    def signupandlogin_database():
        global fname
        global lname
        global uname
        global pword
        global tplayed
        global twon

        fname = fname_e.get()
        lname = lname_e.get()
        uname = uname_e.get()
        pword = pword_e.get()


        conn = sqlite3.connect('people.db')
        c = conn.cursor()
        c.execute("SELECT * FROM mypeople WHERE user_name=? ",(uname,))
        double_username = c.fetchall()
        
        if double_username!=[]:
            uname_e.delete(0,END)
            uname = uname_e.get()
            double_username_label = Label(signup_frame,text="Select Another Username This Username Has Been Used",bg='red4',fg='white').pack()

        elif fname=='' or lname=='' or uname=='' or pword=='':
            information_missing_label = Label(signup_frame,text='Please enter all the information',bg='red4',fg='white').pack()
            fname = fname_e.get()
            lname = lname_e.get()
            uname = uname_e.get()
            pword = pword_e.get()
        
        else:
            c.execute("INSERT INTO mypeople VALUES(?,?,?,?,'0','0')",(fname, lname, uname, pword))
            conn.commit()
            signup_frame.pack_forget()
            information_manager_signup()

            

        '''
        c.execute("SELECT * FROM mypeople")
        print(c.fetchall())
        '''
        #conn.close()
        '''
        fname_e.delete(0,END)
        lname_e.delete(0,END)
        uname_e.delete(0,END)
        pword_e.delete(0,END)
        '''


    welcome_label.pack_forget()
    login_btn.pack_forget()
    signup_btn.pack_forget()

    
    #creating a frame for entries
    signup_frame = Frame(root,height=400,width=300,bg='red4')
    signup_frame.pack()

    register_label = Label(signup_frame,text="Please Enter Information Below!", bg='red4', fg='white', font="Helvetica 12 bold")
    register_label.pack(pady=(50,20))

    fname_text=StringVar()
    lname_text=StringVar()
    uname_text=StringVar()
    pword_text=StringVar()

    #labels and entries
    fname_label = Label(signup_frame,text="First Name*", bg='red4', fg='white', font="Helvetica 12")
    fname_label.pack()
    fname_e = Entry(signup_frame,textvariable=fname_text,borderwidth=2,width=40)
    fname_e.pack()
    

    lname_label = Label(signup_frame,text="Last Name*", bg='red4', fg='white', font="Helvetica 12")
    lname_label.pack()
    lname_e = Entry(signup_frame,textvariable=lname_text,borderwidth=2,width=40)
    lname_e.pack()
    

    uname_label = Label(signup_frame,text="User Name*", bg='red4', fg='white', font="Helvetica 12")
    uname_label.pack()
    uname_e = Entry(signup_frame,textvariable=uname_text,borderwidth=2,width=40)
    uname_e.pack()
    

    pword_label = Label(signup_frame,text="Pass Word*", bg='red4', fg='white', font="Helvetica 12")
    pword_label.pack()
    pword_e = Entry(signup_frame,textvariable=pword_text,borderwidth=2,width=40)
    pword_e.pack()
    
    
    #signup and login button
    signup_and_login_btn = Button(signup_frame,text="Sign up And Login", width=20, command=signupandlogin_database)
    signup_and_login_btn.pack(pady=30)




welcome_label = Label(root,text="Welcome To SOS Game", bg='red4', fg='white', font="Helvetica 12 bold", pady = 100)
welcome_label.pack()


login_btn = Button(root,text="Login", width=20,command=login)
login_btn.pack()

signup_btn= Button(root,text="Sign up", width=20, command=signup)
signup_btn.pack()







root.mainloop()