def return_val(tri, i ,j):
    if ((i>=0) and (j>=0 and j<=i)):
        return tri[i][j]
    else:
        return 0


def find_maximum_sum_dp(tri):
    for i in range (0, num_rows):
        for j in range(0, i+1):
            tri[i][j] += max(return_val(tri, i-1, j-1), return_val(tri, i-1, j))

# Using array to store the values for each row in the dataset.
tri = []
# Using a blank array to store the answers for sub solutions.
tri_sub_soln = []
# Reading values from the file.
fp = open('triangle.txt', 'r')
num_rows = 0
for line in fp:
    values = [int(item) for item in line.split()]
    tri.append(values)
    num_rows += 1
fp.close()
# print(tri)
# print(num_rows)
find_maximum_sum_dp(tri)
print(max(tri[num_rows -1]))