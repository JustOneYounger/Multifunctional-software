import tkinter as tk
import tkinter.messagebox as msgbox
from tkinter import filedialog

import fitz

from Multifunctionalsoftware.Configs.BasicConfig import *
from Multifunctionalsoftware.PDF_Windows.Split_PDF.splitpdf import *


class Split_PDF_Windows(SplitPDF_MainWindow, basicconfig):
    def __init__(self):
        basicconfig.__init__(self)
        SplitPDF_MainWindow.__init__(self)
        self.setupUi(self)

        self.pushButton_quit.clicked.connect(self.closeWindow)
        self.pushButton_split_pdf.clicked.connect(self.split_pdf)
        self.pushButton_save_split_pdf.clicked.connect(self.save_split_pdf)
        self.pushButton_start_pdf_split.clicked.connect(self.start_pdf_split)

    def split_pdf(self):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        self.lineEdit_split_pdf.setText(file_path)

    def save_split_pdf(self):
        root = tk.Tk()
        root.withdraw()
        folder_path = filedialog.askdirectory()
        self.lineEdit_save_split_pdf.setText(folder_path)

    def start_pdf_split(self):
        page_range = self.lineEdit_split_page_range.text()
        save_pdf = self.lineEdit_save_split_pdf.text()
        if save_pdf == "":
            save_pdf = os.path.expanduser("~") + "\\Desktop"
        if "，" in page_range:
            msgbox.showwarning("警告", '请输入英文","。中文"，"不被允许')
        else:
            page_range = page_range.split(',')
            page_range_list = []
            for every_page_range in page_range:
                start, end = map(int, every_page_range.split('-'))
                page_range_list.append([start - 1, end - 1])
            test_list = [item for sublist in page_range_list for item in sublist]

            def split_pdf_mupdf(input_path, output_path, page_ranges):
                pdf_document = fitz.open(input_path)
                total_pages = pdf_document.page_count
                if max(test_list) > total_pages:
                    msgbox.showwarning("警告", "输入的拆分页范围中存在大于PDF总页数的值")
                elif min(test_list) < 0:
                    msgbox.showwarning("警告", "输入的拆分页范围中存在小于0的值")
                else:
                    for start, end in page_ranges:
                        pdf_document_new = fitz.open()
                        for page_num in range(start, end + 1):
                            pdf_page = pdf_document[page_num]
                            pdf_document_new.insert_pdf(pdf_document, from_page=page_num, to_page=page_num)
                        pdf_document_new.save(output_path.format(start + 1, end + 1))
                        pdf_document_new.close()
                msgbox.showwarning("拆分成功", f"拆分结果保存于{save_pdf}")

            if self.lineEdit_split_pdf.text() != "":
                split_pdf_mupdf(self.lineEdit_split_pdf.text(), save_pdf + '/SplitPDF_page_{}_to_{}.pdf',
                                page_range_list)
            else:
                msgbox.showwarning("警告", "未选择PDF文件")
