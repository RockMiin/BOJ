import re

def solution(files):
    
    file_list= []
    result= []
    
    for file in files:

        num= re.findall('[0-9]+', str(file))
        string= re.findall('[^0-9]+', str(file))
        
        file_list.append([string[0], num[0], file[len(string[0])+len(num[0]):]])

        file_list.sort(key = lambda x : (x[0].lower(), int(x[1])))
        
    for file in file_list:
        result.append(''.join(file))
    
    return result
  
# best
# import re

# def solution(files):
#     answer = []
#     files_split = [re.split(r'(\d+)', file) for file in files]
#     files_split.sort(key = lambda x : (x[0].lower(), int(x[1])))
    
#     for i in files_split:
#         answer.append(''.join(i)) 
    
#     return answer
  
# REF : https://github.com/naem1023/codingTest/blob/master/sort/pg-30-17686.py
