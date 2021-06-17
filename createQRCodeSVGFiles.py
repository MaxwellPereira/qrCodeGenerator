import re
import pyqrcode
import png

arq = open('.\\text\\arq.txt', 'r')
dirImg = '.\\imgs\\'
list = arq.readlines()
arq.close()
for i, xLin in enumerate(list):
    name = re.sub('\n','',list[i][list[i].rfind('/')+1:len(list[i])])
    link = re.sub('\n','',list[i])
    url = pyqrcode.create(link)
    #pode-se utilizar svg
    url.svg(dirImg + name + '.svg', scale=30)
