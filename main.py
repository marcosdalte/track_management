from sortTrack import SortTrack
from inputParser import InputParser
from sys import exit, argv
from getopt import getopt

if __name__ == '__main__':
    inputParser = InputParser()
    if (len(argv) == 1):
        inputParser.usage(argv[0])
        exit(0)

    try:
        opts, args = getopt(argv[1:],"hvif:",["help","version"])
        if not opts:
            inputParser.usage(argv[0])
            exit(0)

    except Exception, e:
        inputParser.usage(argv[0])
        exit(0)
    fileName = None
    item = None
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            inputParser.usage(argv[0])
            exit(0)
        elif opt in ("-v", "--version"):
            dir(inputParser)
            inputParser.getVersion()
            exit(0)
        elif opt in ("-f"):
            fileName = arg
        elif opt in ("-i"):
            item = inputParser.inputItem()
        else:
            assert False, "unhandled option"
    sortTrack = SortTrack()
    lista = sortTrack.openFile(fileName,item)
    track1 = sortTrack.createTrack(lista)
    print "Track 1:"
    sortTrack.showTrack(track1)
    lista = sortTrack.removeList(lista,track1)

    print "Track 2:"
    track2 = sortTrack.createTrack(lista)
    sortTrack.showTrack(track2)
