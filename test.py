import unittest
from inputParser import InputParser
from sortTrack import SortTrack

class TestInputParser(unittest.TestCase):

    def test_inputItemEqual(self):
        inputParser = InputParser()
        self.assertEqual(inputParser.inputItem(),['4','4','4','4'])

    def test_inputItemNull(self):
        inputParser = InputParser()
        self.assertEqual(inputParser.inputItem(),[])

class TestSortTrack(unittest.TestCase):
    def test_createTrackEqual(self):
        lista = list()
        lista = [['event1','60'],['event2','60'],['event3','60']]
        sortTrack = SortTrack()
        self.assertEqual(sortTrack.createTrack(lista),[['09:00AM','event1','60'],['10:00AM','event2','60'],['11:00AM','event3','60']])

    def test_removeListEqual(self):
        lista = list()
        lista = [['event1','60'],['event2','60'],['event3','60']]
        remove = [['09:00AM','event1','60'],['10:00AM','event2','60'],['11:00AM','event3','60']]
        sortTrack = SortTrack()
        self.assertEqual(sortTrack.removeList(lista,remove),[])

if __name__ == '__main__':
    unittest.main()


