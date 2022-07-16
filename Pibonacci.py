def 피보나치(n):
    a=1
    b=a+1
    while True:
        a=a+b
        b=b+a
        if b >= n :
            print("n보다 작은 정수 중 가장 큰 피보나치 수 =>", b-a)
            break
피보나치(int(input("범위 n => ")))