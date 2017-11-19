import GetStatus as gs

class StatusTelop:
    def __init__(self):
       self.sutasues = []

    def addLine(self,uri):
        self.sutasues.append(gs.GetStatus(uri))

    def __str__(self):
        str = ""
        for i in self.sutasues:
            sutatsu = i.getTrainStatus()
            str = '【' + sutatsu['lineName'] + '】 ' + sutatsu['status'] + "   "
        return str

