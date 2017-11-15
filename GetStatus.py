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
        contents = self.soup.find('div', id="mdServiceStatus")
        onTime = self.isOnTime(contents)
        result['status'] = contents.find('p').text
        result['lineName'] = self.getLineTitle(contents)
        return result

    def isOnTime(self,contents):
        if len(contents.find_all('trouble')) == 0:
            return True
        else:
            return False

    def getLineTitle(self, contents):
        return None
        #todo

    def update(self):
        html_text = open(self.uri,'r')
        self.soup = BeautifulSoup(html_text.read(),'html.parser')

