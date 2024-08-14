import os.path
import tkinter as tk
import tkinter.messagebox as msgbox
from tkinter import filedialog

import fitz

from Multifunctionalsoftware.Configs.BasicConfig import *
from Multifunctionalsoftware.PDF_Windows.Merge_PDF.mergepdf import *


class Merge_PDF_Windows(MergePDF_MainWindow, basicconfig):
    def __init__(self):
        basicconfig.__init__(self)
        MergePDF_MainWindow.__init__(self)
        self.setupUi(self)

        self.pdf_file_list = []

        self.pushButton_quit.clicked.connect(self.closeWindow)
        self.pushButton_save_mergepdf.clicked.connect(self.save_mergepdf)
        self.pushButton_upload_pdf.clicked.connect(self.upload_pdf)
        self.pushButton_up_pdf.clicked.connect(self.up_pdf)
        self.pushButton_down_pdf.clicked.connect(self.down_pdf)
        self.pushButton_delete_pdf.clicked.connect(self.delete_pdf)
        self.pushButton_start_merge_pdf.clicked.connect(self.start_merge_pdf)

    def save_mergepdf(self):
        root = tk.Tk()
        root.withdraw()
        folder_path = filedialog.askdirectory()
        self.lineEdit_save_merge_pdf.setText(folder_path)

    def upload_pdf(self):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path != "":
            self.pdf_file_list.append(file_path)
            self.listWidget_pdf_list.clear()
            for file in self.pdf_file_list:
                file_name = os.path.basename(file)
                self.listWidget_pdf_list.addItem(file_name)

    def up_pdf(self):
        def move_forward(arr, index):
            if index > 0 and index < len(arr):
                arr[index], arr[index - 1] = arr[index - 1], arr[index]
            return arr

        if self.listWidget_pdf_list.selectedIndexes():
            index = self.listWidget_pdf_list.selectedIndexes()[0].row()
            self.pdf_file_list = move_forward(self.pdf_file_list, index)
            self.listWidget_pdf_list.clear()
            for file in self.pdf_file_list:
                file_name = os.path.basename(file)
                self.listWidget_pdf_list.addItem(file_name)

    def down_pdf(self):
        def move_backward(arr, index):
            if index >= 0 and index < len(arr) - 1:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
            return arr

        if self.listWidget_pdf_list.selectedIndexes():
            index = self.listWidget_pdf_list.selectedIndexes()[0].row()
            self.pdf_file_list = move_backward(self.pdf_file_list, index)
            self.listWidget_pdf_list.clear()
            for file in self.pdf_file_list:
                file_name = os.path.basename(file)
                self.listWidget_pdf_list.addItem(file_name)

    def delete_pdf(self):
        if self.listWidget_pdf_list.selectedIndexes():
            index = self.listWidget_pdf_list.selectedIndexes()[0].row()
            self.pdf_file_list.pop(index)
            self.listWidget_pdf_list.clear()
            for file in self.pdf_file_list:
                file_name = os.path.basename(file)
                self.listWidget_pdf_list.addItem(file_name)

    def start_merge_pdf(self):
        save_path = self.lineEdit_save_merge_pdf.text()
        if save_path == "":
            save_path = os.path.expanduser("~") + "\\Desktop"

        def merge_pdfs(input_paths, output_path):
            merged_pdf = fitz.open()

            for path in input_paths:
                current_pdf = fitz.open(path)
                merged_pdf.insert_pdf(current_pdf, from_page=0, to_page=current_pdf.page_count - 1)
                current_pdf.close()

            merged_pdf.save(output_path)
            merged_pdf.close()

            msgbox.showinfo("合并成功", f"结果保存于{save_path}")

        if self.pdf_file_list:
            merge_pdfs(self.pdf_file_list, os.path.join(save_path, 'merge_PDF.pdf'))
