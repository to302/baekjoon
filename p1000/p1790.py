# coding=utf-8

# https://www.acmicpc.net/problem/1790
# 1부터 N까지의 수를 이어서 쓰면 다음과 같이 새로운 하나의 수를 얻을 수 있다.

# 1234567891011121314151617181920212223...

# 이렇게 만들어진 새로운 수에서, 앞에서 k번째 자리 숫자가 어떤 숫자인지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N(1≤N≤100,000,000)과,  k(1≤k≤1,000,000,000)가 주어진다. N과 k 사이에는 공백이 하나 이상 있다.

# 출력
# 첫째 줄에 앞에서 k번째 자리 숫자를 출력한다. 수의 길이가 k보다 작아서 k번째 자리 숫자가 없는 경우는 -1을 출력한다.

import math

def digit_cnt(digit):
    """자리수 별로 해당 범위의 총 길이 반환 

    For example.
    digit=1 (1-9) : 9*1
    digit=2 (10-99) : 90*2
    digit=3 (100-999) : 900*3
    """
    return 9 * (10**(digit-1)) * (digit)


def n_length(n):
    """숫자가 들어오면 해당 숫자까지의 총 길이 반환
    """
    ndigit = len(str(n))
    nlen = (n - 10**(ndigit-1) + 1) * ndigit
    for i in range(ndigit-1, 0, -1):
        nlen += digit_cnt(i)
    return nlen


N, k = map(int, input().split())

if (n_length(N)<k):
    print(-1)
else:
    l = 1
    u = N
    while(u-l != 1):
        m = math.ceil((l + u)/2)
        if (n_length(m) == k):
            print(str(m)[-1])
            break
        elif (n_length(m) > k):
            u = m
        else:
            l = m
    else:
        m = math.ceil((l + u)/2)
        print(str(m)[k-n_length(l)-1])

# pass # little_hard