# Python program to count the frequency of words in a file. 

f = open("teest.txt","r")

words = f.read().split()
print(words)

count = 0
key = []
value = []

for word in words:
	if not word in key:
		key.append(word)
		value.append(1)
	else:
		x=key.index(word)
		value[x]+=1

print(dict(zip(key,value)))

# word_freq={}

# for word in words:
# 	if word in word_freq.keys():
# 		word_freq[word]+=1
# 	else:
# 		word_freq[word]=1

# print(word_freq)
