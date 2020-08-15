import numpy as np
def run(r,c):
    """ This function does all the calculations necessary. Just provide it with the number of rows and columns.
    Remember that this only works for square matrices, meaning the number of rows must be the same as the number of columns.
    You can run the code with a simple function call outside the function definition
    
    Example: run(4,4)"""
    # gen function creates the matrix and fills it based on the rows and columns you gave
    gen =  lambda row,column : np.arange(1,(row*column)+1).reshape(row,column)
    arr =  gen(r,c)
    
    # Getting the rows of the matrix
    ROWS = []
    for row in arr:
        ROWS.append(row)
        
    #Getting the columns of the matrix
    COLS = []
    for col in range(len(arr)):
        COLS.append(arr[:,col])
        
    #Getting diagonals of the matrix using the offset method of numpy
    DIAG = []

    diff = r - 3
    for v in list(range(-diff,diff+1)):
        DIAG.append(arr.diagonal(offset=v))

    # Finding the backwards diagonal
    rev_arr = arr[:,::-1]
    REV_DIAG = []
    for v in list(range(-diff,diff+1)):
        REV_DIAG.append(rev_arr.diagonal(offset=v))

    # Adding the main diagonals to the backwards ones
    DIAG = DIAG + REV_DIAG




    # Printing the matrix, its rows, columns and diagonal to screen
    print('Matrix:\n', arr)
    print()
    
    print('===========================')
    print('Rows: ', ROWS)
    print('Columns: ', COLS)
    print('Diagonals: ', DIAG)
    print('===========================')
    print()
    

    # COMPUTING SUB-ROWS
    
    # This dictionary will store all the sub-rows. The keys of the matrix will be the row number(starting from 0)
    #and the corresponding values will represent the sub-rows for that row. Apply same for columns
    row_dict = {}
    
    # Looping through all the rows in the matix
    for x in range(len(ROWS)):
        # This variable will store all the sub-rows of a row
        sub_rows = []
        # Since we're grouping in threes, we slice from 0 to 3 then 1 to 4 then 2 to 5...etc..
        start = 0
        stop = 3
        for i in range((len(ROWS[x])-3)+1):
            sub_rows.append(ROWS[x][start:stop])
            # Incrementing start and stop to facililtate the pattern I mentioned above
            start+=1
            stop+=1
        # Adding each list of sub-rows to a dictionary where the row number(starting from 0 serves as the key)
        row_dict[x] = sub_rows
        
    # Printing all the sub-rows   
    print('Sub-Rows: ',row_dict)
    print()
    
    """The comments for #COMPUTING SUB-ROWS SHOULD APPLY TO #COMPUTING SUB-COLUMNS AS WELL"""
    # COMPUTING SUB-COLUMNS
    col_dict = {}
    for x in range(len(COLS)):
        sub_cols = []
        start = 0
        stop = 3
        for i in range((len(COLS[x])-3)+1):
            sub_cols.append(COLS[x][start:stop])
            start+=1
            stop+=1
        col_dict[x] = sub_cols
        
        
    print('Sub-Columns: ',col_dict)
    print()
    
    
    # COMPUTING SUB-DIAGONALS
    diag_dict = {}
    for x in range(len(DIAG)):
        sub_diag = []
        start = 0
        stop = 3
        for i in range((len(DIAG[x])-3)+1):
            sub_diag.append(DIAG[x][start:stop])
            start+=1
            stop+=1
        diag_dict[x] = sub_diag
        
        
    print('Sub-Diagonals: ',diag_dict)
    print()

run(5,5)