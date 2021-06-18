data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))

print('The file is finished reading, there are', len(data), 'data lists.')

print(data[0])

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

#快寫法
good = [d for d in data if 'good' in d]
print(good)

bad = []
for d in data:
    bad.append('bad' in d)

#快寫法
bad = ['bad' in d for d in data]
print(bad)

#Words count.
wc = {} #word_count
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1 #wc[word] is a dictionary
        else:
            wc[word] = 1 #Add new "key" to a dictionary

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])
print(len(wc))
print(wc['Allen'])

while True:
    word = input('What do you want to look for? ')
    if word == 'q':
        break
    if word in wc:
        print(word, 'has showned:', wc[word], 'times')
    else:
        print('The word has not shown before')

print('Thanks for using')
















