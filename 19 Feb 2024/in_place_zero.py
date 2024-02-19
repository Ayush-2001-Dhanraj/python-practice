def set_zeros(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    print(f"{rows} x {cols}")

    tracker = []

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                tracker.append((i, j))

    print(tracker)

    for i , j  in tracker:
        for index in range(cols):
            matrix[i][index] = 0

        for index in range(rows):
            matrix[index][j] = 0

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
set_zeros(matrix)
print(matrix)