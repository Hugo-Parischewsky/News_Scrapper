import requests
import pandas as pd
from bs4 import BeautifulSoup

### Global Variables ###


url = ['https://www.biobiochile.cl',
      'https://www.semana.com',
      'https://ciperchile.cl',
      'https://www.elsur.cl/impresa/2020/03/03/papel/',
      'https://www.eldesconcierto.cl/']




### Class ###


class scraper:

    def __init__(self,url,kw):
        self.url = url
        self.kw = kw
        self.lista_links = []
        self.dup = []
        self.header = []
        self.lista_final = []



    def link_extractor(self):
        for link in self.url:
            r = requests.get(link)
            soup = BeautifulSoup(r.content,'lxml')
            f = soup.find_all('a')
            for href in f:
                a = href.get('href')
                #print(a)
                if isinstance(a,str):
                    #print(a)
                    if len(a.split('https')) > 1:
                        #print(a)
                        if len(a.split('-')) > 5:
                            for word in self.kw:
                                if a.find(str(word)) != -1:
                                    self.lista_links.append(a)

        return self.lista_links
    

    def duplicate(self):
        for b in self.link_extractor():
            if b not in self.dup:
                self.dup.append(b)
                #print(b)
        return self.dup

    def separator(self):
        '''
        Function to isolate header from link
        x1: url (str)
        '''
        links = self.duplicate()
        for x1 in links:

            x1 = x1.split('//')[1]
            x1 = x1.split('/')
            for n in x1:
                if len(n) == 0:
                    x1.pop(-1)
                else:
                    pass
            x1 = x1[-1]
            x1 = x1.split('.')[0]
            x1 = x1.replace('-',' ')
            self.header.append(x1)
        return self.header









