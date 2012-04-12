'''
Created on 12-04-2012

@author: Marta and Dawid Ireno
'''
import unittest

from hack import game

class Test(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.board = game.Board()
        
    def test_gen_dict(self):
        self.board.cells = [(1,1), (3,2)]
        result = self.board.gen_dict()
        self.assertDictContainsSubset({(0,0):1,(1,0):1, (2,0):1, (3,1):1, (4,1):1, (4,2):1, 
                                       (4,3):1, (3,3):1, (2,3):1, (1,2):1, (0,2):1, (0,1):1,
                                        (2,1):2, (2,2):2 }, result)

    def test_should_live_0_1(self):
        result = self.board.should_live(0, True)
        self.assertEqual(result, False)
        result = self.board.should_live(1, True)
        self.assertEqual(result, False)
        
    def test_should_live_2_3(self):
        result = self.board.should_live(2, True)
        self.assertEqual(result, True)
        result = self.board.should_live(2, False)
        self.assertEqual(result, False)
        result = self.board.should_live(3, True)
        self.assertEqual(result, True)
        
    def test_should_live_more_3(self):
        result = self.board.should_live(4, True)
        self.assertEqual(result, False)
        result = self.board.should_live(8, True)
        self.assertEqual(result, False)
        
    def test_tick(self):
        self.board.cells = [(2,1), (2,2), (2,3)]
        self.board.tick()
        expected = [(1,2),(2,2), (3,2)]
        expected.sort()
        self.board.cells.sort()
        self.assertListEqual(expected, self.board.cells)     

    def test_tick_tok(self):
        oscilator_input = [(2,1), (2,2), (2,3)]
        oscilator_input.sort()
        self.board.cells = oscilator_input
        self.board.tick()
        self.board.tick()
        self.board.cells.sort()
        self.assertListEqual(oscilator_input, self.board.cells)    
                
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()