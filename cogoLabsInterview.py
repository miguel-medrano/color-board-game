import random
import Tkinter
'''
CogoLabs Interview Question 11/6/15
Color Board
Represents an m(rows) by n(columns) game board where each square is initially colored one of c different colors.
Goal of game is to change all the board to one single color.
The only allowed moved is to change the upper left square color C to a different color C', and consequently,
if the neighbors of this square have color C, are also changed to color C' and neighbors of these in turn are changed,
if color C, to C' and so on.

Example: n=4, m=4, c=3
(Let the numbers 1,2,3 represent different colors)
1 1 2 3                        (2) (2)  2  3
3 1 1 3  ==============>>>>>    3  (2) (2) 3
1 1 1 3  (Changing upperLeft   (2) (2) (2) 3
2 1 3 2    square color to 2)   2  (2)  3  2
'''

class ColorBoard:
	def __init__(self, m, n, c):
		boardArray = []
		for rowNumber in range(m):
			row = []
			for columnNumber in range(n):
				colorNumber = int(random.random()*c)
				row.append(colorNumber)
			boardArray.append(row)
		self.boardArray = boardArray
		self.rows = m
		self.columns = n
	def getRows(self):
		return self.rows

	def getColumns(self):
		return self.columns

	def getBoardArray(self):
		return self.boardArray

	def printBoard(self):
		boardString = ""
		for row in range(self.rows):
			for column in range(self.columns):
				boardString += str(self.boardArray[row][column]) + ("\n" if column is self.columns-1 else " ")
		print boardString

	def changeTopLeftColor(self, newColor):
		topLeftColor = self.boardArray[0][0]
		def changeCell(row, column):
			self.boardArray[row][column] = newColor
			for offset in [-1,1]:
				if 0 <= row+offset < self.rows:
					if self.boardArray[row+offset][column] is topLeftColor:
						changeCell(row+offset, column)
				if 0 <= column+offset < self.columns:
					if self.boardArray[row][column+offset] is topLeftColor:
						changeCell(row, column+offset)
		if newColor is not topLeftColor:
			changeCell(0,0)

class BoardGUI(Tkinter.Tk):
	def __init__(self, parent):
		Tkinter.Tk.__init__(self, parent)
		self.parent = parent
		self.initalize()

	def initalize(self):
		self.grid()
		rowsLabel = Tkinter.Label(self, text="Number of Rows: ")
		rowsLabel.grid(column=0, row=0)

		columnsLabel = Tkinter.Label(self, text="Number of Columns: ")
		columnsLabel.grid(column=0, row=2)

		colorBoard = ColorBoard(4,4,3)
		colors = ["red","blue","green"]
		boardArray = colorBoard.getBoardArray()
		for row in range(colorBoard.getRows()):
			for column in range(colorBoard.getColumns()):
				colorSquare = Tkinter.Label(self,relief="solid", bd=5, bg=colors[int(boardArray[row][column])],height=5,width=10)
				colorSquare.grid(column=column+1, row=row, sticky='EWNS')


if __name__ == "__main__":
	boardGUI = BoardGUI(None)
	boardGUI.title('Color Board Game')
	boardGUI.mainloop()

'''
gameBoard = Board(4,4,3)
gameBoard.printBoard()
print gameBoard.boardArray
'''