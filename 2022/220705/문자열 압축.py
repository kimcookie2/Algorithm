def solution(s):
    answer = len(s)
    length = len(s)
    
    # 몇개 단위로 나눌 것인지 결정
    for i in range(1, length + 1):
        tmp = ''
        count = 1
        result = ''
        
        # 문자열을 앞에서부터 i개 단위로 잘라서 비교
        for j in range(0, length, i):
            # 범위 체크
            if j + 2 * i <= length:
                # 다음에 올 문자열과 압축이 가능하다면
                if s[j : j + i] == s[j + i : j + 2*i]:
                    tmp = s[j : j + i]
                    count += 1
                # 다음에 올 문자열과 압축이 끝난다면 or 안된다면
                else:
                    if count == 1:
                        result += s[j : j + i]
                    else:
                        result += str(count) + tmp
                    
                    tmp = ''
                    count = 1
            # 범위를 벗어나면 result에 추가
            else:
                if count == 1:
                    result += s[j : j + i]
                else:
                    result += str(count) + tmp
                    
                tmp = ''
                count = 1

        # 더 짧은 압축 방법이 나올 때마다 갱신            
        if len(result) < answer:
            answer = len(result)
                    
    return answer