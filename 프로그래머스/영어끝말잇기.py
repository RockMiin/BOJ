def solution(n, words):
    vocab= []
    idx= 1
    circle= 1
    word_idx= 0
    while word_idx < len(words):
        
        if word_idx != 0 and words[word_idx][0] != words[word_idx-1][-1]:
            return [idx, circle]
        elif words[word_idx] not in vocab:
            vocab.append(words[word_idx])
        else: 
            return [idx, circle]
        
        if idx== n: 
            idx= 0
            circle+=1
        
        word_idx+=1
        idx+=1
    
    return [0, 0]
