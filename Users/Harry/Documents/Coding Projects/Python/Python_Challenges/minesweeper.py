def is_valid_move(grid, row_length, map, output_map, i):
        print(grid+i)
        # Check that the new grid index is within the map string
        if 0 <= grid + i <= len(map) - 1 and output_map.get(grid + i) == None:
            
            # Make sure we don't open a grid that is not adjacent on the map
            # but is adjacent in the string.
            if grid == 0 and (i == -2 or i == - row_length or i == row_length - 2 or i == - (row_length - 2) or i == - (row_length + 2)):
                return False
            elif grid == len(map) -1 and (i == 2 or i == row_length or i == row_length + 2 or i == row_length - 2 or i == - (row_length + 2)):
                return False    
            elif grid + i == 0 and i == - (row_length - 2):
                return False
            elif grid + i == len(map) - 1 and i == row_length - 2:
                return False
            elif i == 2 and map[grid + i - 1] == '\n':
                return False
            elif i == -2 and map[grid + i + 1] == '\n':
                return False
            elif (i == row_length - 2 or i == - (row_length + 2)) and (map[grid + i + 1] == '\n'):
                return False
            elif (i == row_length + 2 or i == - (row_length - 2)) and (map[grid + i - 1] == '\n'):
                return False
            else:
                return True


def solve_mine(map, n):
    new_map_info = {}
    
    # Find size of map
    row_length = map.find('\n') + 1
    map_len = len(map)
    # Iterate through every element in the map
    for grid in range(len(map)):
        if map[grid] == "0":
            
            # Create empty dictionary for the new 'output' map
            new_map_info[grid] = '0'


            
            # For each 0 element, open the '?' elements around it
            for  i in [2, -2, row_length, - row_length, row_length + 2, row_length - 2,
            - (row_length - 2), - (row_length + 2)]:
              
                check = is_valid_move(grid, row_length, map, new_map_info, i)
                
                if check == True:
                    
                    # Convert string index to matrix x,y values
                    row = int(((grid + i) - ((grid + i) % row_length))/row_length)
                    column = int(((grid + i) % row_length)/2)
            
                    # Use open function and add to dictionary 
                    new_val = open(row, column)
                    new_map_info[grid + i] = str(new_val)
                    
                
    map_vals_to_add = {}
    bombs = []
    
    #Now cycle through new_map_info to asses if we can assign bombs
    for grid in new_map_info:
        
        #Check that it isn't already a bomb
        if new_map_info[grid] != 'x':
            
            val = int(new_map_info[grid])
            
            #Make sure it isn't 0 either, they've already been taken care of
            if val != 0:
                
                count = 0
                lst = []
                #Check the unknowns around each val
                for  i in [2, -2, row_length, - row_length, row_length + 2, row_length - 2, 
                - (row_length - 2), - (row_length + 2)]:
                    
                    #Make sure the move is valid
                    check = is_valid_move(grid, row_length, map, new_map_info, i)
                   
                    if check == True:
                        
                        # we count the unknowns around the val
                        count += 1
                        lst.append(grid + i)
                print(count)
                # If the no. of unknowns matches the val numuber we can turn them to bombs
                if count == val:
                    
                    for grid2 in lst:
                        
                        if map_vals_to_add.get(grid2) == None:
                            
                            #Assign bombs
                            map_vals_to_add[grid2] = 'x'
                            bombs.append(grid2)
                            
                    '''for  j in [2, -2, row_length, - row_length, row_length + 2, row_length - 2, 
                    - (row_length - 2), - (row_length + 2)]:
                        #print('here')
                        if grid + j in bombs:
                            pass
                        else:
                            # Check that the new grid index is within the map string
                            check = is_valid_move(grid, row_length, map, i)
                            if check == True:

                                # Convert string index to matrix x,y values
                                row = int(((grid + j) - ((grid + j) % row_length))/row_length)
                                column = int(((grid + j) % row_length)/2)
                                
                                # Use open function and add to dictionary 
                                new_val = open(row, column)
                                map_vals_to_add[grid + j] = str(new_val)'''
                                
    new_map_info.update(map_vals_to_add)            
    new_map = "" 
    for i in range(len(map)):
        if (i + 1) % row_length == 0:
            new_map += '\n'
        elif i % 2 == 1:
            new_map += ' '
        elif i in new_map_info:
            new_map += new_map_info[i]
        else:
            new_map += '?'
    print(new_map)
    return new_map


gamemap = """
? ? ? ? ? ?
? ? ? ? ? ?
? ? ? 0 ? ?
? ? ? ? ? ?
? ? ? ? ? ?
0 0 0 ? ? ?
""".strip()

print(gamemap[0:6])
print((4 - (4%11))/11)