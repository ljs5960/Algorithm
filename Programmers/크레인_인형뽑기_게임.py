'''
Programmers - 크레인 인형뽑기 게임(https://programmers.co.kr/learn/courses/30/lessons/64061)
'''

def solution(board, moves):
    answer = 0
    dolls_arr = []
    
    for move in moves:
        for i in board:
            # 0(빈공간)이 아닐 경우 -> answer에 추가 후 0(빈공간)으로 변경
            if i[move-1] != 0:
                dolls_arr.append(i[move-1])
                i[move-1] = 0
                
                # 뽑은 인형의 array
                if len(dolls_arr) > 1:
                    # 마지막, 마지막+1 인형이 같을 경우
                    if dolls_arr[-1] == dolls_arr[-2]:
                        # 중복된 인형 두개 제거 후, answer + 2
                        dolls_arr.pop(-1)
                        dolls_arr.pop(-1)
                        answer += 2
                break
    return answer