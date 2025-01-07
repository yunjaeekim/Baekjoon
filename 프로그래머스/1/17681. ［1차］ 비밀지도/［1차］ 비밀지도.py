def solution(n, arr1, arr2):
    def two(num, n):
        lst = ""
        cnt = 0
        tmp = 1
        while num > tmp:
            tmp *= 2
            cnt += 1
        tmp = 2**(n-1)
        for i in range(n):
            if num >= tmp:
                lst += "#"
                num = num % tmp
                tmp = tmp // 2
            else:
                lst += " "
                tmp = tmp // 2
        return lst
            
    def combined_string(lst1,lst2):
        lst = []
        answer = ''
        for s1,s2 in zip(lst1,lst2):
            for c1,c2 in zip(s1,s2):
                if c1 == "#" or c2 == "#":
                    answer += "#"
                else:
                    answer += " "
            lst.append(answer)
            answer = ''
        return lst
    answer = combined_string([two(num,n) for num in arr1],  [two(num,n) for num in arr2])
    
    return answer