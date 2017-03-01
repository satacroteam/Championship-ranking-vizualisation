import pycurl,os,re,time
import numpy as np
from StringIO import StringIO
from bs4 import BeautifulSoup

os.chdir('/Users/hola/Desktop/Sorties')
#valeur a modifier pour la periode souhaite
v=np.r_[5:60:1]
for int in v:
   vv=str(int)
   vec=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38]
   dico = {}
   for i in vec:
    a = str(i)
    url1 = 'http://www.lfp.fr/ligue1/competitionPluginClassement/loadClassement?sai='+vv+'&journee1=1&journee2='+a+'&cat=Gen'
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL,url1)
    c.setopt(pycurl.HTTPHEADER, ['X-Requested-With: XMLHttpRequest', 'Content-Type: application/x-www-form-urlencoded'])
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    bodi = buffer.getvalue()
    time.sleep(1)
    soup = BeautifulSoup(bodi, 'html.parser')
    lignes = soup.findAll('tr')
    for l in lignes:
        if (len(l.findAll('td')) == 11):
                team = l.findAll('td')[2].text.replace(" ", "").replace("\n", "").replace("\t", "").encode('ascii',
                                                                                                           'ignore') + \
                       l.findAll('td')[0].text
                teamf = re.sub(r'(([1-9].*|\-))$', r',\1', team)
                teamff = teamf.split(',')
                if teamff[0] in dico.keys():
                  dico[teamff[0]].append([teamff[1]])
                else:
                  dico[teamff[0]] = [[teamff[1]]]
   w = open("output"+vv+".txt", "a")
   for g in dico.items():
    a=str(g)
    b=re.sub(r'(\(u|\[\[u\'|\[u\'|\'\]|\]\)|\')', '', a)
    w.write(b + '\n')
   for g in dico.items():
    a=str(g)
    b=re.sub(r'(\(u|\[\[u\'|\[u\'|\'\]|\]\)|\')', '', a)
    w.write(b + '\n')
