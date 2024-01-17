import numpy as np

def contain_zeros(matrix):
    np_matrix = np.array(matrix)
    return np.all(np_matrix != 0)

def count_entries(arr):
    dct = dict()
    for i in arr:
        if not i in dct:
            dct.update({i:1})
        else:
            dct.update({i:dct.get(i) + 1})
    return dct

def evaluate(board_position, oponent_board):
    player_score = 0
    op_score = 0
    def __score(position):
        var_score = 0
        for row in position:
            row_score_list = [i * j**2 for i, j in count_entries(row).items()]
            var_score += sum(row_score_list)
        return var_score
    player_score = __score(board_position)
    op_score = __score(oponent_board)
    if contain_zeros(board_position) or contain_zeros(oponent_board):
        return -500 + (player_score > op_score) * 1000
    return player_score - op_score

def comp_arrays(arr1, arr2):
    return np.equal(arr1, arr2)

array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([1, 2, 5, 4, 5])

print(array1 * comp_arrays(array1, array2))