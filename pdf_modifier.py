import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pikepdf
import os

class PDFModifierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Modifier")
        self.root.geometry('600x600')

        # Tkinter variables
        self.file_path = ""
        self.pass_written = tk.StringVar()
        self.selected = tk.StringVar()
        self.selected_doc = tk.StringVar()

        # UI setup
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text='Welcome To Your All-in-One Encrypter/Decrypter',
                 fg='Blue', font=('cambria', 16), anchor="center").grid(row=0, column=0)

        self.frame = tk.Frame(self.root, bg='lightgreen', width=300, height=400)
        self.frame.grid(row=1, column=0, padx=150)
        self.frame.grid_propagate(False)

        self.mainbox=ttk.Combobox(self.frame, state='readonly', values=['PDF'],
                     textvariable=self.selected_doc,
                     font=('arial', 10), cursor='hand2')
        self.mainbox.set('Select Doc Type')
        self.mainbox.grid(padx=60, pady=20)

        self.path_entry = tk.Entry(self.frame, state='normal', font=('cambria', 11), width=25)
        self.path_entry.grid()

        self.browse = tk.Button(self.frame, text='Browse', command=self.browse_pdf,
                                font=('cambria', 11), cursor='hand2')
        self.browse.grid(pady=5)

        self.dropbox = ttk.Combobox(self.frame, state='readonly', values=['Decrypt', 'Encrypt'],
                                    textvariable=self.selected, font=('cambria', 11), cursor='hand2')
        self.dropbox.set('Select')
        self.dropbox.grid(pady=10)
        self.dropbox.bind('<<ComboboxSelected>>', self.handle_option)

        tk.Button(self.root, text='Quit', command=self.root.destroy,
                  cursor='hand2', bg='black', fg='white', font=('cambria', 11), width=10).grid(row=2, column=0, padx=130)

    def browse_pdf(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if self.file_path:
            self.path_entry.config(state='normal')
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, self.file_path)
            self.path_entry.config(state='disabled')
            self.browse.config(state='disabled')

    def handle_option(self, event):
        option = self.selected.get()

        txt_pass = tk.Label(self.frame, text='Password', font=('arial', 12),bg='lightgreen')
        txt_pass.grid(row=4, column=0, pady=5)

        self.password_entry = tk.Entry(self.frame, show='*', font=('cambria', 11), textvariable=self.pass_written)
        self.password_entry.grid(row=5, column=0)

        if option == 'Decrypt':
            decrypt_btn = tk.Button(self.frame, text='Decrypt', cursor='hand2', command=self.check_encryption)
            decrypt_btn.grid(row=6, column=0)
            decrypt_btn.bind('<Return>',lambda e:self.check_encryption())
            decrypt_btn.focus_set()
        elif option == 'Encrypt':
            encrypt_btn = tk.Button(self.frame, text='Encrypt', cursor='hand2', command=self.encrypt_pdf)
            encrypt_btn.grid(row=6, column=0)
            encrypt_btn.bind('<Return>',lambda e:self.encrypt_pdf())
            encrypt_btn.focus_set()

    def decrypt_pdf(self):
        password = self.pass_written.get()
        if not password:
            return

        try:
            with pikepdf.open(self.file_path, password=password, allow_overwriting_input=True) as pdf:
                new_pdf = pikepdf.new()
                new_pdf.pages.extend(pdf.pages)
                new_pdf.save(self.file_path, encryption=None)
                messagebox.showinfo('Decryption Successful', "🔓 The PDF was successfully decrypted.")
        except pikepdf.PasswordError:
            messagebox.showerror('Wrong Password', "❌ Incorrect password. Please try again.")
        finally:
            self.pass_written.set('')

    def encrypt_pdf(self):
        password = self.pass_written.get()
        if not password:
            return

        try:
            with pikepdf.open(self.file_path, allow_overwriting_input=True) as pdf:
                pdf.save(self.file_path,
                         encryption=pikepdf.Encryption(user=password, owner=password)
                         )
                messagebox.showinfo("Encryption Complete", "🔒 The PDF was successfully encrypted.")
        except pikepdf.PasswordError:
            messagebox.showerror('Encryption Failed', "⚠️ PDF is already encrypted.")
        finally:
            self.pass_written.set('')

    def check_encryption(self):
        try:
            with pikepdf.open(self.file_path) as pdf:
                if not pdf.is_encrypted:
                    messagebox.showinfo("Already Decrypted", "⚠️ This PDF is not encrypted.")
                else:
                    self.decrypt_pdf()
        except pikepdf.PasswordError:
            self.decrypt_pdf()
        except (pikepdf.PdfError, FileNotFoundError):
            messagebox.showerror("Error", "⚠️ Please select a valid PDF file first.")
        finally:
            self.pass_written.set('')


if __name__ == "__main__":
    root = tk.Tk()
    app = PDFModifierApp(root)
    root.mainloop()


