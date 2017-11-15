from bs4 import BeautifulSoup

class GetStatus:
    def __init__(self,uri):
        html_text = open(uri,'r')
        self.soup = BeautifulSoup(html_text.read(),'html.parser')

    def getStatus(self):
        return self.connectWebToGetStatus()

    def connectWebToGetStatus(self):
        contents = self.soup.find('div', id="mdServiceStatus")
        print(contents.text)



