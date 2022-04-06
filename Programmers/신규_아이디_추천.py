'''
Programmers - 신규 아이디 추천 (https://programmers.co.kr/learn/courses/30/lessons/72410#)
'''

import re

def solution(new_id):
    answer = ''
    
    # STEP1: 대문자 -> 소문자
    new_id = new_id.lower()
    
    # STEP2: 특수문자 제거
    new_id = re.sub('[~!@#$%^&*\(\)=+\[\{\]\}:?,\<\>/]', '', new_id)
        
    # STEP3: 연속 마침표 -> 1개
    new_id = re.sub('[.]+', '.', new_id)
    
    # STEP4: 맨 처음 마침표 제거
    if new_id[0] == '.':
        new_id = new_id[1:]
        
    # STEP5: 빈 문자열 -> 'a'
    if not new_id:
        new_id = 'a'
        
    # STEP6-1: 16자 이상 -> 15자 초과 문자 제거
    new_id = new_id[:15]
    # STEP6-2: 마지막 문자 . -> 제거
    new_id = new_id.rstrip('.')
    
    # STEP7: 2자 이하 -> 마지막 문자 반복
    while True:
        if len(new_id) <= 2:
            new_id += new_id[-1]
        else: break
        
    return new_id