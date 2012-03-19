import datetime
import re 
import os
from pyPdf import PdfFileWriter, PdfFileReader
import xml.etree
from urllib2 import Request, urlopen
from StringIO import StringIO 
import sys
try:
  papername = sys.argv[1]
except:
  print """Usage $ python downloadpaper.py papername
  example python downloadpaper.py KTMPost 
          python downloadpaper.py Kantipur
  Only two paper supported currently"""

def date():  
  """Returns the date in the format used by the url of the newspapers"""
  now = datetime.datetime.now()
  return str(now.day) + str(now.month) + str(now.year)
def totalpages(papername):
  """Retruns the total pages of the paper by counting the pages from the xml file"""
  if papername == "Kantipur":
    file = urlopen('http://epaper.ekantipur.com/' + date() +'/pages.xml')
  if papername == "KTMPost":
    file = urlopen('http://epaper.ekantipur.com/ktpost/' + date() +'/pages.xml')
  data = file.read()
  return data.count('<page>')
def pagelist(papername):
  """Returns a list with all the url of teh individual pages"""
  pages = []
  for i in range(1,totalpages(papername)+1):
    if papername == "Kantipur":
      pages.append('http://epaper.ekantipur.com/' + date() + '/epaperpdf/' + date() +'-md-hr-'+str(i) +'.pdf')
    if papername == "KTMPost":
      pages.append('http://epaper.ekantipur.com/ktpost/' + date() + '/epaperpdf/' + date() +'-md-hr-'+str(i) +'.pdf')
  return pages

def pdfprinter(papername):
  """Prints the pdf output"""
  writer = PdfFileWriter()
  pages = pagelist(papername)
  for i in pages:
    remoteFile = urlopen(Request(i)).read()
    memoryFile = StringIO(remoteFile)
    pdfFile = PdfFileReader(memoryFile)
    currentPage = pdfFile.getPage(0) #just need the first page, we only have one page
    writer.addPage(currentPage)
  outputStream = open(date()+"("+papername+")"+".pdf","wb")
  writer.write(outputStream)
  outputStream.close()

try:
  pdfprinter(papername)
except:
  print "Nothing to do here. Exiting......."  
