import re
import datetime
class SortTrack(object):
    def __init__(self):
        self.lista = None
        self.track = None

    def showTrack(self,track):
        for item in track:
            print item[0],item[1],item[2]

    def removeList(self,lista,track):
        for item in track:
            for cont, remove in enumerate(lista):
                if remove[0] == item[1]:
                    del(lista[cont])
                    break
        self.lista = lista
        return self.lista

    def openFile(self,fileName,item):
        regex = r"[0-9]{2}(?=min)|lightning"
        lista = list()
        if fileName is None:
            File = item
        else:
            File = open(fileName,"r")
        for line in File:
            try:
                description = re.split(regex,line)[0]
                time = re.search(regex, line).group(0)
                lista.append([description,time])
                self.lista = lista
            except Exception, e:
                print "Data Not Found in Item for Conference tracks, please enter minutes" +':\n'+ e.__str__()
                exit(0)
        return self.lista

    def createTrack(self,lista):
        start_hora = 9
        lunch_hora = 12
        stop_hora = 17
        networking_start = 16
        start = datetime.timedelta(hours=start_hora)
        dlunch = datetime.timedelta(hours=lunch_hora)
        lunch = (datetime.datetime.min + dlunch).time()
        dstop = datetime.timedelta(hours=stop_hora)
        stop = (datetime.datetime.min + dstop).time()
        total = (datetime.datetime.min + start).time()

        aux = list()
        tryAgain = 0
        stop_ok = 0
        lunch_ok = 0
        while tryAgain < 25:
            sizeLista = len(lista)
            for cont, item in enumerate(lista):
                if item[1] == 'lightning':
                    item[1] = item[1].replace('lightning','5')
                    continue
                if cont == 0:
                    fmt = (datetime.datetime.min + start).time()
                    start = start + datetime.timedelta(minutes=int(item[1]))
                    total = (datetime.datetime.min + start).time()
                    aux.append([fmt.strftime('%I:%M%p'),item[0],item[1]])
                elif total == lunch:
                    aux.append([lunch.strftime('%I:%M%p'),'Lunch', 60])
                    start = start + datetime.timedelta(minutes=60)
                    total = (datetime.datetime.min + start).time()
                    lunch_ok = 1
                elif total < lunch:
                    close = start + datetime.timedelta(minutes=int(item[1]))
                    close = (datetime.datetime.min + close).time()
                    if close > lunch:
                        close = 0
                        continue
                    fmt = (datetime.datetime.min + start).time()
                    start = start + datetime.timedelta(minutes=int(item[1]))
                    total = (datetime.datetime.min + start).time()
                    aux.append([fmt.strftime('%I:%M%p'),item[0],item[1]])
                elif total == stop or cont+1 == sizeLista:
                    start = start + datetime.timedelta(minutes=60)
                    total = (datetime.datetime.min + start).time()
                    aux.append([stop.strftime('%I:%M%p'),'Networking Event', 5])
                    stop_ok = 1
                    tryAgain = 30
                    break
                elif total > lunch and total < stop:
                    close = start + datetime.timedelta(minutes=int(item[1]))
                    close = (datetime.datetime.min + close).time()
                    if close > stop:
                        close = 0
                        continue
                    fmt = (datetime.datetime.min + start).time()
                    start = start + datetime.timedelta(minutes=int(item[1]))
                    total = (datetime.datetime.min + start).time()
                    aux.append([fmt.strftime('%I:%M%p'),item[0],item[1]])

            if stop_ok == 0 and lunch_ok == 0:
                aux = list()
                tryAgain += 1
                start = datetime.timedelta(hours=start_hora)
                total = (datetime.datetime.min + start).time()
                lista = sorted(lista)
            elif stop_ok == 0:
                self.removeList(lista,aux)
                tryAgain += 1
                if not aux:
                    start = datetime.timedelta(hours=13)
                total = (datetime.datetime.min + start).time()
                lista = sorted(lista)

        self.lista = aux
        return self.lista

