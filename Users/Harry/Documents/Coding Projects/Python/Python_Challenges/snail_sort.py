
def snail(array):
    result = []
    result += array[0]
    
    for j in range(len(array) - 1):
        
        if (j+1) % 2 != 0:

            for i in range(len(array) - (j+1)):
                result.append(array[i + (int((j+2)/2))][- (int((j + 2)/2))])

            for i in range(len(array) - (j+1)):
                result.append(array[- (int((j + 2)/2))][-int((j+2)/2) - (i+1)])
        
        elif (j+1) % 2 == 0:

            for i in range(len(array) - (j+1)):
                result.append(array[-int((j+1)/2) - (i+1)][int((j-1)/2)])

            for i in range(len(array) - (j+1)):
                result.append(array[int((j+1)/2)][i + int((j+1)/2)])
    
    return result

array = [[8, 4, 5, 7, 3, 5, 7], 
         [4, 6, 2, 6, 6, 8, 9], 
         [1, 0, 8, 6, 1, 1, 0], 
         [4, 7, 2, 8, 9, 5, 8],
         [6, 2, 9, 0, 8, 0, 6],
         [4, 6, 9, 1, 4, 2, 3],
         [6, 7, 2, 4, 5, 8, 3]]

print(snail(array))