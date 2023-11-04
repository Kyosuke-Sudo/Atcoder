

from zoneinfo import available_timezones


class ABC326():
    def A(self) -> None:
        s,t = input().split()
        print(s + " " + "san")
        return None
    
    def B(self) -> None:
        n = int(input())
        W = []
        X = []
        for i in range(n):
            w,x = map(int, input().split())
            W.append(w)
            X.append(x)
        answer = 0
        for i in range(n):
            tmp = W[i]
            for j in range(n):
                if i==j:
                    pass
                elif 0<=abs(X[i] - X[j])<=8:
                    tmp += W[j]
            answer = max(answer, tmp)
        print(answer)
        return None

    def B2(self) -> None:
        n = int(input())
        #時間帯ごとの参加可能な人数を保持するのリスト
        participant_by_time_zone = [0 for _ in range(24)]
        #各時間帯の参加可能な人数をリストの各要素の値として加えていく
        for i in range(0, n):
            w, x = map(int, input().split())
            participant_by_time_zone[x] += w

        available = 0
        #0時～23時までの各時間帯を全探索
        for hour in range(24):
            tmp_available = 0
            #各時間帯からさらに8時間差までの地域の人数を合計する
            for interval in range(9):
                #intervalが0~8まで変化するので、
                #17時以降は翌日の時間を含む必要があるが、%で剰余を取ることで24時を越えて時差8時間以内の地域を含めることができる
                tmp_available += participant_by_time_zone[(hour+interval) % 24]
            available = max(available, tmp_available)
        print(available)

    def C(self):
        def helper(row, column):
            #gridの範囲内か判定
            if 0<=row<h and 0<=column<w:
                if grid[row][column] == "#":
                    # #を.に変える
                    grid[row][column] = "."
                    #上下左右斜めのセンサーを調べる
                    helper(row+1, column)
                    helper(row-1, column)
                    helper(row, column+1)
                    helper(row, column-1)
                    helper(row+1, column+1)
                    helper(row+1, column-1)
                    helper(row-1, column+1)
                    helper(row-1, column-1)
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
                    number_of_sensors += helper(row, column)
        return None
    
        print(number_of_sensors)
    def C2(self):
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

    
solve = ABC326()
#solve.A()
#solve.B()
#solve.B2()
#solve.C()
solve.C2()
        