import GetStatus as gs

class StatusTelop:
    def __init__(self):
       self.sutasues = []

    def addLine(self,uri):
        self.checkTypeUri(uri)
        self.sutasues.append(gs.GetStatus(uri))

    def __str__(self):
        str = ""
        for i in self.sutasues:
            sutatsu = i.getTrainStatus()
            str += '【' + sutatsu['lineName'] + '】 ' + sutatsu['status'] + "        "
        return str

    def checkTypeUri(self,uri):
        if not isinstance(uri,str):
            raise TypeError('\"uri\"\'s type must be \"str\"')

    def __eq__(self, other):
        return other.sutasues == self.sutasues