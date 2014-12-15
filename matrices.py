#!/usr/bin/python

# init for empty matrix
# mr = [[0 for i in xrange(len(m1))] for j in xrange(len(m1[0]))]


def matrix_check_equal_sizes(m1, m2):
	if len(m1) != len(m2):
		raise RuntimeError
	for i in range(len(m1)):
		if len(m1[i]) != len(m2[i]):
			raise RuntimeError

def get_empty_matrix(x, y, init_val = 0):
	return [[init_val for i in range(y)] for j in range(x)]

def matrix_add(m1, m2):
	matrix_check_equal_sizes(m1, m2)
	#mr = get_empty_matrix(len(m1), len(m1[0]))
	mr = []
	for i in range(len(m1)):
		mr.append([])
		for j in range(len(m1[i])):
			mr[i].append(m1[i][j] + m2[i][j])
			#mr[i][j] = m1[i][j] + m2[i][j]
	return mr

def matrix_is_diagonal(m):
	for i in range(len(m)):
		for j in range(len(m[i])):
			if i != j and m[i][j] != 0:
				return False
	return True

def matrix_transpose(m):
	mt = get_empty_matrix(len(m[0]), len(m))
	for i in range(len(m)):
		for j in range(len(m[i])):
			mt[j][i] = m[i][j]
	return mt

def matrix_2x2_multiply(m1, m2):
	matrix_check_equal_sizes(m1, m2)
	mr = get_empty_matrix(2, 2)
	mr[0][0] = m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]
	mr[0][1] = m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]
	mr[1][0] = m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]
	mr[0][0] = m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]
	return mr

def matrix_multiply(m1, m2):
	mr = get_empty_matrix(len(m1), len(m2[0]))
	for i in range(len(m1)):
		for j in range(len(m2[0])):
			for k in range(len(m1[0])):
				mr[i][j] += m1[i][k] * m2[k][j]
	return mr

def matrix_determinant(m):
	pass

def matrix_inverse(m):
	pass

ma1 = [[1,2,3],[4,5,6]]
ma2 = [[1,2,3],[4,5,6]]
mar = [[2,4,6],[8,10,12]]

assert(matrix_add(ma1, ma2) == mar)

md1 = [[1,0,0],[0,3,0],[0,0,0]]
md2 = [[1,0,0,0],[0,3,0,0],[0,0,0,0]]
md3 = [[1,0,0],[0,3,0],[0,0,0],[0,0,0]]
assert(matrix_is_diagonal(md1))
assert(matrix_is_diagonal(md2))
assert(matrix_is_diagonal(md3))
md1[0][1] = 1
assert(not matrix_is_diagonal(md1))
md2[0][3] = 1
assert(not matrix_is_diagonal(md2))
md3[3][0] = 1
assert(not matrix_is_diagonal(md3))
md3[3][0] = 0

assert(matrix_transpose(ma1) == [[1,4],[2,5],[3,6]])
assert(matrix_transpose(md3) == [[1,0,0,0],[0,3,0,0],[0,0,0,0]])

assert(matrix_2x2_multiply([[1,0],[0,1]], [[0,1],[1,0]]) == [[0,1],[1,0]])
assert(matrix_multiply([[1,0],[0,1]], [[0,1],[1,0]]) == [[0,1],[1,0]])
assert(matrix_multiply([[4,5,-5],[-1,-4,-2],[-3,1,5],[2,1,4]], [[-4,4,-1,3,-4],[-1,-5,-5,4,-5],[-1,-1,0,-1,1]]) == [[-16,-4,-29,37,-46],[10,18,21,-17,22],[6,-22,-2,-10,12],[-13,-1,-7,6,-9]])




