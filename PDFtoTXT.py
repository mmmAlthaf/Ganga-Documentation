import textract
text = textract.process("CERN.pdf")
f= open("CERN.txt","w+")
f.write(text)
f.close()