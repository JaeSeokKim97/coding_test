from PyPDF2 import PdfFileMerger
import os

folder = 'C:/Users/KJS/Desktop/pdflist/' # 파일위치
fileExt = '.pdf'

pdf_list = [file for file in os.listdir(folder) if file.endswith(fileExt)]

pdf_merger = PdfFileMerger(strict=False)
for file in pdf_list:
	pdf_merger.append(folder + file)

pdf_merger.write("Merged.pdf") # 최종 PDF이름
pdf_merger.close()