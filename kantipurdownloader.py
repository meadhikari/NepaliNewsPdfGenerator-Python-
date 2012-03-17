import datetime
#import urllib2
import re 
import os
from pyPdf import PdfFileWriter, PdfFileReader
import xml.etree
from urllib2 import Request, urlopen
from StringIO import StringIO
output = PdfFileWriter()
now = datetime.datetime.now()
now = str(now.day) + str(now.month) + str(now.year)

actualurl = 'http://epaper.ekantipur.com/1732012/epaperpdf/1732012-md-hr-6.pdf'

file = urlopen('http://epaper.ekantipur.com/ktpost/' + now +'/pages.xml')
data = file.read()
pages = []
count = data.count('<page>')
for i in range(1,count+1):
  pages.append('http://epaper.ekantipur.com/' + now + '/epaperpdf/' +now +'-md-hr-'+str(i) +'.pdf')


for url in pages:
	remoteFile = urlopen(Request(url)).read()
	memoryFile = StringIO(remoteFile)
	pdfFile = PdfFileReader(memoryFile)
        output.addPage(pdfFile.getPage(0))
        outputStream = file("output.pdf","wb")
        output.write(outputStream)
        outputStream.close()

