
docx=input()
word=input()
answer=0; i=0
while i<=(len(docx)-len(word)):
    if docx[i:i+len(word)]== word:
        answer+=1
        i+=len(word)
    else: i+=1
print(answer)
