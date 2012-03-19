import datetime
import re 
import os
from pyPdf import PdfFileWriter, PdfFileReader
import xml.etree
from urllib2 import Request, urlopen
from StringIO import StringIO 
now = datetime.datetime.now()
now = str(now.day) + str(now.month) + str(now.year)
kantipuractualurl = 'http://epaper.ekantipur.com/1732012/epaperpdf/1732012-md-hr-6.pdf'
file = urlopen('http://epaper.ekantipur.com/ktpost/' + now +'/pages.xml')
data = file.read()
pages = []
count = data.count('<page>')
for i in range(1,count+1):
  pages.append('http://epaper.ekantipur.com/' + now + '/epaperpdf/' +now +'-md-hr-'+str(i) +'.pdf')

writer = PdfFileWriter()
for i in pages:
	remoteFile = urlopen(Request(i)).read()
	memoryFile = StringIO(remoteFile)
	pdfFile = PdfFileReader(memoryFile)
	for pageNum in xrange(pdfFile.getNumPages()):
		currentPage = pdfFile.getPage(pageNum)
		writer.addPage(currentPage)


outputStream = open(filename+"(kantipur)"+".pdf","wb")
writer.write(outputStream)
outputStream.close()
