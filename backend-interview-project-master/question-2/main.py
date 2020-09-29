import typing


def main(tomato_grid: typing.List[typing.List[int]]):
    queue = []
    row = len(tomato_grid)
    col = len(tomato_grid[0])
    for i in range(row):
        for j in range(col):
            if tomato_grid[i][j] == -1:
                queue.append([i, j])
    time = 0
    while len(queue) > 0:
        n = len(queue)
        # print("n: ", n)
        if n > 0:
            time += 1
        for i in range(n):
            d = queue[0]
            x = d[0]
            y = d[1]
            queue.pop(0)
            if x - 1 >= 0 and tomato_grid[x - 1][y] == 1:
                tomato_grid[x - 1][y] = -1
                queue.append([x - 1, y])
            if x + 1 < row and tomato_grid[x + 1][y] == 1:
                tomato_grid[x + 1][y] = -1
                queue.append([x + 1, y])
            if y - 1 >= 0 and tomato_grid[x][y - 1] == 1:
                tomato_grid[x][y - 1] = -1
                queue.append([x, y - 1])
            if y + 1 < col and tomato_grid[x][y + 1] == 1:
                tomato_grid[x][y + 1] = -1
                queue.append([x, y + 1])

    # for i in range(row):
    #     for j in range(col):
    #         print(tomato_grid[i][j])
    #     print("\n")

    for i in range(row):
        for j in range(col):
            if tomato_grid[i][j] == 1:
                return -1
    return time - 1


if __name__ == "__main__":
    tomato_grid = [
        [-1, 1, 0, -1, 1],
        [1, 0, 1, -1, 1],
        [1, 0, 0, -1, 1],
    ]
    x = main(tomato_grid)
    assert (x == 2), "Tomatoes will be rotten in 2 dayn"

    tomato_grid = [
        [-1, 1, 0, -1, 1],
        [0, 0, 1, -1, 1],
        [1, 0, 0, -1, 1],
    ]
    assert (main(tomato_grid) == -1), "All tomatoes cannot be rotten"
