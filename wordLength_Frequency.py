
# =================================================================
# 단어의 글자 개수 : 해당 글자 개수를 가진 단어 수
# =================================================================

make_length_wordcount(frankenstein.txt)
# 내용 예시 : I am glad to meet you guys
# 출력
# 1 : 1
# 2 : 2
# 3 : 1
# 4 : 3

def make_length_wordcount(filename):
    f = open("./"+filename, "r")
    text = f.read()
    wordList = text.split()
    wordCount = dict()
    
    for word in wordList:
        value = wordCount.get(len(word))
        if value == None:
            wordCount[len(word)] = 1
        else:
            wordCount[len(word)] += 1
    
    sorted(wordCount.keys())
    print(wordCount)


# =================================================================
# 단어 : 단어 빈도수
# =================================================================

make_length_wordcount(frankenstein.txt)
# 내용 예시 : I am glad to meet you guys
# 출력
# I : 1
# am : 1
# glad : 1
# to : 1
  
def make_word_count(filename):
    f = open("./"+filename, "r")
    text = f.read()
    wordList = text.split()
    wordCount = dict()
    
    for word in wordList:
        new = word.lower()
        value = wordCount.get(new)
        if value == None:
            wordCount[new] = 1
        else:
            wordCount[new] += 1
    
    sorted(wordCount.keys())
    print(wordCount)   
    
    
# =================================================================
# 위 두 가지 함수 결과가 모두 포함된
# '기존파일명_analyzed_Yuna_Lee.txt' 파일 생성
# =================================================================      

analyze_text("frankenstein")
analyze_text("nasdaq")
analyze_text("raven")

def analyze_text(filename):
    
    f = open("./"+filename+".txt", "r")
    text = f.read()
    wordList = text.split()
    wordCount = dict()
    
    for word in wordList:
        value = wordCount.get(len(word))
        if value == None:
            wordCount[len(word)] = 1
        else:
            wordCount[len(word)] += 1
    
    f=open("./"+filename+"_analyzed_Yuna_Lee.txt",'w')
    
    for key, value in wordCount.items():
        data = "Words of length %d : %d\n" %(key, value)
        f.write(data)   
    
    wordCount = dict()
    
    for word in wordList:
        new = word.lower()
        value = wordCount.get(new)
        if value == None:
            wordCount[new] = 1
        else:
            wordCount[new] += 1
    
    for key, value in wordCount.items():
        data = "%s : %d\n" %(key, value)
        f.write(data)
        
    f.close()
    
