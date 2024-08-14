from Multifunctionalsoftware.PDF_Windows.Encrypt_PDF.encryptpdf_windows import *
from Multifunctionalsoftware.PDF_Windows.Merge_PDF.mergepdf_windows import *
from Multifunctionalsoftware.PDF_Windows.Split_PDF.splitpdf_windows import *


class PdfWindowsConfig:
    def open_mergepdf_windows(self):
        self.mergepdf_windows = Merge_PDF_Windows()
        self.mergepdf_windows.show()

    def open_splitpdf_windows(self):
        self.splitpdf_windows = Split_PDF_Windows()
        self.splitpdf_windows.show()

    def open_encryptpdf_windows(self):
        self.encryptpdf_windows = Encrypt_PDF_Windows()
        self.encryptpdf_windows.show()
