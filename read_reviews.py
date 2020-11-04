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

print(data[0])
print('------------------------------------------------')
print(data[1])

# count the average length of lines
sum_len = 0
for d in data:		# d is string(1000000)
	sum_len += len(d)
print('The average length of reviews is:', sum_len/len(data))

# filter
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('There are', len(new), 'lines less than 100 characters')
# check the first line in new.
print(new[0])
