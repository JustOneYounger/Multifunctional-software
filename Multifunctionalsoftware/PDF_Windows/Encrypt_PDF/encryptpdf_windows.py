import os.path
import tkinter as tk
import tkinter.messagebox as msgbox
from tkinter import filedialog

import PyPDF2

from Multifunctionalsoftware.Configs.BasicConfig import *
from Multifunctionalsoftware.PDF_Windows.Encrypt_PDF.encryptpdf import *


class Encrypt_PDF_Windows(Encrypt_PDF_MainWindow, basicconfig):
    def __init__(self):
        basicconfig.__init__(self)
        Encrypt_PDF_MainWindow.__init__(self)
        self.setupUi(self)

        self.pushButton_quit.clicked.connect(self.closeWindow)
        self.pushButton_encrypt_pdf.clicked.connect(self.encrypt_pdf)
        self.pushButton_save_encrypt_pdf.clicked.connect(self.save_encrypt_pdf)
        self.pushButton_start_encrypt_pdf.clicked.connect(self.start_encrypt_pdf)

    def encrypt_pdf(self):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        self.lineEdit_encrypt_pdf.setText(file_path)

    def save_encrypt_pdf(self):
        root = tk.Tk()
        root.withdraw()
        folder_path = filedialog.askdirectory()
        self.lineEdit_save_encrypt_pdf.setText(folder_path)

    def start_encrypt_pdf(self):
        save_path = self.lineEdit_save_encrypt_pdf.text()
        if save_path == "":
            save_path = os.path.expanduser("~") + "\\Desktop"

        def encrypt_pdf(input_file, output_file, password):
            reader = PyPDF2.PdfReader(input_file)
            writer = PyPDF2.PdfWriter()

            for page in reader.pages:
                writer.add_page(page)

            with open(output_file, 'wb') as f:
                writer.encrypt(password)
                writer.write(f)
            msgbox.showinfo("加密成功", f"密码为{password}的encrypt_PDF.pdf已经保存于{save_path}")

        if self.lineEdit_encrypt_pdf.text() == "":
            msgbox.showwarning("警告", "未选择PDF文件")
        else:
            encrypt_pdf(self.lineEdit_encrypt_pdf.text(), os.path.join(save_path, "encrypt_PDF.pdf"),
                        self.lineEdit_password.text())
