
import unittest

"""
We will work on a tic-tac-toe game.

Problem 1.  The board display

We need to print out the board at each turn.

The board will look something like

x|x|
-----
o|o|x
-----
o|x|o

We need to represent this board with an internal variable.
A good choice is a 3x3 matrix.

Each element in the matrix is either an 'x', 'o', or ' ' (blank)

Part 1. Create a function to print out the board given the matrix as an input.

Here's our class

"""

class TicTacToe(object):
    """ plays a tic tac toe game """
    def __init__(self):
        # we need to create a matrix to represent the board here.
        # something like self.matrix=...
        self.matrix=[] # this is an empty matrix. you need to make it a 3x3
        self.matrix=[[' ' for i in range(3)] for j in range(3)]

    def line(self):
        return('-----')

    def line1(self):
        return self.matrix[0][0]+'|'+self.matrix[1][0]+'|'+self.matrix[2][0]
    
    def line2(self):
        return self.matrix[0][1]+'|'+self.matrix[1][1]+'|'+self.matrix[2][1]
    
    def line3(self):
        return self.matrix[0][2]+'|'+self.matrix[1][2]+'|'+self.matrix[2][2]
    
    def printBoard(self):
        return self.line1()+"\n"+self.line()+'\n'+self.line2()+'\n'+\
               self.line()+'\n'+self.line3()+'\n'
        
"""
Here are the tests we need
"""

class testTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game=TicTacToe()
        
    def testClassExists(self):
        self.assertIn('tic tac toe',self.game.__doc__)

    def testMatrix(self):
        self.assertEqual(3,len(self.game.matrix))
        for c in self.game.matrix:
            self.assertEqual([' ',' ',' '],c)

    def testLine(self):
        """ tests for drawing a line """
        self.assertEqual('-----',self.game.line())

    def testLine1(self):
        """ tests for the top line of x and o """
        self.assertEqual(' | | ',self.game.line1())

    def testLine2(self):
        """ tests for the second line of x and o """
        self.assertEqual(' | | ',self.game.line2())
        
    def testLine3(self):
        """ tests for the third line of x and o """
        self.assertEqual(' | | ',self.game.line3())
        
    def testPrintBoard(self):
        self.assertEqual(' | | \n-----\n | | \n-----\n | | \n',self.game.printBoard())
        

if __name__=="__main__":
    unittest.main()
