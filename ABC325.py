

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

solve = ABC326()
#solve.A()
#solve.B()
solve.B2()
        