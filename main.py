from pyPdf import PdfFileWriter, PdfFileReader

def merge_pdf(input,output):
    [output.addPage(input.getPage(page_num)) for page_num in range(input.numPages)]

output = PdfFileWriter()

# Appending  pdf-pages from ten different files in  order
merge_pdf(PdfFileReader(open("1.pdf","rb")),output)
merge_pdf(PdfFileReader(open("2.pdf","rb")),output)
merge_pdf(PdfFileReader(open("3.pdf","rb")),output)
merge_pdf(PdfFileReader(open("4.pdf","rb")),output)
merge_pdf(PdfFileReader(open("5.pdf","rb")),output)
merge_pdf(PdfFileReader(open("6.pdf","rb")),output)
merge_pdf(PdfFileReader(open("7.pdf","rb")),output)
merge_pdf(PdfFileReader(open("8.pdf","rb")),output)
merge_pdf(PdfFileReader(open("9.pdf","rb")),output)
merge_pdf(PdfFileReader(open("10.pdf","rb")),output)


# Writing all the collected pages to a file
output.write(open("output.pdf","wb"))
