# read reviews.txt
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:		# Print every 10000 lines as a progress bar
			print(len(data))
print('There is a total of', len(data), 'lines')		#1000000

# print(data[0])
# print('------------------------------------------------')
# print(data[1])

# count the average length of lines
sum_len = 0
for d in data:
	sum_len += len(d)
print('The average length of reviews is:', sum_len/len(data))
