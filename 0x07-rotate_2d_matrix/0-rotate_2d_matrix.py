#!/usr/bin/python3
"""0. Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """Function to perform the matrix rotation
    """
    n = m = t = 0
    mat_len = len(matrix)
    while n + m < mat_len - 1:
        while n + m < mat_len - 1:
            o, p = n, m
            curr_val = matrix[n][m]
            for i in range(4):
                next_val = matrix[p][(mat_len - 1) - o]
                matrix[p][(mat_len - 1) - o] = curr_val
                curr_val = next_val
                temp = o
                o = p
                p = (mat_len - 1) - temp
            n += 1
        t += 1
        n = m = t


# # figuring it out

# # Pseudocode
# n = 0
# m = 0
# t = 0
# while n + m < len(mat) - 1
# 	while n + m < len(mat) - 1
# 		o = n
# 		p = m
# 		curr_val = mat[o][p]
# 		loop len(mat) times
# 			next_val = mat[p][len(mat) - 1 - o]
# 			mat[p][len(mat) - 1 -o] = curr_val
# 			curr_val = next_val
# 			temp = o
# 			o = p
# 			p = len(mat) - 1 - o

# 		n += 1
# 	t += 1
# 	n = t, m = t


# curr_pos = [0,0]
# new_pos = [curr_pos[1], (n -1) - curr_pos[0]]

# # 5 X 5 matrix
# [0, 0]
# [0, 4]
# [4, 4]
# [4, 0]
# [0, 0]

# [1, 0]
# [0, 3]
# [3, 4]
# [4, 1]
# [1, 0]

# [2, 0]
# [0, 2]
# [2, 4]
# [4, 2]
# [2, 0]

# [3, 0]
# [0, 1]
# [1, 4]
# [4, 3]
# [3, 0]

# [1, 1]
# [1, 3]
# [3, 3]
# [3, 1]
# [1, 1]


# [2, 1]
# [1, 2]
# [2, 3]
# [3, 2]
# [2, 1]

# [2, 2]
# [2, 2]

# # 4 X 4 matrix
# [0, 0]
# [0, 3]
# [3, 3]
# [3, 0]
# [0, 0]

# [1, 0]
# [0, 2]
# [2, 3]
# [3, 1]
# [1, 0]

# [2, 0]
# [0, 1]
# [1, 3]
# [3, 2]
# [2, 0]

# [1, 1]
# [1, 2]
# [2, 2]
# [2, 1]
# [1, 1]
