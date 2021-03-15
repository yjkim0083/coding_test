# 완주하지 못한 선수

원문 URl : https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3

수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

## 제한 사항
- 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
- completion의 길이는 participant의 길이보다 1 작습니다.
- 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
- 참가자 중에는 동명이인이 있을 수 있습니다

## 입출력 예
|participant|completion|return|
|------|---|---|
|["leo", "kiki", "eden"]|["eden", "kiki"]|"leo"|
|["marina", "josipa", "nikola", "vinko", "filipa"]|["josipa", "filipa", "marina", "nikola"]|"vinko"|
|["mislav", "stanko", "mislav", "ana"]|["stanko", "ana", "mislav"]|"mislav"|

## 입출력 예 설명
예제 #1
- "leo"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

예제 #2
- "vinko"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

예제 #3
- "mislav"는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.

## Source
```python
def solution(participant, completion):

    completion_len = len(completion)

    completion_dict = {}

    for v in range(completion_len):
        participant_value = participant[v]
        completion_value = completion[v]

        if completion_dict.get(participant_value):
            del completion_dict[participant_value]
        else:
            completion_dict[participant_value] = 1

        if completion_dict.get(completion_value):
            del completion_dict[completion_value]
        else:
            completion_dict[completion_value] = 1

    participant_value = participant[completion_len]
    if completion_dict.get(participant_value):
        del completion_dict[participant_value]
    else:
        completion_dict[participant_value] = 1

    return list(completion_dict.keys())[0]
```

### description
- participant, completion list를 반복문을 통해 순회한다
- 각 리스트의 값을 dict의 Key값으로 mapping 한다
    - 만약 key값이 존재한다면 그 key를 삭제한다(대회참가 - 완료 되었다는 뜻)
- 위의 방법으로 모든 값을 순회 하면 dict에는 완료하지 못한 1명의 Key값만 남아있게 된다

### 결과
<img src="./../images/hash_1_1.png" width="50%">

### 다른 사람들의 풀이
hash 값을 사용해 누적합을 구하고 계속 차감해 나간뒤 최종 값(특정 사용자의 hash값)을 사용해 해를 구하는 방식이 신기했다

#### participant(출전선수 목록)
- hash 값은 unique 하기 때문에 hash값을 dict의 key로 사용한다
- hash 값을 "temp" 변수에 누적합을 구하여 저장한다

#### completion(완료선수 목록)
- 완료선수명에 대한 hash값을 구해서 "temp" 변수에서 계속 차감해 나간다
- 모두 차감하고 나면 "temp" 변수에는 어떠한 숫자값이 있을 것이며, 
  그 숫자값을 Key로 사용하는 value를 dict에서 찾으면 그 value가 완료하지 못한 선수이다.
```python
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
```
 