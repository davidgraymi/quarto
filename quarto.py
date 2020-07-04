class GamePiece():
    def __init__(self, height, color, shape, fill):
        self.height = height
        self.color = color
        self.shape = shape
        self.fill = fill

    def __str__(self):
        if self.height == 0:
            sheight = 'short'
        else:
            sheight = 'tall'
        if self.color == 0:
            scolor = 'light'
        else:
            scolor = 'dark'
        if self.shape == 0:
            sshape = 'circle'
        else:
            sshape = 'square'
        if self.fill == 0:
            sfill = 'hollow'
        else:
            sfill = 'solid'
        return '['+sheight+','+scolor+','+sshape+','+sfill+']'

    def __eq__(self, other):
        similarity = [0, 0, 0, 0]
        if self.height == other.height:
            similarity[0] = 1
        if self.color == other.color:
            similarity[1] = 1
        if self.shape == other.shape:
            similarity[2] = 1
        if self.fill == other.fill:
            similarity[3] = 1
        return similarity

        

class GameBoard():
    def __init__(self, board):
        self.board = board
        self.diagonal = [ [self.board[0], self.board[5], self.board[10], self.board[15]], [self.board[12], self.board[9], self.board[6], self.board[3]] ]

        self.horizontal = [ [self.board[0], self.board[1], self.board[2], self.board[3]],
                        [self.board[4], self.board[5], self.board[6], self.board[7]],
                        [self.board[8], self.board[9], self.board[10], self.board[11]],
                        [self.board[12], self.board[13], self.board[14], self.board[15]] ]

        self.vertical = [ [self.board[0], self.board[4], self.board[8], self.board[12]],
                        [self.board[1], self.board[5], self.board[9], self.board[13]],
                        [self.board[2], self.board[6], self.board[10], self.board[14]],
                        [self.board[3], self.board[7], self.board[11], self.board[15]] ]

        self.analyze()
    
    def __str__(self):
        return '['+str(self.board[0])+str(self.board[1])+str(self.board[2])+str(self.board[3])+']\n['+str(self.board[4])+str(self.board[5])+str(self.board[6])+str(self.board[7])+']\n['+str(self.board[8])+str(self.board[9])+str(self.board[10])+str(self.board[11])+']\n['+str(self.board[12])+str(self.board[13])+str(self.board[14])+str(self.board[15])+']\n'

    def compare(self, piece1, piece2):
        similarity = [0, 0, 0, 0]
        if isinstance(piece1, GamePiece) and isinstance(piece2, GamePiece):
            if piece1.height == piece2.height:
                similarity[0] = 1
            if piece1.color == piece2.color:
                similarity[1] = 1
            if piece1.shape == piece2.shape:
                similarity[2] = 1
            if piece1.fill == piece2.fill:
                similarity[3] = 1
        return similarity

    def analyze(self):
        print("--------------------------------------- gameboard ---------------------------------------")
        print("---------- diagonal ----------")
        self.verify(self.diagonal)
        print("---------- horizontal ----------")
        self.verify(self.horizontal)
        print("---------- vertical ----------")
        self.verify(self.vertical)
        print("--------------------------------------- end ---------------------------------------")

    def verify(self, lines):
        #single diagonal line
        for line in lines:
            output = ""
            print(str(line[0])+"\n"+str(line[1])+"\n"+str(line[2])+"\n"+str(line[3]))
            finalSimilarity = [0, 0, 0, 0]
            similarities = [[0, 0, 0, 0],[0, 0, 0, 0]]
            equalities = [[0], [0], [0]]

            # print("\nequalities")
            
            #get equality comparison of piece and next in line
            for i in range (0,3):
                equalities[i] = self.compare(line[i], line[i+1])
                # print(equalities[i])

            #get similarities of equality
            for i in range (0,2):
                if equalities[i][0] == 1 and equalities[i+1][0] == 1:
                    similarities[i][0] = 1

                if equalities[i][1] == 1 and equalities[i+1][1] == 1:
                    similarities[i][1] = 1

                if equalities[i][2] == 1 and equalities[i+1][2] == 1:
                    similarities[i][2] = 1

                if equalities[i][3] == 1 and equalities[i+1][3] == 1:
                    similarities[i][3] = 1

            # print("\nsimilarities")
            # print(similarities[0])
            # print(similarities[1])
            
            #compare similarities
            if similarities[0][0] == 1 and similarities[1][0] == 1:
                finalSimilarity[0] = 1

            if similarities[0][1] == 1 and similarities[1][1] == 1:
                finalSimilarity[1] = 1

            if similarities[0][2] == 1 and similarities[1][2] == 1:
                finalSimilarity[2] = 1

            if similarities[0][3] == 1 and similarities[1][3] == 1:
                finalSimilarity[3] = 1
            
            # print("\nfinal")
            print(finalSimilarity)

            #final results
            if finalSimilarity[0] == 1:
                output += "Win by height! "
            if finalSimilarity[1] == 1:
                output += "Win by color! "
            if finalSimilarity[2] == 1:
                output += "Win by shape! "
            if finalSimilarity[3] == 1:
                output += "Win by fill! "
            
            print("\n"+output+"\n")




p = [GamePiece(0, 0, 0, 0),GamePiece(0, 0, 0, 1),GamePiece(0, 0, 1, 0),GamePiece(0, 0, 1, 1),
    GamePiece(0, 1, 0, 0),GamePiece(0, 1, 0, 1),GamePiece(0, 1, 1, 0),GamePiece(0, 1, 1, 1),
    GamePiece(1, 0, 0, 0),GamePiece(1, 0, 0, 1),GamePiece(1, 0, 1, 0),GamePiece(1, 0, 1, 1),
    GamePiece(1, 1, 0, 0),GamePiece(1, 1, 0, 1),GamePiece(1, 1, 1, 0),GamePiece(1, 1, 1, 1)]

empty = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
full = [p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[12], p[13], p[14], p[15]]
diag1 = [p[0], 0, 0, 0, 0, p[1], 0, 0, 0, 0, p[2], 0, 0, 0, 0, p[3]]
b = [GameBoard(full)]
# print(b[0])
# print(b[1])
# print(b[2])