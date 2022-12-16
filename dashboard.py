import time
from tkinter import*
from tkinter import ttk

root = Tk()
root.title("Printing Machine Management")
root.geometry('1200x700')

Persen = StringVar()

########################################################################################################################################

# Informasi 

def turun():
    global Kurang
    global Tambah
    # Informasi Sisa Tinta
    Kurang -= 1
    satupersen.delete(0,5)
    satupersen.insert(0,Kurang)
    if (Kurang <= 0):
        Kurang = 0
        satupersen.delete(0,5)
        satupersen.insert(0, Kurang)

    # Jumlah Cetak
    Tambah += 1
    JumlahCetak.delete(0, 5)
    JumlahCetak.insert(0, Tambah)
    if (Tambah <= 0):
        Tambah = 0
        JumlahCetak.delete(0,5)
        JumlahCetak.insert(0, Tambah)

def reset():
    global Kurang
    satupersen.delete(0, END)
    satupersen.insert(0, 25)
    Kurang = int(satupersen.get())
    # Menurunkan persentase Progress
    progress['value']-=1
    Persen.set(str(progress['value']) + ' % ')

# Multi-Windows

def configPaperA4():
    def saveInputA4():
        A4 = inputA4.get()
        Data_A4.config(state='normal')
        Data_A4.delete(0, 'end')
        Data_A4.insert(0, A4)
        Data_A4.config(state='readonly')
        inputWindow1.destroy()
    inputWindow1 = Tk()
    inputWindow1.geometry("360x200")
    inputWindow1.title("Configuration Paper A4")

    # Judul Second Windows
    Label(inputWindow1, text="Masukkan Jumlah Kertas : A4", bg="#705E78", fg="white", width="50", height="2",font=("Optima", 16, "bold")).pack()

    # Membuat Frame untuk menampung kotak dialog
    s1 = Frame(inputWindow1, bg="#E9DCCC", highlightbackground="black", width=360, height=160)
    s1.place(x=0, y=60)
    inputA4 = Entry(s1, font=("aria",24), justify="center", width=10)
    inputA4.place(x=90,y=30)
    Button(s1, text="Save Changes",fg="black", font=("arial", 12, 'bold'), width=15, command=saveInputA4).place(x=102,y=90)

def configPaperF4():
    def saveInputF4():
        F4 = inputF4.get()
        Data_F4.config(state='normal')
        Data_F4.delete(0, 'end')
        Data_F4.insert(0, F4)
        Data_F4.config(state='readonly')
        inputWindow2.destroy()
    inputWindow2 = Tk()
    inputWindow2.geometry("360x200")
    inputWindow2.title("Configuration Paper F4")

    # Judul Second Windows
    Label(inputWindow2, text="Masukkan Jumlah Kertas : F4", bg="#705E78", fg="white", width="50", height="2",font=("Optima", 16, "bold")).pack()

    # Membuat Frame untuk menampung kotak dialog
    s1 = Frame(inputWindow2, bg="#E9DCCC", highlightbackground="black", width=360, height=160)
    s1.place(x=0, y=60)
    inputF4 = Entry(s1, font=("aria",24), justify="center", width=10)
    inputF4.place(x=90,y=30)
    Button(s1, text="Save Changes",fg="black", font=("arial", 12, 'bold'), width=15, command=saveInputF4).place(x=102,y=90)

def configPaperB5():
    def saveInputB5():
        B5 = inputB5.get()
        Data_B5.config(state='normal')
        Data_B5.delete(0, 'end')
        Data_B5.insert(0, B5)
        Data_B5.config(state='readonly')
        inputWindow3.destroy()
    inputWindow3 = Tk()
    inputWindow3.geometry("360x200")
    inputWindow3.title("Configuration Paper B5")

    # Judul Second Windows
    Label(inputWindow3, text="Masukkan Jumlah Kertas : B5", bg="#705E78", fg="white", width="50", height="2",font=("Optima", 16, "bold")).pack()

    # Membuat Frame untuk menampung kotak dialog
    s1 = Frame(inputWindow3, bg="#E9DCCC", highlightbackground="black", width=360, height=160)
    s1.place(x=0, y=60)
    inputB5 = Entry(s1, font=("aria",24), justify="center", width=10)
    inputB5.place(x=90,y=30)
    Button(s1, text="Save Changes",fg="black", font=("arial", 12, 'bold'), width=15, command=saveInputB5).place(x=102,y=90)

def configPaperLetter():
    def saveInputLetter():
        Letter = inputLetter.get()
        Data_Letter.config(state='normal')
        Data_Letter.delete(0, 'end')
        Data_Letter.insert(0, Letter)
        Data_Letter.config(state='readonly')
        inputWindow4.destroy()
    inputWindow4 = Tk()
    inputWindow4.geometry("360x200")
    inputWindow4.title("Configuration Paper Letter")

    # Judul Second Windows
    Label(inputWindow4, text="Masukkan Jumlah Kertas : Letter", bg="#705E78", fg="white", width="50", height="2",font=("Optima", 16, "bold")).pack()

    # Membuat Frame untuk menampung kotak dialog
    s1 = Frame(inputWindow4, bg="#E9DCCC", highlightbackground="black", width=360, height=160)
    s1.place(x=0, y=60)
    inputLetter = Entry(s1, font=("aria",24), justify="center", width=10)
    inputLetter.place(x=90,y=30)
    Button(s1, text="Save Changes",fg="black", font=("arial", 12, 'bold'), width=15, command=saveInputLetter).place(x=102,y=90)

