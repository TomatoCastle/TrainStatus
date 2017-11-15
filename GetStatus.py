from bs4 import BeautifulSoup

class GetStatus:
    def __init__(self,uri):
        self.uri = uri
        html_text = open(uri,'r')
        self.soup = BeautifulSoup(html_text.read(),'html.parser')

    def getTrainStatus(self):
        return self.connectWebToGetStatus()

    def connectWebToGetStatus(self):
        contents = self.soup.find('div', id="mdServiceStatus")
        onTime = self.checkOnTime(contents)
        nowStatus = contents.find('p').text
        print(nowStatus)

    def isOnTime(self,contents):
        if len(contents.find_all('trouble')) == 0:
            return True
        else:
            return False

    def getLineTitle(self, contents):
        pass #todo

    def update(self):
        html_text = open(self.uri,'r')
        self.soup = BeautifulSoup(html_text.read(),'html.parser')

