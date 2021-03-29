"""
# 가장 큰 수

문제 설명
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
입출력 예
numbers	return
[6, 10, 2]	"6210"
[3, 30, 34, 5, 9]	"9534330"
"""


def solution(numbers):
    answer = ''

    check_num = 9

    while check_num >= 0:
        checked_idx_dict = {idx: number for idx, number in enumerate(numbers) if str(number)[0:1] == str(check_num)}

        if checked_idx_dict:
            if len(checked_idx_dict) == 1:
                k, v = checked_idx_dict.popitem()
                answer += str(v)
                numbers.pop(k)
            else:
                transformed_checked_idx_dict = {}
                max_value_length = len(str(max(list(checked_idx_dict.values()))))
                for k, v in checked_idx_dict.items():
                    if max_value_length - len(str(v)) != 0:
                        v = str(v) + str(check_num) * (max_value_length - len(str(v)))
                        transformed_checked_idx_dict[k] = int(v)
                    else:
                        transformed_checked_idx_dict[k] = v

                print(checked_idx_dict)
                print(transformed_checked_idx_dict)

                transformed_checked_idx_dict = sorted(transformed_checked_idx_dict.items(), key=(lambda x: x[1]),
                                                      reverse=True)

                for _idx, k_v in enumerate(transformed_checked_idx_dict):
                    answer += str(checked_idx_dict[k_v[0]])

        check_num -= 1

    if answer.startswith("0"):
        answer = "0"

    return answer


def solution2(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))


from functools import cmp_to_key


def solution3(numbers):
    numbers = list(map(lambda x: str(x), numbers))
    numbers = sorted(numbers, key=cmp_to_key(lambda a, b: -1 if a + b >= b + a else 1))
    answer = ''.join(numbers)

    return str(int(answer))



print(solution([40, 404]))
print(solution2([40, 404]))
print(solution3([40, 404]))

