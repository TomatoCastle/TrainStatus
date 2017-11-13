from bs4 import BeautifulSoup

class GetStatus:
    def __init__(self,uri):
        html_text = open(uri,'r')
        self.soup = BeautifulSoup(html_text.read(),'html.parser')

    def getInfo(self):
        return self.getBody()

    def getBody(self):
        pass
        #todo



