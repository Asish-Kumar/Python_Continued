import PyPDF2

# creating a pdf file object
pdfFileObj = open('CSD Car Price 22 MAR 18.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

no_of_pages = pdfReader.numPages
big_list = list()
for x in range(no_of_pages):
    # if x != 2:
    #     continue
    pageObj = pdfReader.getPage(x)
    ls = list(pageObj.extractText().split('\n'))
    ls.pop(0)
    try:
        ind = ls.index('Note : ')
        ls = ls[:ind]
    except ValueError:
        pass

    if ls[-1] == '':
        ls = ls[:-1]
    if len(ls)%5 != 0:
        continue
    last_index = len(ls)-1
    begin = 0
    end = 5
    while end<last_index:
        big_list.append(list(ls[begin:end]))
        begin+=5
        end+=5
    #print(len(ls), ls)

for x in big_list:
    try:
        if int(x[3].replace(',', '_')) <= 560000:
            print(x)
    except ValueError:
        continue
pdfFileObj.close()
