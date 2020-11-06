# read reviews.txt
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 == 0:		# Print every 100000 lines as a progress bar
			print(len(data))
print('There is a total of', len(data), 'lines')		#1000000

# print(data[0])
# print('------------------------------------------------')
# print(data[1])

# count the average length of lines
sum_len = 0
for d in data:		# d is string(1000000)
	sum_len += len(d)
print('The average length of reviews is:', sum_len/len(data))

# filter1: filter all lines less than 100 characters
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('There are', len(new), 'lines less than 100 characters')
# check the first line in new.
print(new[0])

# filter2: filter lines containing "good" from the file
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('There are a total of', len(good), 'lines containing good')
print(good[0])

# A more comprehensive but simplier way is:
good = [d for d in data if 'good' in d]
print('There are a total of', len(good), 'lines containing good')
print(good[0])
# output = [(number - 1) for number in reference if number % 2 == 0]
#                |               |          |            |                                
#            equation        variable      list  conditional statement                    

# Similarly:
bad = []
for d in data:
	bad.append('bad' in d)		# print 1000000 True/False
# this is equals to:
bad = ['bad' in d for d in data]

#############################################
# Dictionary: how many 'word' appears
wc = {}		# word_count
for d in data:
	words = d.split()			# default as split('space')  
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1		# 增加新的key進入wc字典

for word in wc:					# Only print words appearred > 100 times
	if wc[word] > 100:
		print(word, wc[word])

print(len(wc))					# how many words there are in total
print(wc['Allen'])				# how many 'Allen' in total

# check the frequency of an input word
while True:
	word = input('Please enter a word that you want to check: ')
	if word == 'q':
		break
	if word in wc:
		print(word, 'appearred', wc[word], 'times')
	else:
		print('This word never appearred.')	# In case 'KeyError'

print('Thank you for using the checking function.')



