from bs4 import BeautifulSoup
import requests

class GetStatus:
    def __init__(self,uri):
        self.checkTypeUri(uri)
        self.uri = uri
        html_text = open(uri,'r')
        #html_text = requests.get(uri)
        self.soup = BeautifulSoup(html_text.read(),'html.parser')
        #self.soup = BeautifulSoup(html_text.text, 'html.parser')
        self.__result = {}

    def getTrainStatus(self):
        #self.update()
        return self.connectWebToGetStatus()

    def connectWebToGetStatus(self):
        contents = self.soup.find('div', id='mdServiceStatus')
        self.__result['status'] = contents.find('p').text
        self.__result['isOntime'] = self.isOnTime(contents)
        self.__result['lineName'] = self.getLineTitle()
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
        #html_text = requests.get(self.uri)
        self.soup = BeautifulSoup(html_text.read(),'html.parser')
        #self.soup = BeautifulSoup(html_text.text, 'html.parser')

    def __str__(self):
        return str(self.__result)

    def checkTypeUri(self,uri):
        if not isinstance(uri,str):
            raise TypeError('\"uri\"\'s type must be \"str\"')

    def __eq__(self, other):
        other_result = other.getTrainStatus()
        this_result = self.getLineTitle()
        return other_result == this_result

