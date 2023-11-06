

class ABC():
    def A(self) -> None:
        s = input()
        for i in range(len(s)):
            if i%2==1 and s[i]=="1":
                print("No")
                exit()
        print("Yes")
        return None
    
    def B(self) -> None:
        n = int(input())
        dict_ = {}
        for i in range(n):
            s = input()
            count = 0
            for j in s:
                if j=="o":
                    count += 1
            dict_[i+1] = count

        dict_ = sorted(dict_.items(), key=lambda dict_: dict_[1], reverse=True)
        print(*[i[0] for i in dict_])
        return None

    def C(self) -> None:
        n, m = map(int, input().split())
        A = list(map(int, input().split()))
        A_dict = {}
        #リストを辞書
        for i in range(len(A)):
            A_dict[i] = A[i]
        #値を基準にして降順にソート
        A_list = sorted(A_dict.items(), key=lambda A_dict:A_dict[1], reverse=True)
        #print(A_dict)
        #print(A_list)
        #各参加者の得点を求める
        points_dict = {}
        for i in range(n):
            S = list(input())
            #i番目の参加者の得点
            point = 0
            for key in range(len(S)):
                if S[key] == "o":
                    #point += A_list[key]
                    point += A_dict[key]
            points_dict[i] = point
        #print(points_dict)
        #何問正解すれば良いかを計算する。    
                    
            #for j in A:
                
        return None

    def D(self) -> None:
        return None


solve = ABC()
#solve.A()
#solve.B()
solve.C()
#solve.D()
