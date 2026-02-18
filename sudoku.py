



class Board:
    '''
    The 9x9 sudoku board, with verification capability.
    set values are stored as integers between 1 and 9, with 0 representing unknowns
    '''

    def __init__(self, array:list[list[int]]|None = None) -> None:
        '''
        Docstring for __init__
        
        :param array: Array representation of a sudoku board
        :type array: list[list[int]]
        '''
    
        self._values = array if (not array is None) else [ [0]*9 for _ in range(9)]
        assert len(self._values) == 9
        for i in self._values: assert len(i) == 9

    def __getitem__(self, key)->int:
        
        return self._values[key[0]][key[1]]
    
    def __setitem__(self, key, value:int):
        self._values[key[0]][key[1]] = value
    
    def __repr__(self) -> str:
        
        return "[" + "]\n[".join([','.join(map(str,x)) for x in self._values]) + "]"
    
    def __iter__(self):
        self.iterand = 0
        return self

    def __next__(self):
        if self.iterand >= 9*9 - 1: raise StopIteration
        self.iterand +=1
        i,j = divmod(self.iterand, 9)
        return self[i,j]
    
    def invalid(self)->bool:
        '''
        Docstring for invalid
        Checks if current board is valid. that is:
        - every digit is either in 1-9, or unknown (=0)
        - every row, column, or box has at maximum one of each digit
        '''
        # invalid values:



        return True
    

if __name__ == "__main__":
    b = Board()
    b[2,1] = 3
    print(b[2,1])
    i = 0
    for x in b:
        i += 1
        x,y = divmod(i, 9)
        b[x,y] = i
    print(b)