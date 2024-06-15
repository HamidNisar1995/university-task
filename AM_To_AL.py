def mat_to_list(adj_mat):
    # create an empty variable for adj list of length equal to leght of adj matrix
    adj_list = [ [] for _ in range(len(adj_mat)) ]
    
    # use two loop outer and inner to access all the value of adj mat 
    ''' inside inner loop if adj mat index has value equal to 1 that means that coloumn has
    an arrow towards that row i.e if 0 has an arrow toward 1 then at adj_mat[0][1] = 1
    '''
    for i in range(len(adj_mat)):
        for j in range(len(adj_mat[i])):
            if adj_mat[i][j] == 1 :
                adj_list[i].append(j)
    return adj_list

# Test Cases

print("---------- Test Cases ---------")


adj_mat =   [[0, 1, 0, 1, 0, 0],
             [0, 0, 1, 0, 0, 0],
             [1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0],
             [0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0]]

output= mat_to_list(adj_mat)
print("first_testcase")
print(output)

adj_mat =   [[0, 1, 0, 1, 0, 1],
             [0, 0, 1, 0, 0, 0],
             [1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0],
             [0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 1, 0]]

output= mat_to_list(adj_mat)
print("Second_testcase")
print(output)