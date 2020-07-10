def islandPerimeter(grid):
    r = len(grid)
    c = len(grid[0])
    perimeter = 0

    for i in range(r):
        for j in range(c):
            if grid[i][j] == 0:continue
            perimeter += 4
            if i > 0:perimeter -= grid[i-1][j]
            if j > 0:perimeter -= grid[i][j-1]
            if i < r-1:perimeter -= grid[i+1][j]
            if j < c-1:perimeter -= grid[i][j+1]

    return perimeter

grid = [
    [0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]
    ]

print(islandPerimeter(grid))






