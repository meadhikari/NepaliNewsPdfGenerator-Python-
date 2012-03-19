import datetime
import re 
import os
from pyPdf import PdfFileWriter, PdfFileReader
import xml.etree
from urllib2 import Request, urlopen
from StringIO import StringIO 
def date():
  """Returns the date in the format used by the url of the newspapers"""
  now = datetime.datetime.now()
  return str(now.day) + str(now.month) + str(now.year)
#kantipuractualurl = 'http://epaper.ekantipur.com/1732012/epaperpdf/1732012-md-hr-6.pdf'
def totalpages():
  """Retruns the total pages of the paper by counting the pages from the xml file"""
  file = urlopen('http://epaper.ekantipur.com/ktpost/' + date() +'/pages.xml')
  data = file.read()
  return data.count('<page>')
def pagelist():
  """Returns a list with all the url of teh individual pages"""
  pages = []
  for i in range(1,totalpages()+1):
    pages.append('http://epaper.ekantipur.com/' + date() + '/epaperpdf/' + date() +'-md-hr-'+str(i) +'.pdf')
  return pages
writer = PdfFileWriter()
pages = pagelist()
for i in pages:
	remoteFile = urlopen(Request(i)).read()
	memoryFile = StringIO(remoteFile)
	pdfFile = PdfFileReader(memoryFile)
	for pageNum in xrange(pdfFile.getNumPages()):
		currentPage = pdfFile.getPage(pageNum)
		writer.addPage(currentPage)


outputStream = open(date()+"(kantipur)"+".pdf","wb")
writer.write(outputStream)
outputStream.close()
