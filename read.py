data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))

print('The file is finished reading, there are', len(data), 'data lists.')

sum_len = 0
for d in data:
   sum_len += len(d)

print('The average is', sum_len/len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print("There are", len(new), "data's length is less than 100")
print(new[0])

good = []
for d in data:
    if "good" in d:
        good.append(d)
print("There are", len(good), "datas mentioned good in the list")
print(good[0])
