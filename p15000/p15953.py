# coding=utf-8

# https://www.acmicpc.net/problem/15953
# 카카오 코드 페스티벌에서 빠질 수 없는 것은 바로 상금이다. 
# 2017년에 개최된 제1회 코드 페스티벌에서는, 본선 진출자 100명 중 21명에게 아래와 같은 기준으로 상금을 부여하였다.

# 순위	상금	인원
# 1등	500만원	1명
# 2등	300만원	2명
# 3등	200만원	3명
# 4등	50만원	4명
# 5등	30만원	5명
# 6등	10만원	6명

# 2018년에 개최될 제2회 코드 페스티벌에서는 상금의 규모가 확대되어, 본선 진출자 64명 중 31명에게 아래와 같은 기준으로 상금을 부여할 예정이다.

# 순위	상금	인원
# 1등	512만원	1명
# 2등	256만원	2명
# 3등	128만원	4명
# 4등	64만원	8명
# 5등	32만원	16명

# 제이지는 자신이 코드 페스티벌에 출전하여 받을 수 있을 상금이 얼마인지 궁금해졌다. 
# 그는 자신이 두 번의 코드 페스티벌 본선 대회에서 얻을 수 있을 총 상금이 얼마인지 알아보기 위해, 
# 상상력을 발휘하여 아래와 같은 가정을 하였다.

# 제1회 코드 페스티벌 본선에 진출하여 a등(1 ≤ a ≤ 100)등을 하였다. 단, 진출하지 못했다면 a = 0으로 둔다.

# 제2회 코드 페스티벌 본선에 진출하여 b등(1 ≤ b ≤ 64)등을 할 것이다. 단, 진출하지 못했다면 b = 0으로 둔다.

# 제이지는 이러한 가정에 따라, 자신이 받을 수 있는 총 상금이 얼마인지를 알고 싶어한다.

# 입력
# 첫 번째 줄에 제이지가 상상력을 발휘하여 가정한 횟수 T(1 ≤ T ≤ 1,000)가 주어진다.

# 다음 T개 줄에는 한 줄에 하나씩 제이지가 해본 가정에 대한 정보가 주어진다. 
# 각 줄에는 두 개의 음이 아닌 정수 a(0 ≤ a ≤ 100)와 b(0 ≤ b ≤ 64)가 공백 하나를 사이로 두고 주어진다.

# 출력
# 각 가정이 성립할 때 제이지가 받을 상금을 원 단위의 정수로 한 줄에 하나씩 출력한다. 입력이 들어오는 순서대로 출력해야 한다.

from sys import stdin

al = [0]
al.extend([500])
al.extend([300]*2)
al.extend([200]*3)
al.extend([50]*4)
al.extend([30]*5)
al.extend([10]*6)

bl = [0]
bl.extend([512])
bl.extend([256]*2)
bl.extend([128]*4)
bl.extend([64]*8)
bl.extend([32]*16)

T = int(stdin.readline())
for _ in range(T):
    a, b = map(int, stdin.readline().rstrip().split())
    sp = 0
    if (a < len(al)):
        sp += al[a]

    if (b < len(bl)):
        sp += bl[b]

    print(sp*10000)


#pass #카카오_코드_페스티벌 #kakao