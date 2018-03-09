#coding:utf-8
import win32com
import win32con
import win32gui
import codecs
from win32com.client import Dispatch
import pythoncom
from gensim.models import Word2Vec
from pprint import pprint
import re, collections
import matplotlib.pyplot as plt

protocol = '38101-1'
txtfile = protocol + '.txt'
docfile = protocol + '.doc'
path = 'D:/Github/5G/word/protocol/'

class MSOffice2txt():
    def __init__(self, fileType=['doc']):
        self.docCom = None
        pythoncom.CoInitialize()
        if type(fileType) is not list:
            return 'Error, please check the fileType, it must be list[]'
        for ft in fileType:
            if ft == 'doc':
                self.docCom = self.docApplicationOpen()

    def close(self):
        self.docApplicationClose(self.docCom)

    def docApplicationOpen(self):
        docCom = win32com.client.Dispatch('Word.Application')
        docCom.Visible = 1
        docCom.DisplayAlerts = 0
        docHwnd = win32gui.FindWindow(None, 'Microsoft Word')
        win32gui.ShowWindow(docHwnd, win32con.SW_HIDE)
        return docCom

    def docApplicationClose(self,docCom):
        if docCom is not None:
            docCom.Quit()

    def doc2Txt(self, docCom, docFile, txtFile):
        doc = docCom.Documents.Open(FileName=docFile,ReadOnly=1)
        doc.SaveAs(txtFile, 2)
        doc.Close()

    def translate(self, filename, txtFilename):
        if filename.endswith('doc') or filename.endswith('docx'):
            if self.docCom is None:
                self.docCom = self.docApplicationOpen()
            self.doc2Txt(self.docCom, filename, txtFilename)
            return True
        else:
            return False

class MyCorpus(object):
	def __init__(self, fname):
		self.fname = fname

	def __iter__(self):
		for line in open(self.fname):
			yield line.lower().split()


if __name__ == '__main__':
	msoffice = MSOffice2txt()
	if msoffice.translate(path + docfile, path + txtfile):
	    print('Successed!')
	else:
	    print('Failed!')
	msoffice.close()

	with open(txtfile, 'r') as f:
		file = f.read()
		words = [word for word in file.split() if re.findall(r'\w', word)]
	print(len(words))

	sentences = MyCorpus(txtfile)
	model = Word2Vec(sentences, size=2, min_count=1)

	x, y = 0, 0
	for word in words:
		say_vector = model[word.lower()]  # get vector for word
		x += say_vector[0]
		y += say_vector[1]
	x /= len(words)
	y /= len(words)


	with open('data.txt', 'a') as f:
		f.write(protocol + ' ' + str(x) + ' ' + str(y) + ' ' + str(len(words)) + '\n')


	'''
	plt.figure()
	plt.scatter(x, y, s=len(words), facecolors='none', edgecolors='r')
	plt.scatter(x, y, s=10, color='r')
	plt.text(x, y, '38211-002')
	plt.show()
	'''
