# coding=utf-8

'''디지털시계
https://www.acmicpc.net/problem/1942

시계 정수: 00:10:11 => 1011 , 22:01:44 => 220144
3의 배수: 각 자리수의 합이 3의 배수이면 참 (123 => 1+2+3 => 6, 6은 3의 배수 => 123은 3의 배수)
'''

from datetime import datetime, timedelta
import sys
input = sys.stdin.readline

# ss = ['00:59:58 01:01:24', '22:47:03 01:03:24', '00:00:09 00:03:37']

def timeInt(ti):
    bt, et = ti.split()
    
    bdt = datetime.strptime(bt, '%H:%M:%S')
    edt = datetime.strptime(et, '%H:%M:%S')
    if bdt > edt:
        edt += timedelta(days=1)
    
    mul3 = 0
    while True:
        if bdt > edt:
            break

        dts = bdt.strftime('%H%M%S')
        if int(dts) % 3 == 0:
            mul3 += 1

        bdt += timedelta(seconds=1)
        
    return(mul3)


for _ in range(3):
    print(timeInt(input()))


# pass -  timeInt : slow


# 수학
# 구현
# 문자열
# 시뮬레이션
# 파싱