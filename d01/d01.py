with open("d01/d01_data.txt","r") as f:
    data = f.readlines()
    print(len(data))

num_0s = []
num_1s = []
for x in data:
    a,b = x.split()
    num_0s.append(int(a))
    num_1s.append(int(b))

print(len(num_0s),len(num_1s))
num_0s.sort()
num_1s.sort()

# part 1
total = 0
for x in range(len(num_0s)):
    total += abs(num_0s[x]-num_1s[x])

print("Total Distance: ",total)


# part 2
num_1_counts = {}
for num in num_1s:
    if num not in num_1_counts.keys():
        num_1_counts[num]=0
    num_1_counts[num] += 1

total_similarity = 0
for num in num_0s:
    if num not in num_1_counts.keys():
        sim =0
    else:
        sim = num_1_counts[num]
    total_similarity += num*sim

print("total similarity: ", total_similarity)