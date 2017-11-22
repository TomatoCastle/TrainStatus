from bs4 import BeautifulSoup
import requests

class GetStatus:
    def __init__(self,uri):
        self.checkTypeUri(uri)
        self.uri = uri
        html_text = open(uri,'r')
        #html_text = requests.get(uri)
        self.soup = BeautifulSoup(html_text.read(),'html.parser')
        self.__result = {}

    def getTrainStatus(self):
        return self.connectWebToGetStatus()

    def connectWebToGetStatus(self):
        contents = self.soup.find('div', id='mdServiceStatus')
        self.__result['status'] = str(contents.find('p').text)
        self.__result['isOntime'] = str(self.isOnTime(contents))
        self.__result['lineName'] = str(self.getLineTitle())
        return self.__result

    def isOnTime(self,contents):
        if len(contents.find_all(class_='trouble')) == 0:
            return True
        else:
            return False

    def getLineTitle(self):
        return self.soup.find('h1',class_='title').text

    def update(self):
        html_text = open(self.uri,'r')
        self.soup = BeautifulSoup(html_text.read(),'html.parser')

    def __str__(self):
        return str(self.__result)

    def checkTypeUri(self,uri):
        if not isinstance(uri,str):
            raise TypeError('\"uri\"\'s type must be \"str\"')


