
class ABC324():
    def A(self) -> None:
        n = int(input())
        A = list(map(int, input().split()))
        _ = A[0]
        for i in A:
            if _!= i:
                print("No")
                exit()
        print("Yes")
        return None
    
    def B(self) -> None:
        n = int(input())
        #3で割り切れる限り割り続ける
        while n%3 == 0:
            n //= 3
        #2で割り切れる限り割り続ける            
        while n%2 == 0:
            n //= 2
        #最後の計算時の商が1なら割り切れたことになるのでYesを返す
        if n==1:
            print("Yes")
        else:
            print("No")
        return None

    def C(self) -> None:
        #tの方が長い文字列である必要がある
        def check(shoter, longer) -> bool:
            #sの方が短い場合は入れ替える
            if len(shoter) > len(longer):
                return check(longer, shoter)
            #問題文よりSの文字列の長さがTの文字列の長さと2文字以上違うことがあるので、この場合はFalseを返す
            if len(shoter) < len(longer) - 1:
                return False
            i,j,miss = 0,0,0
            #長さが短い方の文字列の長さだけ繰り返す
            while i < len(shoter):
                #文字が一致した場合は両方のインデックスを1つすすめる
                if shoter[i] == longer[j]:
                    i += 1
                    j += 1
                else:
                    miss += 1
                    #一致しない文字が2つめになったらFalseを返す
                    if miss > 1:
                        return False
                    #文字列の長さが同じ場合はiも1つすすめる
                    if len(shoter) == len(longer):
                        i += 1
                    #longerの方が1文字長かった場合はjのみ1つ進める。これでインデックスは一致する
                    j += 1
            return True

        n, t = input().split()
        answer = []
        for i in range(int(n)):
            s = input()
            if check(s,t):
                answer.append(i+1)
        print(len(answer))
        print(" ".join(map(str, answer)))
        return None


solve = ABC324()
#solve.A()
solve.B()
#solve.C()
