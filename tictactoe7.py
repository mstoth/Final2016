
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
        # something like self.matrix=[[<expression>] <expression>]
        # instead of numbers, we want characters so use ' ' as the
        # value to fill the matrix (remember we used 0 for the Maze) 
        
        self.matrix=[[' ' for i in range(3)] for j in range(3)]

    def line(self):
        return('-----')

    def line1(self):
        return self.matrix[0][0]+'|'+self.matrix[1][0]+'|'+self.matrix[2][0]
    
    def line2(self):
        return self.matrix[0][1]+'|'+self.matrix[1][1]+'|'+self.matrix[2][1]
    
    def line3(self):
        return self.matrix[0][2]+'|'+self.matrix[1][2]+'|'+self.matrix[2][2]
    
    def getBoard(self):
        return self.line1()+"\n"+self.line()+'\n'+self.line2()+'\n'+\
               self.line()+'\n'+self.line3()+'\n'

    def printBoard(self):
        print(self.getBoard())

    def setX(self,col,row):
        self.matrix[col][row]='x'

    def setO(self,col,row):
        self.matrix[col][row]='o'

    def winner(self,player):
        if player=='x':
            if  self.matrix[0][0]=='x' and self.matrix[1][0]=='x' and \
                self.matrix[2][0]=='x' or \
                self.matrix[0][1]=='x' and self.matrix[1][1]=='x' and \
                self.matrix[2][1]=='x'or \
                self.matrix[0][2]=='x' and self.matrix[1][2]=='x' and \
                self.matrix[2][2]=='x' or \
                self.matrix[0][0]=='x' and self.matrix[0][1]=='x' and \
                self.matrix[0][2]=='x' or \
                self.matrix[1][0]=='x' and self.matrix[1][1]=='x' and \
                self.matrix[1][2]=='x'or \
                self.matrix[2][0]=='x' and self.matrix[2][1]=='x' and \
                self.matrix[2][2]=='x' or \
                self.matrix[0][0]=='x' and self.matrix[1][1]=='x' and \
                self.matrix[2][2]=='x' or \
                self.matrix[2][0]=='x' and self.matrix[1][1]=='x' and \
                self.matrix[0][2]=='x':
                return True
        return False

"""
Here are the tests we need
"""

class testTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game=TicTacToe()
        
    def testClassExists(self):
        self.assertIn('tic tac toe',self.game.__doc__)

    def testMatrix(self):
        # the matrix has a len of 3 (3 lists of 3 elements)
        # this tests that you meet that requirement
        self.assertEqual(3,len(self.game.matrix))

        # each list in the empty matrix should be a list of three blanks
        # this checks each list in the matrix so it's equal to that. 
        for c in self.game.matrix:
            self.assertEqual([' ',' ',' '],c)

    def testLine(self):
        """ tests for drawing a line """
        # We should see '-----' for each horizontal line
        self.assertEqual('-----',self.game.line())

    def testLine1(self):
        """ tests for the top line of x and o """
        # we should see ' | | ' for each line in the blank matrix
        self.assertEqual(' | | ',self.game.line1())

    def testLine2(self):
        """ tests for the second line of x and o """
        self.assertEqual(' | | ',self.game.line2())
        
    def testLine3(self):
        """ tests for the third line of x and o """
        self.assertEqual(' | | ',self.game.line3())
        
    def testGetBoard(self):
        # this tests the complete board for an empty matrix
        self.assertEqual(' | | \n-----\n | | \n-----\n | | \n',self.game.getBoard())

    # we have been returning strings from everything so we can test them.
    # what we want is the board to actually be printed.  Probably a better
    # name for printBoard would be getBoard!
    # I have changed the test and function name for you.
    
    # add a function that will actually print the string to the console.
    # testing for this is deferred because it involves the user interface.
    # just write a method in the TicTacToe class that will call getBoard() and
    # print it to the screen.

    # We have not tested for anything but a blank board.
    # We need to be able to add an 'x' or an 'o'
    # Something like game.setX(col,row) or game.setO(col,row)
    # Here's a test

    def testSetX(self):
        self.game.setX(0,0)
        self.assertEqual(self.game.matrix[0][0],'x')
        
    def testSetO(self):
        self.game.setO(0,0)
        self.assertEqual(self.game.matrix[0][0],'o')

    def testBoardWithValues(self):
        # we want to make sure that the proper display of the board is shown
        self.game.setX(0,0)
        self.game.setO(1,1)
        self.game.setX(2,2)
        self.assertEqual('x| | \n-----\n |o| \n-----\n | |x\n',self.game.getBoard())

    # easy enough! passes right away.

    # we also need to determine if we have a winner.
    # There are 8 possible ways to win.
    # Here is a test for one of them.

    def testBoardIsWinnerForXWithTopRowAllXs(self):
        self.game.setX(0,0)
        self.game.setX(1,0)
        self.game.setX(2,0)
        self.assertTrue(self.game.winner('x'))

    # write the test for the second row winner for x here
    def testSecondRowForX(self):
        self.game.setX(0,1)
        self.game.setX(1,1)
        self.game.setX(2,1)
        self.assertTrue(self.game.winner('x'))
        
    # write the test for the third row winner for x here
    def testSecondRowForX(self):
        self.game.setX(0,2)
        self.game.setX(1,2)
        self.game.setX(2,2)
        self.assertTrue(self.game.winner('x'))
        
    # I will put the rest of them in for you
    def testFirstColX(self):
        self.game.setX(0,0)
        self.game.setX(0,1)
        self.game.setX(0,2)
        self.assertTrue(self.game.winner('x'))
        
    def testSecondColX(self):
        self.game.setX(1,0)
        self.game.setX(1,1)
        self.game.setX(1,2)
        self.assertTrue(self.game.winner('x'))
        
    def testThirdColX(self):
        self.game.setX(2,0)
        self.game.setX(2,1)
        self.game.setX(2,2)
        self.assertTrue(self.game.winner('x'))

    def testDiag1(self):
        self.game.setX(0,0)
        self.game.setX(1,1)
        self.game.setX(2,2)
        self.assertTrue(self.game.winner('x'))
        
    def testDiag2(self):
        self.game.setX(2,0)
        self.game.setX(1,1)
        self.game.setX(0,2)
        self.assertTrue(self.game.winner('x'))
        
    # I'll leave the 'o's to you.
    # it's the same.  Here's where knowing how to use a good text editor is
    # handy.

    # you can copy the code and replace the x with o easily that way.

    # Here's the algorithm for tic tac toe
    # 1. 

if __name__=="__main__":
    unittest.main()
