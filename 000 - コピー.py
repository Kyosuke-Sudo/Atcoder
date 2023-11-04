def DFS(row, column):
    #gridの範囲内か判定
    if 0<=row<h and 0<=column<w:
        if grid[row][column] == "#":
            # #を.に変える
            grid[row][column] = "."
            #上下左右斜めのセンサーを調べる
            DFS(row+1, column)
            DFS(row-1, column)
            DFS(row, column+1)
            DFS(row, column-1)
            DFS(row+1, column+1)
            DFS(row+1, column-1)
            DFS(row-1, column+1)
            DFS(row-1, column-1)
    return 1

#幅優先探索
def BFS(row, column) -> int:
    from collections import deque
    #キューに追加
    queue = deque()
    queue.append((row, column))
    #キューの各要素を調べる
    while queue:
        row, column = queue.popleft()
        #grid内の座標の場合に以降の処理を行う
        if 0<=row<h and 0<=column<w:
            #現在座標が#、つまりセンサーだった場合、上下左右斜めの各座標をキューに加える。
            #また、最後に現在座標を.に書き換えて、再訪問時の再加算を防ぐ。
            if grid[row][column] == "#":
                queue.append((row+1, column))
                queue.append((row-1, column))
                queue.append((row, column+1))
                queue.append((row, column-1))
                queue.append((row+1, column+1))
                queue.append((row+1, column-1))
                queue.append((row-1, column+1))
                queue.append((row-1, column-1))
                grid[row][column] = "."
    #上下左右斜めの分も全て探索後、1つのセンサーとみなすので1を返す
    return 1

h,w = map(int, input().split())
grid = []
for row in range(h):
    s = input()
    s = list(s)
    grid.append(s)

#print(grid)
number_of_sensors = 0
for row in range(h):
    for column in range(w):
        if grid[row][column] == "#":
            #number_of_sensors += DFS(row, column)
            number_of_sensors += BFS(row, column)

print(number_of_sensors)
