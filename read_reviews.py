# read reviews.txt
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:		# Print every 10000 lines
			print(len(data))
print(len(data))		#1000000

print(data[0])
print('------------------------------------------------')
print(data[1])
