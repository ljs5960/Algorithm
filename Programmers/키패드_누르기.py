'''
Programmers - 키패드 누르기(https://programmers.co.kr/learn/courses/30/lessons/67256)
'''

def solution(numbers, hand):
    answer = ''
    location = {
        '1': (0, 0), '2': (0, 1), '3': (0, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2),
        '7': (2, 0), '8': (2, 1), '9': (2, 2),
        '*': (3, 0), '0': (3, 1), '#': (3, 2),
    }
    l_hand = location['*']
    r_hand = location['#']
    
    for number in numbers:
        # 1, 4, 7 -> 왼손
        if number in [1, 4, 7]:
            answer += 'L'
            l_hand = location[str(number)]
            
        # 3, 6, 9 -> 오른손
        elif number in [3, 6, 9]:
            answer += 'R'
            r_hand = location[str(number)]

        # 2, 4, 8, 0 -> 거리계산
        else:
            l_hand_distance_x = abs(l_hand[0] - location[str(number)][0])
            l_hand_distance_y = abs(l_hand[1] - location[str(number)][1])
            l_hand_distance = l_hand_distance_x + l_hand_distance_y
            
            r_hand_distance_x = abs(r_hand[0] - location[str(number)][0])
            r_hand_distance_y = abs(r_hand[1] - location[str(number)][1])
            r_hand_distance = r_hand_distance_x + r_hand_distance_y
            
            # 왼손거리 > 오른손거리 -> 오른손
            if l_hand_distance > r_hand_distance:
                answer += 'R'
                r_hand = location[str(number)]
            
            # 왼손거리 < 오른손거리 -> 왼손
            elif l_hand_distance < r_hand_distance:
                answer += 'L'
                l_hand = location[str(number)]
            # 왼손거리 == 오른손거리
            else: 
                # hand == 오른손
                if hand == 'right':
                    answer += 'R'
                    r_hand = location[str(number)]
                #  hand == 왼손
                else:
                    answer += 'L'
                    l_hand = location[str(number)]
            
    return answer
