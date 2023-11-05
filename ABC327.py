
class ABC():
    def A(self) -> None:
        return None
    
    def B(self) -> None:
        return None

    def C(self) -> None:
        #入力
        A = []
        for i in range(9):
            A.append(list(map(int, input().split())))

        #転置したA
        A_T = list(map(list, zip(*A)))

        #縦、横、3*3内に含まれる数字を記録するためのリスト
        #list_ = [0,1,2,3,4,5,6,7,8,9]

        #行
        for i in range(9):
            #縦、横、3*3内に含まれる数字を記録するためのリスト
            #都度初期化し、行内にあった数字は0に変える
            list_ = [0,1,2,3,4,5,6,7,8,9]
            row = A[i]
            #行に数字があれば、list_の同じ数字を0に変える
            for j in row:
                list_[j] = 0
            #list_の全要素が0ならOK
            for k in list_:
                if k != 0:
                    print("No")
                    exit()
        #列  
        for i in range(9):
            list_ = [0,1,2,3,4,5,6,7,8,9]
            column = A_T[i]
            for j in column:
                list_[j] = 0
            for k in list_:
                if k != 0:
                    print("No")
                    exit()        

        def check_grid(row_start, row_end, column_start) -> bool:
            print(column_start)
            A_grid = []
            for i in range(3):
                A_grid.append(A[i][row_start:row_end])
                list_ = [0,1,2,3,4,5,6,7,8,9]
                for i in A_grid:
                    list_[i[column_start]] = 0
                    list_[i[column_start+1]] = 0
                    list_[i[column_start+2]] = 0                
            for i in list_:
                if i != 0:
                    return False
        
        flag = True
        for row in range(0,7,3):
            for column in range(0,7,3):
                print(row, column)
                flag = check_grid(row, row+3, column)
        
        if flag:
            print("Yes")
        else:
            print("No")

    def D(self) -> None:
        from collections import deque

        def BFS(start, dist, check):
            #global dist, check
            q = deque()
            q.append(start)
            check[start] = True
            dist[start] = 0
            while q:
                now = q.popleft()
                for to in edge[now]:
                    if check[to]:
                        continue
                    check[to] = True
                    dist[to] = (dist[now]+1)%2
                    q.append(to)

        #入力
        n,m = map(int, input().split())
        #A = list(map(int, input().split()))
        #B = list(map(int, input().split()))
        A = list(map(lambda x:int(x)-1, input().split()))
        B = list(map(lambda x:int(x)-1, input().split()))

        #グラフ
        #G = [set() for i in range(n)]
        edge = [[] for i in range(n)]
        for i,j in zip(A,B):
            edge[i].append(j)
            edge[j].append(i)
        #print(edge)

        check = [False]*n
        INF = float("inf")
        dist = [INF]*n
        for i in range(n):
            if not check[i]:
                BFS(i, dist, check)
            
        for i,j in zip(A,B):
            if dist[i] == dist[j]:
                print("No")
                exit()
        
        print("Yes")



solve = ABC()
#solve.A()
#solve.B()
#solve.C()
#solve.D()
