def rotate(matrix):
    #reverse the matrix
    low,high=0,len(matrix)-1
    while (low<high):
        matrix[low],matrix[high]=matrix[high],matrix[low]
    
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]




