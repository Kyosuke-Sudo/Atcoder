

class ABC326():
    def A(self):
        x, y = map(int, input().split())
        if x-3<=y<=x+2:
            print("Yes")
        else:
            print("No")

    def B(self) -> None:
        n = input()
        while True:
            n = str(n)
            n_1 = int(n[0])
            n_2 = int(n[1])
            n_3 = int(n[2])
            if n_1*n_2==n_3:
                print(n)
                return None
            n = int(n)
            n += 1

    def C(self) -> None:
        from collections import Counter
        n, m = map(int, input().split())
        list_A = sorted(list(map(int, input().split())))
        counter = Counter(list_A)
        answer = 0
        for i in counter.keys():
            tmp = 0
            for j in list_A:
                if i <= j < i+m:
                    tmp += 1
            answer = max(answer, tmp)
        #print(list_A)
        #print(counter.elements)
        #print(counter.keys())
        print(answer)
        return None
    
    def C2(self) -> None:
        from collections import Counter
        n, m = map(int, input().split())
        list_A = sorted(list(map(int, input().split())))
        list_B = []
        counter = Counter(list_A)
        for i in range(len(list_A)-1):
            list_B.append(list_A[i+1]-list_A[i])
        #print(list_A)
        #print(list_B)
        answer = 0
        for i in range(n):
            for interval in list_B:
                _ = m
                tmp = 0
                while _ > 0:
                    _ -= interval
                    tmp += 1
            answer = max(answer, tmp)
            print(answer)
        #for start in range(len(list_B)):
        #    _ = m
        #    tmp = 0
        #    while _ > 0:
        #        for i in list_B:
        #            _ -= i
        #            tmp += 1
        #    answer = max(answer, tmp)
        print(answer)
        return None
    
    def C3(self) -> None:
        """
        a[right]：右端のプレゼントの座標
        a[left]：左端のプレゼントの座標
        left：左端のプレゼントのインデックスであり、これまで調べたプレゼントの個数
        right：右端のプレゼントのインデックスであり、区間内に含むプレゼントの数
        """
        n,m = map(int,input().split())
        a = list(map(int,input().split()))
        a.sort()
        #mの最大値よりも大きい値を追加
        #a.append(9000000000000)
        a.append(a[-1]+10**9)
        res = 0
        right = 0
        #プレゼントの数だけ繰り返す
        for left in range(n):
            #右端が左端＋mになるまで繰り返す
            #a[left]はスタート地点、そこから+mした座標までが指定できる範囲
            #その範囲内で、リストaの一番右端の座標を指定するためにrightを増やす
            while a[right] < a[left]+m:
                #print(a[right])
                #右端をインクリメント
                right += 1
            #right,leftはリストaのインデックスなので、right-leftが獲得できるプレゼントの個数になる。
            res = max(res, right-left)
        print(res)
    
    def D(self) -> None:

        return None

solve = ABC326()
#solve.A()
#solve.B()
#solve.C()
#solve.C2()
#solve.C3()
solve.D()