def configPaperLegal():
    def saveInputLegal():
        Legal = inputLegal.get()
        Data_Legal.config(state='normal')
        Data_Legal.delete(0, 'end')
        Data_Legal.insert(0, Legal)
        Data_Legal.config(state='readonly')
        inputWindow5.destroy()
    inputWindow5 = Tk()
    inputWindow5.geometry("360x200")
    inputWindow5.title("Configuration Paper Legal")

    # Judul Second Windows
    Label(inputWindow5, text="Masukkan Jumlah Kertas : Legal", bg="#705E78", fg="white", width="50", height="2",font=("Optima", 16, "bold")).pack()

    # Membuat Frame untuk menampung kotak dialog
    s1 = Frame(inputWindow5, bg="#E9DCCC", highlightbackground="black", width=360, height=160)
    s1.place(x=0, y=60)
    inputLegal = Entry(s1, font=("aria",24), justify="center", width=10)
    inputLegal.place(x=90,y=30)
    Button(s1, text="Save Changes",fg="black", font=("arial", 12, 'bold'), width=15, command=saveInputLegal).place(x=102,y=90)


#######################################################################################################################################

# Membuat Judul Widget
Label(text="Printing Machine Management", bg="#161F6D", fg="white", width="300", height="2", font=("Optima", 35, "bold")).pack()

# Gambar
#Foto = PhotoImage(file="C:\\Users\\ADAP\\Documents\\Latihan Pemrograman\\Tugas Akhir\\Printer.gif") #Letakkan sesuai dengan lokasi foto di PC
#label_foto= Label(image=Foto)
#label_foto.place(x=400, y=125)

#######################################################################################################################################

# Membuat Frame Sambutan

def TutupSambutan():
    Sambutan.destroy()

Sambutan = Tk()
Sambutan.geometry("360x200")
Sambutan.title("Kata Sambutan")

Label(Sambutan, text="Informasi", bg="#77C3F2", fg="black", width="50", height="2",font=("Optima", 20, "bold")).pack()

ss = Frame(Sambutan, bg="#BFB99B", highlightbackground="black", width=360, height=160)
ss.place(x=0, y=60)
Label(ss, text= " Selamat Datang di Printing Machine Management,", bg="#BFB99B", highlightbackground="black", font=("Times New Roman", 12, 'bold')).place(x=5, y=15)
Label(ss, text= " Klik 'Ready' untuk melanjutkan,", bg="#BFB99B", highlightbackground="black", font=("Times New Roman", 12, 'bold')).place(x=75, y=45)
Button(ss, text="Ready",fg="black", font=("arial", 12, 'bold'), width=15, command=TutupSambutan).place(x=102,y=90)

#########################################################################################################################################################################

p7 = Frame(root, bg="#F2CF1D", highlightbackground="black", width=400, height=100)
p7.place(x=5, y=130)
Label(p7, text="Welcome, Your Name!", font=("Rockwell", 24, "bold"), fg="black", bg="#F2CF1D").place(x=20, y=30)

# Menu Informasi Ketersediaan ukuran kertas
p1 = Frame(root, bg="lightgreen", highlightbackground="black", width=400, height=300)
p1.place(x=5, y=240)

Label(p1, text="Info Ketersediaan Kertas", font=("Monaco", 20, "bold"), fg="black", bg="lightgreen").place(x=5, y=5)

p6 = Frame(root, bg="black", highlightbackground="black", width=400, height=5)
p6.place(x=5, y=290)

# Jumlah berbagai ukuran kertas

Lbl_A4 = Label(p1, text="- A4     = ", font=("aria", 18), bg="lightgreen")
Lbl_A4.place(x=10, y=70)

Lbl_F4 = Label(p1, text="- F4     = ", font=("aria", 18), bg="lightgreen")
Lbl_F4.place(x=10, y=110)

Lbl_B5 = Label(p1, text="- B5     = ", font=("aria", 18), bg="lightgreen")
Lbl_B5.place(x=10, y=150)

Lbl_Letter = Label(p1, text="- Letter = ", font=("aria", 18), bg="lightgreen")
Lbl_Letter.place(x=10, y=190)

Lbl_Legal = Label(p1, text="- Legal  = ", font=("aria", 18), bg="lightgreen")
Lbl_Legal.place(x=10, y=230)

# Data Masuk Jumlah berbagai ukuran kertas

Data_A4 = Entry(p1, font=("aria",18), justify="center", width=10)
Data_A4.insert(0,0)
Data_A4.config(state="readonly")
Data_A4.place(x= 120, y= 70)

