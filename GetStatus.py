from bs4 import BeautifulSoup

class GetStatus:
    def __init__(self,uri):
        self.uri = uri
        html_text = open(uri,'r')
        self.soup = BeautifulSoup(html_text.read(),'html.parser')

    def getTrainStatus(self):
        return self.connectWebToGetStatus()

    def connectWebToGetStatus(self):
        result = {}
        contents = self.soup.find('div', id='mdServiceStatus')
        result['status'] = contents.find('p').text
        result['isOntime'] = self.isOnTime(contents)
        result['lineName'] = self.getLineTitle()
        return result

    def isOnTime(self,contents):
        if len(contents.find_all(class_='trouble')) == 0:
            return True
        else:
            return False

    def getLineTitle(self):
        return self.soup.find(class_='title').text
        

    def update(self):
        html_text = open(self.uri,'r')
        self.soup = BeautifulSoup(html_text.read(),'html.parser')

