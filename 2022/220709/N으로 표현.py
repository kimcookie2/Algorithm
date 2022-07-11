def solution(N, number):
    answer = -1
    dp = []
    
    # i => N의 개수
    for i in range(1, 9):
        case = set()
        
        # 5, 55, 555 ...
        check_number = int(str(N) * i)
        case.add(check_number)
        
        for j in range(i - 1):
            # num1 => j 개를 이용해 만든 값
            for num1 in dp[j]:
                # num2 => i - j - 2 개를 이용해 만든 값
                for num2 in dp[i - j - 2]:
                    case.add(num1 - num2)
                    case.add(num1 + num2)
                    case.add(num1 * num2)
                    if num2 != 0:
                        case.add(num1 // num2)
                        
        if number in case:
            answer = i
            break
            
        dp.append(case)
    
    return answer