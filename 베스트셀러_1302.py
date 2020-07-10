
N= int(input())
books=dict()
for i in range(N):
    book=input()
    if book not in books:
        books.setdefault(book, 1)
    elif book in books:
        books[book]+=1

max_value=max(books.values())
arr=[]

for i, j in books.items():
    if j==max_value:
        arr.append(i)
print(sorted(arr)[0])