from tkinter import *
from tkinter import ttk
import tkinter.filedialog
from PIL import ImageTk, Image
from tkinter import messagebox
from io import BytesIO
import os
import pyttsx3
from tkinter.simpledialog import askstring
from cryptography.fernet import Fernet
import base64

class Stegno:

    art = r'''¯\_(ツ)_/¯'''
    art2 = r'''
@(\/)
(\/)-{}-)@
@(={}=)/\)(\/)
(\/(/\)@| (-{}-)
(={}=)@(\/)@(/\)@
(/\)\(={}=)/(\/)
@(\/)\(/\)/(={}=)
(-{}-)""""@/(/\)
|:   |
/::'   \\
/:::     \\
|::'       |
|::        |
\::.       /
':______.'
`""""""`'''
    output_image_size = 0

    def main(self, root):
        root.title('StegnoVault')
        root.geometry('600x600')
        root.resizable(width=False, height=False)
        root.configure(bg='#2c3e50')
        f = Frame(root, bg='#2c3e50')

        title = Label(f, text='StegnoVault', bg='#2c3e50', fg='#ecf0f1')
        title.config(font=('Helvetica', 33, 'bold'))
        title.grid(pady=10)

        b_encode = Button(f, text="Encode", command=lambda: self.frame1_encode(f), padx=14, bg='#3498db', fg='#ecf0f1')
        b_encode.config(font=('Helvetica', 14, 'bold'))
        b_decode = Button(f, text="Decode", padx=14, command=lambda: self.frame1_decode(f), bg='#3498db', fg='#ecf0f1')
        b_decode.config(font=('Helvetica', 14, 'bold'))
        b_decode.grid(pady=12)

        ascii_art = Label(f, text=self.art, bg='#2c3e50', fg='#ecf0f1')
        ascii_art.config(font=('Courier', 60))

        ascii_art2 = Label(f, text=self.art2, bg='#2c3e50', fg='#ecf0f1')
        ascii_art2.config(font=('Courier', 12, 'bold'))

        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        f.grid()
        title.grid(row=1)
        b_encode.grid(row=2)
        b_decode.grid(row=3)
        ascii_art.grid(row=4, pady=10)
        ascii_art2.grid(row=5, pady=5)

    def home(self, frame):
        frame.destroy()
        self.main(root)

    def frame1_decode(self, f):
        f.destroy()
        d_f2 = Frame(root, bg='#2c3e50')
        label_art = Label(d_f2, text=r'٩(^‿^)۶', bg='#2c3e50', fg='#ecf0f1')
        label_art.config(font=('Courier', 90))
        label_art.grid(row=1, pady=50)
        l1 = Label(d_f2, text='Select Image with Hidden text:', bg='#2c3e50', fg='#ecf0f1')
        l1.config(font=('Helvetica', 18))
        l1.grid()
        bws_button = Button(d_f2, text='Select', command=lambda: self.frame2_decode(d_f2), bg='#3498db', fg='#ecf0f1')
        bws_button.config(font=('Helvetica', 18, 'bold'))
        bws_button.grid()
        back_button = Button(d_f2, text='Cancel', command=lambda: Stegno.home(self, d_f2), bg='#e74c3c', fg='#ecf0f1')
        back_button.config(font=('Helvetica', 18, 'bold'))
        back_button.grid(pady=15)
        back_button.grid()
        d_f2.grid()

    def frame2_decode(self, d_f2):
        d_f3 = Frame(root, bg='#2c3e50')
        myfile = tkinter.filedialog.askopenfilename(filetypes=([('png', '*.png'), ('jpeg', '*.jpeg'), ('jpg', '*.jpg'), ('bmp', '*.bmp'), ('tiff', '*.tiff'), ('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error", "You have selected nothing!")
        else:
            myimg = Image.open(myfile, 'r')
            myimage = myimg.resize((300, 200))
            img = ImageTk.PhotoImage(myimage)
            l4 = Label(d_f3, text='Selected Image:', bg='#2c3e50', fg='#ecf0f1')
            l4.config(font=('Helvetica', 18))
            l4.grid()
            panel = Label(d_f3, image=img, bg='#2c3e50')
            panel.image = img
            panel.grid()
            hidden_data = self.decode(myimg)
            print(f"Hidden data: {hidden_data}")  # Debugging statement
            password = askstring("Password", "Enter password for decryption:")
            if password:
                try:
                    cipher_suite = Fernet(base64.urlsafe_b64encode(password.encode().ljust(32)[:32]))
                    decrypted_data = cipher_suite.decrypt(hidden_data.encode()).decode()
                    print(f"Decrypted data: {decrypted_data}")  # Debugging statement
                    l2 = Label(d_f3, text='Hidden data is:', bg='#2c3e50', fg='#ecf0f1')
                    l2.config(font=('Helvetica', 18))
                    l2.grid(pady=10)
                    text_area = Text(d_f3, width=50, height=10, bg='#34495e', fg='#ecf0f1')
                    text_area.insert(INSERT, decrypted_data)
                    text_area.configure(state='disabled')
                    text_area.grid()
                except Exception as e:
                    print(f"Error: {e}")  # Debugging statement
                    messagebox.showerror("Error", "Invalid password or corrupted data!")
            back_button = Button(d_f3, text='Cancel', command=lambda: self.page3(d_f3), bg='#e74c3c', fg='#ecf0f1')
            back_button.config(font=('Helvetica', 11, 'bold'))
            back_button.grid(pady=15)
            back_button.grid()
            show_info = Button(d_f3, text='More Info', command=self.info, bg='#3498db', fg='#ecf0f1')
            show_info.config(font=('Helvetica', 11, 'bold'))
            show_info.grid()
            voice_button = Button(d_f3, text='Read Aloud', command=lambda: self.read_aloud(decrypted_data), bg='#3498db', fg='#ecf0f1')
            voice_button.config(font=('Helvetica', 11, 'bold'))
            voice_button.grid(pady=15)
            d_f3.grid(row=1)
            d_f2.destroy()

    def decode(self, image):
        data = ''
        imgdata = iter(image.getdata())

        while True:
            pixels = [value for value in imgdata.__next__()[:3] +
                      imgdata.__next__()[:3] +
                      imgdata.__next__()[:3]]
            binstr = ''
            for i in pixels[:8]:
                if i % 2 == 0:
                    binstr += '0'
                else:
                    binstr += '1'

            data += chr(int(binstr, 2))
            if pixels[-1] % 2 != 0:
                return data

    def frame1_encode(self, f):
        f.destroy()
        f2 = Frame(root, bg='#2c3e50')
        label_art = Label(f2, text=r'\'\(°Ω°)/\'', bg='#2c3e50', fg='#ecf0f1')
        label_art.config(font=('Courier', 70))
        label_art.grid(row=1, pady=50)
        l1 = Label(f2, text='Select the Image in which \nyou want to hide text:', bg='#2c3e50', fg='#ecf0f1')
        l1.config(font=('Helvetica', 18))
        l1.grid()

        bws_button = Button(f2, text='Select', command=lambda: self.frame2_encode(f2), bg='#3498db', fg='#ecf0f1')
        bws_button.config(font=('Helvetica', 18, 'bold'))
        bws_button.grid()
        back_button = Button(f2, text='Cancel', command=lambda: Stegno.home(self, f2), bg='#e74c3c', fg='#ecf0f1')
        back_button.config(font=('Helvetica', 18, 'bold'))
        back_button.grid(pady=15)
        back_button.grid()
        f2.grid()

    def frame2_encode(self, f2):
        ep = Frame(root, bg='#2c3e50')
        myfile = tkinter.filedialog.askopenfilename(filetypes=([('png', '*.png'), ('jpeg', '*.jpeg'), ('jpg', '*.jpg'), ('bmp', '*.bmp'), ('tiff', '*.tiff'), ('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error", "You have selected nothing!")
        else:
            myimg = Image.open(myfile)
            myimage = myimg.resize((300, 200))
            img = ImageTk.PhotoImage(myimage)
            l3 = Label(ep, text='Selected Image', bg='#2c3e50', fg='#ecf0f1')
            l3.config(font=('Helvetica', 18))
            l3.grid()
            panel = Label(ep, image=img, bg='#2c3e50')
            panel.image = img
            self.output_image_size = os.stat(myfile)
            self.o_image_w, self.o_image_h = myimg.size
            panel.grid()
            l2 = Label(ep, text='Enter the message', bg='#2c3e50', fg='#ecf0f1')
            l2.config(font=('Helvetica', 18))
            l2.grid(pady=15)
            text_area = Text(ep, width=50, height=10, bg='#34495e', fg='#ecf0f1')
            text_area.grid()
            encode_button = Button(ep, text='Cancel', command=lambda: Stegno.home(self, ep), bg='#e74c3c', fg='#ecf0f1')
            encode_button.config(font=('Helvetica', 11, 'bold'))
            clear_button = Button(ep, text='Clear', command=lambda: text_area.delete('1.0', END), bg='#f39c12', fg='#ecf0f1')
            clear_button.config(font=('Helvetica', 11, 'bold'))
            back_button = Button(ep, text='Encode', command=lambda: [self.enc_fun(text_area, myimg), Stegno.home(self, ep)], bg='#3498db', fg='#ecf0f1')
            back_button.config(font=('Helvetica', 11, 'bold'))
            back_button.grid(pady=15)
            encode_button.grid()
            clear_button.grid()
            ep.grid(row=1)
            f2.destroy()

    def enc_fun(self, text_area, myimg):
        data = text_area.get("1.0", "end-1c")
        if len(data) == 0:
            messagebox.showinfo("Alert", "Kindly enter text in TextBox")
        else:
            password = askstring("Password", "Enter password for encryption:")
            if password:
                cipher_suite = Fernet(base64.urlsafe_b64encode(password.encode().ljust(32)[:32]))
                encrypted_data = cipher_suite.encrypt(data.encode())
                print(f"Encrypted data: {encrypted_data.decode()}")  # Debugging statement
                newimg = myimg.copy()
                self.encode_enc(newimg, encrypted_data.decode())
                my_file = BytesIO()
                temp = os.path.splitext(os.path.basename(myimg.filename))[0]
                newimg.save(tkinter.filedialog.asksaveasfilename(initialfile=temp, filetypes=([('png', '*.png')]), defaultextension=".png"))
                self.d_image_size = my_file.tell()
                self.d_image_w, self.d_image_h = newimg.size
                messagebox.showinfo("Success", "Encoding Successful\nFile is saved as Image_with_hiddentext.png in the same directory")

    def encode_enc(self, newimg, data):
        w = newimg.size[0]
        (x, y) = (0, 0)

        for pixel in self.modPix(newimg.getdata(), data):
            newimg.putpixel((x, y), pixel)
            if (x == w - 1):
                x = 0
                y += 1
            else:
                x += 1

    def modPix(self, pix, data):
        datalist = self.genData(data)
        lendata = len(datalist)
        imdata = iter(pix)
        for i in range(lendata):
            pix = [value for value in imdata.__next__()[:3] +
                   imdata.__next__()[:3] +
                   imdata.__next__()[:3]]
            for j in range(0, 8):
                if (datalist[i][j] == '0') and (pix[j] % 2 != 0):
                    pix[j] -= 1
                elif (datalist[i][j] == '1') and (pix[j] % 2 == 0):
                    pix[j] += 1
            if (i == lendata - 1):
                if (pix[-1] % 2 == 0):
                    pix[-1] -= 1
            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1

            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]

    def genData(self, data):
        newd = []

        for i in data:
            newd.append(format(ord(i), '08b'))
        return newd

    def read_aloud(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    def page3(self, frame):
        frame.destroy()
        self.main(root)

    def info(self):
        try:
            str = 'original image:-\nsize of original image:{}mb\nwidth: {}\nheight: {}\n\n' \
                  'decoded image:-\nsize of decoded image: {}mb\nwidth: {}' \
                  '\nheight: {}'.format(self.output_image_size.st_size / 1000000,
                                        self.o_image_w, self.o_image_h,
                                        self.d_image_size / 1000000,
                                        self.d_image_w, self.d_image_h)
            messagebox.showinfo('info', str)
        except:
            messagebox.showinfo('Info', 'Unable to get the information')

root = Tk()

o = Stegno()
o.main(root)

root.mainloop()