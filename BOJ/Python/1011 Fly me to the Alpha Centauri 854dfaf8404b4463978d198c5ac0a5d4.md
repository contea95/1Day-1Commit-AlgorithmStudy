# 1011.Fly me to the Alpha Centauri

## 문제

우현이는 어린 시절, 지구 외의 다른 행성에서도 인류들이 살아갈 수 있는 미래가 오리라 믿었다. 그리고 그가 지구라는 세상에 발을 내려 놓은 지 23년이 지난 지금, 세계 최연소 ASNA 우주 비행사가 되어 새로운 세계에 발을 내려 놓는 영광의 순간을 기다리고 있다.

그가 탑승하게 될 우주선은 Alpha Centauri라는 새로운 인류의 보금자리를 개척하기 위한 대규모 생활 유지 시스템을 탑재하고 있기 때문에, 그 크기와 질량이 엄청난 이유로 최신기술력을 총 동원하여 개발한 공간이동 장치를 탑재하였다. 하지만 이 공간이동 장치는 이동 거리를 급격하게 늘릴 경우 기계에 심각한 결함이 발생하는 단점이 있어서, 이전 작동시기에 k광년을 이동하였을 때는 k-1 , k 혹은 k+1 광년만을 다시 이동할 수 있다. 예를 들어, 이 장치를 처음 작동시킬 경우 -1 , 0 , 1 광년을 이론상 이동할 수 있으나 사실상 음수 혹은 0 거리만큼의 이동은 의미가 없으므로 1 광년을 이동할 수 있으며, 그 다음에는 0 , 1 , 2 광년을 이동할 수 있는 것이다. ( 여기서 다시 2광년을 이동한다면 다음 시기엔 1, 2, 3 광년을 이동할 수 있다. )

![https://www.acmicpc.net/upload/201003/rlaehdgur.JPG](https://www.acmicpc.net/upload/201003/rlaehdgur.JPG)

김우현은 공간이동 장치 작동시의 에너지 소모가 크다는 점을 잘 알고 있기 때문에 x지점에서 y지점을 향해 최소한의 작동 횟수로 이동하려 한다. 하지만 y지점에 도착해서도 공간 이동장치의 안전성을 위하여 y지점에 도착하기 바로 직전의 이동거리는 반드시 1광년으로 하려 한다.

김우현을 위해 x지점부터 정확히 y지점으로 이동하는데 필요한 공간 이동 장치 작동 횟수의 최솟값을 구하는 프로그램을 작성하라.

## 입력

입력의 첫 줄에는 테스트케이스의 개수 T가 주어진다. 각각의 테스트 케이스에 대해 현재 위치 x 와 목표 위치 y 가 정수로 주어지며, x는 항상 y보다 작은 값을 갖는다. (0 ≤ x < y < 231)

## 출력

각 테스트 케이스에 대해 x지점으로부터 y지점까지 정확히 도달하는데 필요한 최소한의 공간이동 장치 작동 횟수를 출력한다.

## 예제 입력 1

```
3
0 3
1 5
45 50

```

## 예제 출력 1

```
3
3
4
```

```python
import sys
t = int(sys.stdin.readline())
count = []
for i in range(t):
    x, y = map(int, sys.stdin.readline().split())
    distance = y - x
    list1 = [0]
    list2 = [0]
    add_count = 1
    odd_check = 0
    while 1:
        if odd_check == 0:
            list2.append(add_count)
            if sum(list1) < distance and distance <= sum(list2):
                break
            list1 = list2[:]
            odd_check = 1
        elif odd_check == 1:
            list2.append(add_count)
            if sum(list1) < distance and distance <= sum(list2):
                break
            list1 = list2[:]
            add_count += 1
            odd_check = 0
    count.append(len(list2)-1)

for j in count:
    print(j)
```

이 코드는 답은 맞지만 제한 시간에 못미치는 코드이다.

```python
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    distance = y - x
    num = 1
    while True:
        if num ** 2 <= distance < (num + 1) ** 2:
            break
        num += 1
    if num ** 2 == distance:
        print((num * 2) - 1)
    elif num ** 2 < distance <= num ** 2 + num:
        print(num * 2)
    else:
        print((num * 2) + 1)
```

먼저 이 그림을 보자.

[https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcOelTB%2FbtqxLV1KyPF%2FXrvDHVIy2GR9SfKmwVNlNk%2Fimg.png](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcOelTB%2FbtqxLV1KyPF%2FXrvDHVIy2GR9SfKmwVNlNk%2Fimg.png)

위 그림은 y와 x간의 거리 차이, 이동 횟수, 이동거리를 나타낸 것이다.

새로운 숫자가 나오는 때마다 끊기도 하였다. 규칙을 찾아보면 새로운 문자는 제곱수 다음에 새로운 숫자 1이 추가가 된다는 것이다. 거리 차이가 제곱수 차이일 때 이동 횟수는 [제곱수*2-1] 이다.

그 다음 (제곱수 + 1) 부터 (제곱수 + 루트 제곱수)까지 이동 횟수가 같고 이동 횟수는 [제곱수 * 2]로 구할 수 있다.

마지막으로 (제곱수 + 루트 제곱수 + 1)부터 (다음제곱수 - 1) 까지 이동 횟수가 같고 이동 횟수는 [제곱수 * 2 + 1]로 구할 수 있다.

먼저  루프를 돌려서 y와 x간의 거리 차이가 어느 위치에 있는지 조사한다.

num = 1부터 시작하여서 num^2 ≤ distance < (num+1)^2 으로 distance에 맞는 num을 구한다. 

그 다음 num을 조사하는데 num^2이 distance와 같으면 num * 2 - 1의 이동거리를 가진다.

num^2이 distance보다 작고, num^2 + num이 distance보다 크면 num * 2의 이동거리를 가진다.

그 이외의 경우(num^2 + num이 distance보다 작은 경우)는 num * 2 + 1의 이동거리를 가진다.