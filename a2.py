#David Tran 500890757
#Assistance from: Eric Harley
def crossword (L):  
    #Helper function crosswordCreator that places the first word in the list in the center of a 20x20 matrix and calls
    ''' on other helper functions'''
    def crosswordCreator(L):
        matrix = [[' ']*20 for j in range (20)] #Creates 20x20 matrix
        start = (20 - len(L[0]))//2
        c = start
        for i in range(len(L[0])): # for loop that places word in the center of the matrix
            matrix[10][c] = L[0][i]
            c += 1
        for j in range(1,len(L)):# for loop helps call on helper functions: addvertical and addhorizontal
            #indexes of odd numbers will be placed vertically, even numbers will be placed horizontally. 
            '''Which is done by calling on other helper functions'''
            if j%2 == 1: 
                word = L[j]
                matrix = addvertical(matrix,word)
            else:
                word = L[j]
                matrix = addhorizontal(matrix,word)
        return matrix #returns matrix

    def addvertical(matrix,word): #Calls on helper function "verticalscan" and places word vertically in the matrix if vertcheck returns True
        vertcheck = False 
        report = ''
        letterfound = False
        for i in range(20):#runs through the rows of matrix
            for j in range(20): #runs through columns of matrix
                vertcheck,report = verticalscan(matrix,word,i,j) #calls on helper function and recieves "vertcheck" and "report"
                if vertcheck: #vertcheck indicates if word can be legally placed in the crossword. Places word if vertcheck is true
                    report = ''
                    for k in range(len(word)):
                        matrix[i+k][j] = word[k]
                    return matrix 
        for letter in word: #Checks if there are matching letters in the word and matrix
            for i in range(20):
                for j in range(20):
                    if letter == matrix[i][j]:
                        letterfound = True
        if not letterfound:
            report = 'no matching letter'
        print(word,':',report) #prints word followed by the report
        return matrix

    def verticalscan(matrix,word,row,column): #Checks if the word can be legally placed in the matrix starting from the row and column given
        if len(word) > 20: #if word is longer than the dimensions of matrix, returns false
            return False, 'reaches outside grid'
        matchfound = False
        report = ''
        for i in range(len(word)):
            if row + i > 19: #Checks if word can fit in the matrix when placed, if it can't, it returns false
                return False,'illegal adjacencies'
            letter = word[i]
            matrixletter = matrix[row + i][column]
            if row+i != 0: 
                if i == 0 and matrix[row - 1][column].isalpha(): #checks if the index above the first letter is a letter, returns false if Truue
                    return False, 'illegal adjacencies'
            if row+i != 19 and i != len(word) - 1: #Checks index under current row contains a letter that is the same as the next letter of the word
                if row + i + 1 > 19:
                    if matrix[row + 1][column].isalpha() and matrix[row + 1][column] != word[i + 1]:
                        return False, 'illegal adjacencies'               
                else:
                    if matrix[row + i + 1][column].isalpha() and matrix[row + i + 1][column] != word[i + 1]:
                        return False, 'illegal adjacencies'
            elif row+i != 19 and i == len(word) - 1: #if the for loop is at the last letter of the word, checks if the index under it is a letter, returns False if True
                if row + i + 1 > 19:
                    if matrix[row + 1][column].isalpha():
                        return False, 'illegal adjacencies'
                else:
                    if matrix[row + i + 1][column].isalpha():
                        return False, 'illegal adjacencies'
            if letter == matrixletter: 
                #Checks if columns next to the current index are not letters, returns false if true
                if column == 0:
                    if not matrix[row + i][column + 1].isalpha():
                        return False,'illegal adjacencies'
                    else:
                        matchfound = True
                elif column == 19:
                    if not matrix[row + i][column - 1].isalpha():
                        return False,'illegal adjacencies'
                    else:
                        matchfound = True
                else:
                    if not matrix[row + i][column + 1].isalpha() and not matrix[row + i][column - 1].isalpha():
                        return False,'illegal adjacencies'
                    else:
                        matchfound = True
            if matrixletter == ' ':
                # Checks if columns next to current index are not empty spaces(are letters), returns False if True
                if column == 0:
                    if matrix[row + i][column + 1] != ' ':
                        return False,'illegal adjacencies'
                    else:
                        continue
                elif column == 19:
                    if matrix[row + i][column - 1] != ' ':
                        return False,'illegal adjacencies'
                    else:
                        continue
                else:
                    if matrix[row + i][column + 1] != ' ' or matrix[row + i][column - 1] != ' ':
                        return False,'illegal adjacencies'
                    else:
                        continue
            elif matrixletter != letter: #returns False if letter isn't the same as the letter in the matrix
                return False, 'illegal adjacencies'
        return matchfound,'' #returns True and empty report (indicates that there were no errors)
    def addhorizontal(matrix,word): #does the same thing as addvertical, except it calls on helper function "horizontalscan" 
        horcheck = False
        letterfound = False
        report = ''
        for i in range(20): 
            for j in range(20): 
                horcheck,report = horizontalscan(matrix,word,i,j) 
                if horcheck:
                    report = ''
                    for k in range(len(word)):
                        matrix[i][j + k] = word[k]
                    return matrix
        for letter in word: 
            for i in range(20):
                for j in range(20):
                    if letter == matrix[i][j]:
                        letterfound = True
        if not letterfound: 
            report = 'no matching letter'
        print(word,':',report) 
        return matrix
    def horizontalscan(matrix,word,row,column): #Does the same thing as verticalscan, but looks at adjacent columns rather than rows
        if len(word) > 20:
            return False, 'reaches outside grid'
        matchfound = False
        report = ''
        for i in range(len(word)):
            if column + i > 19:
                return False,'illegal adjacencies'
            letter = word[i]
            matrixletter = matrix[row][column + i]
            if column+i != 0:
                if i == 0 and matrix[row][column - 1].isalpha():
                    return False, 'illegal adjacencies'
            if column+i != 19 and i != len(word) - 1:
                if column + i + 1 > 19:
                    if matrix[row][column + 1].isalpha() and matrix[row][column + 1] != word[i + 1]:
                        return False, 'illegal adjacencies'
                else:
                    if matrix[row][column + i + 1].isalpha() and matrix[row][column + i + 1] != word[i + 1]:
                        return False, 'illegal adjacencies'
            elif column+i != 19 and i == len(word) - 1:
                if column + i + 1 > 19:
                    if matrix[row][column + 1].isalpha():
                        return False, 'illegal adjacencies'
                else:
                    if matrix[row][column + i + 1].isalpha():
                        return False, 'illegal adjacencies'                
            if letter == matrixletter:
                if row == 0:
                    if not matrix[row + 1][column + i].isalpha():
                        return False,'illegal adjacencies'
                    else:
                        matchfound = True
                elif row == 19:
                    if not matrix[row - 1][column + i].isalpha():
                        return False,'illegal adjacencies'
                    else:
                        matchfound = True
                else:
                    if not matrix[row + 1][column + i].isalpha() and not matrix[row - 1][column + i].isalpha():
                        return False,'illegal adjacencies'
                    else:
                        matchfound = True
            if matrixletter == ' ':
                if row == 0:
                    if matrix[row + 1][column + i] != ' ':
                        return False,'illegal adjacencies'
                    else:
                        continue
                elif row == 19:
                    if  matrix[row - 1][column + i] != ' ':
                        return False,'illegal adjacencies'
                    else:
                        continue
                else:
                    if matrix[row + 1][column + i] != ' ' or matrix[row - 1][column + i] != ' ':
                        return False,'illegal adjacencies'
                    else:
                        continue
            elif matrixletter != letter:
                return False, 'illegal adjacencies'
        return matchfound,''
    return crosswordCreator(L)
print(['clowning','addle','apple','incline','plan','prove','burr','messaging','lose','post','mantis','nicely','yam','noise','ese','month','month','snapple','whiff'])
matrix = crossword(['clowning','addle','apple','incline','plan','prove','burr','messaging','lose','post','mantis','nicely','yam','noise','ese','month','month','snapple','whiff'])
print('_'*20)
for i in range(20): #prints out matrix
    for j in range(20):
        print(matrix[i][j],end='')
    print()
print('-'*20)
print(['aspsdfddfdasdqwewfkl','hospital','all','aid','allstars','lost','oooho','poool','apple','baa','aaaaaa','hi','bat','frozen','newlywed','dolphin','region','winning','pi','xxx','good'])
matrix = crossword(['aspsdfddfdasdqwewfkl','hospital','all','aid','allstars','lost','oooho','poool','apple','baa','aaaaaa','hi','bat','frozen','newlywed','dolphin','region','winning','pi','xxx','good'])
print('_'*20)
for i in range(20): #prints out matrix
    for j in range(20):
        print(matrix[i][j],end='')
    print()
print('-'*20)