Data_F4 = Entry(p1, font=("aria",18), justify="center", width=10)
Data_F4.insert(0,0)
Data_F4.config(state="readonly")
Data_F4.place(x= 120, y= 110)

Data_B5 = Entry(p1, font=("aria",18), justify="center", width=10)
Data_B5.insert(0,0)
Data_B5.config(state="readonly")
Data_B5.place(x= 120, y= 150)

Data_Letter = Entry(p1, font=("aria",18), justify="center", width=10)
Data_Letter.insert(0,0)
Data_Letter.config(state="readonly")
Data_Letter.place(x= 120, y= 190)

Data_Legal = Entry(p1, font=("aria",18), justify="center", width=10)
Data_Legal.insert(0,0)
Data_Legal.config(state="readonly")
Data_Legal.place(x= 120, y= 230)

# Tombol Menu Tombol Perintah
Tombol_Config_A4 = Button(p1, fg="black", font=("arial", 12, 'bold'), width=10, text="Tambah", command = configPaperA4).place(x=280,y=70)
Tombol_Config_F4 = Button(p1, fg="black", font=("arial", 12, 'bold'), width=10, text="Tambah", command = configPaperF4).place(x=280,y=110)
Tombol_Config_B4 = Button(p1, fg="black", font=("arial", 12, 'bold'), width=10, text="Tambah", command = configPaperB5).place(x=280,y=150)
Tombol_Config_Letter = Button(p1, fg="black", font=("arial", 12, 'bold'), width=10, text="Tambah", command = configPaperLetter).place(x=280,y=190)
Tombol_Config_Legal = Button(p1, fg="black", font=("arial", 12, 'bold'), width=10, text="Tambah", command = configPaperLegal).place(x=280,y=230)

# Informasi Sisa Tinta
p2 = Frame(root, bg="#7DA2A9", highlightbackground="black", width=340, height=250)
p2.place(x=850, y=130)
p3 = Frame(root, bg="black", highlightbackground="black", width=340, height=5)
p3.place(x=850, y=180)
Label(p2, text="Informasi Sisa Tinta", font=("Monaco", 20, 'bold'), fg="black", bg="#7DA2A9").place(x=10, y=10)


# Bikin Statur Bar Sisa Tinta di P2

Label(p2, textvariable= Persen, font=("Copperplate", 45, 'bold'), fg="black", bg="#7DA2A9").place(x=115, y=60)
progress = ttk.Progressbar(p2, length=300, orient=HORIZONTAL, mode='determinate', maximum=100, value=101)
progress.place(x=20, y=150)


#-----------------------------------------------------------------------#

# Bikin perhitungan 25 cetak berkurang 1%
satupersen = Entry(p2, font=("aria",12), justify="center")
satupersen.insert(0, 25)
satupersen.place(x=20,y=200)

Kurang = int(satupersen.get())
Ku = Button(p2, fg="black", font=("arial", 10, 'bold'), width=6, text="Use", command = turun).place(x=210,y=200)
Re = Button(p2, fg="black", font=("arial", 10, 'bold'), width=6, text="Set", command = reset).place(x=270,y=200)

#-------------------------------------------------------------------------#

# Bikin Fungsi Counter Jumlah Seluruh Cetak

p4 = Frame(root, bg='#F4DB7D', highlightbackground="black", width=340, height=150)
p4.place(x=850, y=390)
Label(p4, text="Jumlah Cetak", font=("Monaco", 20, 'bold'), fg="black", bg="#F4DB7D").place(x=75, y=10)
p5 = Frame(root, bg="black", highlightbackground="black", width=340, height=5)
p5.place(x=850, y=440)

JumlahCetak = Entry(p4, font=("aria",20, 'bold'), justify="center", width=15)
JumlahCetak.insert(0,0)
JumlahCetak.place(x=55, y=80)

Tambah = int(JumlahCetak.get())

# Membuat Tampilan Informasi Jam
def start():
    text= time.strftime("%H:%M:%S")
    label.config(text= text)
    label.after(200,start)

p8 = Frame(root, bg='#FFB8B3', highlightbackground="black", width=400, height=140)
p8.place(x=5, y=550)
Label(p8, text="Info Waktu", font=("Monaco", 20, 'bold'), fg="black", bg="#FFB8B3").place(x=110, y=5)
p9 = Frame(p8, bg="black", highlightbackground="black", width=400, height=5)
p9.place(x=5, y=40)

label = Label(p8, bg='#FFB8B3',font=("DS-Digital", 36, 'bold'))
label.place(x=90, y=60)
start()

# Membuat Tombol Keluar
def TutupProgram():
    root.destroy()

p10 = Frame(root, bg='#CAC7C8', highlightbackground="black", width=340, height=140)
p10.place(x=850, y=550)

Keluar = Button(p10, bg="#FF0005", fg="white", font=("arial", 16, 'bold'), width=10, height=3, text="Keluar", command = TutupProgram).place(x=100,y=25)

root.mainloop()
Sambutan.mainloop()
