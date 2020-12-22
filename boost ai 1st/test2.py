
global res
res= 0
def solution(arr):
    answer = []
    cnt = 1
    global res

    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            cnt += 1
        elif arr[i] != arr[i + 1]:
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)

    print(answer)
    if answer!=[1]:
        solution(answer)
        res+=1
    return res+1




# arr= [1, 1]
arr= [1, 2, 3]
# arr= [1, 1, 3, 3, 2, 2, 4, 5, 1, 1, 1, 3, 3, 3]
print(solution(arr))
