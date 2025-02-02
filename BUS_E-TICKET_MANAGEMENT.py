from tkinter import *
import tkinter as tk
import mysql.connector
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog
from sqlalchemy import create_engine
import pyqrcode
import qrcode
import io

def SIGNIN_N_SIGNUP_PAGE():
    # Connect to MySQL Database
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="password123",
      database="buseticket"
    )

    # Create Table to Store User Information
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE IF NOT EXISTS login_page (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255), email_id VARCHAR(255), mobile_no VARCHAR(255))")
    def change_password():
        def new_password():
            # get inputs from user
            email = email_entry1.get()
            current_password = entry_current_password.get()
            new_password = entry_new_password.get()

            # check if current password is correct
            mycursor.execute("SELECT password FROM login_page WHERE email_id = %s", (email,))
            result = mycursor.fetchone()
            if result is None:
                messagebox.showwarning(title="Change Password->Error", message="Invalid username.")
                return
            if result[0] != current_password:
                messagebox.showerror(title="Change Password->Error", message="Incorrect password.")
                return
            if(result[0]==entry_new_password.get()):
                messagebox.showwarning(title="Change Password->Error",
                                       message="Sorry,This Is your Old Password.Make Sure To Enter a New Password.")
            else:
                if (entry_confirm_password.get() == entry_new_password.get()):
                    # update password in database
                    mycursor.execute("UPDATE login_page SET password = %s WHERE email_id = %s", (new_password, email))
                    mydb.commit()

                    # display success message
                    messagebox.showinfo(title="Change Password", message="Password changed successfully")
                    root2.destroy()
                    SIGNIN_N_SIGNUP_PAGE()
                else:
                    messagebox.showwarning(title="Change Password->Error",
                                           message="Make Sure That Whether You Entered Same Password In The New Password and Confirm Password ? ")

        root2 = Tk()
        icon = ImageTk.PhotoImage(file='windowBusIcon.png')
        root2.wm_iconphoto(False, icon)
        root2.geometry("1470x745")
        root2.title("Login Page")
        canvas = Canvas(root2, width=800, height=800, bg="#b3ffff")

        canvas.pack(fill="both", expand=True)
        img = Image.open("login page.png")
        resize = img.resize((600, 500))
        new = ImageTk.PhotoImage(resize)
        canvas.create_image(400, 120, image=new, anchor='nw')
        welcome = Label(root2, text="Welcome to Bus E-Ticket Management", font=('Brush Script MT', 50, 'bold'),
                        bg="#b3ffff")
        welcome.place(x=250, y=10)
        login = Label(root2, text="Change Password", font=('Bodoni MT Black',24, 'bold'), fg="#0000ff", bg="#b3ffff")
        login.place(x=570, y=130)
        email_label1 = Label(root2, text="Email Address",font=('Arial', 13, 'bold'), bg="#b3ffff")
        email_entry1 = Entry(root2)
        label_current_password = Label(root2, text="Current password",font=('Arial', 13, 'bold'), bg="#b3ffff")
        entry_current_password = Entry(root2, show="*")
        label_new_password = Label(root2, text="New password",font=('Arial', 13, 'bold'), bg="#b3ffff")
        entry_new_password = Entry(root2, show="*")
        label_confirm_password = Label(root2, text="Confirm password", font=('Arial', 13, 'bold'), bg="#b3ffff")
        entry_confirm_password = Entry(root2, show="*")

        button_change_password = Button(root2, text="Change Password", command=new_password,font=('Arial', 12, 'bold'), bg="green")
        email_label1.place(x=570, y=210)
        email_entry1.place(x=690, y=210, width=180)
        label_current_password.place(x=520, y=255)
        entry_current_password.place(x=690, y=260, width=180)
        label_new_password.place(x=555, y=305)
        entry_new_password.place(x=690, y=310, width=180)
        label_confirm_password.place(x=535, y=360)
        entry_confirm_password.place(x=690, y=360, width=180)
        button_change_password.place(x=635, y=475, width=150)
        def login_page1():
            root2.destroy()
            SIGNIN_N_SIGNUP_PAGE()
        login_button = Button(root2, text="Login Page", font=('Arial', 12, 'bold'), bg='red',
                                command=login_page1)
        login_button.place(x=655, y=525, width=110)

        root2.mainloop()
    def signup():
        def signed_up():
            username =username_entry.get()
            password = password_entry.get()
            email = email_entry.get()
            mobile = mobile_entry.get()
            if username == '' or password == '' or email == '' or mobile == '':
                messagebox.showwarning(title="Signup Page->Error", message="Please enter valid information.")
                return
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM login_page WHERE email_id=%s", (email,))
            result = mycursor.fetchone()
            if result:
                messagebox.showerror(title="Signup Page->Error", message="Email Address already exists.")
                return
            mycursor.execute("INSERT INTO login_page (username, password, email_id, mobile_no) VALUES (%s, %s, %s, %s)",
                             (username, password, email, mobile))
            mydb.commit()
            messagebox.showinfo(title="Signup Page", message="User created successfully.")
            root1.destroy()
            SIGNIN_N_SIGNUP_PAGE()


        root1 = Tk()
        icon = ImageTk.PhotoImage(file='windowBusIcon.png')
        root1.wm_iconphoto(False, icon)
        root1.geometry("1470x745")
        root1.title("SignUp Page")
        canvas1= Canvas(root1, width=800, height=800, bg="#b3ffff")
        canvas1.pack(fill="both", expand=True)
        img1 = Image.open("login page.png")
        resize1 = img1.resize((600, 500))
        new1 = ImageTk.PhotoImage(resize1)
        canvas1.create_image(400, 120, image=new1, anchor='nw')
        welcome = Label(root1, text="Welcome to Bus E-Ticket Management", font=('Brush Script MT', 50, 'bold'),
                        bg="#b3ffff")
        welcome.place(x=250, y=10)
        signup = Label(root1, text="Signup Info", font=('Bodoni MT Black', 30, 'bold'), fg="#0000ff", bg="#b3ffff")
        signup.place(x=600, y=130)
        username_label = Label(root1, text="Name", font=('Arial', 15, 'bold'), bg="#b3ffff")
        username_label.place(x=570, y=210)
        username_entry = Entry(root1)
        username_entry.place(x=690, y=220, width=180)
        mobile_label = Label(root1, text="Mobile Number", font=('Arial', 15, 'bold'), bg="#b3ffff")
        mobile_label.place(x=550, y=350)
        mobile_entry = Entry(root1)
        mobile_entry.place(x=699, y=355, width=180)
        password_label = Label(root1, text="Password", font=('Arial', 15, 'bold'), bg="#b3ffff")
        password_label.place(x=570, y=305)
        password_entry = Entry(root1, show="*")
        password_entry.place(x=690, y=310, width=180)
        email_label = Label(root1, text="Email Address", font=('Arial', 15, 'bold'), bg="#b3ffff")
        email_label.place(x=550, y=255)
        email_entry = Entry(root1, width=60)
        email_entry.place(x=690, y=260, width=180)
        registerbutton = Button(root1, text="Register Now", font=('Arial', 12, 'bold'), bg='green',
                                command=signed_up)
        registerbutton.place(x=655, y=475, width=110)
        def login_page1():
            root1.destroy()
            SIGNIN_N_SIGNUP_PAGE()
        login_button = Button(root1, text="Login Page", font=('Arial', 12, 'bold'), bg='red',
                                command=login_page1)
        login_button.place(x=655, y=525, width=110)
        root1.mainloop()
    # Sign In Function
    def sign_in():
        emailid = email_entry.get()
        password = password_entry.get()
        if emailid == '' or password == '':
            messagebox.showwarning(title="SignIn Page->Error", message="Please enter valid information.")
            return
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM login_page WHERE email_id = %s AND password = %s", (emailid, password))
        result = mycursor.fetchone()
        if result:
            messagebox.showinfo(title="SignIn Page->Successfully Logged In", message="\tHello "+result[1]+" !\nWelcome to BUS-E-Ticket Management")
            root.destroy()

            def HOME_BUTTON_PAGE():
                def home():
                    messagebox.showinfo(title="HOME PAGE", message="Already,You Were In Home Page")

                def Bus_E_Ticket():
                    def create_Bet():
                        # newwn.destroy()
                        def CREATE_BET_PAGE():
                            def ticket_type():
                                if (click1.get() == "Travel As You Please Tickets"):
                                    a1.destroy()
                                    b1 = Tk()
                                    b1.geometry("1490x745")
                                    b1.title("Getting Detail from User")
                                    icon = ImageTk.PhotoImage(file='windowBusIcon.png')
                                    b1.wm_iconphoto(False, icon)
                                    cana = Canvas(b1, width=800, height=800)
                                    cana.pack(fill="both", expand=True)
                                    img2 = Image.open("bgforwindow6.png")
                                    resize3 = img2.resize((1490, 745))
                                    new2 = ImageTk.PhotoImage(resize3)
                                    cana.create_image(0, 0, image=new2, anchor='nw')
                                    rules_photo = PhotoImage(file='TAYPT.png')
                                    criteria_label = Label(b1, text="Criteria & Rules To Apply TAYPT",
                                                           font=('times', 25, 'bold'))
                                    criteria_label.place(x=450, y=50)
                                    rules_label = Label(b1, fg='#00FF00', bg='white', relief=RAISED, bd=10, padx=0,
                                                        pady=0,
                                                        image=rules_photo, compound='top')
                                    rules_label.place(x=25, y=100)
                                    Next_button = Button(b1, text='Next', bg="green", font=('times', 14, 'bold'),
                                                         command=lambda: nextpage())
                                    Next_button.place(x=650, y=600)

                                    def nextpage():
                                        rules_label.destroy()
                                        criteria_label.destroy()
                                        Next_button.destroy()
                                        # details info
                                        name = StringVar()
                                        NAME = name.get()
                                        address1 = StringVar()
                                        ADDRESS = address1.get()
                                        age1 = StringVar()
                                        AGE = age1.get()
                                        pincode1 = StringVar()
                                        PINCODE = pincode1.get()
                                        dob1 = StringVar()
                                        DOB = dob1.get()
                                        aadhar1 = StringVar()
                                        AADHARNO = aadhar1.get()
                                        BETID = StringVar()
                                        BETid = BETID.get()
                                        district = StringVar()
                                        DISTRICT = district.get()
                                        state = StringVar()
                                        STATE = state.get()
                                        valid_date = StringVar()
                                        VALID_DATE = valid_date.get()
                                        expire_date = StringVar()
                                        EXPIRE_DATE = expire_date.get()
                                        mobile1 = StringVar()
                                        MOBILE = mobile1.get()
                                        font = Label(b1, text="Create your Bus E-Ticket", font=('Arial', 30, 'bold'),
                                                     bg="#b3ffff")
                                        font.place(x=200, y=25)
                                        BETid_label = Label(b1, text="BET id", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        BETid_label.place(x=50, y=100)
                                        BETid_entry = Entry(b1, textvariable=BETid, width=35)
                                        BETid_entry.place(x=175, y=100, width=100)
                                        name = Label(b1, text="Name", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        name.place(x=50, y=150)
                                        name_entry = Entry(b1, textvariable=NAME, width=35)
                                        name_entry.place(x=175, y=150, width=100)
                                        Address = Label(b1, text="Address", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        Address.place(x=50, y=200)
                                        Address_entry = Entry(b1, textvariable=ADDRESS, width=35)
                                        Address_entry.place(x=175, y=200, width=100)
                                        pincode = Label(b1, text="Pincode", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        pincode.place(x=50, y=250)
                                        pincode_entry = Entry(b1, textvariable=PINCODE, width=35)
                                        pincode_entry.place(x=175, y=250, width=100)
                                        district_label = Label(b1, text="District", font=('Arial', 15, 'bold'),
                                                               bg="#ffff4d")
                                        district_label.place(x=50, y=300)
                                        district_entry = Entry(b1, textvariable=DISTRICT, width=35)
                                        district_entry.place(x=175, y=300, width=100)
                                        state = Label(b1, text="State", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        state.place(x=50, y=350)
                                        state_entry = Entry(b1, textvariable=STATE, width=35)
                                        state_entry.place(x=175, y=350, width=100)
                                        aadhar = Label(b1, text="Aadhar No", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        aadhar.place(x=50, y=400)
                                        aadhar_entry = Entry(b1, textvariable=AADHARNO, width=35)
                                        aadhar_entry.place(x=175, y=400, width=100)
                                        valid_date_label = Label(b1, text="Valid From", font=('Arial', 15, 'bold'),
                                                                 bg="#ffff4d")
                                        valid_date_label.place(x=700, y=100)
                                        valid_date_entry = Entry(b1, textvariable=VALID_DATE, width=35)
                                        valid_date_entry.place(x=850, y=100, width=100)
                                        expire_date_label = Label(b1, text="Expire Till", font=('Arial', 15, 'bold'),
                                                                  bg="#ffff4d")
                                        expire_date_label.place(x=700, y=150)
                                        expire_date_entry = Entry(b1, textvariable=EXPIRE_DATE, width=35)
                                        expire_date_entry.place(x=850, y=150, width=100)
                                        mobileno = Label(b1, text="Mobile No", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        mobileno.place(x=700, y=200)
                                        mobileno_entry = Entry(b1, textvariable=MOBILE, width=35)
                                        mobileno_entry.place(x=850, y=200, width=100)
                                        gender_label = Label(b1, text="Gender", font=('Arial', 15, 'bold'),
                                                             bg="#ffff4d")
                                        gender_label.place(x=700, y=250)
                                        gender_options = ["Male", "Female", "Transgender"]
                                        gender = StringVar()
                                        gender.set("Select")
                                        gender1 = OptionMenu(b1, gender, *gender_options)
                                        gender1.place(x=850, y=250)
                                        dob_label = Label(b1, text="Date of Birth", font=('Arial', 15, 'bold'),
                                                          bg="#ffff4d")
                                        dob_label.place(x=700, y=300)
                                        dob_entry = Entry(b1, textvariable=DOB, width=35)
                                        dob_entry.place(x=850, y=300, width=100)
                                        upload_aadhar_button = Button(b1, text='Upload Aadhar Card',
                                                                      font=('times', 14, 'bold'),
                                                                      command=lambda: upload_aadhar_card())
                                        upload_aadhar_button.place(x=900, y=350)

                                        def switchButtonState2():
                                            if (upload_photo_button['state'] == DISABLED):
                                                upload_photo_button['state'] = NORMAL

                                        global filename1

                                        def upload_aadhar_card():
                                            global filename1
                                            global filename1, img1
                                            f_types = [('Png files', '*.png'), ('Jpg Files', '*.jpg')]
                                            filename1 = filedialog.askopenfilename(filetypes=f_types)
                                            img1 = ImageTk.PhotoImage(file=filename1)
                                            messagebox.showinfo(title="Details Info",
                                                                message="Successfully uploaded your Aadhar Card")
                                            switchButtonState2()

                                        global filename1, img1
                                        debo_label = Label(b1, text="Depot", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        debo_label.place(x=50, y=450)
                                        debo_options = ["Adyar", "Ambathur Industrial Estate", " Ambathur OT",
                                                        " Anna Nagar (West)", "Avadi", "Ayanavaram", "Broadway",
                                                        "C.M.B.T", "Central Rly station", "Guindy Industrial Estate",
                                                        "Iyyappanthangal", "K.K.Nagar", "M.K.B.Nagar", "Mandaveli",
                                                        "Pallavaram", "Perambur", "Poonamallee", "Redhills", "Saidapet",
                                                        "Sriperumbathur", "T.Nagar", "Tambaram (West)", "Thiruvanmiyur",
                                                        "Thiruvotriyur", "Tondiarpet", "Vadapalani", " Vallalar Nagar",
                                                        "Velachery", "Villivakkam"]
                                        debo = StringVar()
                                        debo.set("Select")
                                        debo1 = OptionMenu(b1, debo, *debo_options)
                                        debo1.place(x=175, y=450)
                                        ticket_label = Label(b1, text="Ticket Type", font=('Arial', 15, 'bold'),
                                                             bg="#ffff4d")
                                        ticket_label.place(x=50, y=500)
                                        Ticket_options = ["TAYPT"]
                                        ticket = StringVar()
                                        ticket.set("Select")
                                        Ticket1 = OptionMenu(b1, ticket, *Ticket_options)
                                        Ticket1.place(x=175, y=500)
                                        age = Label(b1, text="Age", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        age.place(x=50, y=550)
                                        age_entry = Entry(b1, textvariable=AGE, width=35)
                                        age_entry.place(x=175, y=550, width=100)
                                        upload_photo_button = Button(b1, text='Upload photo',
                                                                     font=('times', 14, 'bold'),
                                                                     command=lambda: upload_file(), state=DISABLED)
                                        upload_photo_button.place(x=400, y=125)
                                        upload_data_button = Button(b1, text='Upload data', font=('times', 16, 'bold'),
                                                                    bg="#00ffbf", command=lambda: add_data(),
                                                                    state=DISABLED)
                                        upload_data_button.place(x=75, y=625)

                                        def my_command():
                                            b1.destroy()
                                            HOME_BUTTON_PAGE()

                                        click_btn = PhotoImage(file='Small_Home_ Icon.png')
                                        button = Button(b1, image=click_btn, command=my_command)
                                        button.place(x=30, y=25)

                                        def my_command1():
                                            b1.destroy()
                                            CREATE_BET_PAGE()

                                        click_btn1 = PhotoImage(file='small_back_icon.png')
                                        button1 = Button(b1, image=click_btn1, command=my_command1)
                                        button1.place(x=95, y=25)

                                        def switchButtonState1():
                                            if (upload_data_button['state'] == DISABLED):
                                                upload_data_button['state'] = NORMAL

                                        global filename

                                        def upload_file():
                                            if (
                                                    BETid_entry.get() == "" or name_entry.get() == "" or gender.get() == "Select" or dob_entry.get() == "" or Address_entry.get() == "" or pincode_entry.get() == "" or district_entry.get() == "" or state_entry.get() == "" or aadhar_entry.get() == "" or debo.get() == "Select" or ticket.get() == "Select" or valid_date_entry.get() == "" or expire_date_entry.get() == "" or age_entry.get() == "" or mobileno_entry.get() == ""):
                                                messagebox.showerror(title="Getting user Details->Error",
                                                                     message="Please Make Sure To Enter All details")
                                            else:
                                                global filename
                                                global filename, img
                                                f_types = [('Png files', '*.png'), ('Jpg Files', '*.jpg')]
                                                filename = filedialog.askopenfilename(filetypes=f_types)
                                                img = ImageTk.PhotoImage(file=filename)
                                                b_1 = Button(b1, image=img)  # using Button
                                                b_1.place(x=400, y=175)  # display uploaded photo
                                                switchButtonState1()

                                        def switchButtonState12():
                                            if (mybutton2['state'] == DISABLED):
                                                mybutton2['state'] = NORMAL

                                        global filename, img

                                        def create_code():
                                            input_path = filedialog.asksaveasfilename(title="save image", filetypes=(
                                                ("PNG File", ".png"), ("All Files", "*.*")))
                                            switchButtonState12()
                                            if input_path:
                                                if input_path.endswith(".png"):
                                                    get_code = pyqrcode.create(
                                                        "BET ID:" + BETid_entry.get() + "\n" + "NAME:" + name_entry.get() + "\n" + "GENDER:" + gender.get() + "\n" + "DATE OF BIRTH:" + dob_entry.get() + "\n" + "AGE:" + age_entry.get() + "\n" + "RESIDENTIAL ADDRESS:" + Address_entry.get() + "\n" + "PINCODE:" + pincode_entry.get() + "\n" + "DISTRICT:" + district_entry.get() + "\n" + "STATE:" + state_entry.get() + "\n" + "AADHHAR NO:" + aadhar_entry.get() + "\n" + "DEPOT:" + debo.get() + "\n" + "BUS E-TICKET TYPE:" + ticket.get() + "\n" + "VALID FROM:" + valid_date_entry.get() + "\n" + "EXPIRE TILL:" + expire_date_entry.get() + "\n" + "MOBILE NO:" + mobileno_entry.get() + "\n")
                                                    # get_code.png(input_path, scale=5)
                                                    get_code.png(input_path, scale=5)
                                                    with Image.open(input_path) as img:
                                                        img_resized = img.resize((200, 200))
                                                        img_resized.save(input_path)

                                                    messagebox.showinfo(title="Generate QR-code",
                                                                        message=f"Successfully Generated QR-Code For Details \n QR code saved to {input_path}")

                                                else:
                                                    input_path = f'{input_path}.png'
                                                    get_code = pyqrcode.create(
                                                        "BET ID:" + BETid_entry.get() + "\n" + "NAME:" + name_entry.get() + "\n" + "GENDER:" + gender.get() + "\n" + "DATE OF BIRTH:" + dob_entry.get() + "\n" + "AGE:" + age_entry.get() + "\n" + "RESIDENTIAL ADDRESS:" + Address_entry.get() + "\n" + "PINCODE:" + pincode_entry.get() + "\n" + "DISTRICT:" + district_entry.get() + "\n" + "STATE:" + state_entry.get() + "\n" + "AADHHAR NO:" + aadhar_entry.get() + "\n" + "DEPOT:" + debo.get() + "\n" + "BUS E-TICKET TYPE:" + ticket.get() + "\n" + "VALID FROM:" + valid_date_entry.get() + "\n" + "EXPIRE TILL:" + expire_date_entry.get() + "\n" + "MOBILE NO:" + mobileno_entry.get() + "\n")
                                                    get_code.png(input_path, scale=5)
                                                    with Image.open(input_path) as img:
                                                        img_resized = img.resize((200, 200))
                                                        img_resized.save(input_path)

                                                    messagebox.showinfo(title="Generate QR-code",
                                                                        message=f"Successfully Generated QR-Code For Details \n QR code saved to {input_path}")

                                        def create_code1():
                                            data = BETid_entry.get()

                                            # Create QR code object
                                            qr = qrcode.QRCode(
                                                version=None,
                                                error_correction=qrcode.constants.ERROR_CORRECT_L,
                                                box_size=10,
                                                border=4,
                                            )
                                            qr.add_data(data)
                                            qr.make(fit=True)

                                            # Create QR code image with fill color and background color
                                            qr_image = qr.make_image(fill_color="yellow", back_color="blue")

                                            # Load logo image
                                            logo_image = Image.open("windowBusIcon.png")

                                            # Resize logo image to fit inside QR code
                                            logo_size = (qr_image.size[0] // 7, qr_image.size[1] // 7)

                                            # logo_size = (qr_image.size[0] // 4, qr_image.size[1] // 4)
                                            logo_image = logo_image.resize(logo_size)

                                            # Calculate position to place logo image inside QR code
                                            logo_pos = (
                                                (qr_image.size[0] - logo_size[0]) // 2,
                                                (qr_image.size[1] - logo_size[1]) // 2)

                                            # Paste logo image onto QR code image
                                            qr_image.paste(logo_image)

                                            # Resize QR code image to 100x100 pixels
                                            qr_image = qr_image.resize((175, 175))

                                            # Get file path from user using file dialog
                                            file_path = filedialog.asksaveasfilename(title="Save QR Code",
                                                                                     filetypes=(
                                                                                     ("PNG Files", "*.png"),))

                                            # Save QR code image to file
                                            if file_path:
                                                if file_path.endswith(".png"):
                                                    qr_image.save(file_path, "PNG")
                                                    messagebox.showinfo(title="QR Code Saved",
                                                                        message=f"Successfully Generated QR-Code For BET ID \n QR code saved to {file_path}")
                                                else:
                                                    file_path = f'{file_path}.png'
                                                    qr_image.save(file_path, "PNG")
                                                    messagebox.showinfo(title="QR Code Saved",
                                                                        message=f"Successfully Generated QR-Code For BET ID \n QR code saved to {file_path}")

                                        mybutton = Button(b1, text="Generate QR-Code For Details",
                                                          font=('times', 11, 'bold'), bg="#00ff00", state=DISABLED,
                                                          command=create_code)
                                        mybutton.place(x=250, y=625)
                                        mybutton2 = Button(b1, text="Generate QR-Code for BET ID ",
                                                           font=('times', 11, 'bold'),
                                                           bg="#00ff00",
                                                           state=DISABLED, command=create_code1)
                                        mybutton2.place(x=500, y=625)

                                        def switchButtonState():
                                            if (mybutton['state'] == DISABLED):
                                                mybutton['state'] = NORMAL

                                        def add_data():  # Add data to MySQL table
                                            # upload_aadhar_card()
                                            global img, filename
                                            global img1, filename1
                                            with open("mytextfile.txt", "a") as f:
                                                f.write(BETid_entry.get() + "\n")
                                            fob = open(filename, 'rb')  # filename from upload_file()
                                            fob = fob.read()
                                            fob1 = open(filename1, 'rb')
                                            fob1 = fob1.read()
                                            data = (BETid_entry.get(), name_entry.get(), Address_entry.get(),
                                                    pincode_entry.get(), district_entry.get(), state_entry.get(),
                                                    aadhar_entry.get(),
                                                    debo.get(), ticket.get(), valid_date_entry.get(),
                                                    expire_date_entry.get(), mobileno_entry.get(), fob, age_entry.get(),
                                                    fob1, gender.get(), dob_entry.get())
                                            try:
                                                my_conn = create_engine(
                                                    "mysql+mysqldb://root:password123@localhost/buseticket")
                                                my_conn.execute("INSERT INTO person_details(bet_id,name,address,pincode,district,state,aadhar_no,depot,ticket_type,valid_from,expire_till,mobile_no,profile_pic,age,aadhar_card_pic,gender,date_of_birth) \
                                                                                                                                                  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                                                data)
                                                switchButtonState()
                                            except:
                                                messagebox.showerror(title="Getting user Details->Error",
                                                                     message="01.Make Sure To Enter All details \n 02.Make sure that You have Entered correct details\n like BET ID,AADHAR NUMBER,MOBILE NUMBER etc")

                                        b1.mainloop()

                                    b1.mainloop()
                                elif (click1.get() == "Pay & Get"):
                                    a1.destroy()
                                    b2 = Tk()
                                    b2.geometry("1490x745")
                                    b2.title("Getting Detail from User")
                                    icon = ImageTk.PhotoImage(file='windowBusIcon.png')
                                    b2.wm_iconphoto(False, icon)
                                    cana = Canvas(b2, width=800, height=800)
                                    cana.pack(fill="both", expand=True)
                                    img2 = Image.open("bgforwindow6.png")
                                    resize3 = img2.resize((1490, 745))
                                    new2 = ImageTk.PhotoImage(resize3)
                                    cana.create_image(0, 0, image=new2, anchor='nw')

                                    # details info
                                    name = StringVar()
                                    NAME = name.get()
                                    address1 = StringVar()
                                    ADDRESS = address1.get()
                                    pincode1 = StringVar()
                                    PINCODE = pincode1.get()
                                    dob1 = StringVar()
                                    DOB = dob1.get()
                                    aadhar1 = StringVar()
                                    AADHARNO = aadhar1.get()
                                    BETID = StringVar()
                                    BETid = BETID.get()
                                    district = StringVar()
                                    DISTRICT = district.get()
                                    state = StringVar()
                                    STATE = state.get()
                                    mobile1 = StringVar()
                                    MOBILE = mobile1.get()
                                    price11 = StringVar()
                                    PRICE = price11.get()
                                    age1 = StringVar()
                                    AGE = age1.get()

                                    def my_command():
                                        b2.destroy()
                                        HOME_BUTTON_PAGE()

                                    click_btn = PhotoImage(file='Small_Home_ Icon.png')
                                    button = Button(b2, image=click_btn, command=my_command)
                                    button.place(x=30, y=25)

                                    def my_command1():
                                        b2.destroy()
                                        CREATE_BET_PAGE()

                                    click_btn1 = PhotoImage(file='small_back_icon.png')
                                    button1 = Button(b2, image=click_btn1, command=my_command1)
                                    button1.place(x=95, y=25)
                                    age = Label(b2, text="Age", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                    age.place(x=50, y=550)
                                    age_entry = Entry(b2, textvariable=AGE, width=35)
                                    age_entry.place(x=175, y=550, width=100)
                                    font = Label(b2, text="Create your Bus E-Ticket", font=('Arial', 30, 'bold'),
                                                 bg="#b3ffff")
                                    font.place(x=200, y=25)
                                    BETid_label = Label(b2, text="BET id", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                    BETid_label.place(x=50, y=100)
                                    BETid_entry = Entry(b2, textvariable=BETid, width=35)
                                    BETid_entry.place(x=175, y=100, width=100)
                                    name = Label(b2, text="Name", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                    name.place(x=50, y=150)
                                    name_entry = Entry(b2, textvariable=NAME, width=35)
                                    name_entry.place(x=175, y=150, width=100)
                                    Address = Label(b2, text="Address", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                    Address.place(x=50, y=200)
                                    Address_entry = Entry(b2, textvariable=ADDRESS, width=35)
                                    Address_entry.place(x=175, y=200, width=100)
                                    pincode = Label(b2, text="Pincode", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                    pincode.place(x=50, y=250)
                                    pincode_entry = Entry(b2, textvariable=PINCODE, width=35)
                                    pincode_entry.place(x=175, y=250, width=100)
                                    district_label = Label(b2, text="District", font=('Arial', 15, 'bold'),
                                                           bg="#ffff4d")
                                    district_label.place(x=50, y=300)
                                    district_entry = Entry(b2, textvariable=DISTRICT, width=35)
                                    district_entry.place(x=175, y=300, width=100)
                                    state = Label(b2, text="State", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                    state.place(x=50, y=350)
                                    state_entry = Entry(b2, textvariable=STATE, width=35)
                                    state_entry.place(x=175, y=350, width=100)
                                    aadhar = Label(b2, text="Aadhar No", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                    aadhar.place(x=50, y=400)
                                    aadhar_entry = Entry(b2, textvariable=AADHARNO, width=35)
                                    aadhar_entry.place(x=175, y=400, width=100)

                                    price_label = Label(b2, text="Price Amount", font=('Arial', 15, 'bold'),
                                                        bg="#ffff4d")
                                    price_label.place(x=700, y=200)
                                    price1 = Entry(b2, textvariable=PRICE, width=35)
                                    price1.place(x=850, y=200)
                                    mobileno = Label(b2, text="Mobile No", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                    mobileno.place(x=700, y=250)
                                    mobileno_entry = Entry(b2, textvariable=MOBILE, width=35)
                                    mobileno_entry.place(x=850, y=250, width=100)
                                    debo_label = Label(b2, text="Depot", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                    debo_label.place(x=50, y=450)
                                    gender_label = Label(b2, text="Gender", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                    gender_label.place(x=700, y=300)
                                    gender_options = ["Male", "Female", "Transgender"]
                                    gender = StringVar()
                                    gender.set("Select")
                                    gender1 = OptionMenu(b2, gender, *gender_options)
                                    gender1.place(x=850, y=300)
                                    dob_label = Label(b2, text="Date of Birth", font=('Arial', 15, 'bold'),
                                                      bg="#ffff4d")
                                    dob_label.place(x=700, y=350)
                                    dob_entry = Entry(b2, textvariable=DOB, width=35)
                                    dob_entry.place(x=850, y=350, width=100)
                                    debo_options = ["Adyar", "Ambathur Industrial Estate", " Ambathur OT",
                                                    " Anna Nagar (West)", "Avadi", "Ayanavaram", "Broadway", "C.M.B.T",
                                                    "Central Rly station", "Guindy Industrial Estate",
                                                    "Iyyappanthangal", "K.K.Nagar", "M.K.B.Nagar", "Mandaveli",
                                                    "Pallavaram", "Perambur", "Poonamallee", "Redhills", "Saidapet",
                                                    "Sriperumbathur", "T.Nagar", "Tambaram (West)", "Thiruvanmiyur",
                                                    "Thiruvotriyur", "Tondiarpet", "Vadapalani", " Vallalar Nagar",
                                                    "Velachery", "Villivakkam"]
                                    debo = StringVar()
                                    debo.set("Select")
                                    debo1 = OptionMenu(b2, debo, *debo_options)
                                    debo1.place(x=175, y=450)
                                    ticket_label = Label(b2, text="Ticket Type", font=('Arial', 15, 'bold'),
                                                         bg="#ffff4d")
                                    ticket_label.place(x=50, y=500)
                                    Ticket_options = ["Pay and Get"]
                                    ticket = StringVar()
                                    ticket.set("Select")
                                    Ticket1 = OptionMenu(b2, ticket, *Ticket_options)
                                    Ticket1.place(x=175, y=500)
                                    upload_aadhar_button = Button(b2, text='Upload Aadhar Card',
                                                                  font=('times', 14, 'bold'),
                                                                  command=lambda: upload_aadhar_card())
                                    upload_aadhar_button.place(x=900, y=400)

                                    def switchButtonState12():
                                        if (mybutton2['state'] == DISABLED):
                                            mybutton2['state'] = NORMAL

                                    def switchButtonState2():
                                        if (upload_photo_button['state'] == DISABLED):
                                            upload_photo_button['state'] = NORMAL

                                    global filename1

                                    def upload_aadhar_card():
                                        global filename1
                                        global filename1, img1
                                        f_types = [('Png files', '*.png'), ('Jpg Files', '*.jpg')]
                                        filename1 = filedialog.askopenfilename(filetypes=f_types)
                                        img1 = ImageTk.PhotoImage(file=filename1)
                                        messagebox.showinfo(title="Details Info",
                                                            message="Successfully uploaded your Aadhar Card")
                                        switchButtonState2()

                                    global filename1, img1

                                    upload_photo_button = Button(b2, text='Upload photo', font=('times', 14, 'bold'),
                                                                 command=lambda: upload_file(), state=DISABLED)
                                    upload_photo_button.place(x=400, y=125)
                                    upload_data_button = Button(b2, text='Upload data', font=('times', 16, 'bold'),
                                                                bg="#00ffbf", command=lambda: add_data(),
                                                                state=DISABLED)
                                    upload_data_button.place(x=75, y=625)

                                    def switchButtonState1():
                                        if (upload_data_button['state'] == DISABLED):
                                            upload_data_button['state'] = NORMAL

                                    global filename

                                    def upload_file():
                                        if (
                                                BETid_entry.get() == "" or name_entry.get() == "" or dob_entry.get() == "" or gender.get() == "Select" or age_entry.get() == "" or Address_entry.get() == "" or pincode_entry.get() == "" or district_entry.get() == "" or state_entry.get() == "" or aadhar_entry.get() == "" or debo.get() == "Select" or ticket.get() == "Select" or price1.get() == "" or mobileno_entry.get() == ""):
                                            messagebox.showerror(title="Getting user Details->Error",
                                                                 message="Please Make Sure To Enter All details")
                                        else:
                                            global filename
                                            global filename, img
                                            f_types = [('Png files', '*.png'), ('Jpg Files', '*.jpg')]
                                            filename = filedialog.askopenfilename(filetypes=f_types)
                                            img = ImageTk.PhotoImage(file=filename)
                                            b_1 = Button(b2, image=img)  # using Button
                                            b_1.place(x=400, y=175)  # display uploaded photo
                                            switchButtonState1()

                                    def switchButtonState12():
                                        if (mybutton2['state'] == DISABLED):
                                            mybutton2['state'] = NORMAL

                                    global filename, img

                                    def create_code():
                                        input_path = filedialog.asksaveasfilename(title="save image", filetypes=(
                                            ("PNG File", ".png"), ("All Files", "*.*")))
                                        switchButtonState12()
                                        if input_path:
                                            if input_path.endswith(".png"):
                                                get_code = pyqrcode.create(
                                                    "BET ID:" + BETid_entry.get() + "\n" + "NAME:" + name_entry.get() + "\n" + "DATE OF BIRTH:" + dob_entry.get() + "\n" + "GENDER:" + gender.get() + "\n" + "AGE:" + age_entry.get() + "\n" + "RESIDENTIAL ADDRESS:" + Address_entry.get() + "\n" + "PINCODE:" + pincode_entry.get() + "\n" + "DISTRICT:" + district_entry.get() + "\n" + "STATE:" + state_entry.get() + "\n" + "AADHHAR NO:" + aadhar_entry.get() + "\n" + "DEPOT:" + debo.get() + "\n" + "BUS E-TICKET TYPE:" + ticket.get() + "\n" + "PRICE:" + price1.get() + "\n" + "MOBILE NO:" + mobileno_entry.get() + "\n")
                                                get_code.png(input_path, scale=5)
                                                with Image.open(input_path) as img:
                                                    img_resized = img.resize((150, 150))
                                                    img_resized.save(input_path)
                                                messagebox.showinfo(title="Generate QR-code",
                                                                    message=f"Successfully Generated QR-Code For Details \n QR code saved to {input_path}")

                                            else:
                                                input_path = f'{input_path}.png'
                                                get_code = pyqrcode.create(
                                                    "BET ID:" + BETid_entry.get() + "\n" + "NAME:" + name_entry.get() + "\n" + "DATE OF BIRTH:" + dob_entry.get() + "\n" + "GENDER:" + gender.get() + "\n" + "AGE:" + age_entry.get() + "\n" + "RESIDENTIAL ADDRESS:" + Address_entry.get() + "\n" + "PINCODE:" + pincode_entry.get() + "\n" + "DISTRICT:" + district_entry.get() + "\n" + "STATE:" + state_entry.get() + "\n" + "AADHHAR NO:" + aadhar_entry.get() + "\n" + "DEPOT:" + debo.get() + "\n" + "BUS E-TICKET TYPE:" + ticket.get() + "\n" + "PRICE:" + price1.get() + "\n" + "MOBILE NO:" + mobileno_entry.get() + "\n")

                                                get_code.png(input_path, scale=5)
                                                with Image.open(input_path) as img:
                                                    img_resized = img.resize((200, 200))
                                                    img_resized.save(input_path)
                                                messagebox.showinfo(title="Generate QR-code",
                                                                    message=f"Successfully Generated QR-Code For Details \n QR code saved to {input_path}")

                                    def create_code1():
                                        data = BETid_entry.get()

                                        # Create QR code object
                                        qr = qrcode.QRCode(
                                            version=None,
                                            error_correction=qrcode.constants.ERROR_CORRECT_L,
                                            box_size=10,
                                            border=4,
                                        )
                                        qr.add_data(data)
                                        qr.make(fit=True)

                                        # Create QR code image with fill color and background color
                                        qr_image = qr.make_image(fill_color="blue", back_color="pink")

                                        # Load logo image
                                        logo_image = Image.open("windowBusIcon.png")

                                        # Resize logo image to fit inside QR code
                                        logo_size = (qr_image.size[0] // 7, qr_image.size[1] // 7)

                                        # logo_size = (qr_image.size[0] // 4, qr_image.size[1] // 4)
                                        logo_image = logo_image.resize(logo_size)

                                        # Calculate position to place logo image inside QR code
                                        logo_pos = (
                                            (qr_image.size[0] - logo_size[0]) // 2,
                                            (qr_image.size[1] - logo_size[1]) // 2)

                                        # Paste logo image onto QR code image
                                        qr_image.paste(logo_image)

                                        # Resize QR code image to 100x100 pixels
                                        qr_image = qr_image.resize((175, 175))

                                        # Get file path from user using file dialog
                                        file_path = filedialog.asksaveasfilename(title="Save QR Code",
                                                                                 filetypes=(("PNG Files", "*.png"),))

                                        # Save QR code image to file
                                        if file_path:
                                            if file_path.endswith(".png"):
                                                qr_image.save(file_path, "PNG")
                                                messagebox.showinfo(title="QR Code Saved",
                                                                    message=f"Successfully Generated QR-Code For BET ID \n QR code saved to {file_path}")
                                            else:
                                                file_path = f'{file_path}.png'
                                                qr_image.save(file_path, "PNG")
                                                messagebox.showinfo(title="QR Code Saved",
                                                                    message=f"Successfully Generated QR-Code For BET ID \n QR code saved to {file_path}")

                                    mybutton = Button(b2, text="Generate QR-Code For Details",
                                                      font=('times', 11, 'bold'),
                                                      bg="#00ff00", state=DISABLED, command=create_code)
                                    mybutton.place(x=250, y=625)
                                    mybutton2 = Button(b2, text="Generate QR-Code for BET ID ",
                                                       font=('times', 11, 'bold'),
                                                       bg="#00ff00",
                                                       state=DISABLED, command=create_code1)
                                    mybutton2.place(x=500, y=625)

                                    def switchButtonState():
                                        if (mybutton['state'] == DISABLED):
                                            mybutton['state'] = NORMAL

                                    def add_data():  # Add data to MySQL table
                                        global img, filename
                                        fob = open(filename, 'rb')  # filename from upload_file()
                                        fob = fob.read()
                                        global img1, filename1
                                        with open("mytextfile.txt", "a") as f:
                                            f.write(BETid_entry.get() + "\n")
                                        fob1 = open(filename1, 'rb')  # filename from upload_file()
                                        fob1 = fob1.read()
                                        data = (
                                        BETid_entry.get(), name_entry.get(), Address_entry.get(), pincode_entry.get(),
                                        district_entry.get(),
                                        state_entry.get(), aadhar_entry.get(),
                                        debo.get(), ticket.get(),
                                        price1.get(),
                                        mobileno_entry.get(), fob, age_entry, fob1, gender.get(), dob_entry.get())
                                        try:
                                            my_conn = create_engine(
                                                "mysql+mysqldb://root:password123@localhost/buseticket")
                                            my_conn.execute("INSERT INTO person_details(bet_id,name,address,pincode,district,state,aadhar_no,depot,ticket_type,price_amount,mobile_no,profile_pic,Age,Aadhar_card_pic,gender,date_of_birth) \
                                                                                                                   VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                                            data)
                                            switchButtonState()
                                        except:
                                            messagebox.showerror(title="Getting user Details->Error",
                                                                 message="01.Make Sure To Enter All details \n 02.Make sure that You have Entered correct details\n like BET ID,AADHAR NUMBER,MOBILE NUMBER etc")

                                    b2.mainloop()
                                elif (click1.get() == "Monthly Commuter Season Ticket"):
                                    a1.destroy()
                                    b3 = Tk()
                                    b3.geometry("1490x745")
                                    b3.title("Getting Detail from User")
                                    icon = ImageTk.PhotoImage(file='windowBusIcon.png')
                                    b3.wm_iconphoto(False, icon)
                                    cana = Canvas(b3, width=800, height=800)
                                    cana.pack(fill="both", expand=True)
                                    img2 = Image.open("bgforwindow6.png")
                                    resize3 = img2.resize((1490, 745))
                                    new2 = ImageTk.PhotoImage(resize3)
                                    cana.create_image(0, 0, image=new2, anchor='nw')
                                    rules_photo = PhotoImage(file='MST.png')
                                    criteria_label = Label(b3, text="Adult Wise Price List", font=('times', 25, 'bold'))
                                    criteria_label.place(x=550, y=50)
                                    rules_label = Label(b3, fg='#00FF00', bg='white', relief=RAISED, bd=10, padx=0,
                                                        pady=0,
                                                        image=rules_photo, compound='top')
                                    rules_label.place(x=80, y=100)
                                    Next_button = Button(b3, text='Next', bg="green", font=('times', 14, 'bold'),
                                                         command=lambda: next1())
                                    Next_button.place(x=650, y=600)

                                    def next1():
                                        rules_label.destroy()
                                        criteria_label.destroy()
                                        Next_button.destroy()

                                        def nextpage():
                                            rules_label1.destroy()
                                            criteria_label1.destroy()
                                            Next_button1.destroy()

                                            # details info

                                            name = StringVar()
                                            NAME = name.get()
                                            address1 = StringVar()
                                            ADDRESS = address1.get()
                                            pincode1 = StringVar()
                                            PINCODE = pincode1.get()
                                            aadhar1 = StringVar()
                                            AADHARNO = aadhar1.get()
                                            BETID = StringVar()
                                            BETid = BETID.get()
                                            district = StringVar()
                                            DISTRICT = district.get()
                                            state = StringVar()
                                            STATE = state.get()
                                            valid_date = StringVar()
                                            VALID_DATE = valid_date.get()
                                            expire_date = StringVar()
                                            EXPIRE_DATE = expire_date.get()
                                            mobile1 = StringVar()
                                            MOBILE = mobile1.get()
                                            dob = StringVar()
                                            DOB = dob.get()

                                            form_123 = StringVar()
                                            FORM12 = form_123.get()
                                            to_123 = StringVar()
                                            TO12 = to_123.get()
                                            form_1223 = StringVar()
                                            FORM122 = form_1223.get()
                                            to_1223 = StringVar()
                                            TO122 = to_1223.get()

                                            def my_command():
                                                b3.destroy()
                                                HOME_BUTTON_PAGE()

                                            click_btn = PhotoImage(file='Small_Home_ Icon.png')
                                            button = Button(b3, image=click_btn, command=my_command)
                                            button.place(x=30, y=25)

                                            def my_command1():
                                                b3.destroy()
                                                CREATE_BET_PAGE()

                                            click_btn1 = PhotoImage(file='small_back_icon.png')
                                            button1 = Button(b3, image=click_btn1, command=my_command1)
                                            button1.place(x=95, y=25)
                                            font = Label(b3, text="Create your Bus E-Ticket",
                                                         font=('Arial', 30, 'bold'), bg="#b3ffff")
                                            font.place(x=200, y=25)
                                            BETid_label = Label(b3, text="BET id", font=('Arial', 15, 'bold'),
                                                                bg="#ffff4d")
                                            BETid_label.place(x=50, y=100)
                                            BETid_entry = Entry(b3, textvariable=BETid, width=35)
                                            BETid_entry.place(x=175, y=100, width=100)
                                            name = Label(b3, text="Name", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                            name.place(x=50, y=150)
                                            name_entry = Entry(b3, textvariable=NAME, width=35)
                                            name_entry.place(x=175, y=150, width=100)
                                            Address = Label(b3, text="Address", font=('Arial', 15, 'bold'),
                                                            bg="#ffff4d")
                                            Address.place(x=50, y=200)
                                            Address_entry = Entry(b3, textvariable=ADDRESS, width=35)
                                            Address_entry.place(x=175, y=200, width=100)
                                            pincode = Label(b3, text="Pincode", font=('Arial', 15, 'bold'),
                                                            bg="#ffff4d")
                                            pincode.place(x=50, y=250)
                                            pincode_entry = Entry(b3, textvariable=PINCODE, width=35)
                                            pincode_entry.place(x=175, y=250, width=100)
                                            district_label = Label(b3, text="District", font=('Arial', 15, 'bold'),
                                                                   bg="#ffff4d")
                                            district_label.place(x=50, y=300)
                                            district_entry = Entry(b3, textvariable=DISTRICT, width=35)
                                            district_entry.place(x=175, y=300, width=100)
                                            state = Label(b3, text="State", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                            state.place(x=50, y=350)
                                            state_entry = Entry(b3, textvariable=STATE, width=35)
                                            state_entry.place(x=175, y=350, width=100)
                                            aadhar = Label(b3, text="Aadhar No", font=('Arial', 15, 'bold'),
                                                           bg="#ffff4d")
                                            aadhar.place(x=50, y=400)
                                            aadhar_entry = Entry(b3, textvariable=AADHARNO, width=35)
                                            aadhar_entry.place(x=175, y=400, width=100)
                                            valid_date_label = Label(b3, text="Valid From", font=('Arial', 15, 'bold'),
                                                                     bg="#ffff4d")
                                            valid_date_label.place(x=700, y=100)
                                            valid_date_entry = Entry(b3, textvariable=VALID_DATE, width=35)
                                            valid_date_entry.place(x=850, y=100, width=100)
                                            expire_date_label = Label(b3, text="Expire Till",
                                                                      font=('Arial', 15, 'bold'), bg="#ffff4d")
                                            expire_date_label.place(x=700, y=150)
                                            expire_date_entry = Entry(b3, textvariable=EXPIRE_DATE, width=35)
                                            expire_date_entry.place(x=850, y=150, width=100)
                                            mobileno = Label(b3, text="Mobile No", font=('Arial', 15, 'bold'),
                                                             bg="#ffff4d")
                                            mobileno.place(x=700, y=250)
                                            mobileno_entry = Entry(b3, textvariable=MOBILE, width=35)
                                            mobileno_entry.place(x=850, y=250, width=100)
                                            part1 = Label(b3, text="Part-I", font=('Arial', 12, 'bold'), bg="#cc0099")
                                            part1.place(x=700, y=350)
                                            from1_label = Label(b3, text="From-I", font=('Arial', 15, 'bold'),
                                                                bg="#ffff4d")
                                            from1_label.place(x=700, y=400)
                                            from12 = Entry(b3, textvariable=FORM12, width=35)
                                            from12.place(x=850, y=400)
                                            to1_label = Label(b3, text="To-I", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                            to1_label.place(x=700, y=450)
                                            to12 = Entry(b3, textvariable=TO12, width=35)
                                            to12.place(x=850, y=450)
                                            part2 = Label(b3, text="Part-II", font=('Arial', 12, 'bold'), bg="#cc0099")
                                            part2.place(x=700, y=500)
                                            from2_label = Label(b3, text="From-II", font=('Arial', 15, 'bold'),
                                                                bg="#ffff4d")
                                            from2_label.place(x=700, y=550)
                                            from22 = Entry(b3, textvariable=FORM122, width=35)
                                            from22.place(x=850, y=550)
                                            to2_label = Label(b3, text="To-II", font=('Arial', 15, 'bold'),
                                                              bg="#ffff4d")
                                            to2_label.place(x=700, y=600)
                                            to22 = Entry(b3, textvariable=TO122, width=35)
                                            to22.place(x=850, y=600)
                                            debo_label = Label(b3, text="Depot", font=('Arial', 15, 'bold'),
                                                               bg="#ffff4d")
                                            debo_label.place(x=50, y=450)
                                            debo_options = ["Adyar", "Ambathur Industrial Estate", " Ambathur OT",
                                                            " Anna Nagar (West)", "Avadi", "Ayanavaram", "Broadway",
                                                            "C.M.B.T",
                                                            "Central Rly station", "Guindy Industrial Estate",
                                                            "Iyyappanthangal",
                                                            "K.K.Nagar", "M.K.B.Nagar", "Mandaveli", "Pallavaram",
                                                            "Perambur",
                                                            "Poonamallee", "Redhills", "Saidapet", "Sriperumbathur",
                                                            "T.Nagar",
                                                            "Tambaram (West)", "Thiruvanmiyur", "Thiruvotriyur",
                                                            "Tondiarpet",
                                                            "Vadapalani", " Vallalar Nagar", "Velachery", "Villivakkam"]

                                            debo = StringVar()
                                            debo.set("Select")
                                            debo1 = OptionMenu(b3, debo, *debo_options)
                                            debo1.place(x=175, y=450)
                                            ticket_label = Label(b3, text="Ticket Type", font=('Arial', 15, 'bold'),
                                                                 bg="#ffff4d")
                                            ticket_label.place(x=50, y=500)
                                            Ticket_options = ["MST"]
                                            ticket = StringVar()
                                            ticket.set("Select")
                                            Ticket1 = OptionMenu(b3, ticket, *Ticket_options)
                                            Ticket1.place(x=175, y=500)
                                            age1 = StringVar()
                                            AGE = age1.get()
                                            age = Label(b3, text="Age", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                            age.place(x=50, y=550)
                                            age_entry = Entry(b3, textvariable=AGE, width=35)
                                            age_entry.place(x=175, y=550, width=100)
                                            gender_label = Label(b3, text="Gender", font=('Arial', 15, 'bold'),
                                                                 bg="#ffff4d")
                                            gender_label.place(x=700, y=200)
                                            gender_options = ["Male", "Female", "Transgender"]
                                            gender = StringVar()
                                            gender.set("Select")
                                            gender1 = OptionMenu(b3, gender, *gender_options)
                                            gender1.place(x=850, y=200)
                                            dob_label = Label(b3, text="Date of Birth", font=('Arial', 15, 'bold'),
                                                              bg="#ffff4d")
                                            dob_label.place(x=700, y=300)
                                            dob_entry = Entry(b3, textvariable=DOB, width=35)
                                            dob_entry.place(x=850, y=300, width=100)
                                            upload_photo_button = Button(b3, text='Upload photo',
                                                                         font=('times', 14, 'bold'),
                                                                         command=lambda: upload_file(), state=DISABLED)
                                            upload_photo_button.place(x=400, y=125)
                                            upload_data_button = Button(b3, text='Upload data',
                                                                        font=('times', 16, 'bold'), bg="#00ffbf",
                                                                        command=lambda: add_data(), state=DISABLED)
                                            upload_data_button.place(x=75, y=625)
                                            upload_aadhar_button = Button(b3, text='Upload Aadhar Card',
                                                                          font=('times', 14, 'bold'),
                                                                          command=lambda: upload_aadhar_card())
                                            upload_aadhar_button.place(x=800, y=650)

                                            def switchButtonState12():
                                                if (mybutton2['state'] == DISABLED):
                                                    mybutton2['state'] = NORMAL

                                            def switchButtonState2():
                                                if (upload_photo_button['state'] == DISABLED):
                                                    upload_photo_button['state'] = NORMAL

                                            global filename1

                                            def upload_aadhar_card():
                                                global filename1
                                                global filename1, img1
                                                f_types = [('Png files', '*.png'), ('Jpg Files', '*.jpg')]
                                                filename1 = filedialog.askopenfilename(filetypes=f_types)
                                                img1 = ImageTk.PhotoImage(file=filename1)
                                                messagebox.showinfo(title="Details Info",
                                                                    message="Successfully uploaded your Aadhar Card")
                                                switchButtonState2()

                                            def switchButtonState1():
                                                if (upload_data_button['state'] == DISABLED):
                                                    upload_data_button['state'] = NORMAL

                                            global filename

                                            def upload_file():
                                                if (
                                                        BETid_entry.get() == "" or name_entry.get() == "" or age_entry.get() == "" or Address_entry.get() == "" or pincode_entry.get() == "" or district_entry.get() == "" or state_entry.get() == "" or aadhar_entry.get() == "" or debo.get() == "Select" or ticket.get() == "Select" or gender.get() == "Select" or valid_date_entry.get() == "" or expire_date_entry.get() == "" or mobileno_entry.get() == "" or dob_entry.get() == "" or from12.get() == "" or to12.get() == "" or from22.get() == "" or to22.get() == ""):
                                                    messagebox.showerror(title="Getting user Details->Error",
                                                                         message="Please Make Sure To Enter All details")
                                                else:
                                                    global filename
                                                    global filename, img

                                                    f_types = [('Png files', '*.png'), ('Jpg Files', '*.jpg')]
                                                    filename = filedialog.askopenfilename(filetypes=f_types)
                                                    img = ImageTk.PhotoImage(file=filename)
                                                    b_1 = Button(b3, image=img)  # using Button
                                                    b_1.place(x=400, y=175)  # display uploaded photo
                                                    switchButtonState1()

                                            global filename, img
                                            global filename1
                                            global filename1, img1

                                            def create_code():
                                                input_path = filedialog.asksaveasfilename(title="save image",
                                                                                          filetypes=(
                                                                                              ("PNG File", ".png"),
                                                                                              ("All Files", "*.*")))
                                                switchButtonState12()
                                                if input_path:
                                                    if input_path.endswith(".png"):
                                                        get_code = pyqrcode.create(
                                                            "BET ID:" + BETid_entry.get() + "\n" + "NAME:" + name_entry.get() + "\n" + "AGE:" + age_entry.get() + "\n" + "RESIDENTIAL ADDRESS:" + Address_entry.get() + "\n" + "PINCODE:" + pincode_entry.get() + "\n" + "DISTRICT:" + district_entry.get() + "\n" + "STATE:" + state_entry.get() + "\n" + "AADHHAR NO:" + aadhar_entry.get() + "\n" + "DEPOT:" + debo.get() + "\n" + "BUS E-TICKET TYPE:" + ticket.get() + "\n" + "VALID FROM:" + valid_date_entry.get() + "\n" + "EXPIRE TILL:" + expire_date_entry.get() + "\n" + "GENDER:" + gender.get() + "\n" + "MOBILE NO:" + mobileno_entry.get() + "\n" + "DATE OF BIRTH:" + dob_entry.get() + "\n" + "FROM-I:" + from12.get() + "\n" + "TO-I:" + to12.get() + "\n" + "FROM-II:" + from22.get() + "\n" + "TO-II:" + to22.get())
                                                        get_code.png(input_path, scale=5)
                                                        with Image.open(input_path) as img:
                                                            img_resized = img.resize((200, 200))
                                                            img_resized.save(input_path)
                                                        messagebox.showinfo(title="Generate QR-code",
                                                                            message=f"Successfully Generated QR-Code For Details \n QR code saved to {input_path}")

                                                    else:
                                                        input_path = f'{input_path}.png'
                                                        get_code = pyqrcode.create(
                                                            "BET ID:" + BETid_entry.get() + "\n" + "NAME:" + name_entry.get() + "\n" + "AGE:" + age_entry.get() + "\n" + "RESIDENTIAL ADDRESS:" + Address_entry.get() + "\n" + "PINCODE:" + pincode_entry.get() + "\n" + "DISTRICT:" + district_entry.get() + "\n" + "STATE:" + state_entry.get() + "\n" + "AADHHAR NO:" + aadhar_entry.get() + "\n" + "DEPOT:" + debo.get() + "\n" + "BUS E-TICKET TYPE:" + ticket.get() + "\n" + "VALID FROM:" + valid_date_entry.get() + "\n" + "EXPIRE TILL:" + expire_date_entry.get() + "\n" + "GENDER:" + gender.get() + "\n" + "MOBILE NO:" + mobileno_entry.get() + "\n" + "DATE OF BIRTH:" + dob_entry.get() + "\n" + "FROM-I:" + from12.get() + "\n" + "TO-I:" + to12.get() + "\n" + "FROM-II:" + from22.get() + "\n" + "TO-II:" + to22.get())
                                                        get_code.png(input_path, scale=5)
                                                        with Image.open(input_path) as img:
                                                            img_resized = img.resize((200, 200))
                                                            img_resized.save(input_path)
                                                        messagebox.showinfo(title="Generate QR-code",
                                                                            message=f"Successfully Generated QR-Code For Details \n QR code saved to {input_path}")

                                            def create_code1():
                                                data = BETid_entry.get()

                                                # Create QR code object
                                                qr = qrcode.QRCode(
                                                    version=None,
                                                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                                                    box_size=10,
                                                    border=4,
                                                )
                                                qr.add_data(data)
                                                qr.make(fit=True)

                                                # Create QR code image with fill color and background color
                                                qr_image = qr.make_image(fill_color="white", back_color="orange")

                                                # Load logo image
                                                logo_image = Image.open("windowBusIcon.png")

                                                # Resize logo image to fit inside QR code
                                                logo_size = (qr_image.size[0] // 7, qr_image.size[1] // 7)

                                                # logo_size = (qr_image.size[0] // 4, qr_image.size[1] // 4)
                                                logo_image = logo_image.resize(logo_size)

                                                # Calculate position to place logo image inside QR code
                                                logo_pos = (
                                                    (qr_image.size[0] - logo_size[0]) // 2,
                                                    (qr_image.size[1] - logo_size[1]) // 2)

                                                # Paste logo image onto QR code image
                                                qr_image.paste(logo_image)

                                                # Resize QR code image to 100x100 pixels
                                                qr_image = qr_image.resize((175, 175))

                                                # Get file path from user using file dialog
                                                file_path = filedialog.asksaveasfilename(title="Save QR Code",
                                                                                         filetypes=(
                                                                                         ("PNG Files", "*.png"),))

                                                # Save QR code image to file
                                                if file_path:
                                                    if file_path.endswith(".png"):
                                                        qr_image.save(file_path, "PNG")
                                                        messagebox.showinfo(title="QR Code Saved",
                                                                            message=f"Successfully Generated QR-Code For BET ID \n QR code saved to {file_path}")
                                                    else:
                                                        file_path = f'{file_path}.png'
                                                        qr_image.save(file_path, "PNG")
                                                        messagebox.showinfo(title="QR Code Saved",
                                                                            message=f"Successfully Generated QR-Code For BET ID \n QR code saved to {file_path}")

                                            mybutton = Button(b3, text="Generate QR-Code For Details",
                                                              font=('times', 11, 'bold'),
                                                              bg="#00ff00", state=DISABLED, command=create_code)
                                            mybutton.place(x=250, y=625)
                                            mybutton2 = Button(b3, text="Generate QR-Code for BET ID ",
                                                               font=('times', 11, 'bold'),
                                                               bg="#00ff00",
                                                               state=DISABLED, command=create_code1)
                                            mybutton2.place(x=475, y=660)

                                            def switchButtonState():
                                                if (mybutton['state'] == DISABLED):
                                                    mybutton['state'] = NORMAL

                                            def add_data():
                                                global img, filename
                                                global filename1
                                                global filename1, img1
                                                with open("mytextfile.txt", "a") as f:
                                                    f.write(BETid_entry.get() + "\n")
                                                fob = open(filename, 'rb')
                                                fob = fob.read()
                                                fob1 = open(filename1, 'rb')
                                                fob1 = fob1.read()
                                                data = (BETid_entry.get(), name_entry.get(), Address_entry.get(),
                                                        pincode_entry.get(),
                                                        district_entry.get(),
                                                        state_entry.get(), aadhar_entry.get(),
                                                        debo.get(), ticket.get(), valid_date_entry.get(),
                                                        expire_date_entry.get(),

                                                        mobileno_entry.get(), from12.get(), to12.get(),
                                                        from22.get(), to22.get(), fob, age_entry.get(), dob_entry.get(),
                                                        fob1, gender.get())

                                                try:
                                                    my_conn = create_engine(
                                                        "mysql+mysqldb://root:password123@localhost/buseticket")
                                                    my_conn.execute("INSERT INTO person_details(bet_id,name,address,pincode,district,state,aadhar_no,depot,ticket_type,valid_from,expire_till,mobile_no,from_I,to_I,from_II,to_II,profile_pic,age,date_of_birth,aadhar_card_pic,gender) \
                                                                                                                                                                                                  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                                                    data)
                                                    switchButtonState()
                                                except:
                                                    messagebox.showerror(title="Getting user Details->Error",
                                                                         message="01.Make Sure To Enter All details \n 02.Make sure that You have Entered correct details\n like BET ID,AADHAR NUMBER,MOBILE NUMBER etc")

                                            b3.mainloop()

                                        rules_photo1 = PhotoImage(file='ProcedureforMST.png')
                                        criteria_label1 = Label(b3, text="Procedure To Apply MST",
                                                                font=('times', 25, 'bold'))
                                        criteria_label1.place(x=450, y=50)
                                        rules_label1 = Label(b3, fg='#00FF00', bg='white', relief=RAISED, bd=10, padx=0,
                                                             pady=0,
                                                             image=rules_photo1, compound='top')
                                        rules_label1.place(x=80, y=100)
                                        Next_button1 = Button(b3, text='Next', bg="green", font=('times', 14, 'bold'),
                                                              command=lambda: nextpage())
                                        Next_button1.place(x=650, y=600)
                                        b3.mainloop()

                                    b3.mainloop()
                                elif (click1.get() == "Students"):
                                    a1.destroy()
                                    b4 = Tk()
                                    b4.geometry("1490x745")
                                    b4.title("Getting Detail from User")
                                    icon = ImageTk.PhotoImage(file='windowBusIcon.png')
                                    b4.wm_iconphoto(False, icon)
                                    cana = Canvas(b4, width=800, height=800)
                                    cana.pack(fill="both", expand=True)
                                    img2 = Image.open("bgforwindow6.png")
                                    resize3 = img2.resize((1490, 745))
                                    new2 = ImageTk.PhotoImage(resize3)
                                    cana.create_image(0, 0, image=new2, anchor='nw')
                                    rules_photo = PhotoImage(file='SCT.png')
                                    criteria_label = Label(b4, text="Adult Wise Price List", font=('times', 25, 'bold'))
                                    criteria_label.place(x=550, y=50)
                                    rules_label = Label(b4, fg='#00FF00', bg='white', relief=RAISED, bd=10, padx=0,
                                                        pady=0,
                                                        image=rules_photo, compound='top')
                                    rules_label.place(x=80, y=100)
                                    Next_button = Button(b4, text='Next', bg="green", font=('times', 14, 'bold'),
                                                         command=lambda: next1())
                                    Next_button.place(x=650, y=600)

                                    def next1():
                                        rules_label.destroy()
                                        criteria_label.destroy()
                                        Next_button.destroy()

                                        def nextpage():
                                            rules_label1.destroy()
                                            criteria_label1.destroy()
                                            Next_button1.destroy()

                                            # details info

                                            name = StringVar()
                                            NAME = name.get()
                                            address1 = StringVar()
                                            ADDRESS = address1.get()
                                            pincode1 = StringVar()
                                            PINCODE = pincode1.get()
                                            aadhar1 = StringVar()
                                            AADHARNO = aadhar1.get()
                                            BETID = StringVar()
                                            BETid = BETID.get()
                                            district = StringVar()
                                            DISTRICT = district.get()
                                            state = StringVar()
                                            STATE = state.get()
                                            valid_date = StringVar()
                                            VALID_DATE = valid_date.get()
                                            expire_date = StringVar()
                                            EXPIRE_DATE = expire_date.get()
                                            mobile1 = StringVar()
                                            MOBILE = mobile1.get()
                                            dob = StringVar()
                                            DOB = dob.get()
                                            college1 = StringVar()
                                            COLLEGE = college1.get()

                                            form_123 = StringVar()
                                            FORM12 = form_123.get()
                                            to_123 = StringVar()
                                            TO12 = to_123.get()
                                            form_1223 = StringVar()
                                            FORM122 = form_1223.get()
                                            to_1223 = StringVar()
                                            TO122 = to_1223.get()

                                            def my_command():
                                                b4.destroy()
                                                HOME_BUTTON_PAGE()

                                            click_btn = PhotoImage(file='Small_Home_ Icon.png')
                                            button = Button(b4, image=click_btn, command=my_command)
                                            button.place(x=30, y=25)

                                            def my_command1():
                                                b4.destroy()
                                                CREATE_BET_PAGE()

                                            click_btn1 = PhotoImage(file='small_back_icon.png')
                                            button1 = Button(b4, image=click_btn1, command=my_command1)
                                            button1.place(x=95, y=25)
                                            font = Label(b4, text="Create your Bus E-Ticket",
                                                         font=('Arial', 22, 'bold'),
                                                         bg="#b3ffff")
                                            font.place(x=200, y=25)
                                            BETid_label = Label(b4, text="BET id", font=('Arial', 15, 'bold'),
                                                                bg="#ffff4d")
                                            BETid_label.place(x=50, y=100)
                                            BETid_entry = Entry(b4, textvariable=BETid, width=35)
                                            BETid_entry.place(x=175, y=100, width=100)
                                            name = Label(b4, text="Name", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                            name.place(x=50, y=150)
                                            name_entry = Entry(b4, textvariable=NAME, width=35)
                                            name_entry.place(x=175, y=150, width=100)
                                            Address = Label(b4, text="Address", font=('Arial', 15, 'bold'),
                                                            bg="#ffff4d")
                                            Address.place(x=50, y=200)
                                            Address_entry = Entry(b4, textvariable=ADDRESS, width=35)
                                            Address_entry.place(x=175, y=200, width=100)
                                            pincode = Label(b4, text="Pincode", font=('Arial', 15, 'bold'),
                                                            bg="#ffff4d")
                                            pincode.place(x=50, y=250)
                                            pincode_entry = Entry(b4, textvariable=PINCODE, width=35)
                                            pincode_entry.place(x=175, y=250, width=100)
                                            district_label = Label(b4, text="District", font=('Arial', 15, 'bold'),
                                                                   bg="#ffff4d")
                                            district_label.place(x=50, y=300)
                                            district_entry = Entry(b4, textvariable=DISTRICT, width=35)
                                            district_entry.place(x=175, y=300, width=100)
                                            state = Label(b4, text="State", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                            state.place(x=50, y=350)
                                            state_entry = Entry(b4, textvariable=STATE, width=35)
                                            state_entry.place(x=175, y=350, width=100)
                                            aadhar = Label(b4, text="Aadhar No", font=('Arial', 15, 'bold'),
                                                           bg="#ffff4d")
                                            aadhar.place(x=50, y=400)
                                            aadhar_entry = Entry(b4, textvariable=AADHARNO, width=35)
                                            aadhar_entry.place(x=175, y=400, width=100)
                                            college_label = Label(b4, text="College Name", font=('Arial', 15, 'bold'),
                                                                  bg="#ffff4d")
                                            college_label.place(x=700, y=50)
                                            college_entry = Entry(b4, textvariable=COLLEGE, width=35)
                                            college_entry.place(x=850, y=50, width=100)
                                            valid_date_label = Label(b4, text="Valid From", font=('Arial', 15, 'bold'),
                                                                     bg="#ffff4d")
                                            valid_date_label.place(x=700, y=100)
                                            valid_date_entry = Entry(b4, textvariable=VALID_DATE, width=35)
                                            valid_date_entry.place(x=850, y=100, width=100)
                                            expire_date_label = Label(b4, text="Expire Till",
                                                                      font=('Arial', 15, 'bold'),
                                                                      bg="#ffff4d")
                                            expire_date_label.place(x=700, y=150)
                                            expire_date_entry = Entry(b4, textvariable=EXPIRE_DATE, width=35)
                                            expire_date_entry.place(x=850, y=150, width=100)
                                            mobileno = Label(b4, text="Mobile No", font=('Arial', 15, 'bold'),
                                                             bg="#ffff4d")
                                            mobileno.place(x=700, y=250)
                                            mobileno_entry = Entry(b4, textvariable=MOBILE, width=35)
                                            mobileno_entry.place(x=850, y=250, width=100)
                                            part1 = Label(b4, text="Part-I", font=('Arial', 12, 'bold'), bg="#cc0099")
                                            part1.place(x=700, y=350)
                                            from1_label = Label(b4, text="From-I", font=('Arial', 15, 'bold'),
                                                                bg="#ffff4d")
                                            from1_label.place(x=700, y=400)
                                            from12 = Entry(b4, textvariable=FORM12, width=35)
                                            from12.place(x=850, y=400)
                                            to1_label = Label(b4, text="To-I", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                            to1_label.place(x=700, y=450)
                                            to12 = Entry(b4, textvariable=TO12, width=35)
                                            to12.place(x=850, y=450)
                                            part2 = Label(b4, text="Part-II", font=('Arial', 12, 'bold'), bg="#cc0099")
                                            part2.place(x=700, y=500)
                                            from2_label = Label(b4, text="From-II", font=('Arial', 15, 'bold'),
                                                                bg="#ffff4d")
                                            from2_label.place(x=700, y=550)
                                            from22 = Entry(b4, textvariable=FORM122, width=35)
                                            from22.place(x=850, y=550)
                                            to2_label = Label(b4, text="To-II", font=('Arial', 15, 'bold'),
                                                              bg="#ffff4d")
                                            to2_label.place(x=700, y=600)
                                            to22 = Entry(b4, textvariable=TO122, width=35)
                                            to22.place(x=850, y=600)
                                            debo_label = Label(b4, text="Depot", font=('Arial', 15, 'bold'),
                                                               bg="#ffff4d")
                                            debo_label.place(x=50, y=450)
                                            debo_options = ["Adyar", "Ambathur Industrial Estate", " Ambathur OT",
                                                            " Anna Nagar (West)", "Avadi", "Ayanavaram", "Broadway",
                                                            "C.M.B.T",
                                                            "Central Rly station", "Guindy Industrial Estate",
                                                            "Iyyappanthangal",
                                                            "K.K.Nagar", "M.K.B.Nagar", "Mandaveli", "Pallavaram",
                                                            "Perambur",
                                                            "Poonamallee", "Redhills", "Saidapet", "Sriperumbathur",
                                                            "T.Nagar",
                                                            "Tambaram (West)", "Thiruvanmiyur", "Thiruvotriyur",
                                                            "Tondiarpet",
                                                            "Vadapalani", " Vallalar Nagar", "Velachery", "Villivakkam"]

                                            debo = StringVar()
                                            debo.set("Select")
                                            debo1 = OptionMenu(b4, debo, *debo_options)
                                            debo1.place(x=175, y=450)
                                            ticket_label = Label(b4, text="Ticket Type", font=('Arial', 15, 'bold'),
                                                                 bg="#ffff4d")
                                            ticket_label.place(x=50, y=500)
                                            Ticket_options = ["SCT"]
                                            ticket = StringVar()
                                            ticket.set("Select")
                                            Ticket1 = OptionMenu(b4, ticket, *Ticket_options)
                                            Ticket1.place(x=175, y=500)
                                            age1 = StringVar()
                                            AGE = age1.get()
                                            age = Label(b4, text="Age", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                            age.place(x=50, y=550)
                                            age_entry = Entry(b4, textvariable=AGE, width=35)
                                            age_entry.place(x=175, y=550, width=100)
                                            gender_label = Label(b4, text="Gender", font=('Arial', 15, 'bold'),
                                                                 bg="#ffff4d")
                                            gender_label.place(x=700, y=200)
                                            gender_options = ["Male", "Female", "Transgender"]
                                            gender = StringVar()
                                            gender.set("Select")
                                            gender1 = OptionMenu(b4, gender, *gender_options)
                                            gender1.place(x=850, y=200)
                                            dob_label = Label(b4, text="Date of Birth", font=('Arial', 15, 'bold'),
                                                              bg="#ffff4d")
                                            dob_label.place(x=700, y=300)
                                            dob_entry = Entry(b4, textvariable=DOB, width=35)
                                            dob_entry.place(x=850, y=300, width=100)
                                            upload_photo_button = Button(b4, text='Upload photo',
                                                                         font=('times', 14, 'bold'),
                                                                         command=lambda: upload_file(), state=DISABLED)
                                            upload_photo_button.place(x=400, y=125)
                                            upload_data_button = Button(b4, text='Upload data',
                                                                        font=('times', 16, 'bold'),
                                                                        bg="#00ffbf",
                                                                        command=lambda: add_data(), state=DISABLED)
                                            upload_data_button.place(x=75, y=625)
                                            upload_aadhar_button = Button(b4, text='Upload Aadhar Card',
                                                                          font=('times', 14, 'bold'),
                                                                          command=lambda: upload_aadhar_card())
                                            upload_aadhar_button.place(x=800, y=650)

                                            def switchButtonState12():
                                                if (mybutton2['state'] == DISABLED):
                                                    mybutton2['state'] = NORMAL

                                            def switchButtonState2():
                                                if (upload_photo_button['state'] == DISABLED):
                                                    upload_photo_button['state'] = NORMAL

                                            global filename1

                                            def upload_aadhar_card():
                                                global filename1
                                                global filename1, img1
                                                f_types = [('Png files', '*.png'), ('Jpg Files', '*.jpg')]
                                                filename1 = filedialog.askopenfilename(filetypes=f_types)
                                                img1 = ImageTk.PhotoImage(file=filename1)
                                                messagebox.showinfo(title="Details Info",
                                                                    message="Successfully uploaded your Aadhar Card")
                                                switchButtonState2()

                                            def switchButtonState1():
                                                if (upload_data_button['state'] == DISABLED):
                                                    upload_data_button['state'] = NORMAL

                                            global filename

                                            def upload_file():
                                                if (
                                                        BETid_entry.get() == "" or college_entry.get() == "" or name_entry.get() == "" or age_entry.get() == "" or Address_entry.get() == "" or pincode_entry.get() == "" or district_entry.get() == "" or state_entry.get() == "" or aadhar_entry.get() == "" or debo.get() == "Select" or ticket.get() == "Select" or gender.get() == "Select" or valid_date_entry.get() == "" or expire_date_entry.get() == "" or mobileno_entry.get() == "" or dob_entry.get() == "" or from12.get() == "" or to12.get() == "" or from22.get() == "" or to22.get() == ""):
                                                    messagebox.showerror(title="Getting user Details->Error",
                                                                         message="Please Make Sure To Enter All details")
                                                else:
                                                    global filename
                                                    global filename, img

                                                    f_types = [('Png files', '*.png'), ('Jpg Files', '*.jpg')]
                                                    filename = filedialog.askopenfilename(filetypes=f_types)
                                                    img = ImageTk.PhotoImage(file=filename)
                                                    b_1 = Button(b4, image=img)  # using Button
                                                    b_1.place(x=400, y=175)  # display uploaded photo
                                                    switchButtonState1()

                                            global filename, img
                                            global filename1
                                            global filename1, img1

                                            def create_code():
                                                input_path = filedialog.asksaveasfilename(title="save image",
                                                                                          filetypes=(
                                                                                              ("PNG File", ".png"),
                                                                                              ("All Files", "*.*")))
                                                switchButtonState12()
                                                if input_path:
                                                    if input_path.endswith(".png"):
                                                        get_code = pyqrcode.create(
                                                            "BET ID:" + BETid_entry.get() + "\n" + "NAME:" + name_entry.get() + "\n" + "AGE:" + age_entry.get() + "\n" + "RESIDENTIAL ADDRESS:" + Address_entry.get() + "\n" + "PINCODE:" + pincode_entry.get() + "\n" + "DISTRICT:" + district_entry.get() + "\n" + "STATE:" + state_entry.get() + "\n" + "AADHHAR NO:" + aadhar_entry.get() + "\n" + "DEPOT:" + debo.get() + "\n" + "COLLEGE NAME:" + college_entry.get() + "\n" + "BUS E-TICKET TYPE:" + ticket.get() + "\n" + "VALID FROM:" + valid_date_entry.get() + "\n" + "EXPIRE TILL:" + expire_date_entry.get() + "\n" + "GENDER:" + gender.get() + "\n" + "MOBILE NO:" + mobileno_entry.get() + "\n" + "DATE OF BIRTH:" + dob_entry.get() + "\n" + "FROM-I:" + from12.get() + "\n" + "TO-I:" + to12.get() + "\n" + "FROM-II:" + from22.get() + "\n" + "TO-II:" + to22.get())
                                                        get_code.png(input_path, scale=5)
                                                        with Image.open(input_path) as img:
                                                            img_resized = img.resize((200, 200))
                                                            img_resized.save(input_path)
                                                        messagebox.showinfo(title="Generate QR-code",
                                                                            message=f"Successfully Generated QR-Code For Details \n QR code saved to {input_path}")

                                                    else:
                                                        input_path = f'{input_path}.png'
                                                        get_code = pyqrcode.create(
                                                            "BET ID:" + BETid_entry.get() + "\n" + "NAME:" + name_entry.get() + "\n" + "AGE:" + age_entry.get() + "\n" + "RESIDENTIAL ADDRESS:" + Address_entry.get() + "\n" + "PINCODE:" + pincode_entry.get() + "\n" + "DISTRICT:" + district_entry.get() + "\n" + "STATE:" + state_entry.get() + "\n" + "AADHHAR NO:" + aadhar_entry.get() + "\n" + "DEPOT:" + debo.get() + "\n" + "COLLEGE NAME:" + college_entry.get() + "\n" + "BUS E-TICKET TYPE:" + ticket.get() + "\n" + "VALID FROM:" + valid_date_entry.get() + "\n" + "EXPIRE TILL:" + expire_date_entry.get() + "\n" + "GENDER:" + gender.get() + "\n" + "MOBILE NO:" + mobileno_entry.get() + "\n" + "DATE OF BIRTH:" + dob_entry.get() + "\n" + "FROM-I:" + from12.get() + "\n" + "TO-I:" + to12.get() + "\n" + "FROM-II:" + from22.get() + "\n" + "TO-II:" + to22.get())

                                                        get_code.png(input_path, scale=5)
                                                        with Image.open(input_path) as img:
                                                            img_resized = img.resize((200, 200))
                                                            img_resized.save(input_path)
                                                        messagebox.showinfo(title="Generate QR-code",
                                                                            message=f"Successfully Generated QR-Code For Details \n QR code saved to {input_path}")

                                            def create_code1():
                                                data = BETid_entry.get()

                                                # Create QR code object
                                                qr = qrcode.QRCode(
                                                    version=None,
                                                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                                                    box_size=10,
                                                    border=4,
                                                )
                                                qr.add_data(data)
                                                qr.make(fit=True)

                                                # Create QR code image with fill color and background color
                                                qr_image = qr.make_image(fill_color="white", back_color="red")

                                                # Load logo image
                                                logo_image = Image.open("windowBusIcon.png")

                                                # Resize logo image to fit inside QR code
                                                logo_size = (qr_image.size[0] // 7, qr_image.size[1] // 7)

                                                # logo_size = (qr_image.size[0] // 4, qr_image.size[1] // 4)
                                                logo_image = logo_image.resize(logo_size)

                                                # Calculate position to place logo image inside QR code
                                                logo_pos = (
                                                    (qr_image.size[0] - logo_size[0]) // 2,
                                                    (qr_image.size[1] - logo_size[1]) // 2)

                                                # Paste logo image onto QR code image
                                                qr_image.paste(logo_image)

                                                # Resize QR code image to 100x100 pixels
                                                qr_image = qr_image.resize((175, 175))

                                                # Get file path from user using file dialog
                                                file_path = filedialog.asksaveasfilename(title="Save QR Code",
                                                                                         filetypes=(
                                                                                         ("PNG Files", "*.png"),))

                                                # Save QR code image to file
                                                if file_path:
                                                    if file_path.endswith(".png"):
                                                        qr_image.save(file_path, "PNG")
                                                        messagebox.showinfo(title="QR Code Saved",
                                                                            message=f"Successfully Generated QR-Code For BET ID \n QR code saved to {file_path}")
                                                    else:
                                                        file_path = f'{file_path}.png'
                                                        qr_image.save(file_path, "PNG")
                                                        messagebox.showinfo(title="QR Code Saved",
                                                                            message=f"Successfully Generated QR-Code For BET ID \n QR code saved to {file_path}")

                                            mybutton = Button(b4, text="Generate QR-Code For Details",
                                                              font=('times', 11, 'bold'),
                                                              bg="#00ff00", state=DISABLED, command=create_code)
                                            mybutton.place(x=250, y=625)
                                            mybutton2 = Button(b4, text="Generate QR-Code for BET ID ",
                                                               font=('times', 11, 'bold'),
                                                               bg="#00ff00",
                                                               state=DISABLED, command=create_code1)
                                            mybutton2.place(x=475, y=660)

                                            def switchButtonState():
                                                if (mybutton['state'] == DISABLED):
                                                    mybutton['state'] = NORMAL

                                            def add_data():
                                                global img, filename
                                                global filename1
                                                global filename1, img1
                                                with open("mytextfile.txt", "a") as f:
                                                    f.write(BETid_entry.get() + "\n")
                                                fob = open(filename, 'rb')
                                                fob = fob.read()
                                                fob1 = open(filename1, 'rb')
                                                fob1 = fob1.read()
                                                data = (
                                                    BETid_entry.get(), name_entry.get(), Address_entry.get(),
                                                    pincode_entry.get(),
                                                    district_entry.get(),
                                                    state_entry.get(), aadhar_entry.get(),
                                                    debo.get(), ticket.get(), valid_date_entry.get(),
                                                    expire_date_entry.get(),

                                                    mobileno_entry.get(), college_entry.get(), from12.get(), to12.get(),
                                                    from22.get(), to22.get(), fob, age_entry.get(), dob_entry.get(),
                                                    fob1, gender.get())

                                                try:
                                                    my_conn = create_engine(
                                                        "mysql+mysqldb://root:password123@localhost/buseticket")
                                                    my_conn.execute("INSERT INTO person_details(bet_id,name,address,pincode,district,state,aadhar_no,depot,ticket_type,valid_from,expire_till,mobile_no,college,from_I,to_I,from_II,to_II,profile_pic,age,date_of_birth,aadhar_card_pic,gender) \
                                                                                                                                                                                                   VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                                                    data)
                                                    switchButtonState()
                                                except:
                                                    messagebox.showerror(title="Getting user Details->Error",
                                                                         message="01.Make Sure To Enter All details \n 02.Make sure that You have Entered correct details\n like BET ID,AADHAR NUMBER,MOBILE NUMBER etc")

                                            b4.mainloop()

                                        rules_photo1 = PhotoImage(file='procedureforSCT.png')
                                        criteria_label1 = Label(b4, text="Procedure To Apply SCT",
                                                                font=('times', 25, 'bold'))
                                        criteria_label1.place(x=450, y=50)
                                        rules_label1 = Label(b4, fg='#00FF00', bg='white', relief=RAISED, bd=10, padx=0,
                                                             pady=0,
                                                             image=rules_photo1, compound='top')
                                        rules_label1.place(x=80, y=100)
                                        Next_button1 = Button(b4, text='Next', bg="green", font=('times', 14, 'bold'),
                                                              command=lambda: nextpage())
                                        Next_button1.place(x=650, y=600)
                                        b4.mainloop()

                                    b4.mainloop()

                                elif (click1.get() == "Journalists/Reporters"):
                                    a1.destroy()
                                    b5 = Tk()
                                    b5.geometry("1490x745")
                                    b5.title("Getting Detail from User")
                                    icon = ImageTk.PhotoImage(file='windowBusIcon.png')
                                    b5.wm_iconphoto(False, icon)
                                    cana = Canvas(b5, width=800, height=800)
                                    cana.pack(fill="both", expand=True)
                                    img2 = Image.open("bgforwindow6.png")
                                    resize3 = img2.resize((1490, 745))
                                    new2 = ImageTk.PhotoImage(resize3)
                                    cana.create_image(0, 0, image=new2, anchor='nw')
                                    rules_photo = PhotoImage(file='PressReporter.png')
                                    criteria_label = Label(b5, text="Criteria & Rules To Apply Reporter/Journalist",
                                                           font=('times', 25, 'bold'))
                                    criteria_label.place(x=450, y=50)
                                    rules_label = Label(b5, fg='#00FF00', bg='white', relief=RAISED, bd=10, padx=0,
                                                        pady=0,
                                                        image=rules_photo, compound='top')
                                    rules_label.place(x=100, y=100)
                                    Next_button = Button(b5, text='Next', bg="green", font=('times', 14, 'bold'),
                                                         command=lambda: nextpage())
                                    Next_button.place(x=650, y=600)

                                    def nextpage():
                                        rules_label.destroy()
                                        criteria_label.destroy()
                                        Next_button.destroy()
                                        # details info
                                        name = StringVar()
                                        NAME = name.get()
                                        address1 = StringVar()
                                        ADDRESS = address1.get()
                                        age1 = StringVar()
                                        AGE = age1.get()
                                        pincode1 = StringVar()
                                        PINCODE = pincode1.get()
                                        dob1 = StringVar()
                                        DOB = dob1.get()
                                        aadhar1 = StringVar()
                                        AADHARNO = aadhar1.get()
                                        BETID = StringVar()
                                        BETid = BETID.get()
                                        district = StringVar()
                                        DISTRICT = district.get()
                                        state = StringVar()
                                        STATE = state.get()
                                        valid_date = StringVar()
                                        VALID_DATE = valid_date.get()
                                        expire_date = StringVar()
                                        EXPIRE_DATE = expire_date.get()
                                        mobile1 = StringVar()
                                        MOBILE = mobile1.get()

                                        def my_command():
                                            b5.destroy()
                                            HOME_BUTTON_PAGE()

                                        click_btn = PhotoImage(file='Small_Home_ Icon.png')
                                        button = Button(b5, image=click_btn, command=my_command)
                                        button.place(x=30, y=25)

                                        def my_command1():
                                            b5.destroy()
                                            CREATE_BET_PAGE()

                                        click_btn1 = PhotoImage(file='small_back_icon.png')
                                        button1 = Button(b5, image=click_btn1, command=my_command1)
                                        button1.place(x=95, y=25)

                                        font = Label(b5, text="Create your Bus E-Ticket", font=('Arial', 22, 'bold'),
                                                     bg="#b3ffff")
                                        font.place(x=200, y=25)
                                        BETid_label = Label(b5, text="BET id", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        BETid_label.place(x=50, y=100)
                                        BETid_entry = Entry(b5, textvariable=BETid, width=35)
                                        BETid_entry.place(x=175, y=100, width=100)
                                        name = Label(b5, text="Name", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        name.place(x=50, y=150)
                                        name_entry = Entry(b5, textvariable=NAME, width=35)
                                        name_entry.place(x=175, y=150, width=100)
                                        Address = Label(b5, text="Address", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        Address.place(x=50, y=200)
                                        Address_entry = Entry(b5, textvariable=ADDRESS, width=35)
                                        Address_entry.place(x=175, y=200, width=100)
                                        pincode = Label(b5, text="Pincode", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        pincode.place(x=50, y=250)
                                        pincode_entry = Entry(b5, textvariable=PINCODE, width=35)
                                        pincode_entry.place(x=175, y=250, width=100)
                                        district_label = Label(b5, text="District", font=('Arial', 15, 'bold'),
                                                               bg="#ffff4d")
                                        district_label.place(x=50, y=300)
                                        district_entry = Entry(b5, textvariable=DISTRICT, width=35)
                                        district_entry.place(x=175, y=300, width=100)
                                        state = Label(b5, text="State", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        state.place(x=50, y=350)
                                        state_entry = Entry(b5, textvariable=STATE, width=35)
                                        state_entry.place(x=175, y=350, width=100)
                                        aadhar = Label(b5, text="Aadhar No", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        aadhar.place(x=50, y=400)
                                        aadhar_entry = Entry(b5, textvariable=AADHARNO, width=35)
                                        aadhar_entry.place(x=175, y=400, width=100)
                                        valid_date_label = Label(b5, text="Valid From", font=('Arial', 15, 'bold'),
                                                                 bg="#ffff4d")
                                        valid_date_label.place(x=700, y=100)
                                        valid_date_entry = Entry(b5, textvariable=VALID_DATE, width=35)
                                        valid_date_entry.place(x=850, y=100, width=100)
                                        expire_date_label = Label(b5, text="Expire Till", font=('Arial', 15, 'bold'),
                                                                  bg="#ffff4d")
                                        expire_date_label.place(x=700, y=150)
                                        expire_date_entry = Entry(b5, textvariable=EXPIRE_DATE, width=35)
                                        expire_date_entry.place(x=850, y=150, width=100)
                                        mobileno = Label(b5, text="Mobile No", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        mobileno.place(x=700, y=200)
                                        mobileno_entry = Entry(b5, textvariable=MOBILE, width=35)
                                        mobileno_entry.place(x=850, y=200, width=100)
                                        gender_label = Label(b5, text="Gender", font=('Arial', 15, 'bold'),
                                                             bg="#ffff4d")
                                        gender_label.place(x=700, y=250)
                                        gender_options = ["Male", "Female", "Transgender"]
                                        gender = StringVar()
                                        gender.set("Select")
                                        gender1 = OptionMenu(b5, gender, *gender_options)
                                        gender1.place(x=850, y=250)
                                        dob_label = Label(b5, text="Date of Birth", font=('Arial', 15, 'bold'),
                                                          bg="#ffff4d")
                                        dob_label.place(x=700, y=300)
                                        dob_entry = Entry(b5, textvariable=DOB, width=35)
                                        dob_entry.place(x=850, y=300, width=100)
                                        upload_aadhar_button = Button(b5, text='Upload Aadhar Card',
                                                                      font=('times', 14, 'bold'),
                                                                      command=lambda: upload_aadhar_card(),
                                                                      state=DISABLED)
                                        upload_aadhar_button.place(x=900, y=400)
                                        upload_RJ_button = Button(b5, text='Upload Reporter/Journalist ID Proof',
                                                                  font=('times', 14, 'bold'),
                                                                  command=lambda: Upload_Reporter_Journalist())
                                        upload_RJ_button.place(x=900, y=350)

                                        def switchButtonState2():
                                            if (upload_photo_button['state'] == DISABLED):
                                                upload_photo_button['state'] = NORMAL

                                        def switchButtonState20():
                                            if (upload_aadhar_button['state'] == DISABLED):
                                                upload_aadhar_button['state'] = NORMAL

                                        global filename1

                                        def upload_aadhar_card():
                                            global filename1
                                            global filename1, img1
                                            f_types = [('Png files', '*.png'), ('Jpg Files', '*.jpg')]
                                            filename1 = filedialog.askopenfilename(filetypes=f_types)
                                            img1 = ImageTk.PhotoImage(file=filename1)
                                            messagebox.showinfo(title="Details Info",
                                                                message="Successfully uploaded your Aadhar Card")
                                            switchButtonState2()

                                        global filename1, img1
                                        global filename1

                                        def Upload_Reporter_Journalist():
                                            global filename2
                                            global filename2, img2
                                            f_types = [('Png files', '*.png'), ('Jpg Files', '*.jpg')]
                                            filename2 = filedialog.askopenfilename(filetypes=f_types)
                                            img2 = ImageTk.PhotoImage(file=filename2)
                                            messagebox.showinfo(title="Details Info",
                                                                message="Successfully uploaded your Reporter/Journalist ID Proof")
                                            switchButtonState20()

                                        global filename2, img2
                                        debo_label = Label(b5, text="Depot", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        debo_label.place(x=50, y=450)
                                        debo_options = ["Adyar", "Ambathur Industrial Estate", " Ambathur OT",
                                                        " Anna Nagar (West)",
                                                        "Avadi", "Ayanavaram", "Broadway", "C.M.B.T",
                                                        "Central Rly station",
                                                        "Guindy Industrial Estate", "Iyyappanthangal", "K.K.Nagar",
                                                        "M.K.B.Nagar",
                                                        "Mandaveli", "Pallavaram", "Perambur", "Poonamallee",
                                                        "Redhills", "Saidapet",
                                                        "Sriperumbathur", "T.Nagar", "Tambaram (West)", "Thiruvanmiyur",
                                                        "Thiruvotriyur", "Tondiarpet", "Vadapalani", " Vallalar Nagar",
                                                        "Velachery",
                                                        "Villivakkam"]
                                        debo = StringVar()
                                        debo.set("Select")
                                        debo1 = OptionMenu(b5, debo, *debo_options)
                                        debo1.place(x=175, y=450)
                                        ticket_label = Label(b5, text="Ticket Type", font=('Arial', 15, 'bold'),
                                                             bg="#ffff4d")
                                        ticket_label.place(x=50, y=500)
                                        Ticket_options = ["Reporter/Journalist"]
                                        ticket = StringVar()
                                        ticket.set("Select")
                                        Ticket1 = OptionMenu(b5, ticket, *Ticket_options)
                                        Ticket1.place(x=175, y=500)
                                        age = Label(b5, text="Age", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        age.place(x=50, y=550)
                                        age_entry = Entry(b5, textvariable=AGE, width=35)
                                        age_entry.place(x=175, y=550, width=100)
                                        upload_photo_button = Button(b5, text='Upload photo',
                                                                     font=('times', 14, 'bold'),
                                                                     command=lambda: upload_file(), state=DISABLED)
                                        upload_photo_button.place(x=400, y=125)
                                        upload_data_button = Button(b5, text='Upload data', font=('times', 16, 'bold'),
                                                                    bg="#00ffbf",
                                                                    command=lambda: add_data(), state=DISABLED)
                                        upload_data_button.place(x=75, y=625)

                                        def switchButtonState1():
                                            if (upload_data_button['state'] == DISABLED):
                                                upload_data_button['state'] = NORMAL

                                        global filename

                                        def upload_file():
                                            if (
                                                    BETid_entry.get() == "" or name_entry.get() == "" or gender.get() == "Select" or dob_entry.get() == "" or Address_entry.get() == "" or pincode_entry.get() == "" or district_entry.get() == "" or state_entry.get() == "" or aadhar_entry.get() == "" or debo.get() == "Select" or ticket.get() == "Select" or valid_date_entry.get() == "" or expire_date_entry.get() == "" or age_entry.get() == "" or mobileno_entry.get() == ""):
                                                messagebox.showerror(title="Getting user Details->Error",
                                                                     message="Please Make Sure To Enter All details")
                                            else:
                                                global filename
                                                global filename, img
                                                f_types = [('Png files', '*.png'), ('Jpg Files', '*.jpg')]
                                                filename = filedialog.askopenfilename(filetypes=f_types)
                                                img = ImageTk.PhotoImage(file=filename)
                                                b_1 = Button(b5, image=img)  # using Button
                                                b_1.place(x=400, y=175)  # display uploaded photo
                                                switchButtonState1()

                                        def switchButtonState12():
                                            if (mybutton2['state'] == DISABLED):
                                                mybutton2['state'] = NORMAL

                                        global filename, img

                                        def create_code():
                                            input_path = filedialog.asksaveasfilename(title="save image", filetypes=(
                                                ("PNG File", ".png"), ("All Files", "*.*")))
                                            switchButtonState12()
                                            if input_path:
                                                if input_path.endswith(".png"):
                                                    get_code = pyqrcode.create(
                                                        "BET ID:" + BETid_entry.get() + "\n" + "NAME:" + name_entry.get() + "\n" + "GENDER:" + gender.get() + "\n" + "DATE OF BIRTH:" + dob_entry.get() + "\n" + "AGE:" + age_entry.get() + "\n" + "RESIDENTIAL ADDRESS:" + Address_entry.get() + "\n" + "PINCODE:" + pincode_entry.get() + "\n" + "DISTRICT:" + district_entry.get() + "\n" + "STATE:" + state_entry.get() + "\n" + "AADHHAR NO:" + aadhar_entry.get() + "\n" + "DEPOT:" + debo.get() + "\n" + "BUS E-TICKET TYPE:" + ticket.get() + "\n" + "VALID FROM:" + valid_date_entry.get() + "\n" + "EXPIRE TILL:" + expire_date_entry.get() + "\n" + "MOBILE NO:" + mobileno_entry.get() + "\n")
                                                    # get_code.png(input_path, scale=5)
                                                    get_code.png(input_path, scale=5)
                                                    with Image.open(input_path) as img:
                                                        img_resized = img.resize((200, 200))
                                                        img_resized.save(input_path)

                                                    messagebox.showinfo(title="Generate QR-code",
                                                                        message=f"Successfully Generated QR-Code For Details \n QR code saved to {input_path}")

                                                else:
                                                    input_path = f'{input_path}.png'
                                                    get_code = pyqrcode.create(
                                                        "BET ID:" + BETid_entry.get() + "\n" + "NAME:" + name_entry.get() + "\n" + "GENDER:" + gender.get() + "\n" + "DATE OF BIRTH:" + dob_entry.get() + "\n" + "AGE:" + age_entry.get() + "\n" + "RESIDENTIAL ADDRESS:" + Address_entry.get() + "\n" + "PINCODE:" + pincode_entry.get() + "\n" + "DISTRICT:" + district_entry.get() + "\n" + "STATE:" + state_entry.get() + "\n" + "AADHHAR NO:" + aadhar_entry.get() + "\n" + "DEPOT:" + debo.get() + "\n" + "BUS E-TICKET TYPE:" + ticket.get() + "\n" + "VALID FROM:" + valid_date_entry.get() + "\n" + "EXPIRE TILL:" + expire_date_entry.get() + "\n" + "MOBILE NO:" + mobileno_entry.get() + "\n")
                                                    get_code.png(input_path, scale=5)
                                                    with Image.open(input_path) as img:
                                                        img_resized = img.resize((200, 200))
                                                        img_resized.save(input_path)

                                                    messagebox.showinfo(title="Generate QR-code",
                                                                        message=f"Successfully Generated QR-Code For Details \n QR code saved to {input_path}")

                                        def create_code1():
                                            data = BETid_entry.get()

                                            # Create QR code object
                                            qr = qrcode.QRCode(
                                                version=None,
                                                error_correction=qrcode.constants.ERROR_CORRECT_L,
                                                box_size=10,
                                                border=4,
                                            )
                                            qr.add_data(data)
                                            qr.make(fit=True)

                                            # Create QR code image with fill color and background color
                                            qr_image = qr.make_image(fill_color="yellow", back_color="magenta")

                                            # Load logo image
                                            logo_image = Image.open("windowBusIcon.png")

                                            # Resize logo image to fit inside QR code
                                            logo_size = (qr_image.size[0] // 7, qr_image.size[1] // 7)

                                            # logo_size = (qr_image.size[0] // 4, qr_image.size[1] // 4)
                                            logo_image = logo_image.resize(logo_size)

                                            # Calculate position to place logo image inside QR code
                                            logo_pos = (
                                                (qr_image.size[0] - logo_size[0]) // 2,
                                                (qr_image.size[1] - logo_size[1]) // 2)

                                            # Paste logo image onto QR code image
                                            qr_image.paste(logo_image)

                                            # Resize QR code image to 100x100 pixels
                                            qr_image = qr_image.resize((175, 175))

                                            # Get file path from user using file dialog
                                            file_path = filedialog.asksaveasfilename(title="Save QR Code",
                                                                                     filetypes=(
                                                                                     ("PNG Files", "*.png"),))

                                            # Save QR code image to file
                                            if file_path:
                                                if file_path.endswith(".png"):
                                                    qr_image.save(file_path, "PNG")
                                                    messagebox.showinfo(title="QR Code Saved",
                                                                        message=f"Successfully Generated QR-Code For BET ID \n QR code saved to {file_path}")
                                                else:
                                                    file_path = f'{file_path}.png'
                                                    qr_image.save(file_path, "PNG")
                                                    messagebox.showinfo(title="QR Code Saved",
                                                                        message=f"Successfully Generated QR-Code For BET ID \n QR code saved to {file_path}")

                                        mybutton = Button(b5, text="Generate QR-Code For Details",
                                                          font=('times', 11, 'bold'),
                                                          bg="#00ff00", state=DISABLED, command=create_code)
                                        mybutton.place(x=250, y=625)
                                        mybutton2 = Button(b5, text="Generate QR-Code for BET ID ",
                                                           font=('times', 11, 'bold'),
                                                           bg="#00ff00",
                                                           state=DISABLED, command=create_code1)
                                        mybutton2.place(x=500, y=625)

                                        def switchButtonState():
                                            if (mybutton['state'] == DISABLED):
                                                mybutton['state'] = NORMAL

                                        def add_data():  # Add data to MySQL table
                                            # upload_aadhar_card()
                                            global img, filename
                                            global img1, filename1
                                            with open("mytextfile.txt", "a") as f:
                                                f.write(BETid_entry.get() + "\n")
                                            fob2 = open(filename2, 'rb')
                                            fob2 = fob2.read()
                                            fob = open(filename, 'rb')  # filename from upload_file()
                                            fob = fob.read()
                                            fob1 = open(filename1, 'rb')
                                            fob1 = fob1.read()
                                            data = (BETid_entry.get(), name_entry.get(), Address_entry.get(),
                                                    pincode_entry.get(),
                                                    district_entry.get(), state_entry.get(), aadhar_entry.get(),
                                                    debo.get(), ticket.get(), valid_date_entry.get(),
                                                    expire_date_entry.get(),
                                                    mobileno_entry.get(), fob, age_entry.get(), fob1, gender.get(),
                                                    dob_entry.get(),
                                                    fob2)
                                            try:
                                                my_conn = create_engine(
                                                    "mysql+mysqldb://root:password123@localhost/buseticket")
                                                my_conn.execute("INSERT INTO person_details(bet_id,name,address,pincode,district,state,aadhar_no,depot,ticket_type,valid_from,expire_till,mobile_no,profile_pic,age,aadhar_card_pic,gender,date_of_birth,ReporterRjournalist_pic) \
                                                                                                                                                                      VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                                                data)
                                                switchButtonState()
                                            except:
                                                messagebox.showerror(title="Getting user Details->Error",
                                                                     message="01.Make Sure To Enter All details \n 02.Make sure that You have Entered correct details\n like BET ID,AADHAR NUMBER,MOBILE NUMBER etc")

                                        b5.mainloop()

                                    b5.mainloop()
                                elif (click1.get() == "Blind"):
                                    a1.destroy()
                                    b6 = Tk()
                                    b6.geometry("1490x745")
                                    b6.title("Getting Detail from User")
                                    icon = ImageTk.PhotoImage(file='windowBusIcon.png')
                                    b6.wm_iconphoto(False, icon)
                                    cana = Canvas(b6, width=800, height=800)
                                    cana.pack(fill="both", expand=True)
                                    img2 = Image.open("bgforwindow6.png")
                                    resize3 = img2.resize((1490, 745))
                                    new2 = ImageTk.PhotoImage(resize3)
                                    cana.create_image(0, 0, image=new2, anchor='nw')
                                    rules_photo = PhotoImage(file='Blind.png')
                                    criteria_label = Label(b6, text="Criteria & Rules To Apply Blind",
                                                           font=('times', 25, 'bold'))
                                    criteria_label.place(x=450, y=50)
                                    rules_label = Label(b6, fg='#00FF00', bg='white', relief=RAISED, bd=10, padx=0,
                                                        pady=0,
                                                        image=rules_photo, compound='top')
                                    rules_label.place(x=25, y=100)
                                    Next_button = Button(b6, text='Next', bg="green", font=('times', 14, 'bold'),
                                                         command=lambda: nextpage())
                                    Next_button.place(x=650, y=600)

                                    def nextpage():
                                        rules_label.destroy()
                                        criteria_label.destroy()
                                        Next_button.destroy()
                                        # details info
                                        name = StringVar()
                                        NAME = name.get()
                                        address1 = StringVar()
                                        ADDRESS = address1.get()
                                        age1 = StringVar()
                                        AGE = age1.get()
                                        pincode1 = StringVar()
                                        PINCODE = pincode1.get()
                                        dob1 = StringVar()
                                        DOB = dob1.get()
                                        aadhar1 = StringVar()
                                        AADHARNO = aadhar1.get()
                                        BETID = StringVar()
                                        BETid = BETID.get()
                                        district = StringVar()
                                        DISTRICT = district.get()
                                        state = StringVar()
                                        STATE = state.get()
                                        valid_date = StringVar()
                                        VALID_DATE = valid_date.get()
                                        expire_date = StringVar()
                                        EXPIRE_DATE = expire_date.get()
                                        disability1 = StringVar()
                                        DISABILITY_PERCENTAGE = disability1.get()
                                        mobile1 = StringVar()
                                        MOBILE = mobile1.get()

                                        def my_command():
                                            b6.destroy()
                                            HOME_BUTTON_PAGE()

                                        click_btn = PhotoImage(file='Small_Home_ Icon.png')
                                        button = Button(b6, image=click_btn, command=my_command)
                                        button.place(x=30, y=25)

                                        def my_command1():
                                            b6.destroy()
                                            CREATE_BET_PAGE()

                                        click_btn1 = PhotoImage(file='small_back_icon.png')
                                        button1 = Button(b6, image=click_btn1, command=my_command1)
                                        button1.place(x=95, y=25)
                                        font = Label(b6, text="Create your Bus E-Ticket", font=('Arial', 22, 'bold'),
                                                     bg="#b3ffff")
                                        font.place(x=200, y=25)
                                        BETid_label = Label(b6, text="BET id", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        BETid_label.place(x=50, y=100)
                                        BETid_entry = Entry(b6, textvariable=BETid, width=35)
                                        BETid_entry.place(x=175, y=100, width=100)
                                        name = Label(b6, text="Name", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        name.place(x=50, y=150)
                                        name_entry = Entry(b6, textvariable=NAME, width=35)
                                        name_entry.place(x=175, y=150, width=100)
                                        Address = Label(b6, text="Address", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        Address.place(x=50, y=200)
                                        Address_entry = Entry(b6, textvariable=ADDRESS, width=35)
                                        Address_entry.place(x=175, y=200, width=100)
                                        pincode = Label(b6, text="Pincode", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        pincode.place(x=50, y=250)
                                        pincode_entry = Entry(b6, textvariable=PINCODE, width=35)
                                        pincode_entry.place(x=175, y=250, width=100)
                                        district_label = Label(b6, text="District", font=('Arial', 15, 'bold'),
                                                               bg="#ffff4d")
                                        district_label.place(x=50, y=300)
                                        district_entry = Entry(b6, textvariable=DISTRICT, width=35)
                                        district_entry.place(x=175, y=300, width=100)
                                        state = Label(b6, text="State", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        state.place(x=50, y=350)
                                        state_entry = Entry(b6, textvariable=STATE, width=35)
                                        state_entry.place(x=175, y=350, width=100)
                                        aadhar = Label(b6, text="Aadhar No", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        aadhar.place(x=50, y=400)
                                        aadhar_entry = Entry(b6, textvariable=AADHARNO, width=35)
                                        aadhar_entry.place(x=175, y=400, width=100)
                                        disability_label = Label(b6, text="Disability(%)", font=('Arial', 15, 'bold'),
                                                                 bg="#ffff4d")
                                        disability_label.place(x=700, y=50)
                                        disability_entry = Entry(b6, textvariable=DISABILITY_PERCENTAGE, width=35)
                                        disability_entry.place(x=850, y=50, width=100)
                                        valid_date_label = Label(b6, text="Valid From", font=('Arial', 15, 'bold'),
                                                                 bg="#ffff4d")
                                        valid_date_label.place(x=700, y=100)
                                        valid_date_entry = Entry(b6, textvariable=VALID_DATE, width=35)
                                        valid_date_entry.place(x=850, y=100, width=100)
                                        expire_date_label = Label(b6, text="Expire Till", font=('Arial', 15, 'bold'),
                                                                  bg="#ffff4d")
                                        expire_date_label.place(x=700, y=150)
                                        expire_date_entry = Entry(b6, textvariable=EXPIRE_DATE, width=35)
                                        expire_date_entry.place(x=850, y=150, width=100)
                                        mobileno = Label(b6, text="Mobile No", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        mobileno.place(x=700, y=200)
                                        mobileno_entry = Entry(b6, textvariable=MOBILE, width=35)
                                        mobileno_entry.place(x=850, y=200, width=100)
                                        gender_label = Label(b6, text="Gender", font=('Arial', 15, 'bold'),
                                                             bg="#ffff4d")
                                        gender_label.place(x=700, y=250)
                                        gender_options = ["Male", "Female", "Transgender"]
                                        gender = StringVar()
                                        gender.set("Select")
                                        gender1 = OptionMenu(b6, gender, *gender_options)
                                        gender1.place(x=850, y=250)
                                        dob_label = Label(b6, text="Date of Birth", font=('Arial', 15, 'bold'),
                                                          bg="#ffff4d")
                                        dob_label.place(x=700, y=300)
                                        dob_entry = Entry(b6, textvariable=DOB, width=35)
                                        dob_entry.place(x=850, y=300, width=100)
                                        upload_aadhar_button = Button(b6, text='Upload Aadhar Card',
                                                                      font=('times', 14, 'bold'),
                                                                      command=lambda: upload_aadhar_card(),
                                                                      state=DISABLED)
                                        upload_aadhar_button.place(x=900, y=400)
                                        upload_RJ_button = Button(b6, text='Upload Disability ID Proof Issued By DRO ',
                                                                  font=('times', 14, 'bold'),
                                                                  command=lambda: Upload_disability_proof())
                                        upload_RJ_button.place(x=900, y=350)

                                        def switchButtonState2():
                                            if (upload_photo_button['state'] == DISABLED):
                                                upload_photo_button['state'] = NORMAL

                                        def switchButtonState20():
                                            if (upload_aadhar_button['state'] == DISABLED):
                                                upload_aadhar_button['state'] = NORMAL

                                        global filename1

                                        def upload_aadhar_card():
                                            global filename1
                                            global filename1, img1
                                            f_types = [('Png files', '*.png'), ('Jpg Files', '*.jpg')]
                                            filename1 = filedialog.askopenfilename(filetypes=f_types)
                                            img1 = ImageTk.PhotoImage(file=filename1)
                                            messagebox.showinfo(title="Details Info",
                                                                message="Successfully uploaded your Aadhar Card")
                                            switchButtonState2()

                                        global filename1, img1
                                        global filename1

                                        def Upload_disability_proof():
                                            global filename2
                                            global filename2, img2
                                            f_types = [('Png files', '*.png'), ('Jpg Files', '*.jpg')]
                                            filename2 = filedialog.askopenfilename(filetypes=f_types)
                                            img2 = ImageTk.PhotoImage(file=filename2)
                                            messagebox.showinfo(title="Details Info",
                                                                message="Successfully uploaded your Disability ID Proof Issued By DRO")
                                            switchButtonState20()

                                        global filename2, img2
                                        debo_label = Label(b6, text="Depot", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        debo_label.place(x=50, y=450)
                                        debo_options = ["Adyar", "Ambathur Industrial Estate", " Ambathur OT",
                                                        " Anna Nagar (West)",
                                                        "Avadi", "Ayanavaram", "Broadway", "C.M.B.T",
                                                        "Central Rly station",
                                                        "Guindy Industrial Estate", "Iyyappanthangal", "K.K.Nagar",
                                                        "M.K.B.Nagar",
                                                        "Mandaveli", "Pallavaram", "Perambur", "Poonamallee",
                                                        "Redhills", "Saidapet",
                                                        "Sriperumbathur", "T.Nagar", "Tambaram (West)", "Thiruvanmiyur",
                                                        "Thiruvotriyur", "Tondiarpet", "Vadapalani", " Vallalar Nagar",
                                                        "Velachery",
                                                        "Villivakkam"]
                                        debo = StringVar()
                                        debo.set("Select")
                                        debo1 = OptionMenu(b6, debo, *debo_options)
                                        debo1.place(x=175, y=450)
                                        ticket_label = Label(b6, text="Ticket Type", font=('Arial', 15, 'bold'),
                                                             bg="#ffff4d")
                                        ticket_label.place(x=50, y=500)
                                        Ticket_options = ["Blind"]
                                        ticket = StringVar()
                                        ticket.set("Select")
                                        Ticket1 = OptionMenu(b6, ticket, *Ticket_options)
                                        Ticket1.place(x=175, y=500)
                                        age = Label(b6, text="Age", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        age.place(x=50, y=550)
                                        age_entry = Entry(b6, textvariable=AGE, width=35)
                                        age_entry.place(x=175, y=550, width=100)
                                        upload_photo_button = Button(b6, text='Upload photo',
                                                                     font=('times', 14, 'bold'),
                                                                     command=lambda: upload_file(), state=DISABLED)
                                        upload_photo_button.place(x=400, y=125)
                                        upload_data_button = Button(b6, text='Upload data', font=('times', 16, 'bold'),
                                                                    bg="#00ffbf",
                                                                    command=lambda: add_data(), state=DISABLED)
                                        upload_data_button.place(x=75, y=625)

                                        def switchButtonState1():
                                            if (upload_data_button['state'] == DISABLED):
                                                upload_data_button['state'] = NORMAL

                                        global filename

                                        def upload_file():
                                            if (disability_entry.get() > '40'):
                                                if (
                                                        BETid_entry.get() == "" or disability_entry.get() == "" or name_entry.get() == "" or gender.get() == "Select" or dob_entry.get() == "" or Address_entry.get() == "" or pincode_entry.get() == "" or district_entry.get() == "" or state_entry.get() == "" or aadhar_entry.get() == "" or debo.get() == "Select" or ticket.get() == "Select" or valid_date_entry.get() == "" or expire_date_entry.get() == "" or age_entry.get() == "" or mobileno_entry.get() == ""):
                                                    messagebox.showerror(title="Getting user Details->Error",
                                                                         message="Please Make Sure To Enter All details")
                                                else:
                                                    global filename
                                                    global filename, img
                                                    f_types = [('Png files', '*.png'), ('Jpg Files', '*.jpg')]
                                                    filename = filedialog.askopenfilename(filetypes=f_types)
                                                    img = ImageTk.PhotoImage(file=filename)
                                                    b_1 = Button(b6, image=img)  # using Button
                                                    b_1.place(x=400, y=175)  # display uploaded photo
                                                    switchButtonState1()
                                            else:
                                                messagebox.showerror(title="Getting user Details->Error",
                                                                     message="Sorry,The Disability Should Be More Than 40%")

                                        def switchButtonState12():
                                            if (mybutton2['state'] == DISABLED):
                                                mybutton2['state'] = NORMAL

                                        global filename, img

                                        def create_code():
                                            input_path = filedialog.asksaveasfilename(title="save image", filetypes=(
                                                ("PNG File", ".png"), ("All Files", "*.*")))
                                            switchButtonState12()
                                            if input_path:
                                                if input_path.endswith(".png"):
                                                    get_code = pyqrcode.create(
                                                        "BET ID:" + BETid_entry.get() + "\n" + "NAME:" + name_entry.get() + "\n" + "GENDER:" + gender.get() + "\n" + "DATE OF BIRTH:" + dob_entry.get() + "\n" + "AGE:" + age_entry.get() + "\n" + "RESIDENTIAL ADDRESS:" + Address_entry.get() + "\n" + "PINCODE:" + pincode_entry.get() + "\n" + "DISTRICT:" + district_entry.get() + "\n" + "STATE:" + state_entry.get() + "\n" + "AADHHAR NO:" + aadhar_entry.get() + "\n" + "DEPOT:" + debo.get() + "\n" + "BUS E-TICKET TYPE:" + ticket.get() + "\n" + "DISABILITY PERCENTAGE:" + disability_entry.get() + "\n" + "VALID FROM:" + valid_date_entry.get() + "\n" + "EXPIRE TILL:" + expire_date_entry.get() + "\n" + "MOBILE NO:" + mobileno_entry.get() + "\n")
                                                    # get_code.png(input_path, scale=5)
                                                    get_code.png(input_path, scale=5)
                                                    with Image.open(input_path) as img:
                                                        img_resized = img.resize((200, 200))
                                                        img_resized.save(input_path)

                                                    messagebox.showinfo(title="Generate QR-code",
                                                                        message=f"Successfully Generated QR-Code For Details \n QR code saved to {input_path}")

                                                else:
                                                    input_path = f'{input_path}.png'
                                                    get_code = pyqrcode.create(
                                                        "BET ID:" + BETid_entry.get() + "\n" + "NAME:" + name_entry.get() + "\n" + "GENDER:" + gender.get() + "\n" + "DATE OF BIRTH:" + dob_entry.get() + "\n" + "AGE:" + age_entry.get() + "\n" + "RESIDENTIAL ADDRESS:" + Address_entry.get() + "\n" + "PINCODE:" + pincode_entry.get() + "\n" + "DISTRICT:" + district_entry.get() + "\n" + "STATE:" + state_entry.get() + "\n" + "AADHHAR NO:" + aadhar_entry.get() + "\n" + "DEPOT:" + debo.get() + "\n" + "BUS E-TICKET TYPE:" + ticket.get() + "\n" + "DISABILITY PERCENTAGE:" + disability_entry.get() + "\n" + "VALID FROM:" + valid_date_entry.get() + "\n" + "EXPIRE TILL:" + expire_date_entry.get() + "\n" + "MOBILE NO:" + mobileno_entry.get() + "\n")
                                                    get_code.png(input_path, scale=5)
                                                    with Image.open(input_path) as img:
                                                        img_resized = img.resize((200, 200))
                                                        img_resized.save(input_path)

                                                    messagebox.showinfo(title="Generate QR-code",
                                                                        message=f"Successfully Generated QR-Code For Details \n QR code saved to {input_path}")

                                        def create_code1():
                                            data = BETid_entry.get()

                                            # Create QR code object
                                            qr = qrcode.QRCode(
                                                version=None,
                                                error_correction=qrcode.constants.ERROR_CORRECT_L,
                                                box_size=10,
                                                border=4,
                                            )
                                            qr.add_data(data)
                                            qr.make(fit=True)

                                            # Create QR code image with fill color and background color
                                            qr_image = qr.make_image(fill_color="green", back_color="#ccccff")

                                            # Load logo image
                                            logo_image = Image.open("windowBusIcon.png")

                                            # Resize logo image to fit inside QR code
                                            logo_size = (qr_image.size[0] // 7, qr_image.size[1] // 7)

                                            # logo_size = (qr_image.size[0] // 4, qr_image.size[1] // 4)
                                            logo_image = logo_image.resize(logo_size)

                                            # Calculate position to place logo image inside QR code
                                            logo_pos = (
                                                (qr_image.size[0] - logo_size[0]) // 2,
                                                (qr_image.size[1] - logo_size[1]) // 2)

                                            # Paste logo image onto QR code image
                                            qr_image.paste(logo_image)

                                            # Resize QR code image to 100x100 pixels
                                            qr_image = qr_image.resize((175, 175))

                                            # Get file path from user using file dialog
                                            file_path = filedialog.asksaveasfilename(title="Save QR Code",
                                                                                     filetypes=(
                                                                                     ("PNG Files", "*.png"),))

                                            # Save QR code image to file
                                            if file_path:
                                                if file_path.endswith(".png"):
                                                    qr_image.save(file_path, "PNG")
                                                    messagebox.showinfo(title="QR Code Saved",
                                                                        message=f"Successfully Generated QR-Code For BET ID \n QR code saved to {file_path}")
                                                else:
                                                    file_path = f'{file_path}.png'
                                                    qr_image.save(file_path, "PNG")
                                                    messagebox.showinfo(title="QR Code Saved",
                                                                        message=f"Successfully Generated QR-Code For BET ID \n QR code saved to {file_path}")

                                        mybutton = Button(b6, text="Generate QR-Code For Details",
                                                          font=('times', 11, 'bold'),
                                                          bg="#00ff00", state=DISABLED, command=create_code)
                                        mybutton.place(x=250, y=625)
                                        mybutton2 = Button(b6, text="Generate QR-Code for BET ID ",
                                                           font=('times', 11, 'bold'),
                                                           bg="#00ff00",
                                                           state=DISABLED, command=create_code1)
                                        mybutton2.place(x=500, y=625)

                                        def switchButtonState():
                                            if (mybutton['state'] == DISABLED):
                                                mybutton['state'] = NORMAL

                                        def add_data():  # Add data to MySQL table
                                            # upload_aadhar_card()
                                            global img, filename
                                            global img1, filename1
                                            with open("mytextfile.txt", "a") as f:
                                                f.write(BETid_entry.get() + "\n")
                                            fob2 = open(filename2, 'rb')
                                            fob2 = fob2.read()
                                            fob = open(filename, 'rb')  # filename from upload_file()
                                            fob = fob.read()
                                            fob1 = open(filename1, 'rb')
                                            fob1 = fob1.read()
                                            data = (BETid_entry.get(), name_entry.get(), Address_entry.get(),
                                                    pincode_entry.get(),
                                                    district_entry.get(), state_entry.get(), aadhar_entry.get(),
                                                    debo.get(), ticket.get(), valid_date_entry.get(),
                                                    expire_date_entry.get(),
                                                    mobileno_entry.get(), fob, age_entry.get(), fob1, gender.get(),
                                                    dob_entry.get(),
                                                    fob2, disability_entry.get())
                                            try:
                                                my_conn = create_engine(
                                                    "mysql+mysqldb://root:password123@localhost/buseticket")
                                                my_conn.execute("INSERT INTO person_details(bet_id,name,address,pincode,district,state,aadhar_no,depot,ticket_type,valid_from,expire_till,mobile_no,profile_pic,age,aadhar_card_pic,gender,date_of_birth,ReporterRjournalist_pic,disability_percentage) \
                                                                                                                                                                      VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                                                data)
                                                switchButtonState()
                                            except:
                                                messagebox.showerror(title="Getting user Details->Error",
                                                                     message="01.Make Sure To Enter All details \n 02.Make sure that You have Entered correct details\n like BET ID,AADHAR NUMBER,MOBILE NUMBER etc")

                                        b6.mainloop()

                                    b6.mainloop()
                                elif (click1.get() == "Handicapped/Mentally Retarded"):
                                    a1.destroy()
                                    b7 = Tk()
                                    b7.geometry("1490x745")
                                    b7.title("Getting Detail from User")
                                    icon = ImageTk.PhotoImage(file='windowBusIcon.png')
                                    b7.wm_iconphoto(False, icon)
                                    cana = Canvas(b7, width=800, height=800)
                                    cana.pack(fill="both", expand=True)
                                    img2 = Image.open("bgforwindow6.png")
                                    resize3 = img2.resize((1490, 745))
                                    new2 = ImageTk.PhotoImage(resize3)
                                    cana.create_image(0, 0, image=new2, anchor='nw')
                                    rules_photo = PhotoImage(file='Handicapped&Mentally.png')
                                    criteria_label = Label(b7,
                                                           text="Criteria & Rules To Apply Handicapped/Mentally Retarded",
                                                           font=('times', 25, 'bold'))
                                    criteria_label.place(x=330, y=50)
                                    rules_label = Label(b7, fg='#00FF00', bg='white', relief=RAISED, bd=10, padx=0,
                                                        pady=0,
                                                        image=rules_photo, compound='top')
                                    rules_label.place(x=25, y=100)
                                    Next_button = Button(b7, text='Next', bg="green", font=('times', 14, 'bold'),
                                                         command=lambda: nextpage())
                                    Next_button.place(x=650, y=600)

                                    def nextpage():
                                        rules_label.destroy()
                                        criteria_label.destroy()
                                        Next_button.destroy()
                                        # details info
                                        name = StringVar()
                                        NAME = name.get()
                                        address1 = StringVar()
                                        Gname = StringVar()
                                        GNAME = Gname.get()
                                        ADDRESS = address1.get()
                                        age1 = StringVar()
                                        AGE = age1.get()
                                        pincode1 = StringVar()
                                        PINCODE = pincode1.get()
                                        dob1 = StringVar()
                                        DOB = dob1.get()
                                        aadhar1 = StringVar()
                                        AADHARNO = aadhar1.get()
                                        BETID = StringVar()
                                        BETid = BETID.get()
                                        district = StringVar()
                                        DISTRICT = district.get()
                                        state = StringVar()
                                        STATE = state.get()
                                        valid_date = StringVar()
                                        VALID_DATE = valid_date.get()
                                        expire_date = StringVar()
                                        EXPIRE_DATE = expire_date.get()
                                        disability1 = StringVar()
                                        DISABILITY_PERCENTAGE = disability1.get()
                                        mobile1 = StringVar()
                                        MOBILE = mobile1.get()

                                        def my_command():
                                            b7.destroy()
                                            HOME_BUTTON_PAGE()

                                        click_btn = PhotoImage(file='Small_Home_ Icon.png')
                                        button = Button(b7, image=click_btn, command=my_command)
                                        button.place(x=30, y=25)

                                        def my_command1():
                                            b7.destroy()
                                            CREATE_BET_PAGE()

                                        click_btn1 = PhotoImage(file='small_back_icon.png')
                                        button1 = Button(b7, image=click_btn1, command=my_command1)
                                        button1.place(x=95, y=25)
                                        font = Label(b7, text="Create your Bus E-Ticket", font=('Arial', 22, 'bold'),
                                                     bg="#b3ffff")
                                        font.place(x=200, y=25)
                                        BETid_label = Label(b7, text="BET id", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        BETid_label.place(x=50, y=100)
                                        BETid_entry = Entry(b7, textvariable=BETid, width=35)
                                        BETid_entry.place(x=175, y=100, width=100)
                                        name = Label(b7, text="Name", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        name.place(x=50, y=150)
                                        name_entry = Entry(b7, textvariable=NAME, width=35)
                                        name_entry.place(x=175, y=150, width=100)
                                        Address = Label(b7, text="Address", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        Address.place(x=50, y=200)
                                        Address_entry = Entry(b7, textvariable=ADDRESS, width=35)
                                        Address_entry.place(x=175, y=200, width=100)
                                        pincode = Label(b7, text="Pincode", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        pincode.place(x=50, y=250)
                                        pincode_entry = Entry(b7, textvariable=PINCODE, width=35)
                                        pincode_entry.place(x=175, y=250, width=100)
                                        district_label = Label(b7, text="District", font=('Arial', 15, 'bold'),
                                                               bg="#ffff4d")
                                        district_label.place(x=50, y=300)
                                        district_entry = Entry(b7, textvariable=DISTRICT, width=35)
                                        district_entry.place(x=175, y=300, width=100)
                                        state = Label(b7, text="State", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        state.place(x=50, y=350)
                                        state_entry = Entry(b7, textvariable=STATE, width=35)
                                        state_entry.place(x=175, y=350, width=100)
                                        aadhar = Label(b7, text="Aadhar No", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        aadhar.place(x=50, y=400)
                                        aadhar_entry = Entry(b7, textvariable=AADHARNO, width=35)
                                        aadhar_entry.place(x=175, y=400, width=100)
                                        disability_label = Label(b7, text="Disability(%)", font=('Arial', 15, 'bold'),
                                                                 bg="#ffff4d")
                                        disability_label.place(x=700, y=50)
                                        disability_entry = Entry(b7, textvariable=DISABILITY_PERCENTAGE, width=35)
                                        disability_entry.place(x=850, y=50, width=100)
                                        valid_date_label = Label(b7, text="Valid From", font=('Arial', 15, 'bold'),
                                                                 bg="#ffff4d")
                                        valid_date_label.place(x=700, y=100)
                                        valid_date_entry = Entry(b7, textvariable=VALID_DATE, width=35)
                                        valid_date_entry.place(x=850, y=100, width=100)
                                        expire_date_label = Label(b7, text="Expire Till", font=('Arial', 15, 'bold'),
                                                                  bg="#ffff4d")
                                        expire_date_label.place(x=700, y=150)
                                        expire_date_entry = Entry(b7, textvariable=EXPIRE_DATE, width=35)
                                        expire_date_entry.place(x=850, y=150, width=100)
                                        mobileno = Label(b7, text="Mobile No", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        mobileno.place(x=700, y=200)
                                        mobileno_entry = Entry(b7, textvariable=MOBILE, width=35)
                                        mobileno_entry.place(x=850, y=200, width=100)
                                        gender_label = Label(b7, text="Gender", font=('Arial', 15, 'bold'),
                                                             bg="#ffff4d")
                                        gender_label.place(x=700, y=250)
                                        gender_options = ["Male", "Female", "Transgender"]
                                        gender = StringVar()
                                        gender.set("Select")
                                        gender1 = OptionMenu(b7, gender, *gender_options)
                                        gender1.place(x=850, y=250)
                                        dob_label = Label(b7, text="Date of Birth", font=('Arial', 15, 'bold'),
                                                          bg="#ffff4d")
                                        dob_label.place(x=700, y=300)
                                        dob_entry = Entry(b7, textvariable=DOB, width=35)
                                        dob_entry.place(x=850, y=300, width=100)

                                        gname_label = Label(b7, text="Attendant Name", font=('Arial', 15, 'bold'),
                                                            bg="#ffff4d")
                                        gname_label.place(x=700, y=350)
                                        gname_entry = Entry(b7, textvariable=GNAME, width=35)
                                        gname_entry.place(x=875, y=350, width=100)
                                        upload_aadhar_button = Button(b7, text='Upload Aadhar Card',
                                                                      font=('times', 14, 'bold'),
                                                                      command=lambda: upload_aadhar_card(),
                                                                      state=DISABLED)
                                        upload_aadhar_button.place(x=900, y=500)
                                        upload_RJ_button = Button(b7, text='Upload Disability ID Proof Issued By DRO ',
                                                                  font=('times', 14, 'bold'),
                                                                  command=lambda: Upload_Handicapped_Mentally_Retarded_proof(),
                                                                  state=DISABLED)
                                        upload_RJ_button.place(x=900, y=450)
                                        upload_guardian_button = Button(b7, text='Upload Attendant Photo',
                                                                        font=('times', 14, 'bold'),
                                                                        command=lambda: upload_guardian())
                                        upload_guardian_button.place(x=900, y=400)

                                        def switchButtonState22():
                                            if (upload_RJ_button['state'] == DISABLED):
                                                upload_RJ_button['state'] = NORMAL

                                        def upload_guardian():
                                            global filename3
                                            global filename3, img3
                                            f_types = [('Png files', '*.png'), ('Jpg Files', '*.jpg')]
                                            filename3 = filedialog.askopenfilename(filetypes=f_types)
                                            img3 = ImageTk.PhotoImage(file=filename3)
                                            messagebox.showinfo(title="Details Info",
                                                                message="Successfully uploaded your Attendant Photo")
                                            switchButtonState22()

                                        global filename3, img3
                                        global filename3

                                        def switchButtonState2():
                                            if (upload_photo_button['state'] == DISABLED):
                                                upload_photo_button['state'] = NORMAL

                                        def switchButtonState20():
                                            if (upload_aadhar_button['state'] == DISABLED):
                                                upload_aadhar_button['state'] = NORMAL

                                        global filename1

                                        def upload_aadhar_card():
                                            global filename1
                                            global filename1, img1
                                            f_types = [('Png files', '*.png'), ('Jpg Files', '*.jpg')]
                                            filename1 = filedialog.askopenfilename(filetypes=f_types)
                                            img1 = ImageTk.PhotoImage(file=filename1)
                                            messagebox.showinfo(title="Details Info",
                                                                message="Successfully uploaded your Aadhar Card")
                                            switchButtonState2()

                                        global filename1, img1
                                        global filename1

                                        def Upload_Handicapped_Mentally_Retarded_proof():
                                            global filename2
                                            global filename2, img2
                                            f_types = [('Png files', '*.png'), ('Jpg Files', '*.jpg')]
                                            filename2 = filedialog.askopenfilename(filetypes=f_types)
                                            img2 = ImageTk.PhotoImage(file=filename2)
                                            messagebox.showinfo(title="Details Info",
                                                                message="Successfully uploaded your Disability ID Proof Issued By DRO")
                                            switchButtonState20()

                                        global filename2, img2
                                        debo_label = Label(b7, text="Depot", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        debo_label.place(x=50, y=450)
                                        debo_options = ["Adyar", "Ambathur Industrial Estate", " Ambathur OT",
                                                        " Anna Nagar (West)",
                                                        "Avadi", "Ayanavaram", "Broadway", "C.M.B.T",
                                                        "Central Rly station",
                                                        "Guindy Industrial Estate", "Iyyappanthangal", "K.K.Nagar",
                                                        "M.K.B.Nagar",
                                                        "Mandaveli", "Pallavaram", "Perambur", "Poonamallee",
                                                        "Redhills", "Saidapet",
                                                        "Sriperumbathur", "T.Nagar", "Tambaram (West)", "Thiruvanmiyur",
                                                        "Thiruvotriyur", "Tondiarpet", "Vadapalani", " Vallalar Nagar",
                                                        "Velachery",
                                                        "Villivakkam"]
                                        debo = StringVar()
                                        debo.set("Select")
                                        debo1 = OptionMenu(b7, debo, *debo_options)
                                        debo1.place(x=175, y=450)
                                        ticket_label = Label(b7, text="Ticket Type", font=('Arial', 15, 'bold'),
                                                             bg="#ffff4d")
                                        ticket_label.place(x=50, y=500)
                                        Ticket_options = ["Handicapped/Mentally Retarded"]
                                        ticket = StringVar()
                                        ticket.set("Select")
                                        Ticket1 = OptionMenu(b7, ticket, *Ticket_options)
                                        Ticket1.place(x=175, y=500)
                                        age = Label(b7, text="Age", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        age.place(x=50, y=550)
                                        age_entry = Entry(b7, textvariable=AGE, width=35)
                                        age_entry.place(x=175, y=550, width=100)
                                        upload_photo_button = Button(b7, text='Upload photo',
                                                                     font=('times', 14, 'bold'),
                                                                     command=lambda: upload_file(), state=DISABLED)
                                        upload_photo_button.place(x=400, y=125)
                                        upload_data_button = Button(b7, text='Upload data', font=('times', 16, 'bold'),
                                                                    bg="#00ffbf",
                                                                    command=lambda: add_data(), state=DISABLED)
                                        upload_data_button.place(x=75, y=625)

                                        def switchButtonState1():
                                            if (upload_data_button['state'] == DISABLED):
                                                upload_data_button['state'] = NORMAL

                                        global filename

                                        def upload_file():
                                            if (disability_entry.get() > '40'):
                                                if (
                                                        BETid_entry.get() == "" or gname_entry.get() == "" or disability_entry.get() == "" or name_entry.get() == "" or gender.get() == "Select" or dob_entry.get() == "" or Address_entry.get() == "" or pincode_entry.get() == "" or district_entry.get() == "" or state_entry.get() == "" or aadhar_entry.get() == "" or debo.get() == "Select" or ticket.get() == "Select" or valid_date_entry.get() == "" or expire_date_entry.get() == "" or age_entry.get() == "" or mobileno_entry.get() == ""):
                                                    messagebox.showerror(title="Getting user Details->Error",
                                                                         message="Please Make Sure To Enter All details")
                                                else:
                                                    global filename
                                                    global filename, img
                                                    f_types = [('Png files', '*.png'), ('Jpg Files', '*.jpg')]
                                                    filename = filedialog.askopenfilename(filetypes=f_types)
                                                    img = ImageTk.PhotoImage(file=filename)
                                                    b_1 = Button(b7, image=img)  # using Button
                                                    b_1.place(x=400, y=175)  # display uploaded photo
                                                    switchButtonState1()
                                            else:
                                                messagebox.showerror(title="Getting user Details->Error",
                                                                     message="Sorry,The Disability Should Be More Than 40%")

                                        def switchButtonState12():
                                            if (mybutton2['state'] == DISABLED):
                                                mybutton2['state'] = NORMAL

                                        global filename, img

                                        def create_code():
                                            input_path = filedialog.asksaveasfilename(title="save image", filetypes=(
                                                ("PNG File", ".png"), ("All Files", "*.*")))
                                            switchButtonState12()
                                            if input_path:
                                                if input_path.endswith(".png"):
                                                    get_code = pyqrcode.create(
                                                        "BET ID:" + BETid_entry.get() + "\n" + "NAME:" + name_entry.get() + "\n" + "GENDER:" + gender.get() + "\n" + "DATE OF BIRTH:" + dob_entry.get() + "\n" + "AGE:" + age_entry.get() + "\n" + "RESIDENTIAL ADDRESS:" + Address_entry.get() + "\n" + "PINCODE:" + pincode_entry.get() + "\n" + "DISTRICT:" + district_entry.get() + "\n" + "STATE:" + state_entry.get() + "\n" + "AADHHAR NO:" + aadhar_entry.get() + "\n" + "DEPOT:" + debo.get() + "\n" + "BUS E-TICKET TYPE:" + ticket.get() + "\n" + "DISABILITY PERCENTAGE:" + disability_entry.get() + "\n" + "ATTENDANT NAME:" + gname_entry.get() + "\n" + "VALID FROM:" + valid_date_entry.get() + "\n" + "EXPIRE TILL:" + expire_date_entry.get() + "\n" + "MOBILE NO:" + mobileno_entry.get() + "\n")
                                                    # get_code.png(input_path, scale=5)
                                                    get_code.png(input_path, scale=5)
                                                    with Image.open(input_path) as img:
                                                        img_resized = img.resize((200, 200))
                                                        img_resized.save(input_path)

                                                    messagebox.showinfo(title="Generate QR-code",
                                                                        message=f"Successfully Generated QR-Code For Details \n QR code saved to {input_path}")

                                                else:
                                                    input_path = f'{input_path}.png'
                                                    get_code = pyqrcode.create(
                                                        "BET ID:" + BETid_entry.get() + "\n" + "NAME:" + name_entry.get() + "\n" + "GENDER:" + gender.get() + "\n" + "DATE OF BIRTH:" + dob_entry.get() + "\n" + "AGE:" + age_entry.get() + "\n" + "RESIDENTIAL ADDRESS:" + Address_entry.get() + "\n" + "PINCODE:" + pincode_entry.get() + "\n" + "DISTRICT:" + district_entry.get() + "\n" + "STATE:" + state_entry.get() + "\n" + "AADHHAR NO:" + aadhar_entry.get() + "\n" + "DEPOT:" + debo.get() + "\n" + "BUS E-TICKET TYPE:" + ticket.get() + "\n" + "DISABILITY PERCENTAGE:" + disability_entry.get() + "\n" + "ATTENDANT NAME:" + gname_entry.get() + "\n" + "VALID FROM:" + valid_date_entry.get() + "\n" + "EXPIRE TILL:" + expire_date_entry.get() + "\n" + "MOBILE NO:" + mobileno_entry.get() + "\n")
                                                    get_code.png(input_path, scale=5)
                                                    with Image.open(input_path) as img:
                                                        img_resized = img.resize((200, 200))
                                                        img_resized.save(input_path)

                                                    messagebox.showinfo(title="Generate QR-code",
                                                                        message=f"Successfully Generated QR-Code For Details \n QR code saved to {input_path}")

                                        def create_code1():
                                            data = BETid_entry.get()

                                            # Create QR code object
                                            qr = qrcode.QRCode(
                                                version=None,
                                                error_correction=qrcode.constants.ERROR_CORRECT_L,
                                                box_size=10,
                                                border=4,
                                            )
                                            qr.add_data(data)
                                            qr.make(fit=True)

                                            # Create QR code image with fill color and background color
                                            qr_image = qr.make_image(fill_color="green", back_color="#7575a3")

                                            # Load logo image
                                            logo_image = Image.open("windowBusIcon.png")

                                            # Resize logo image to fit inside QR code
                                            logo_size = (qr_image.size[0] // 7, qr_image.size[1] // 7)

                                            # logo_size = (qr_image.size[0] // 4, qr_image.size[1] // 4)
                                            logo_image = logo_image.resize(logo_size)

                                            # Calculate position to place logo image inside QR code
                                            logo_pos = (
                                                (qr_image.size[0] - logo_size[0]) // 2,
                                                (qr_image.size[1] - logo_size[1]) // 2)

                                            # Paste logo image onto QR code image
                                            qr_image.paste(logo_image)

                                            # Resize QR code image to 100x100 pixels
                                            qr_image = qr_image.resize((175, 175))

                                            # Get file path from user using file dialog
                                            file_path = filedialog.asksaveasfilename(title="Save QR Code",
                                                                                     filetypes=(
                                                                                     ("PNG Files", "*.png"),))

                                            # Save QR code image to file
                                            if file_path:
                                                if file_path.endswith(".png"):
                                                    qr_image.save(file_path, "PNG")
                                                    messagebox.showinfo(title="QR Code Saved",
                                                                        message=f"Successfully Generated QR-Code For BET ID \n QR code saved to {file_path}")
                                                else:
                                                    file_path = f'{file_path}.png'
                                                    qr_image.save(file_path, "PNG")
                                                    messagebox.showinfo(title="QR Code Saved",
                                                                        message=f"Successfully Generated QR-Code For BET ID \n QR code saved to {file_path}")

                                        mybutton = Button(b7, text="Generate QR-Code For Details",
                                                          font=('times', 11, 'bold'),
                                                          bg="#00ff00", state=DISABLED, command=create_code)
                                        mybutton.place(x=250, y=625)
                                        mybutton2 = Button(b7, text="Generate QR-Code for BET ID ",
                                                           font=('times', 11, 'bold'),
                                                           bg="#00ff00",
                                                           state=DISABLED, command=create_code1)
                                        mybutton2.place(x=500, y=625)

                                        def switchButtonState():
                                            if (mybutton['state'] == DISABLED):
                                                mybutton['state'] = NORMAL

                                        def add_data():  # Add data to MySQL table
                                            # upload_aadhar_card()
                                            global img, filename
                                            global img1, filename1
                                            global img3, filename3

                                            with open("mytextfile.txt", "a") as f:
                                                f.write(BETid_entry.get() + "\n")
                                            fob3 = open(filename3, 'rb')
                                            fob3 = fob3.read()
                                            fob2 = open(filename2, 'rb')
                                            fob2 = fob2.read()
                                            fob = open(filename, 'rb')  # filename from upload_file()
                                            fob = fob.read()
                                            fob1 = open(filename1, 'rb')
                                            fob1 = fob1.read()
                                            data = (BETid_entry.get(), name_entry.get(), Address_entry.get(),
                                                    pincode_entry.get(),
                                                    district_entry.get(), state_entry.get(), aadhar_entry.get(),
                                                    debo.get(), ticket.get(), valid_date_entry.get(),
                                                    expire_date_entry.get(),
                                                    mobileno_entry.get(), fob, age_entry.get(), fob1, gender.get(),
                                                    dob_entry.get(),
                                                    fob2, disability_entry.get(), fob3, gname_entry.get())
                                            try:
                                                my_conn = create_engine(
                                                    "mysql+mysqldb://root:password123@localhost/buseticket")
                                                my_conn.execute("INSERT INTO person_details(bet_id,name,address,pincode,district,state,aadhar_no,depot,ticket_type,valid_from,expire_till,mobile_no,profile_pic,age,aadhar_card_pic,gender,date_of_birth,ReporterRjournalist_pic,disability_percentage,attendant_pic,attendant_name) \
                                                                                                                                                                      VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                                                data)
                                                switchButtonState()
                                            except:
                                                messagebox.showerror(title="Getting user Details->Error",
                                                                     message="01.Make Sure To Enter All details \n 02.Make sure that You have Entered correct details\n like BET ID,AADHAR NUMBER,MOBILE NUMBER etc")

                                        b7.mainloop()

                                    b7.mainloop()
                                elif (click1.get() == "Freedom Fighters"):
                                    a1.destroy()
                                    b8 = Tk()
                                    b8.geometry("1490x745")
                                    b8.title("Getting Detail from User")
                                    icon = ImageTk.PhotoImage(file='windowBusIcon.png')
                                    b8.wm_iconphoto(False, icon)
                                    cana = Canvas(b8, width=800, height=800)
                                    cana.pack(fill="both", expand=True)
                                    img2 = Image.open("bgforwindow6.png")
                                    resize3 = img2.resize((1490, 745))
                                    new2 = ImageTk.PhotoImage(resize3)
                                    cana.create_image(0, 0, image=new2, anchor='nw')
                                    rules_photo = PhotoImage(file='FreedomFighter.png')
                                    criteria_label = Label(b8, text="Criteria & Rules To Apply Freedom Fighters",
                                                           font=('times', 25, 'bold'))
                                    criteria_label.place(x=300, y=50)
                                    rules_label = Label(b8, fg='#00FF00', bg='white', relief=RAISED, bd=10, padx=0,
                                                        pady=0,
                                                        image=rules_photo, compound='top')
                                    rules_label.place(x=25, y=100)
                                    Next_button = Button(b8, text='Next', bg="green", font=('times', 14, 'bold'),
                                                         command=lambda: nextpage())
                                    Next_button.place(x=650, y=600)

                                    def nextpage():
                                        rules_label.destroy()
                                        criteria_label.destroy()
                                        Next_button.destroy()
                                        # details info
                                        name = StringVar()
                                        NAME = name.get()
                                        address1 = StringVar()
                                        ADDRESS = address1.get()
                                        age1 = StringVar()
                                        AGE = age1.get()
                                        pincode1 = StringVar()
                                        PINCODE = pincode1.get()
                                        dob1 = StringVar()
                                        DOB = dob1.get()
                                        aadhar1 = StringVar()
                                        AADHARNO = aadhar1.get()
                                        BETID = StringVar()
                                        BETid = BETID.get()
                                        district = StringVar()
                                        DISTRICT = district.get()
                                        state = StringVar()
                                        STATE = state.get()
                                        valid_date = StringVar()
                                        VALID_DATE = valid_date.get()
                                        expire_date = StringVar()
                                        EXPIRE_DATE = expire_date.get()
                                        mobile1 = StringVar()
                                        MOBILE = mobile1.get()

                                        def my_command():
                                            b8.destroy()
                                            HOME_BUTTON_PAGE()

                                        click_btn = PhotoImage(file='Small_Home_ Icon.png')
                                        button = Button(b8, image=click_btn, command=my_command)
                                        button.place(x=30, y=25)

                                        def my_command1():
                                            b8.destroy()
                                            CREATE_BET_PAGE()

                                        click_btn1 = PhotoImage(file='small_back_icon.png')
                                        button1 = Button(b8, image=click_btn1, command=my_command1)
                                        button1.place(x=95, y=25)

                                        font = Label(b8, text="Create your Bus E-Ticket", font=('Arial', 22, 'bold'),
                                                     bg="#b3ffff")
                                        font.place(x=200, y=25)
                                        BETid_label = Label(b8, text="BET id", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        BETid_label.place(x=50, y=100)
                                        BETid_entry = Entry(b8, textvariable=BETid, width=35)
                                        BETid_entry.place(x=175, y=100, width=100)
                                        name = Label(b8, text="Name", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        name.place(x=50, y=150)
                                        name_entry = Entry(b8, textvariable=NAME, width=35)
                                        name_entry.place(x=175, y=150, width=100)
                                        Address = Label(b8, text="Address", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        Address.place(x=50, y=200)
                                        Address_entry = Entry(b8, textvariable=ADDRESS, width=35)
                                        Address_entry.place(x=175, y=200, width=100)
                                        pincode = Label(b8, text="Pincode", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        pincode.place(x=50, y=250)
                                        pincode_entry = Entry(b8, textvariable=PINCODE, width=35)
                                        pincode_entry.place(x=175, y=250, width=100)
                                        district_label = Label(b8, text="District", font=('Arial', 15, 'bold'),
                                                               bg="#ffff4d")
                                        district_label.place(x=50, y=300)
                                        district_entry = Entry(b8, textvariable=DISTRICT, width=35)
                                        district_entry.place(x=175, y=300, width=100)
                                        state = Label(b8, text="State", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        state.place(x=50, y=350)
                                        state_entry = Entry(b8, textvariable=STATE, width=35)
                                        state_entry.place(x=175, y=350, width=100)
                                        aadhar = Label(b8, text="Aadhar No", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        aadhar.place(x=50, y=400)
                                        aadhar_entry = Entry(b8, textvariable=AADHARNO, width=35)
                                        aadhar_entry.place(x=175, y=400, width=100)
                                        valid_date_label = Label(b8, text="Valid From", font=('Arial', 15, 'bold'),
                                                                 bg="#ffff4d")
                                        valid_date_label.place(x=700, y=100)
                                        valid_date_entry = Entry(b8, textvariable=VALID_DATE, width=35)
                                        valid_date_entry.place(x=850, y=100, width=100)
                                        expire_date_label = Label(b8, text="Expire Till", font=('Arial', 15, 'bold'),
                                                                  bg="#ffff4d")
                                        expire_date_label.place(x=700, y=150)
                                        expire_date_entry = Entry(b8, textvariable=EXPIRE_DATE, width=35)
                                        expire_date_entry.place(x=850, y=150, width=100)
                                        mobileno = Label(b8, text="Mobile No", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        mobileno.place(x=700, y=200)
                                        mobileno_entry = Entry(b8, textvariable=MOBILE, width=35)
                                        mobileno_entry.place(x=850, y=200, width=100)
                                        gender_label = Label(b8, text="Gender", font=('Arial', 15, 'bold'),
                                                             bg="#ffff4d")
                                        gender_label.place(x=700, y=250)
                                        gender_options = ["Male", "Female", "Transgender"]
                                        gender = StringVar()
                                        gender.set("Select")
                                        gender1 = OptionMenu(b8, gender, *gender_options)
                                        gender1.place(x=850, y=250)
                                        dob_label = Label(b8, text="Date of Birth", font=('Arial', 15, 'bold'),
                                                          bg="#ffff4d")
                                        dob_label.place(x=700, y=300)
                                        dob_entry = Entry(b8, textvariable=DOB, width=35)
                                        dob_entry.place(x=850, y=300, width=100)
                                        upload_aadhar_button = Button(b8, text='Upload Aadhar Card',
                                                                      font=('times', 14, 'bold'),
                                                                      command=lambda: upload_aadhar_card(),
                                                                      state=DISABLED)
                                        upload_aadhar_button.place(x=900, y=400)
                                        upload_RJ_button = Button(b8,
                                                                  text='Upload Freedom Fighter Pension/F.A Proof Issued By State/Central Government',
                                                                  font=('times', 12, 'bold'),
                                                                  command=lambda: Upload_Freedom_Fighter())
                                        upload_RJ_button.place(x=700, y=350)

                                        def switchButtonState2():
                                            if (upload_photo_button['state'] == DISABLED):
                                                upload_photo_button['state'] = NORMAL

                                        def switchButtonState20():
                                            if (upload_aadhar_button['state'] == DISABLED):
                                                upload_aadhar_button['state'] = NORMAL

                                        global filename1

                                        def upload_aadhar_card():
                                            global filename1
                                            global filename1, img1
                                            f_types = [('Png files', '*.png'), ('Jpg Files', '*.jpg')]
                                            filename1 = filedialog.askopenfilename(filetypes=f_types)
                                            img1 = ImageTk.PhotoImage(file=filename1)
                                            messagebox.showinfo(title="Details Info",
                                                                message="Successfully uploaded your Aadhar Card")
                                            switchButtonState2()

                                        global filename1, img1
                                        global filename1

                                        def Upload_Freedom_Fighter():
                                            global filename2
                                            global filename2, img2
                                            f_types = [('Png files', '*.png'), ('Jpg Files', '*.jpg')]
                                            filename2 = filedialog.askopenfilename(filetypes=f_types)
                                            img2 = ImageTk.PhotoImage(file=filename2)
                                            messagebox.showinfo(title="Details Info",
                                                                message="Successfully uploaded your Freedom Fighters ID Proof")
                                            switchButtonState20()

                                        global filename2, img2
                                        debo_label = Label(b8, text="Depot", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        debo_label.place(x=50, y=450)
                                        debo_options = ["Adyar", "Ambathur Industrial Estate", " Ambathur OT",
                                                        " Anna Nagar (West)",
                                                        "Avadi", "Ayanavaram", "Broadway", "C.M.B.T",
                                                        "Central Rly station",
                                                        "Guindy Industrial Estate", "Iyyappanthangal", "K.K.Nagar",
                                                        "M.K.B.Nagar",
                                                        "Mandaveli", "Pallavaram", "Perambur", "Poonamallee",
                                                        "Redhills", "Saidapet",
                                                        "Sriperumbathur", "T.Nagar", "Tambaram (West)", "Thiruvanmiyur",
                                                        "Thiruvotriyur", "Tondiarpet", "Vadapalani", " Vallalar Nagar",
                                                        "Velachery",
                                                        "Villivakkam"]
                                        debo = StringVar()
                                        debo.set("Select")
                                        debo1 = OptionMenu(b8, debo, *debo_options)
                                        debo1.place(x=175, y=450)
                                        ticket_label = Label(b8, text="Ticket Type", font=('Arial', 15, 'bold'),
                                                             bg="#ffff4d")
                                        ticket_label.place(x=50, y=500)
                                        Ticket_options = ["Freedom Fighters"]
                                        ticket = StringVar()
                                        ticket.set("Select")
                                        Ticket1 = OptionMenu(b8, ticket, *Ticket_options)
                                        Ticket1.place(x=175, y=500)
                                        age = Label(b8, text="Age", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        age.place(x=50, y=550)
                                        age_entry = Entry(b8, textvariable=AGE, width=35)
                                        age_entry.place(x=175, y=550, width=100)
                                        upload_photo_button = Button(b8, text='Upload photo',
                                                                     font=('times', 14, 'bold'),
                                                                     command=lambda: upload_file(), state=DISABLED)
                                        upload_photo_button.place(x=400, y=125)
                                        upload_data_button = Button(b8, text='Upload data', font=('times', 16, 'bold'),
                                                                    bg="#00ffbf",
                                                                    command=lambda: add_data(), state=DISABLED)
                                        upload_data_button.place(x=75, y=625)

                                        def switchButtonState1():
                                            if (upload_data_button['state'] == DISABLED):
                                                upload_data_button['state'] = NORMAL

                                        global filename

                                        def upload_file():
                                            if (
                                                    BETid_entry.get() == "" or name_entry.get() == "" or gender.get() == "Select" or dob_entry.get() == "" or Address_entry.get() == "" or pincode_entry.get() == "" or district_entry.get() == "" or state_entry.get() == "" or aadhar_entry.get() == "" or debo.get() == "Select" or ticket.get() == "Select" or valid_date_entry.get() == "" or expire_date_entry.get() == "" or age_entry.get() == "" or mobileno_entry.get() == ""):
                                                messagebox.showerror(title="Getting user Details->Error",
                                                                     message="Please Make Sure To Enter All details")
                                            else:
                                                global filename
                                                global filename, img
                                                f_types = [('Png files', '*.png'), ('Jpg Files', '*.jpg')]
                                                filename = filedialog.askopenfilename(filetypes=f_types)
                                                img = ImageTk.PhotoImage(file=filename)
                                                b_1 = Button(b8, image=img)  # using Button
                                                b_1.place(x=400, y=175)  # display uploaded photo
                                                switchButtonState1()

                                        def switchButtonState12():
                                            if (mybutton2['state'] == DISABLED):
                                                mybutton2['state'] = NORMAL

                                        global filename, img

                                        def create_code():
                                            input_path = filedialog.asksaveasfilename(title="save image", filetypes=(
                                                ("PNG File", ".png"), ("All Files", "*.*")))
                                            switchButtonState12()
                                            if input_path:
                                                if input_path.endswith(".png"):
                                                    get_code = pyqrcode.create(
                                                        "BET ID:" + BETid_entry.get() + "\n" + "NAME:" + name_entry.get() + "\n" + "GENDER:" + gender.get() + "\n" + "DATE OF BIRTH:" + dob_entry.get() + "\n" + "AGE:" + age_entry.get() + "\n" + "RESIDENTIAL ADDRESS:" + Address_entry.get() + "\n" + "PINCODE:" + pincode_entry.get() + "\n" + "DISTRICT:" + district_entry.get() + "\n" + "STATE:" + state_entry.get() + "\n" + "AADHHAR NO:" + aadhar_entry.get() + "\n" + "DEPOT:" + debo.get() + "\n" + "BUS E-TICKET TYPE:" + ticket.get() + "\n" + "VALID FROM:" + valid_date_entry.get() + "\n" + "EXPIRE TILL:" + expire_date_entry.get() + "\n" + "MOBILE NO:" + mobileno_entry.get() + "\n")
                                                    # get_code.png(input_path, scale=5)
                                                    get_code.png(input_path, scale=5)
                                                    with Image.open(input_path) as img:
                                                        img_resized = img.resize((150, 150))
                                                        img_resized.save(input_path)

                                                    messagebox.showinfo(title="Generate QR-code",
                                                                        message=f"Successfully Generated QR-Code For Details \n QR code saved to {input_path}")

                                                else:
                                                    input_path = f'{input_path}.png'
                                                    get_code = pyqrcode.create(
                                                        "BET ID:" + BETid_entry.get() + "\n" + "NAME:" + name_entry.get() + "\n" + "GENDER:" + gender.get() + "\n" + "DATE OF BIRTH:" + dob_entry.get() + "\n" + "AGE:" + age_entry.get() + "\n" + "RESIDENTIAL ADDRESS:" + Address_entry.get() + "\n" + "PINCODE:" + pincode_entry.get() + "\n" + "DISTRICT:" + district_entry.get() + "\n" + "STATE:" + state_entry.get() + "\n" + "AADHHAR NO:" + aadhar_entry.get() + "\n" + "DEPOT:" + debo.get() + "\n" + "BUS E-TICKET TYPE:" + ticket.get() + "\n" + "VALID FROM:" + valid_date_entry.get() + "\n" + "EXPIRE TILL:" + expire_date_entry.get() + "\n" + "MOBILE NO:" + mobileno_entry.get() + "\n")
                                                    get_code.png(input_path, scale=5)
                                                    with Image.open(input_path) as img:
                                                        img_resized = img.resize((200, 200))
                                                        img_resized.save(input_path)

                                                    messagebox.showinfo(title="Generate QR-code",
                                                                        message=f"Successfully Generated QR-Code For Details \n QR code saved to {input_path}")

                                        def create_code1():
                                            data = BETid_entry.get()

                                            # Create QR code object
                                            qr = qrcode.QRCode(
                                                version=None,
                                                error_correction=qrcode.constants.ERROR_CORRECT_L,
                                                box_size=10,
                                                border=4,
                                            )
                                            qr.add_data(data)
                                            qr.make(fit=True)

                                            # Create QR code image with fill color and background color
                                            qr_image = qr.make_image(fill_color="#ff3300", back_color="white")

                                            # Load logo image
                                            logo_image = Image.open("windowBusIcon.png")

                                            # Resize logo image to fit inside QR code
                                            logo_size = (qr_image.size[0] // 7, qr_image.size[1] // 7)

                                            # logo_size = (qr_image.size[0] // 4, qr_image.size[1] // 4)
                                            logo_image = logo_image.resize(logo_size)

                                            # Calculate position to place logo image inside QR code
                                            logo_pos = (
                                                (qr_image.size[0] - logo_size[0]) // 2,
                                                (qr_image.size[1] - logo_size[1]) // 2)

                                            # Paste logo image onto QR code image
                                            qr_image.paste(logo_image)

                                            # Resize QR code image to 100x100 pixels
                                            qr_image = qr_image.resize((175, 175))

                                            # Get file path from user using file dialog
                                            file_path = filedialog.asksaveasfilename(title="Save QR Code",
                                                                                     filetypes=(
                                                                                     ("PNG Files", "*.png"),))

                                            # Save QR code image to file
                                            if file_path:
                                                if file_path.endswith(".png"):
                                                    qr_image.save(file_path, "PNG")
                                                    messagebox.showinfo(title="QR Code Saved",
                                                                        message=f"Successfully Generated QR-Code For BET ID \n QR code saved to {file_path}")
                                                else:
                                                    file_path = f'{file_path}.png'
                                                    qr_image.save(file_path, "PNG")
                                                    messagebox.showinfo(title="QR Code Saved",
                                                                        message=f"Successfully Generated QR-Code For BET ID \n QR code saved to {file_path}")

                                        mybutton = Button(b8, text="Generate QR-Code For Details",
                                                          font=('times', 11, 'bold'),
                                                          bg="#00ff00", state=DISABLED, command=create_code)
                                        mybutton.place(x=250, y=625)
                                        mybutton2 = Button(b8, text="Generate QR-Code for BET ID ",
                                                           font=('times', 11, 'bold'),
                                                           bg="#00ff00",
                                                           state=DISABLED, command=create_code1)
                                        mybutton2.place(x=500, y=625)

                                        def switchButtonState():
                                            if (mybutton['state'] == DISABLED):
                                                mybutton['state'] = NORMAL

                                        def add_data():  # Add data to MySQL table
                                            # upload_aadhar_card()
                                            global img, filename
                                            global img1, filename1
                                            with open("mytextfile.txt", "a") as f:
                                                f.write(BETid_entry.get() + "\n")
                                            fob2 = open(filename2, 'rb')
                                            fob2 = fob2.read()
                                            fob = open(filename, 'rb')  # filename from upload_file()
                                            fob = fob.read()
                                            fob1 = open(filename1, 'rb')
                                            fob1 = fob1.read()
                                            data = (BETid_entry.get(), name_entry.get(), Address_entry.get(),
                                                    pincode_entry.get(),
                                                    district_entry.get(), state_entry.get(), aadhar_entry.get(),
                                                    debo.get(), ticket.get(), valid_date_entry.get(),
                                                    expire_date_entry.get(),
                                                    mobileno_entry.get(), fob, age_entry.get(), fob1, gender.get(),
                                                    dob_entry.get(),
                                                    fob2)
                                            try:
                                                my_conn = create_engine(
                                                    "mysql+mysqldb://root:password123@localhost/buseticket")
                                                my_conn.execute("INSERT INTO person_details(bet_id,name,address,pincode,district,state,aadhar_no,depot,ticket_type,valid_from,expire_till,mobile_no,profile_pic,age,aadhar_card_pic,gender,date_of_birth,freedom_fighter_pic) \
                                                                                                                                                                       VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                                                data)
                                                switchButtonState()
                                            except:
                                                messagebox.showerror(title="Getting user Details->Error",
                                                                     message="01.Make Sure To Enter All details \n 02.Make sure that You have Entered correct details\n like BET ID,AADHAR NUMBER,MOBILE NUMBER etc")

                                        b8.mainloop()

                                    b8.mainloop()
                                elif (click1.get() == "Senior Citizen"):
                                    a1.destroy()
                                    b9 = Tk()
                                    b9.geometry("1490x745")
                                    b9.title("Getting Detail from User")
                                    icon = ImageTk.PhotoImage(file='windowBusIcon.png')
                                    b9.wm_iconphoto(False, icon)
                                    cana = Canvas(b9, width=800, height=800)
                                    cana.pack(fill="both", expand=True)
                                    img2 = Image.open("bgforwindow6.png")
                                    resize3 = img2.resize((1490, 745))
                                    new2 = ImageTk.PhotoImage(resize3)
                                    cana.create_image(0, 0, image=new2, anchor='nw')
                                    rules_photo = PhotoImage(file='SeniorCitizen.png')
                                    criteria_label = Label(b9, text="Criteria & Rules To Apply Senior Citizen",
                                                           font=('times', 25, 'bold'))
                                    criteria_label.place(x=330, y=50)
                                    rules_label = Label(b9, fg='#00FF00', bg='white', relief=RAISED, bd=10, padx=0,
                                                        pady=0,
                                                        image=rules_photo, compound='top')
                                    rules_label.place(x=25, y=100)
                                    Next_button = Button(b9, text='Next', bg="green", font=('times', 14, 'bold'),
                                                         command=lambda: nextpage())
                                    Next_button.place(x=650, y=600)

                                    def nextpage():
                                        rules_label.destroy()
                                        criteria_label.destroy()
                                        Next_button.destroy()
                                        # details info
                                        name = StringVar()
                                        NAME = name.get()
                                        address1 = StringVar()
                                        Gname = StringVar()
                                        GNAME = Gname.get()
                                        ADDRESS = address1.get()
                                        age1 = StringVar()
                                        AGE = age1.get()
                                        pincode1 = StringVar()
                                        PINCODE = pincode1.get()
                                        dob1 = StringVar()
                                        DOB = dob1.get()
                                        aadhar1 = StringVar()
                                        AADHARNO = aadhar1.get()
                                        BETID = StringVar()
                                        BETid = BETID.get()
                                        district = StringVar()
                                        DISTRICT = district.get()
                                        state = StringVar()
                                        STATE = state.get()
                                        valid_date = StringVar()
                                        VALID_DATE = valid_date.get()
                                        expire_date = StringVar()
                                        EXPIRE_DATE = expire_date.get()
                                        mobile1 = StringVar()
                                        MOBILE = mobile1.get()

                                        def my_command():
                                            b9.destroy()
                                            HOME_BUTTON_PAGE()

                                        click_btn = PhotoImage(file='Small_Home_ Icon.png')
                                        button = Button(b9, image=click_btn, command=my_command)
                                        button.place(x=30, y=25)

                                        def my_command1():
                                            b9.destroy()
                                            CREATE_BET_PAGE()

                                        click_btn1 = PhotoImage(file='small_back_icon.png')
                                        button1 = Button(b9, image=click_btn1, command=my_command1)
                                        button1.place(x=95, y=25)
                                        font = Label(b9, text="Create your Bus E-Ticket", font=('Arial', 22, 'bold'),
                                                     bg="#b3ffff")
                                        font.place(x=200, y=25)
                                        BETid_label = Label(b9, text="BET id", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        BETid_label.place(x=50, y=100)
                                        BETid_entry = Entry(b9, textvariable=BETid, width=35)
                                        BETid_entry.place(x=175, y=100, width=100)
                                        name = Label(b9, text="Name", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        name.place(x=50, y=150)
                                        name_entry = Entry(b9, textvariable=NAME, width=35)
                                        name_entry.place(x=175, y=150, width=100)
                                        Address = Label(b9, text="Address", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        Address.place(x=50, y=200)
                                        Address_entry = Entry(b9, textvariable=ADDRESS, width=35)
                                        Address_entry.place(x=175, y=200, width=100)
                                        pincode = Label(b9, text="Pincode", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        pincode.place(x=50, y=250)
                                        pincode_entry = Entry(b9, textvariable=PINCODE, width=35)
                                        pincode_entry.place(x=175, y=250, width=100)
                                        district_label = Label(b9, text="District", font=('Arial', 15, 'bold'),
                                                               bg="#ffff4d")
                                        district_label.place(x=50, y=300)
                                        district_entry = Entry(b9, textvariable=DISTRICT, width=35)
                                        district_entry.place(x=175, y=300, width=100)
                                        state = Label(b9, text="State", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        state.place(x=50, y=350)
                                        state_entry = Entry(b9, textvariable=STATE, width=35)
                                        state_entry.place(x=175, y=350, width=100)
                                        aadhar = Label(b9, text="Aadhar No", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        aadhar.place(x=50, y=400)
                                        aadhar_entry = Entry(b9, textvariable=AADHARNO, width=35)
                                        aadhar_entry.place(x=175, y=400, width=100)

                                        valid_date_label = Label(b9, text="Valid From", font=('Arial', 15, 'bold'),
                                                                 bg="#ffff4d")
                                        valid_date_label.place(x=700, y=100)
                                        valid_date_entry = Entry(b9, textvariable=VALID_DATE, width=35)
                                        valid_date_entry.place(x=850, y=100, width=100)
                                        expire_date_label = Label(b9, text="Expire Till", font=('Arial', 15, 'bold'),
                                                                  bg="#ffff4d")
                                        expire_date_label.place(x=700, y=150)
                                        expire_date_entry = Entry(b9, textvariable=EXPIRE_DATE, width=35)
                                        expire_date_entry.place(x=850, y=150, width=100)
                                        mobileno = Label(b9, text="Mobile No", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        mobileno.place(x=700, y=200)
                                        mobileno_entry = Entry(b9, textvariable=MOBILE, width=35)
                                        mobileno_entry.place(x=850, y=200, width=100)
                                        gender_label = Label(b9, text="Gender", font=('Arial', 15, 'bold'),
                                                             bg="#ffff4d")
                                        gender_label.place(x=700, y=250)
                                        gender_options = ["Male", "Female", "Transgender"]
                                        gender = StringVar()
                                        gender.set("Select")
                                        gender1 = OptionMenu(b9, gender, *gender_options)
                                        gender1.place(x=850, y=250)
                                        dob_label = Label(b9, text="Date of Birth", font=('Arial', 15, 'bold'),
                                                          bg="#ffff4d")
                                        dob_label.place(x=700, y=300)
                                        dob_entry = Entry(b9, textvariable=DOB, width=35)
                                        dob_entry.place(x=850, y=300, width=100)
                                        upload_aadhar_button = Button(b9, text='Upload Aadhar Card',
                                                                      font=('times', 14, 'bold'),
                                                                      command=lambda: upload_aadhar_card(),
                                                                      state=DISABLED)
                                        upload_aadhar_button.place(x=800, y=450)
                                        upload_RJ_button = Button(b9, text='Upload Ration Card ',
                                                                  font=('times', 14, 'bold'),
                                                                  command=lambda: Upload_SeniorCitizen_proof()
                                                                  )
                                        upload_RJ_button.place(x=800, y=400)

                                        def switchButtonState2():
                                            if (upload_photo_button['state'] == DISABLED):
                                                upload_photo_button['state'] = NORMAL

                                        def switchButtonState20():
                                            if (upload_aadhar_button['state'] == DISABLED):
                                                upload_aadhar_button['state'] = NORMAL

                                        global filename1

                                        def upload_aadhar_card():
                                            global filename1
                                            global filename1, img1
                                            f_types = [('Png files', '*.png'), ('Jpg Files', '*.jpg')]
                                            filename1 = filedialog.askopenfilename(filetypes=f_types)
                                            img1 = ImageTk.PhotoImage(file=filename1)
                                            messagebox.showinfo(title="Details Info",
                                                                message="Successfully uploaded your Aadhar Card")
                                            switchButtonState2()

                                        global filename1, img1
                                        global filename1

                                        def Upload_SeniorCitizen_proof():
                                            global filename2
                                            global filename2, img2
                                            f_types = [('Png files', '*.png'), ('Jpg Files', '*.jpg')]
                                            filename2 = filedialog.askopenfilename(filetypes=f_types)
                                            img2 = ImageTk.PhotoImage(file=filename2)
                                            messagebox.showinfo(title="Details Info",
                                                                message="Successfully uploaded your Ration Card")
                                            switchButtonState20()

                                        global filename2, img2
                                        debo_label = Label(b9, text="Depot", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        debo_label.place(x=50, y=450)
                                        debo_options = ["Adyar", "Ambathur Industrial Estate", " Ambathur OT",
                                                        " Anna Nagar (West)",
                                                        "Avadi", "Ayanavaram", "Broadway", "C.M.B.T",
                                                        "Central Rly station",
                                                        "Guindy Industrial Estate", "Iyyappanthangal", "K.K.Nagar",
                                                        "M.K.B.Nagar",
                                                        "Mandaveli", "Pallavaram", "Perambur", "Poonamallee",
                                                        "Redhills", "Saidapet",
                                                        "Sriperumbathur", "T.Nagar", "Tambaram (West)", "Thiruvanmiyur",
                                                        "Thiruvotriyur", "Tondiarpet", "Vadapalani", " Vallalar Nagar",
                                                        "Velachery",
                                                        "Villivakkam"]
                                        debo = StringVar()
                                        debo.set("Select")
                                        debo1 = OptionMenu(b9, debo, *debo_options)
                                        debo1.place(x=175, y=450)
                                        ticket_label = Label(b9, text="Ticket Type", font=('Arial', 15, 'bold'),
                                                             bg="#ffff4d")
                                        ticket_label.place(x=50, y=500)
                                        Ticket_options = ["Senior Citizen"]
                                        ticket = StringVar()
                                        ticket.set("Select")
                                        Ticket1 = OptionMenu(b9, ticket, *Ticket_options)
                                        Ticket1.place(x=175, y=500)
                                        age = Label(b9, text="Age", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        age.place(x=50, y=550)
                                        age_entry = Entry(b9, textvariable=AGE, width=35)
                                        age_entry.place(x=175, y=550, width=100)
                                        upload_photo_button = Button(b9, text='Upload photo',
                                                                     font=('times', 14, 'bold'),
                                                                     command=lambda: upload_file(), state=DISABLED)
                                        upload_photo_button.place(x=400, y=125)
                                        upload_data_button = Button(b9, text='Upload data', font=('times', 16, 'bold'),
                                                                    bg="#00ffbf",
                                                                    command=lambda: add_data(), state=DISABLED)
                                        upload_data_button.place(x=75, y=625)

                                        def switchButtonState1():
                                            if (upload_data_button['state'] == DISABLED):
                                                upload_data_button['state'] = NORMAL

                                        global filename

                                        def upload_file():
                                            if (age_entry.get() > '59'):
                                                if (
                                                        BETid_entry.get() == "" or name_entry.get() == "" or gender.get() == "Select" or dob_entry.get() == "" or Address_entry.get() == "" or pincode_entry.get() == "" or district_entry.get() == "" or state_entry.get() == "" or aadhar_entry.get() == "" or debo.get() == "Select" or ticket.get() == "Select" or valid_date_entry.get() == "" or expire_date_entry.get() == "" or age_entry.get() == "" or mobileno_entry.get() == ""):
                                                    messagebox.showerror(title="Getting user Details->Error",
                                                                         message="Please Make Sure To Enter All details")
                                                else:
                                                    global filename
                                                    global filename, img
                                                    f_types = [('Png files', '*.png'), ('Jpg Files', '*.jpg')]
                                                    filename = filedialog.askopenfilename(filetypes=f_types)
                                                    img = ImageTk.PhotoImage(file=filename)
                                                    b_1 = Button(b9, image=img)  # using Button
                                                    b_1.place(x=400, y=175)  # display uploaded photo
                                                    switchButtonState1()
                                            else:
                                                messagebox.showerror(title="Getting user Details->Error",
                                                                     message="Sorry,Age Must be Greater Than 59 So Your Are Not Eligible Senior Citizen %")

                                        def switchButtonState12():
                                            if (mybutton2['state'] == DISABLED):
                                                mybutton2['state'] = NORMAL

                                        global filename, img

                                        def create_code():
                                            input_path = filedialog.asksaveasfilename(title="save image", filetypes=(
                                                ("PNG File", ".png"), ("All Files", "*.*")))
                                            switchButtonState12()
                                            if input_path:
                                                if input_path.endswith(".png"):
                                                    get_code = pyqrcode.create(
                                                        "BET ID:" + BETid_entry.get() + "\n" + "NAME:" + name_entry.get() + "\n" + "GENDER:" + gender.get() + "\n" + "DATE OF BIRTH:" + dob_entry.get() + "\n" + "AGE:" + age_entry.get() + "\n" + "RESIDENTIAL ADDRESS:" + Address_entry.get() + "\n" + "PINCODE:" + pincode_entry.get() + "\n" + "DISTRICT:" + district_entry.get() + "\n" + "STATE:" + state_entry.get() + "\n" + "AADHHAR NO:" + aadhar_entry.get() + "\n" + "DEPOT:" + debo.get() + "\n" + "BUS E-TICKET TYPE:" + ticket.get() + "\n" + "DISABILITY PERCENTAGE:" + "VALID FROM:" + valid_date_entry.get() + "\n" + "EXPIRE TILL:" + expire_date_entry.get() + "\n" + "MOBILE NO:" + mobileno_entry.get() + "\n")
                                                    # get_code.png(input_path, scale=5)
                                                    get_code.png(input_path, scale=5)
                                                    with Image.open(input_path) as img:
                                                        img_resized = img.resize((200, 200))
                                                        img_resized.save(input_path)

                                                    messagebox.showinfo(title="Generate QR-code",
                                                                        message=f"Successfully Generated QR-Code For Details \n QR code saved to {input_path}")

                                                else:
                                                    input_path = f'{input_path}.png'
                                                    get_code = pyqrcode.create(
                                                        "BET ID:" + BETid_entry.get() + "\n" + "NAME:" + name_entry.get() + "\n" + "GENDER:" + gender.get() + "\n" + "DATE OF BIRTH:" + dob_entry.get() + "\n" + "AGE:" + age_entry.get() + "\n" + "RESIDENTIAL ADDRESS:" + Address_entry.get() + "\n" + "PINCODE:" + pincode_entry.get() + "\n" + "DISTRICT:" + district_entry.get() + "\n" + "STATE:" + state_entry.get() + "\n" + "AADHHAR NO:" + aadhar_entry.get() + "\n" + "DEPOT:" + debo.get() + "\n" + "BUS E-TICKET TYPE:" + ticket.get() + "\n" + "DISABILITY PERCENTAGE:" + "VALID FROM:" + valid_date_entry.get() + "\n" + "EXPIRE TILL:" + expire_date_entry.get() + "\n" + "MOBILE NO:" + mobileno_entry.get() + "\n")
                                                    get_code.png(input_path, scale=5)
                                                    with Image.open(input_path) as img:
                                                        img_resized = img.resize((200, 200))
                                                        img_resized.save(input_path)

                                                    messagebox.showinfo(title="Generate QR-code",
                                                                        message=f"Successfully Generated QR-Code For Details \n QR code saved to {input_path}")

                                        def create_code1():
                                            data = BETid_entry.get()

                                            # Create QR code object
                                            qr = qrcode.QRCode(
                                                version=None,
                                                error_correction=qrcode.constants.ERROR_CORRECT_L,
                                                box_size=10,
                                                border=4,
                                            )
                                            qr.add_data(data)
                                            qr.make(fit=True)

                                            # Create QR code image with fill color and background color
                                            qr_image = qr.make_image(fill_color="white", back_color="#996633")

                                            # Load logo image
                                            logo_image = Image.open("windowBusIcon.png")

                                            # Resize logo image to fit inside QR code
                                            logo_size = (qr_image.size[0] // 7, qr_image.size[1] // 7)

                                            # logo_size = (qr_image.size[0] // 4, qr_image.size[1] // 4)
                                            logo_image = logo_image.resize(logo_size)

                                            # Calculate position to place logo image inside QR code
                                            logo_pos = (
                                                (qr_image.size[0] - logo_size[0]) // 2,
                                                (qr_image.size[1] - logo_size[1]) // 2)

                                            # Paste logo image onto QR code image
                                            qr_image.paste(logo_image)

                                            # Resize QR code image to 100x100 pixels
                                            qr_image = qr_image.resize((175, 175))

                                            # Get file path from user using file dialog
                                            file_path = filedialog.asksaveasfilename(title="Save QR Code",
                                                                                     filetypes=(
                                                                                     ("PNG Files", "*.png"),))

                                            # Save QR code image to file
                                            if file_path:
                                                if file_path.endswith(".png"):
                                                    qr_image.save(file_path, "PNG")
                                                    messagebox.showinfo(title="QR Code Saved",
                                                                        message=f"Successfully Generated QR-Code For BET ID \n QR code saved to {file_path}")
                                                else:
                                                    file_path = f'{file_path}.png'
                                                    qr_image.save(file_path, "PNG")
                                                    messagebox.showinfo(title="QR Code Saved",
                                                                        message=f"Successfully Generated QR-Code For BET ID \n QR code saved to {file_path}")

                                        mybutton = Button(b9, text="Generate QR-Code For Details",
                                                          font=('times', 11, 'bold'),
                                                          bg="#00ff00", state=DISABLED, command=create_code)
                                        mybutton.place(x=250, y=625)
                                        mybutton2 = Button(b9, text="Generate QR-Code for BET ID ",
                                                           font=('times', 11, 'bold'),
                                                           bg="#00ff00",
                                                           state=DISABLED, command=create_code1)
                                        mybutton2.place(x=500, y=625)

                                        def switchButtonState():
                                            if (mybutton['state'] == DISABLED):
                                                mybutton['state'] = NORMAL

                                        def add_data():  # Add data to MySQL table
                                            # upload_aadhar_card()
                                            global img, filename
                                            global img1, filename1

                                            with open("mytextfile.txt", "a") as f:
                                                f.write(BETid_entry.get() + "\n")

                                            fob2 = open(filename2, 'rb')
                                            fob2 = fob2.read()
                                            fob = open(filename, 'rb')  # filename from upload_file()
                                            fob = fob.read()
                                            fob1 = open(filename1, 'rb')
                                            fob1 = fob1.read()
                                            data = (BETid_entry.get(), name_entry.get(), Address_entry.get(),
                                                    pincode_entry.get(),
                                                    district_entry.get(), state_entry.get(), aadhar_entry.get(),
                                                    debo.get(), ticket.get(), valid_date_entry.get(),
                                                    expire_date_entry.get(),
                                                    mobileno_entry.get(), fob, age_entry.get(), fob1, gender.get(),
                                                    dob_entry.get(),
                                                    fob2,)
                                            try:
                                                my_conn = create_engine(
                                                    "mysql+mysqldb://root:password123@localhost/buseticket")
                                                my_conn.execute("INSERT INTO person_details(bet_id,name,address,pincode,district,state,aadhar_no,depot,ticket_type,valid_from,expire_till,mobile_no,profile_pic,age,aadhar_card_pic,gender,date_of_birth,ration_card_pic) \
                                                                                                                                                                       VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                                                data)
                                                switchButtonState()
                                            except:
                                                messagebox.showerror(title="Getting user Details->Error",
                                                                     message="01.Make Sure To Enter All details \n 02.Make sure that You have Entered correct details\n like BET ID,AADHAR NUMBER,MOBILE NUMBER etc")

                                        b9.mainloop()

                                    b9.mainloop()
                                elif (click1.get() == "Select"):
                                    messagebox.showwarning(title="Ticket Type selection->Error",
                                                           message="Sorry,Make sure to select anyone option in Ticket Type")

                            a1 = Tk()
                            a1.geometry("1490x745")
                            a1.title("Getting Detail from User")
                            icon = ImageTk.PhotoImage(file='windowBusIcon.png')
                            a1.wm_iconphoto(False, icon)
                            cana = Canvas(a1, width=800, height=800)
                            cana.pack(fill="both", expand=True)
                            img2 = Image.open("bgforwindow6.png")
                            resize3 = img2.resize((1490, 745))
                            new2 = ImageTk.PhotoImage(resize3)
                            cana.create_image(0, 0, image=new2, anchor='nw')
                            font = Label(a1, text="Select your Bus E-Ticket Type", font=('Arial', 30, 'bold'),
                                         bg="#b3ffff")
                            font.place(x=200, y=25)
                            ticket_label = Label(a1, text="Ticket Type", font=('Arial', 15, 'bold'), bg="#ffff4d")
                            ticket_label.place(x=50, y=200)
                            Ticket_options = ["Travel As You Please Tickets", "Pay & Get",
                                              "Monthly Commuter Season Ticket", "Students", "Journalists/Reporters",
                                              "Handicapped/Mentally Retarded", "Blind", "Freedom Fighters",
                                              "Senior Citizen"]
                            click1 = StringVar()
                            click1.set("Select")
                            Ticket = OptionMenu(a1, click1, *Ticket_options)
                            Ticket.place(x=200, y=200)
                            proceed_button = Button(a1, text="Proceed", font=('Arial', 20, 'bold'), bg="#80ff80",
                                                    command=ticket_type)
                            proceed_button.place(x=85, y=275)

                            def my_command():
                                a1.destroy()
                                HOME_BUTTON_PAGE()

                            click_btn = PhotoImage(file='Small_Home_ Icon.png')
                            button = Button(a1, image=click_btn, command=my_command)
                            button.place(x=0, y=10)

                            def my_command1():
                                a1.destroy()
                                MANAGING_BET()

                            click_btn1 = PhotoImage(file='small_back_icon.png')
                            button1 = Button(a1, image=click_btn1, command=my_command1)
                            button1.place(x=65, y=10)
                            a1.mainloop()

                        CREATE_BET_PAGE()

                    def show_Bet():
                        # newwn.destroy()

                        def show_all():
                            # a2.destroy()
                            my_conn = create_engine("mysql+mysqldb://root:password123@localhost/buseticket")
                            z1 = Tk()
                            z1.geometry("1490x745")
                            z1.title("Showing All Records")
                            icon = ImageTk.PhotoImage(file='windowBusIcon.png')
                            z1.wm_iconphoto(False, icon)
                            z1.configure(bg='#b3ffff')

                            trv = ttk.Treeview(z1, selectmode='browse')
                            trv.grid(row=12, column=0, padx=20, pady=20)
                            trv["columns"] = (
                                "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16",
                                "17",
                                "18", "19", "20", "21", "22", "23")
                            trv['show'] = 'headings'
                            trv.column("1", width=50, anchor='c', stretch=False)
                            trv.column("2", width=75, anchor='c', stretch=False)
                            trv.column("3", width=200, anchor='c', stretch=False)
                            trv.column("4", width=50, anchor='c', stretch=False)
                            trv.column("5", width=50, anchor='c', stretch=False)
                            trv.column("6", width=50, anchor='c', stretch=False)
                            trv.column("7", width=50, anchor='c', stretch=False)
                            trv.column("8", width=50, anchor='c', stretch=False)
                            trv.column("9", width=50, anchor='c', stretch=False)
                            trv.column("10", width=50, anchor='c', stretch=False)
                            trv.column("11", width=50, anchor='c', stretch=False)
                            trv.column("12", width=50, anchor='c', stretch=False)
                            trv.column("13", width=50, anchor='c', stretch=False)
                            trv.column("14", width=50, anchor='c', stretch=False)
                            trv.column("15", width=50, anchor='c', stretch=False)
                            trv.column("16", width=50, anchor='c', stretch=False)
                            trv.column("17", width=50, anchor='c', stretch=False)
                            trv.column("18", width=50, anchor='c', stretch=False)
                            trv.column("19", width=50, anchor='c', stretch=False)
                            trv.column("20", width=50, anchor='c', stretch=False)
                            trv.column("21", width=50, anchor='c', stretch=False)
                            trv.column("22", width=50, anchor='c', stretch=False)
                            trv.column("23", width=50, anchor='c', stretch=False)

                            trv.heading("1", text="bet_id")
                            trv.heading("2", text="name")
                            trv.heading("3", text="address")
                            trv.heading("4", text="pincode")
                            trv.heading("5", text="district")
                            trv.heading("6", text="state")
                            trv.heading("7", text="aadhar_no")
                            trv.heading("8", text="depot")
                            trv.heading("9", text="ticket_type")
                            trv.heading("10", text="valid_from")
                            trv.heading("11", text="expire_till")
                            trv.heading("12", text="price_amount")
                            trv.heading("13", text="mobile_no")
                            trv.heading("14", text="college")
                            trv.heading("15", text="from_I")
                            trv.heading("16", text="to_I")
                            trv.heading("17", text="from_II")
                            trv.heading("18", text="to_II")
                            trv.heading("19", text="age")
                            trv.heading("20", text="gender")
                            trv.heading("21", text="date of birth")
                            trv.heading("22", text="disability percentage")
                            trv.heading("23", text="attendant name")

                            r_set = my_conn.execute("SELECT * from person_details")
                            for dt in r_set:
                                trv.insert("", 'end', iid=dt[0], text=dt[0], values=(
                                    dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6], dt[7], dt[8], dt[9], dt[10],
                                    dt[11],
                                    dt[12],
                                    dt[13], dt[14], dt[15], dt[16], dt[17], dt[19], dt[21], dt[22], dt[24], dt[26]))
                            vs = ttk.Scrollbar(z1, orient='vertical', command=trv.yview)
                            trv.configure(yscrollcommand=vs.set)
                            vs.grid(row=12, column=1, sticky="ns")
                            hs = ttk.Scrollbar(z1, orient='horizontal', command=trv.xview)
                            trv.configure(xscrollcommand=hs.set)
                            hs.grid(row=18, column=0, sticky="ew")

                            def my_command():
                                z1.destroy()
                                HOME_BUTTON_PAGE()

                            click_btn = PhotoImage(file='Small_Home_ Icon.png')
                            button = Button(z1, image=click_btn, command=my_command)
                            button.grid(row=0, column=0)

                            def my_command1():
                                z1.destroy()
                                SHOW_DATA_PAGE()

                            click_btn1 = PhotoImage(file='small_back_icon.png')
                            button1 = Button(z1, image=click_btn1, command=my_command1)
                            button1.grid(row=3, column=0)
                            z1.mainloop()

                        def show_particular():
                            # a2.destroy()
                            z2 = Tk()
                            z2.geometry("1490x745")
                            z2.title("Showing Particular Record")
                            icon = ImageTk.PhotoImage(file='windowBusIcon.png')
                            z2.wm_iconphoto(False, icon)
                            z2.configure(bg='#b3ffff')
                            z2.geometry("1475x745")

                            global trv
                            l1 = Label(z2, text='Enter BET ID ', bg='yellow', width=40)
                            l1.grid(row=1, column=1)
                            e1 = Entry(z2, width=10, bg='white', font=22)
                            e1.grid(row=1, column=2, padx=5)
                            b1 = Button(z2, text='Show Details', width=15, bg='green',
                                        command=lambda: my_details(e1.get()))
                            b1.grid(row=3, column=2, padx=5, pady=20)
                            my_str1 = StringVar(value='Searching For Person Details...')
                            l2 = Label(z2, textvariable=my_str1, width=30, fg='red', font=16)
                            l2.grid(row=4, column=0, columnspan=2)
                            my_str = StringVar(value='')
                            l2 = Label(z2, textvariable=my_str, width=30, fg='red', font=16)
                            l2.grid(row=11, column=0, columnspan=2)
                            my_conn = create_engine("mysql+mysqldb://root:password123@localhost/buseticket")

                            def my_command():
                                z2.destroy()
                                HOME_BUTTON_PAGE()

                            click_btn = PhotoImage(file='Small_Home_ Icon.png')
                            button = Button(z2, image=click_btn, command=my_command)
                            button.grid(row=0, column=0)

                            def my_command1():
                                z2.destroy()
                                SHOW_DATA_PAGE()

                            click_btn1 = PhotoImage(file='small_back_icon.png')
                            button1 = Button(z2, image=click_btn1, command=my_command1)
                            button1.grid(row=0, column=1)

                            def my_details(id):
                                global trv

                                try:
                                    val = id
                                    my_data = [val]
                                    query = "SELECT bet_id,name,address,pincode,district,state,aadhar_no,depot,ticket_type,valid_from,expire_till,price_amount,mobile_no,college,from_I,to_I,from_II,to_II,age,gender,date_of_birth,disability_percentage,attendant_name FROM person_details WHERE bet_id=%s"
                                    my_row = my_conn.execute(query, my_data)
                                    student = list(my_row.fetchone())
                                    l1 = [r for r in my_row.keys()]
                                    trv = ttk.Treeview(z2, selectmode='browse')

                                    trv.grid(row=6, column=0, columnspan=4, padx=5, pady=20)
                                    my_str1.set("Person Details ")
                                    my_str.set("Got 1 Result ")
                                    trv['height'] = 3
                                    trv['columns'] = l1
                                    trv['show'] = 'headings'

                                    for i in l1:
                                        trv.column(i, anchor='c', width=58, stretch=False)
                                        trv.heading(i, text=i)
                                    trv.insert("", 'end', iid=0, values=student)
                                    hs = ttk.Scrollbar(z2, orient='horizontal', command=trv.xview)
                                    trv.configure(xscrollcommand=hs.set)
                                    hs.grid(row=7, column=1, sticky="ew")
                                except:
                                    messagebox.showerror(title="Showing record",
                                                         message="There is No Record With This Id" + val)
                                    my_str1.set("Person Details")
                                    for item in trv.get_children():
                                        trv.delete(item)
                                    my_str.set("No Data Found")

                            z2.mainloop()

                        def profile_particular12():

                            def tab1():
                                z3 = Tk()

                                def dispropic(id):
                                    z3.destroy()
                                    my_w = tk.Tk()
                                    my_w.geometry("1490x745")
                                    my_w.configure(bg="#b3ffff")
                                    my_w.title("Result->Profile picture")
                                    icon = ImageTk.PhotoImage(file='windowBusIcon.png')
                                    my_w.wm_iconphoto(False, icon)
                                    try:
                                        my_conn = create_engine("mysql+mysqldb://root:password123@localhost/buseticket")
                                        my_row = ("SELECT profile_pic FROM person_details WHERE bet_id=%s")
                                        a = my_conn.execute(my_row, id)
                                        student = a.fetchone()
                                        img = Image.open(io.BytesIO(student[0]))
                                        img = ImageTk.PhotoImage(img)
                                        l2 = tk.Label(my_w, image=img)  # using Label
                                        l2.pack()
                                    except:
                                        label = Label(my_w,
                                                      text="Make sure to enter proper Bet_Id to view the profile picture",
                                                      font=('Arial', 25, 'bold'), bg="yellow")
                                        label.pack()
                                        messagebox.showerror(title="Search Profile picture->Error",
                                                             message="Sorry Invalid Bet_Id")

                                    def tab2():
                                        my_w.destroy()
                                        tab1()

                                    back = tk.Button(my_w, text="Back", font=('Arial', 15, 'bold'), bg="red",
                                                     command=lambda: tab2())  # using Button
                                    back.pack()
                                    my_w.mainloop()

                                z3.geometry("1490x745")
                                z3.title("Searching profile picture")
                                icon = ImageTk.PhotoImage(file='windowBusIcon.png')
                                z3.wm_iconphoto(False, icon)
                                z3.configure(bg='#b3ffff')
                                z3.geometry("1475x745")
                                l1 = Label(z3, text='Enter BET ID ', bg='yellow', width=40)
                                l1.grid(row=3, column=1)
                                e1 = Entry(z3, width=10, bg='white', font=22)
                                e1.grid(row=3, column=2, padx=5)
                                b1 = Button(z3, text='Show Details', width=15, bg='green',
                                            command=lambda: dispropic(e1.get()))
                                b1.grid(row=3, column=4, padx=5, pady=20)

                                def my_command():
                                    z3.destroy()
                                    HOME_BUTTON_PAGE()

                                click_btn = PhotoImage(file='Small_Home_ Icon.png')
                                button = Button(z3, image=click_btn, command=my_command)
                                button.grid(row=0, column=0)

                                def my_command1():
                                    z3.destroy()
                                    SHOW_DATA_PAGE()

                                click_btn1 = PhotoImage(file='small_back_icon.png')
                                button1 = Button(z3, image=click_btn1, command=my_command1)
                                button1.grid(row=0, column=1)
                                z3.mainloop()

                            tab1()

                        def SHOW_DATA_PAGE():
                            a2 = Tk()
                            a2.geometry("1490x745")
                            a2.title("Searching Details for user")
                            icon = ImageTk.PhotoImage(file='windowBusIcon.png')
                            a2.wm_iconphoto(False, icon)
                            cana = Canvas(a2, width=800, height=800)
                            cana.pack(fill="both", expand=True)
                            img2 = Image.open("searchimageforwindow.png")
                            resize3 = img2.resize((1490, 745))
                            new2 = ImageTk.PhotoImage(resize3)
                            cana.create_image(0, 0, image=new2, anchor='nw')

                            show_part_photo = PhotoImage(file='search_particular_icon.png')
                            show_particular_label = Label(a2, fg='#00FF00', bg='white', relief=RAISED, bd=10, padx=0,
                                                          pady=0,
                                                          image=show_part_photo, compound='top')
                            show_particular_label.place(x=150, y=20)

                            def show_particular1():
                                a2.destroy()
                                show_particular()

                            show_particular_button = Button(a2, text="Show Particular\n  Record",
                                                            font=('Arial', 20, 'bold'),
                                                            command=show_particular1)
                            show_particular_button.place(x=200, y=350)
                            show_all_photo = PhotoImage(file='search_all_icon.png')
                            show_all_label = Label(a2, fg='#00FF00', bg='white', relief=RAISED, bd=10, padx=0, pady=0,
                                                   image=show_all_photo, compound='top')
                            show_all_label.place(x=550, y=20)

                            def show_all1():
                                a2.destroy()
                                show_all()

                            show_all_button = Button(a2, text="Show All Record\n", font=('Arial', 20, 'bold'),
                                                     command=show_all1)
                            show_all_button.place(x=590, y=350)

                            profile_photo = PhotoImage(file='profilepic_show_icon.png')
                            profile_particular_label = Label(a2, fg='#00FF00', bg='white', relief=RAISED, bd=10, padx=0,
                                                             pady=0,
                                                             image=profile_photo, compound='top')
                            profile_particular_label.place(x=950, y=20)

                            def profile_particular1():
                                a2.destroy()
                                profile_particular12()

                            profile_particular_button = Button(a2, text="Show Particular Profile\nPicture",
                                                               font=('Arial', 20, 'bold'),
                                                               command=profile_particular1)
                            profile_particular_button.place(x=940, y=350)

                            def my_command():
                                a2.destroy()
                                HOME_BUTTON_PAGE()

                            click_btn = PhotoImage(file='Small_Home_ Icon.png')
                            button = Button(a2, image=click_btn, command=my_command)
                            button.place(x=0, y=10)

                            def my_command1():
                                a2.destroy()
                                MANAGING_BET()

                            click_btn1 = PhotoImage(file='small_back_icon.png')
                            button1 = Button(a2, image=click_btn1, command=my_command1)
                            button1.place(x=65, y=10)
                            a2.mainloop()

                        SHOW_DATA_PAGE()

                    def modify_Bet():
                        # newwn.destroy()

                        def Modify_data12():
                            # a3.destroy()

                            root = Tk()

                            cnx = mysql.connector.connect(
                                user='root',
                                password='password123',
                                host='localhost',
                                database='buseticket'
                            )
                            cursor = cnx.cursor()

                            # GUI for modifying data

                            root.title("Modify details")
                            root.geometry("1490x745")
                            icon = ImageTk.PhotoImage(file='windowBusIcon.png')
                            root.wm_iconphoto(False, icon)
                            cana = Canvas(root, width=800, height=800)
                            cana.pack(fill="both", expand=True)
                            img2 = Image.open("bgforwindow6.png")
                            resize3 = img2.resize((1490, 745))
                            new2 = ImageTk.PhotoImage(resize3)
                            cana.create_image(0, 0, image=new2, anchor='nw')

                            def nextpage(val):
                                global va1
                                val1 = val

                                def fetch_data(val1):

                                    id = val1
                                    query = "SELECT * FROM person_details WHERE bet_id = %s"
                                    cursor.execute(query, (id,))
                                    result = cursor.fetchone()
                                    if result:
                                        name = StringVar()
                                        NAME = name.get()
                                        address1 = StringVar()
                                        ADDRESS = address1.get()
                                        pincode1 = StringVar()
                                        PINCODE = pincode1.get()
                                        aadhar1 = StringVar()
                                        AADHARNO = aadhar1.get()
                                        BETID = StringVar()
                                        BETid = BETID.get()
                                        district = StringVar()
                                        DISTRICT = district.get()
                                        state = StringVar()
                                        STATE = state.get()
                                        valid_date = StringVar()
                                        VALID_DATE = valid_date.get()
                                        expire_date = StringVar()
                                        EXPIRE_DATE = expire_date.get()
                                        mobile1 = StringVar()
                                        MOBILE = mobile1.get()
                                        dob = StringVar()
                                        DOB = dob.get()
                                        college1 = StringVar()
                                        COLLEGE = college1.get()
                                        price = StringVar()
                                        PRICE = price.get()
                                        form_123 = StringVar()
                                        FORM12 = form_123.get()
                                        to_123 = StringVar()
                                        TO12 = to_123.get()
                                        form_1223 = StringVar()
                                        FORM122 = form_1223.get()
                                        to_1223 = StringVar()
                                        TO122 = to_1223.get()
                                        font = Label(root, text="Modify your Bus E-Ticket", font=('Arial', 22, 'bold'),
                                                     bg="#b3ffff")
                                        font.place(x=200, y=25)
                                        BETid_label = Label(root, text="BET id", font=('Arial', 15, 'bold'),
                                                            bg="#ffff4d")
                                        BETid_label.place(x=50, y=100)
                                        BETid_entry = Entry(root, textvariable=BETid, width=35)
                                        BETid_entry.place(x=175, y=100, width=100)
                                        name = Label(root, text="Name", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        name.place(x=50, y=150)
                                        name_entry = Entry(root, textvariable=NAME, width=35)
                                        name_entry.place(x=175, y=150, width=100)
                                        Address = Label(root, text="Address", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        Address.place(x=50, y=200)
                                        Address_entry = Entry(root, textvariable=ADDRESS, width=35)
                                        Address_entry.place(x=175, y=200, width=100)
                                        pincode = Label(root, text="Pincode", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        pincode.place(x=50, y=250)
                                        pincode_entry = Entry(root, textvariable=PINCODE, width=35)
                                        pincode_entry.place(x=175, y=250, width=100)
                                        district_label = Label(root, text="District", font=('Arial', 15, 'bold'),
                                                               bg="#ffff4d")
                                        district_label.place(x=50, y=300)
                                        district_entry = Entry(root, textvariable=DISTRICT, width=35)
                                        district_entry.place(x=175, y=300, width=100)
                                        state = Label(root, text="State", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        state.place(x=50, y=350)
                                        state_entry = Entry(root, textvariable=STATE, width=35)
                                        state_entry.place(x=175, y=350, width=100)
                                        aadhar = Label(root, text="Aadhar No", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        aadhar.place(x=50, y=400)
                                        aadhar_entry = Entry(root, textvariable=AADHARNO, width=35)
                                        aadhar_entry.place(x=175, y=400, width=100)
                                        college_label = Label(root, text="College Name", font=('Arial', 15, 'bold'),
                                                              bg="#ffff4d")
                                        college_label.place(x=700, y=50)
                                        college_entry = Entry(root, textvariable=COLLEGE, width=35)
                                        college_entry.place(x=850, y=50, width=100)
                                        valid_date_label = Label(root, text="Valid From", font=('Arial', 15, 'bold'),
                                                                 bg="#ffff4d")
                                        valid_date_label.place(x=700, y=100)
                                        valid_date_entry = Entry(root, textvariable=VALID_DATE, width=35)
                                        valid_date_entry.place(x=850, y=100, width=100)
                                        expire_date_label = Label(root, text="Expire Till", font=('Arial', 15, 'bold'),
                                                                  bg="#ffff4d")
                                        expire_date_label.place(x=700, y=150)
                                        expire_date_entry = Entry(root, textvariable=EXPIRE_DATE, width=35)
                                        expire_date_entry.place(x=850, y=150, width=100)
                                        mobileno = Label(root, text="Mobile No", font=('Arial', 15, 'bold'),
                                                         bg="#ffff4d")
                                        mobileno.place(x=700, y=250)
                                        mobileno_entry = Entry(root, textvariable=MOBILE, width=35)
                                        mobileno_entry.place(x=850, y=250, width=100)
                                        part1 = Label(root, text="Part-I", font=('Arial', 12, 'bold'), bg="#cc0099")
                                        part1.place(x=700, y=350)
                                        from1_label = Label(root, text="From-I", font=('Arial', 15, 'bold'),
                                                            bg="#ffff4d")
                                        from1_label.place(x=700, y=400)
                                        from12 = Entry(root, textvariable=FORM12, width=35)
                                        from12.place(x=850, y=400)
                                        to1_label = Label(root, text="To-I", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        to1_label.place(x=700, y=450)
                                        to12 = Entry(root, textvariable=TO12, width=35)
                                        to12.place(x=850, y=450)
                                        part2 = Label(root, text="Part-II", font=('Arial', 12, 'bold'), bg="#cc0099")
                                        part2.place(x=700, y=500)
                                        from2_label = Label(root, text="From-II", font=('Arial', 15, 'bold'),
                                                            bg="#ffff4d")
                                        from2_label.place(x=700, y=550)
                                        from22 = Entry(root, textvariable=FORM122, width=35)
                                        from22.place(x=850, y=550)
                                        to2_label = Label(root, text="To-II", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        to2_label.place(x=700, y=600)
                                        to22 = Entry(root, textvariable=TO122, width=35)
                                        to22.place(x=850, y=600)
                                        attendant = StringVar()
                                        ATTENDANT = attendant.get()
                                        attendant_label = Label(root, text="Attendant Name", font=('Arial', 15, 'bold'),
                                                                bg="#ffff4d")
                                        attendant_label.place(x=700, y=650)
                                        attendant_entry = Entry(root, textvariable=ATTENDANT, width=35)
                                        attendant_entry.place(x=900, y=650, width=100)
                                        debo_label = Label(root, text="Depot", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        debo_label.place(x=50, y=450)
                                        debo = StringVar()
                                        DEBO = debo.get()
                                        debo1 = Entry(root, textvariable=DEBO, width=35)
                                        debo1.place(x=175, y=450)
                                        ticket_label = Label(root, text="Ticket Type", font=('Arial', 15, 'bold'),
                                                             bg="#ffff4d")
                                        ticket_label.place(x=50, y=500)
                                        ticket = StringVar()
                                        TICKET = ticket.get()
                                        Ticket1 = Entry(root, textvariable=TICKET, width=35)
                                        Ticket1.place(x=175, y=500)
                                        age1 = StringVar()
                                        AGE = age1.get()
                                        age = Label(root, text="Age", font=('Arial', 15, 'bold'), bg="#ffff4d")
                                        age.place(x=50, y=550)
                                        age_entry = Entry(root, textvariable=AGE, width=35)
                                        age_entry.place(x=175, y=550, width=100)
                                        price_label = Label(root, text="Price", font=('Arial', 15, 'bold'),
                                                            bg="#ffff4d")
                                        price_label.place(x=50, y=600)
                                        price_entry = Entry(root, textvariable=PRICE, width=35)
                                        price_entry.place(x=175, y=600)
                                        disability = StringVar()
                                        DISABILITY = disability.get()
                                        disability_label = Label(root, text="Disability %", font=('Arial', 15, 'bold'),
                                                                 bg="#ffff4d")
                                        disability_label.place(x=50, y=650)
                                        disability_entry = Entry(root, textvariable=DISABILITY, width=35)
                                        disability_entry.place(x=175, y=650, width=100)
                                        gender_label = Label(root, text="Gender", font=('Arial', 15, 'bold'),
                                                             bg="#ffff4d")
                                        gender_label.place(x=700, y=200)
                                        gender = StringVar()
                                        GENDER = gender.get()
                                        gender1 = Entry(root, textvariable=GENDER, width=35)
                                        gender1.place(x=850, y=200)
                                        dob_label = Label(root, text="Date of Birth", font=('Arial', 15, 'bold'),
                                                          bg="#ffff4d")
                                        dob_label.place(x=700, y=300)
                                        dob_entry = Entry(root, textvariable=DOB, width=35)
                                        dob_entry.place(x=850, y=300, width=100)

                                        BETid_entry.insert(0, result[0])
                                        name_entry.insert(0, result[1])
                                        Address_entry.insert(0, result[2])
                                        pincode_entry.insert(0, result[3])
                                        district_entry.insert(0, result[4])
                                        state_entry.insert(0, result[5])
                                        aadhar_entry.insert(0, result[6])
                                        debo1.insert(0, result[7])
                                        Ticket1.insert(0, result[8])
                                        valid_date_entry.insert(0, result[9])
                                        expire_date_entry.insert(0, result[10])
                                        price_entry.insert(0, result[11])
                                        mobileno_entry.insert(0, result[12])
                                        college_entry.insert(0, result[13])
                                        from12.insert(0, result[14])
                                        to12.insert(0, result[15])
                                        from22.insert(0, result[16])
                                        to22.insert(0, result[17])
                                        age_entry.insert(0, result[19])
                                        gender1.insert(0, result[21])
                                        dob_entry.insert(0, result[22])
                                        disability_entry.insert(0, result[24])
                                        attendant_entry.insert(0, result[26])

                                        def generate():
                                            input_path = filedialog.asksaveasfilename(title="save image", filetypes=(
                                                ("PNG File", ".png"), ("All Files", "*.*")))
                                            if input_path:
                                                if input_path.endswith(".png"):
                                                    get_code = pyqrcode.create(
                                                        "BET ID:" + BETid_entry.get() + "\n" + "NAME:" + name_entry.get() + "\n" + "AGE:" + age_entry.get() + "\n" + "RESIDENTIAL ADDRESS:" + Address_entry.get() + "\n" + "PINCODE:" + pincode_entry.get() + "\n" + "DISTRICT:" + district_entry.get() + "\n" + "STATE:" + state_entry.get() + "\n" + "AADHHAR NO:" + aadhar_entry.get() + "\n" + "DEPOT:" + debo1.get() + "\n" + "COLLEGE NAME:" + college_entry.get() + "\n" + "BUS E-TICKET TYPE:" + ticket.get() + "\n" + "VALID FROM:" + valid_date_entry.get() + "\n" + "EXPIRE TILL:" + expire_date_entry.get() + "COLLEGE NAME:" + college_entry.get() + "\n" + "GENDER:" + gender.get() + "\n" + "MOBILE NO:" + mobileno_entry.get() + "\n" + "DATE OF BIRTH:" + dob_entry.get() + "\n" + "FROM-I:" + from12.get() + "\n" + "TO-I:" + to12.get() + "\n" + "FROM-II:" + from22.get() + "\n" + "TO-II:" + to22.get() + "\n" + "ATTENDANT NAME:" + attendant_entry.get() + "\n" + "DISABILITY PERCENTAGE:" + disability_entry.get() + "\n")
                                                    get_code.png(input_path, scale=5)
                                                    with Image.open(input_path) as img:
                                                        img_resized = img.resize((200, 200))
                                                        img_resized.save(input_path)
                                                    messagebox.showinfo(title="Generate QR-code",
                                                                        message=f"Successfully Generated QR-Code For Details \n QR code saved to {input_path}")

                                                else:
                                                    input_path = f'{input_path}.png'
                                                    get_code = pyqrcode.create(
                                                        "BET ID:" + BETid_entry.get() + "\n" + "NAME:" + name_entry.get() + "\n" + "AGE:" + age_entry.get() + "\n" + "RESIDENTIAL ADDRESS:" + Address_entry.get() + "\n" + "PINCODE:" + pincode_entry.get() + "\n" + "DISTRICT:" + district_entry.get() + "\n" + "STATE:" + state_entry.get() + "\n" + "AADHHAR NO:" + aadhar_entry.get() + "\n" + "DEPOT:" + debo1.get() + "\n" + "COLLEGE NAME:" + college_entry.get() + "\n" + "BUS E-TICKET TYPE:" + ticket.get() + "\n" + "VALID FROM:" + valid_date_entry.get() + "\n" + "EXPIRE TILL:" + expire_date_entry.get() + "COLLEGE NAME:" + college_entry.get() + "\n" + "GENDER:" + gender.get() + "\n" + "MOBILE NO:" + mobileno_entry.get() + "\n" + "DATE OF BIRTH:" + dob_entry.get() + "\n" + "FROM-I:" + from12.get() + "\n" + "TO-I:" + to12.get() + "\n" + "FROM-II:" + from22.get() + "\n" + "TO-II:" + to22.get() + "\n" + "ATTENDANT NAME:" + attendant_entry.get() + "\n" + "DISABILITY PERCENTAGE:" + disability_entry.get() + "\n")
                                                    get_code.png(input_path, scale=5)
                                                    with Image.open(input_path) as img:
                                                        img_resized = img.resize((200, 200))
                                                        img_resized.save(input_path)
                                                    messagebox.showinfo(title="Generate QR-code",
                                                                        message=f"Successfully Generated QR-Code For Details \n QR code saved to {input_path}")

                                        def switchButtonState2():
                                            if (generate_button['state'] == DISABLED):
                                                generate_button['state'] = NORMAL

                                        def modify_data():
                                            a = BETid_entry.get()
                                            b = name_entry.get()
                                            c = Address_entry.get()
                                            d = pincode_entry.get()
                                            e = district_entry.get()
                                            f = state_entry.get()
                                            g = aadhar_entry.get()
                                            h = debo1.get()
                                            i = Ticket1.get()
                                            j = valid_date_entry.get()
                                            k = expire_date_entry.get()
                                            l = price_entry.get()
                                            m = mobileno_entry.get()
                                            n = college_entry.get()
                                            o = from12.get()
                                            p = to12.get()
                                            q = from22.get()
                                            r = to22.get()
                                            s = age_entry.get()
                                            t = gender1.get()
                                            u = dob_entry.get()
                                            v = disability_entry.get()
                                            w = attendant_entry.get()
                                            switchButtonState2()
                                            query = "UPDATE person_details SET name = %s,address = %s,pincode=%s,district=%s,state=%s,aadhar_no=%s,depot=%s,ticket_type=%s,valid_from=%s,expire_till=%s,price_amount=%s,mobile_no=%s,college=%s,from_I=%s,to_I=%s,from_II=%s,to_II=%s,age=%s,gender=%s,date_of_birth=%s,disability_percentage=%s,attendant_name=%s WHERE bet_id = %s"
                                            cursor.execute(query, (
                                                b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, a))
                                            cnx.commit()
                                            messagebox.showinfo("Info", "Data updated successfully")

                                            # Button to modify data

                                        modify_button = Button(root, text="Modify Data", font=('Arial', 12, 'bold'),
                                                               command=modify_data, bg="cyan")
                                        modify_button.place(x=1200, y=500)
                                        generate_button = Button(root, text="Generate QRcode",
                                                                 font=('Arial', 12, 'bold'),
                                                                 bg="green", command=generate, state=DISABLED)
                                        generate_button.place(x=1200, y=550)

                                        def calling():
                                            font.destroy()
                                            BETid_label.destroy()
                                            BETid_entry.destroy()
                                            name_entry.destroy()
                                            name.destroy()
                                            Address.destroy()
                                            Address_entry.destroy()
                                            pincode.destroy()
                                            pincode_entry.destroy()
                                            disability_label.destroy()
                                            disability_entry.destroy()
                                            district_label.destroy()
                                            district_entry.destroy()
                                            state.destroy()
                                            state_entry.destroy()
                                            aadhar.destroy()
                                            aadhar_entry.destroy()
                                            college_label.destroy()
                                            college_entry.destroy()
                                            valid_date_label.destroy()
                                            valid_date_entry.destroy()
                                            expire_date_label.destroy()
                                            expire_date_entry.destroy()
                                            mobileno.destroy()
                                            mobileno_entry.destroy()
                                            part1.destroy()
                                            part2.destroy()
                                            from1_label.destroy()
                                            from2_label.destroy()
                                            from12.destroy()
                                            from22.destroy()
                                            to1_label.destroy()
                                            to2_label.destroy()
                                            to12.destroy()
                                            to22.destroy()
                                            debo_label.destroy()
                                            debo1.destroy()
                                            ticket_label.destroy()
                                            Ticket1.destroy()
                                            age.destroy()
                                            age_entry.destroy()
                                            attendant_label.destroy()
                                            attendant_entry.destroy()
                                            price_label.destroy()
                                            price_entry.destroy()
                                            dob_entry.destroy()
                                            dob_label.destroy()
                                            gender_label.destroy()
                                            gender1.destroy()
                                            back_button.destroy()
                                            modify_button.destroy()
                                            generate_button.destroy()
                                            frontpage()

                                        back_button = Button(root, text="Back", font=('Arial', 12, 'bold'),
                                                             command=calling,
                                                             bg="red")
                                        back_button.place(x=1200, y=600)



                                    else:

                                        tk.messagebox.showinfo("Info", "No data found for this ID")
                                        frontpage()

                                fetch_data(val1)

                                root.mainloop()

                            def frontpage():
                                def nextpage1(id):
                                    BETid_entry1.destroy()
                                    BETid_label1.destroy()
                                    fetch_button1.destroy()
                                    val = id
                                    nextpage(val)

                                    BETid_entry1.destroy()
                                    BETid_label1.destroy()
                                    fetch_button1.destroy()

                                BETID = StringVar()
                                BETid = BETID.get()
                                BETid_label1 = Label(root, text="Enter BET ID", font=('Arial', 15, 'bold'),
                                                     bg="#ffff4d")
                                BETid_label1.place(x=50, y=100)
                                BETid_entry1 = Entry(root, textvariable=BETid, width=35)
                                BETid_entry1.place(x=210, y=100, width=100)
                                fetch_button1 = Button(root, text="Fetch Data", font=('Arial', 10, 'bold'), bg="green",
                                                       command=lambda: nextpage1(BETid_entry1.get()))
                                fetch_button1.place(x=350, y=100)

                            frontpage()

                            def my_command():
                                root.destroy()
                                HOME_BUTTON_PAGE()

                            click_btn = PhotoImage(file='Small_Home_ Icon.png')
                            button = Button(root, image=click_btn, command=my_command)
                            button.place(x=30, y=25)

                            def my_command1():
                                root.destroy()
                                MODIFYrDELETE_BET_PAGE()

                            click_btn1 = PhotoImage(file='small_back_icon.png')
                            button1 = Button(root, image=click_btn1, command=my_command1)
                            button1.place(x=95, y=25)
                            root.mainloop()

                            cursor.close()
                            cnx.close()

                        def Delete_data():
                            # a3.destroy()

                            def delete_record():
                                # Connect to the MySQL database
                                mydb = mysql.connector.connect(
                                    host="localhost",
                                    user="root",
                                    password="password123",
                                    database="buseticket"
                                )
                                cursor = mydb.cursor()
                                id = entry_id.get()
                                # Check if the record exists
                                record_exists = False
                                sql = "SELECT * FROM person_details WHERE bet_id = %s"
                                values = (id,)
                                cursor.execute(sql, values)
                                result = cursor.fetchone()
                                if result:
                                    record_exists = True

                                # Delete the record if it exists
                                my_var = messagebox.askyesnocancel(title="Delete Record",
                                                                   message="Are you sure to delete " + id + " Record")
                                if my_var:
                                    if record_exists:
                                        sql = "DELETE FROM person_details WHERE bet_id = %s"
                                        cursor.execute(sql, values)
                                        mydb.commit()
                                        messagebox.showinfo(title="Delete Record",
                                                            message="Record with ID " + id + " has been deleted Successfully")


                                    elif (id == ""):
                                        messagebox.showwarning(title="Delete Record",
                                                               message="Please,Make Sure to Enter a Bet_id")


                                    else:
                                        messagebox.showerror(title="Delete Record",
                                                             message="Sorry,There is No Record with ID " + id)

                            # Tkinter GUI code
                            root1 = tk.Tk()
                            root1.geometry("1490x745")
                            root1.title("Delete Record")
                            icon = ImageTk.PhotoImage(file='windowBusIcon.png')
                            root1.wm_iconphoto(False, icon)
                            cana = Canvas(root1, width=800, height=800)
                            cana.pack(fill="both", expand=True)
                            img2 = Image.open("busbg.png")
                            resize3 = img2.resize((1490, 745))
                            new2 = ImageTk.PhotoImage(resize3)
                            cana.create_image(0, 0, image=new2, anchor='nw')
                            label_id = tk.Label(root1, text="Delete Your Bus E-Ticket", bg="light blue",
                                                font=('Arial', 22, 'bold'), )
                            label_id.place(x=200, y=50)
                            root1.title("Delete Record")
                            label_id = tk.Label(root1, text="BET ID", bg="yellow", font=('Arial', 15, 'bold'), )
                            label_id.place(x=175, y=150)

                            entry_id = tk.Entry(root1)
                            entry_id.place(x=250, y=150)
                            delete_button = tk.Button(root1, text="Delete Record", bg="red", font=('Arial', 14, 'bold'),
                                                      command=delete_record)
                            delete_button.place(x=200, y=200)
                            label_result = tk.Label(root1, font=('Arial', 18, 'bold'), bg="cyan")
                            label_result.place(x=300, y=300)

                            def my_command():
                                root1.destroy()
                                HOME_BUTTON_PAGE()

                            click_btn = PhotoImage(file='Small_Home_ Icon.png')
                            button = Button(root1, image=click_btn, command=my_command)
                            button.place(x=30, y=25)

                            def my_command1():
                                root1.destroy()
                                MODIFYrDELETE_BET_PAGE()

                            click_btn1 = PhotoImage(file='small_back_icon.png')
                            button1 = Button(root1, image=click_btn1, command=my_command1)
                            button1.place(x=95, y=25)
                            root1.mainloop()

                        def MODIFYrDELETE_BET_PAGE():
                            a3 = Tk()
                            a3.geometry("1490x745")
                            a3.title("Modifying Data")
                            icon = ImageTk.PhotoImage(file='windowBusIcon.png')
                            a3.wm_iconphoto(False, icon)
                            cana = Canvas(a3, width=800, height=800)
                            cana.pack(fill="both", expand=True)
                            img2 = Image.open("bgforwindow5.png")
                            resize3 = img2.resize((1490, 745))
                            new2 = ImageTk.PhotoImage(resize3)
                            cana.create_image(0, 0, image=new2, anchor='nw')
                            # create BeT icon
                            modify_Bet_photo = PhotoImage(file='modifydata_icon.png')
                            modify_Bet_label = Label(a3, fg='#00FF00', bg='white', relief=RAISED, bd=10, padx=0, pady=0,
                                                     image=modify_Bet_photo, compound='top')
                            modify_Bet_label.place(x=150, y=20)

                            def Modify_data11():
                                a3.destroy()
                                Modify_data12()

                            modify_Bet_button = Button(a3, text="Modify\nBus E-Ticket", font=('Arial', 20, 'bold'),
                                                       command=Modify_data11)
                            modify_Bet_button.place(x=200, y=350)
                            # show_Bet_record icon
                            delete_Bet_photo = PhotoImage(file='delete_icon.png')
                            delete_Bet_label = Label(a3, fg='#00FF00', bg='white', relief=RAISED, bd=10, padx=0, pady=0,
                                                     image=delete_Bet_photo, compound='top')
                            delete_Bet_label.place(x=550, y=20)

                            def Delete_data1():
                                a3.destroy()
                                Delete_data()

                            delete_Bet_button = Button(a3, text="Delete Bus E-Ticket\n  Record ",
                                                       font=('Arial', 20, 'bold'),
                                                       command=Delete_data1)
                            delete_Bet_button.place(x=570, y=350)

                            def my_command():
                                a3.destroy()
                                HOME_BUTTON_PAGE()

                            click_btn = PhotoImage(file='Small_Home_ Icon.png')
                            button = Button(a3, image=click_btn, command=my_command)
                            button.place(x=0, y=10)

                            def my_command1():
                                a3.destroy()
                                MANAGING_BET()

                            click_btn1 = PhotoImage(file='small_back_icon.png')
                            button1 = Button(a3, image=click_btn1, command=my_command1)
                            button1.place(x=65, y=10)
                            a3.mainloop()

                        MODIFYrDELETE_BET_PAGE()

                    wn.destroy()

                    def MANAGING_BET():
                        newwn = Tk()
                        newwn.geometry("1490x745")
                        newwn.title("Managing Bus E-Ticket")
                        icon = ImageTk.PhotoImage(file='windowBusIcon.png')
                        newwn.wm_iconphoto(False, icon)
                        cana = Canvas(newwn, width=800, height=800)
                        cana.pack(fill="both", expand=True)
                        img2 = Image.open("bgforwindow5.png")
                        resize3 = img2.resize((1490, 745))
                        new2 = ImageTk.PhotoImage(resize3)
                        cana.create_image(0, 0, image=new2, anchor='nw')
                        # create BeT icon
                        create_Bet_photo = PhotoImage(file='createimg.png')
                        create_Bet_label = Label(newwn, fg='#00FF00', bg='white', relief=RAISED, bd=10, padx=0, pady=0,
                                                 image=create_Bet_photo, compound='top')
                        create_Bet_label.place(x=150, y=20)

                        def create1():
                            newwn.destroy()
                            create_Bet()

                        create_Bet_button = Button(newwn, text="Create & Apply\nBus E-Ticket",
                                                   font=('Arial', 20, 'bold'),
                                                   command=create1)
                        create_Bet_button.place(x=200, y=350)
                        # show_Bet_record icon
                        show_Bet_photo = PhotoImage(file='showimg.png')
                        show_Bet_label = Label(newwn, fg='#00FF00', bg='white', relief=RAISED, bd=10, padx=0, pady=0,
                                               image=show_Bet_photo, compound='top')
                        show_Bet_label.place(x=550, y=20)

                        def show1():
                            newwn.destroy()
                            show_Bet()

                        show_Bet_button = Button(newwn, text="Show Bus E-Ticket\n  Record ", font=('Arial', 20, 'bold'),
                                                 command=show1)
                        show_Bet_button.place(x=570, y=350)
                        # modify_beticon
                        modify_bet_photo = PhotoImage(file='modifyimg.png')
                        modify_bet_label = Label(newwn, fg='#00FF00', bg='white', relief=RAISED, bd=10, padx=0, pady=0,
                                                 image=modify_bet_photo, compound='top')
                        modify_bet_label.place(x=950, y=20)

                        def modify1():
                            newwn.destroy()
                            modify_Bet()

                        modify_bet_button = Button(newwn, text="Modify/Delete Bus \nE-Ticket  Record",
                                                   font=('Arial', 20, 'bold'),
                                                   command=modify1)
                        modify_bet_button.place(x=975, y=350)

                        def my_command():
                            newwn.destroy()
                            HOME_BUTTON_PAGE()

                        click_btn = PhotoImage(file='Small_Home_ Icon.png')
                        button = Button(newwn, image=click_btn, command=my_command)
                        button.place(x=0, y=10)
                        newwn.mainloop()

                    MANAGING_BET()

                def photo():
                    wn.destroy()
                    # Define the list of images and their names
                    images = [
                        {
                            "name": "COVID-19 SAFETY AWARENESS AND SAFETY BUS OPERATION",
                            "file": "img36.jpg",
                        },
                        {
                            "name": "MTC - MD PRESENTED COMPLIMENTARY GIFTS TO OUR CREWS",
                            "file": "img4.jpg",
                        },
                        {
                            "name": "MTC - AWARDS",
                            "file": "img27.jpg",
                        },
                        {
                            "name": "ALL MDS MEETING",
                            "file": "img21.png",
                        },
                        {
                            "name": "ALL MDS MEETING",
                            "file": "img22.jpg",
                        },
                        {
                            "name": "ALL MDS MEETING",
                            "file": "img23.png",
                        },

                        {
                            "name": "ALL MDS MEETING",
                            "file": "img24.png",
                        },

                        {
                            "name": "ALL MDS MEETING",
                            "file": "img25.png",
                        },
                        {
                            "name": "ALL MDS MEETING",
                            "file": "img26.png",
                        },

                        {
                            "name": "75th INDEPENDENCE DAY",
                            "file": "img5.jpg",
                        },
                        {
                            "name": "75th INDEPENDENCE DAY",
                            "file": "img6.jpg",
                        },
                        {
                            "name": "75th INDEPENDENCE DAY",
                            "file": "img7.jpg",
                        },
                        {
                            "name": "75th INDEPENDENCE DAY",
                            "file": "img8.jpg",
                        },

                        {
                            "name": "75th INDEPENDENCE DAY",
                            "file": "img9.jpg",
                        },

                        {
                            "name": "75th INDEPENDENCE DAY",
                            "file": "img10.jpg",
                        },
                        {
                            "name": "75th INDEPENDENCE DAY",
                            "file": "img11.jpg",
                        },
                        {
                            "name": "75th INDEPENDENCE DAY",
                            "file": "img12.jpg",
                        },
                        {
                            "name": "75th INDEPENDENCE DAY",
                            "file": "img13.jpg",
                        },
                        {
                            "name": "75th INDEPENDENCE DAY",
                            "file": "img14.jpg",
                        },

                        {
                            "name": "75th INDEPENDENCE DAY",
                            "file": "img15.jpg",
                        },

                        {
                            "name": "75th INDEPENDENCE DAY",
                            "file": "img16.jpg",
                        },
                        {
                            "name": "75th INDEPENDENCE DAY",
                            "file": "img17.jpg",
                        },
                        {
                            "name": "75th INDEPENDENCE DAY",
                            "file": "img18.jpg",
                        },
                        {
                            "name": "75th INDEPENDENCE DAY",
                            "file": "img19.jpg",
                        },
                        {
                            "name": "75th INDEPENDENCE DAY",
                            "file": "img20.jpg",
                        },
                        {
                            "name": "72ND REPUBLIC DAY",
                            "file": "img28.jpg",
                        },
                        {
                            "name": "72ND REPUBLIC DAY",
                            "file": "img29.jpg",
                        },

                        {
                            "name": "32-ND ROAD SAFETY MONTH",
                            "file": "img30.jpg",
                        },
                        {
                            "name": "32-ND ROAD SAFETY MONTH",
                            "file": "img31.jpg",
                        },
                        {
                            "name": "32-ND ROAD SAFETY MONTH",
                            "file": "img32.jpg",
                        },
                        {
                            "name": "32-ND ROAD SAFETY MONTH",
                            "file": "img33.jpg",
                        },
                        {
                            "name": "32-ND ROAD SAFETY MONTH",
                            "file": "img34.jpg",
                        },
                        {
                            "name": "32-ND ROAD SAFETY MONTH",
                            "file": "img35.jpg",
                        },
                        {
                            "name": "15th UMI awards",
                            "file": "img1.png",
                        },
                        {
                            "name": "15th UMI awards",
                            "file": "img2.png",
                        },
                        {
                            "name": "15th UMI awards",
                            "file": "img3.png",
                        },

                    ]
                    global current_image_index, current_image, current_image_name

                    # Initialize the current image index
                    current_image_index = 0

                    # Load the first image and its name
                    current_image = Image.open(images[current_image_index]["file"])
                    current_image_name = images[current_image_index]["name"]

                    # Define a function to display the next image
                    def show_next_image():
                        global current_image_index, current_image, current_image_name

                        # Increment the current image index
                        current_image_index += 1

                        # If the index is greater than or equal to the number of images, wrap around to the beginning
                        if current_image_index >= len(images):
                            current_image_index = 0

                        # Load the new image and its name
                        current_image = Image.open(images[current_image_index]["file"])
                        current_image_name = images[current_image_index]["name"]

                        # Update the label and image
                        label.config(text=current_image_name)
                        image_tk = ImageTk.PhotoImage(current_image)
                        canvas.itemconfigure(canvas_image, image=image_tk)
                        canvas.image = image_tk

                    # Define a function to display the previous image
                    def show_previous_image():
                        global current_image_index, current_image, current_image_name

                        # Decrement the current image index
                        current_image_index -= 1

                        # If the index is less than zero, wrap around to the end
                        if current_image_index < 0:
                            current_image_index = len(images) - 1

                        # Load the new image and its name
                        current_image = Image.open(images[current_image_index]["file"])
                        current_image_name = images[current_image_index]["name"]

                        # Update the label and image
                        label.config(text=current_image_name, bg="yellow", font=('Arial', 20, 'bold'))
                        image_tk = ImageTk.PhotoImage(current_image)
                        canvas.itemconfigure(canvas_image, image=image_tk)
                        canvas.image = image_tk

                    # Create the main window and widgets
                    c = tk.Tk()
                    c.geometry("1490x745")

                    def my_command():
                        c.destroy()
                        HOME_BUTTON_PAGE()

                    click_btn = PhotoImage(file='Small_Home_ Icon.png')
                    button = Button(c, image=click_btn, command=my_command, anchor="nw")
                    button.place(x=5, y=0)

                    c.title("Photo")
                    icon = ImageTk.PhotoImage(file='windowBusIcon.png')
                    c.wm_iconphoto(False, icon)
                    c.configure(bg='white')

                    label = tk.Label(c, text=current_image_name, bg="yellow", font=('Arial', 20, 'bold'))
                    label.place(x=250, y=65)

                    canvas = tk.Canvas(c, width=current_image.width, height=current_image.height)
                    canvas.place(x=100, y=105)

                    image_tk = ImageTk.PhotoImage(current_image)
                    canvas_image = canvas.create_image(0, 0, anchor="nw", image=image_tk)
                    canvas.image = image_tk

                    next_button = tk.Button(c, text="Next", bg="green", font=('Arial', 20, 'bold'),
                                            command=show_next_image)
                    next_button.place(x=725, y=600)

                    back_button = tk.Button(c, text="Back", bg="red", font=('Arial', 20, 'bold'),
                                            command=show_previous_image)
                    back_button.place(x=625, y=600)

                    # Run the application
                    c.mainloop()

                def about():
                    wn.destroy()

                    def History():
                        d1 = Tk()
                        d1.geometry("1490x745")
                        d1.title("About us")
                        icon = ImageTk.PhotoImage(file='windowBusIcon.png')
                        d1.wm_iconphoto(False, icon)
                        d1.configure(bg='white')
                        about_photo = PhotoImage(file='aboutus.png')
                        about_label1 = Label(d1, image=about_photo)
                        about_label1.place(x=125, y=50)
                        history_photo = PhotoImage(file='history.png')
                        history_label1 = Label(d1, image=history_photo)
                        history_label1.place(x=100, y=290)
                        growth_photo = PhotoImage(file='growth.png'
                                                  )
                        growth_label1 = Label(d1, image=growth_photo)
                        growth_label1.place(x=600, y=50)

                        def my_command():
                            d1.destroy()
                            HOME_BUTTON_PAGE()

                        click_btn = PhotoImage(file='Small_Home_ Icon.png')
                        button = Button(d1, image=click_btn, command=my_command)
                        button.place(x=30, y=25)

                        def my_command1():
                            d1.destroy()
                            ABOUT_PAGE()

                        click_btn1 = PhotoImage(file='small_back_icon.png')
                        button1 = Button(d1, image=click_btn1, command=my_command1)
                        button1.place(x=95, y=25)
                        d1.mainloop()

                    def busfare():
                        # Define the list of images and their names
                        images = [
                            {
                                "name": "Adult Wise Fare Amount in AC Bus Service ",
                                "file": "Ac_service.png",
                            },
                            {
                                "name": "Adult Wise Fare Amount in Deluxe Bus Service",
                                "file": "Deluxe_service.png",
                            },
                            {
                                "name": "Adult Wise Fare Amount in Express Bus Service",
                                "file": "express_service.png",
                            },
                            {
                                "name": "Adult Wise Fare Amount in Ordinary Bus Service",
                                "file": "ordinary_services.png",
                            },
                        ]
                        global current_image_index, current_image, current_image_name

                        # Initialize the current image index
                        current_image_index = 0

                        # Load the first image and its name
                        current_image = Image.open(images[current_image_index]["file"])
                        current_image_name = images[current_image_index]["name"]

                        # Define a function to display the next image
                        def show_next_image():
                            global current_image_index, current_image, current_image_name

                            # Increment the current image index
                            current_image_index += 1

                            # If the index is greater than or equal to the number of images, wrap around to the beginning
                            if current_image_index >= len(images):
                                current_image_index = 0

                            # Load the new image and its name
                            current_image = Image.open(images[current_image_index]["file"])
                            current_image_name = images[current_image_index]["name"]

                            # Update the label and image
                            label.config(text=current_image_name)
                            image_tk = ImageTk.PhotoImage(current_image)
                            canvas.itemconfigure(canvas_image, image=image_tk)
                            canvas.image = image_tk

                        # Define a function to display the previous image
                        def show_previous_image():
                            global current_image_index, current_image, current_image_name

                            # Decrement the current image index
                            current_image_index -= 1

                            # If the index is less than zero, wrap around to the end
                            if current_image_index < 0:
                                current_image_index = len(images) - 1

                            # Load the new image and its name
                            current_image = Image.open(images[current_image_index]["file"])
                            current_image_name = images[current_image_index]["name"]

                            # Update the label and image
                            label.config(text=current_image_name, bg="yellow", font=('Arial', 20, 'bold'))
                            image_tk = ImageTk.PhotoImage(current_image)
                            canvas.itemconfigure(canvas_image, image=image_tk)
                            canvas.image = image_tk

                        # Create the main window and widgets
                        d2 = tk.Tk()
                        d2.geometry("1490x745")

                        def my_command():
                            d2.destroy()
                            HOME_BUTTON_PAGE()

                        click_btn = PhotoImage(file='Small_Home_ Icon.png')
                        button = Button(d2, image=click_btn, command=my_command, anchor="nw")
                        button.place(x=5, y=0)

                        def my_command1():
                            d2.destroy()
                            ABOUT_PAGE()

                        click_btn1 = PhotoImage(file='small_back_icon.png')
                        button1 = Button(d2, image=click_btn1, command=my_command1, anchor="nw")
                        button1.place(x=70, y=0)

                        d2.title("Different Bus Fare And Adult Wise Fare")
                        icon = ImageTk.PhotoImage(file='windowBusIcon.png')
                        d2.wm_iconphoto(False, icon)
                        d2.configure(bg='white')

                        label = tk.Label(d2, text=current_image_name, bg="yellow", font=('Arial', 20, 'bold'))
                        label.place(x=425, y=65)

                        canvas = tk.Canvas(d2, width=current_image.width, height=current_image.height)
                        canvas.place(x=100, y=105)

                        image_tk = ImageTk.PhotoImage(current_image)
                        canvas_image = canvas.create_image(0, 0, anchor="nw", image=image_tk)
                        canvas.image = image_tk

                        next_button = tk.Button(d2, text="Next", bg="green", font=('Arial', 20, 'bold'),
                                                command=show_next_image)
                        next_button.place(x=725, y=500)

                        back_button = tk.Button(d2, text="Back", bg="red", font=('Arial', 20, 'bold'),
                                                command=show_previous_image)
                        back_button.place(x=625, y=500)

                        # Run the application
                        d2.mainloop()

                    def service():
                        d3 = Tk()
                        d3.geometry("1490x745")
                        d3.title("Service")
                        icon = ImageTk.PhotoImage(file='windowBusIcon.png')
                        d3.wm_iconphoto(False, icon)
                        d3.configure(bg='white')
                        service_photo = PhotoImage(file='bus_service.png')
                        service_label1 = Label(d3, image=service_photo)
                        service_label1.place(x=125, y=0)

                        def my_command():
                            d3.destroy()
                            HOME_BUTTON_PAGE()

                        click_btn = PhotoImage(file='Small_Home_ Icon.png')
                        button = Button(d3, image=click_btn, command=my_command)
                        button.place(x=30, y=25)

                        def my_command1():
                            d3.destroy()
                            ABOUT_PAGE()

                        click_btn1 = PhotoImage(file='small_back_icon.png')
                        button1 = Button(d3, image=click_btn1, command=my_command1)
                        button1.place(x=95, y=25)
                        d3.mainloop()

                    def ABOUT_PAGE():
                        d = Tk()
                        d.geometry("1490x745")
                        d.title("About")
                        icon = ImageTk.PhotoImage(file='windowBusIcon.png')
                        d.wm_iconphoto(False, icon)
                        cana = Canvas(d, width=800, height=800)
                        cana.pack(fill="both", expand=True)
                        img2 = Image.open("bgforwindow5.png")
                        resize3 = img2.resize((1490, 745))
                        new2 = ImageTk.PhotoImage(resize3)
                        cana.create_image(0, 0, image=new2, anchor='nw')
                        # create BeT icon
                        history_photo = PhotoImage(file='History_icon.png')
                        history_label = Label(d, fg='#00FF00', bg='white', relief=RAISED, bd=10, padx=0, pady=0,
                                              image=history_photo, compound='top')
                        history_label.place(x=150, y=20)

                        def history1():
                            d.destroy()
                            History()

                        history_button = Button(d, text="About us", font=('Arial', 20, 'bold'),
                                                command=history1)
                        history_button.place(x=250, y=350)
                        # show_Bet_record icon
                        busfare_photo = PhotoImage(file='bus_fare_icon.png')
                        busfare_label = Label(d, fg='#00FF00', bg='white', relief=RAISED, bd=10, padx=0, pady=0,
                                              image=busfare_photo, compound='top')
                        busfare_label.place(x=550, y=20)

                        def busfare1():
                            d.destroy()
                            busfare()

                        busfare_button = Button(d, text="Bus Wise Fare \n Amount ", font=('Arial', 20, 'bold'),
                                                command=busfare1)
                        busfare_button.place(x=600, y=350)
                        # modify_beticon
                        service_photo = PhotoImage(file='service_icon.png')
                        service_label = Label(d, fg='#00FF00', bg='white', relief=RAISED, bd=10, padx=0, pady=0,
                                              image=service_photo, compound='top')
                        service_label.place(x=950, y=20)

                        def service1():
                            d.destroy()
                            service()

                        service_button = Button(d, text="Service", font=('Arial', 20, 'bold'),
                                                command=service1)
                        service_button.place(x=1050, y=350)

                        def my_command():
                            d.destroy()
                            HOME_BUTTON_PAGE()

                        click_btn = PhotoImage(file='Small_Home_ Icon.png')
                        button = Button(d, image=click_btn, command=my_command)
                        button.place(x=0, y=10)
                        d.mainloop()

                    ABOUT_PAGE()

                def logout():
                    wn.destroy()
                    messagebox.showinfo(title="Logout page", message="\tSuccessfully Logged out...")
                    SIGNIN_N_SIGNUP_PAGE()

                # --------------------------Afterer log in--------------------------
                wn = Tk()
                icon0 = ImageTk.PhotoImage(file='windowBusIcon.png')
                wn.wm_iconphoto(False, icon0)
                wn.geometry("1490x745")
                wn.title("Bus E-Ticket->Home Page")
                # background
                can = Canvas(wn, width=800, height=800)
                can.pack(fill="both", expand=True)
                img1 = Image.open("bgforwindow2.png")
                resize2 = img1.resize((1490, 745))
                new1 = ImageTk.PhotoImage(resize2)
                can.create_image(0, 0, image=new1, anchor='nw')
                # home icon
                home_photo = PhotoImage(file='Home Icon.png')
                home_label = Label(wn, fg='#00FF00', bg='black', relief=RAISED, bd=10, padx=0, pady=0, image=home_photo,
                                   compound='top')
                home_label.place(x=50, y=20)
                home_button = Button(wn, text="Home", font=('Arial', 20, 'bold'), command=home)
                home_button.place(x=120, y=275)
                # ticket icon
                ticket_photo = PhotoImage(file='Ticket_Icon.png')
                ticket_label = Label(wn, fg='#00FF00', bg='black', relief=RAISED, bd=10, padx=0, pady=0,
                                     image=ticket_photo,
                                     compound='top')
                ticket_label.place(x=350, y=20)
                ticket_button = Button(wn, text="Bus E-Ticket", font=('Arial', 20, 'bold'), command=Bus_E_Ticket)
                ticket_button.place(x=370, y=275)
                # photo icon
                photo_photo = PhotoImage(file='photo_icon.png')
                photo_label = Label(wn, fg='#00FF00', bg='black', relief=RAISED, bd=10, padx=0, pady=0,
                                    image=photo_photo,
                                    compound='top')
                photo_label.place(x=675, y=20)
                photo_button = Button(wn, text="Photo", font=('Arial', 20, 'bold'), command=photo)
                photo_button.place(x=750, y=275)
                # about icon
                about_photo = PhotoImage(file='aboutIcon.png')
                about_label = Label(wn, fg='#00FF00', bg='black', relief=RAISED, bd=10, padx=0, pady=0,
                                    image=about_photo,
                                    compound='top')
                about_label.place(x=1000, y=20)
                about_button = Button(wn, text="About", font=('Arial', 20, 'bold'), command=about)
                about_button.place(x=1075, y=275)
                # logout icon
                logout_photo = PhotoImage(file='logoutIcon.png')
                logout_label = Label(wn, fg='#00FF00', bg='black', relief=RAISED, bd=10, padx=0, pady=0,
                                     image=logout_photo,
                                     compound='top')
                logout_label.place(x=600, y=375)
                logout_button = Button(wn, text="Logout", font=('Arial', 20, 'bold'), command=logout)
                logout_button.place(x=675, y=625)

                wn.mainloop()

            HOME_BUTTON_PAGE()
        else:
            messagebox.showerror(title="SignIn Page->Error", message="Invalid username or password.")
    # Create GUI
    root = Tk()
    icon = ImageTk.PhotoImage(file='windowBusIcon.png')
    root.wm_iconphoto(False, icon)
    root.geometry("1470x745")
    root.title("Login Page")
    canvas = Canvas(root, width=800, height=800, bg="#b3ffff")
    canvas.pack(fill="both", expand=True)
    img = Image.open("login page.png")
    resize = img.resize((600, 500))
    new = ImageTk.PhotoImage(resize)
    canvas.create_image(400, 120, image=new, anchor='nw')
    welcome = Label(root, text="Welcome to Bus E-Ticket Management", font=('Brush Script MT', 50, 'bold'), bg="#b3ffff")
    welcome.place(x=250, y=10)
    login = Label(root, text="Login Info", font=('Bodoni MT Black', 30, 'bold'), fg="#0000ff", bg="#b3ffff")
    login.place(x=600, y=130)

    password_label = Label(root, text="Password", font=('Arial', 15, 'bold'), bg="#b3ffff")
    password_label.place(x=570, y=305)
    password_entry = Entry(root, show="*")
    password_entry.place(x=690, y=310, width=180)

    email_label = Label(root, text="Email Address", font=('Arial', 15, 'bold'), bg="#b3ffff")
    email_label.place(x=550, y=255)

    email_entry = Entry(root,width=60)
    email_entry.place(x=690, y=260, width=180)


    sign_in_button = Button(root, text="Sign In", font=('Arial', 15, 'bold'), bg='green', command=sign_in)
    sign_in_button.place(x=660, y=460, width=80)
    def sign_up1():
        root.destroy()
        signup()
    sign_up_button = Button(root, text="Sign Up", font=('Arial', 15, 'bold'), bg='#ffff00', command=sign_up1)
    sign_up_button.place(x=660, y=505, width=80)
    def change1():
        root.destroy()
        change_password()
    change_button = Button(root, text="Change Password ", font=('Arial', 10, 'bold'), bg='red', command=change1)
    change_button.place(x=633, y=385, width=130)

    root.mainloop()
SIGNIN_N_SIGNUP_PAGE()