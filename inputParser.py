class InputParser:
    def __init__(self):
        self.author = "Marcos Dalte <marcosdalte@gmail.com>"
        self.copyright = "Copyright (C) 2017 ThoughtWorks"
        self.license = "ThoughtWorks"
        self.version = '1.0.0'

    def getVersion(self):
        print "\n"
        print "Conference Track Management", self.version
        print self.copyright
        print "\n\n"

    def usage(self,argv):
        print """Usage: %s [-v] [-h] [-f input.txt]
            -i Insert track list manually.
            -v, --version\t\tShow Version Program.
            -h, --help\t\tShow help list.
            -f Specify a file to Open.
        """ % argv

    def inputItem(self):
        itemList = list()
        i = 0
        while 1:
            i+=1
            item = raw_input('Enter Item For Track List %s:' %i)
            if item == '':
                break
            itemList.append(item)
        return itemList

