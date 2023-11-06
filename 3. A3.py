dict1 = { "k2": [5, 18, 16, 18, 18], 

"k1": [17, 18, 5, 17, 17, 16], 

"k3": [17, 18, 16, 5, 9] 

}

''' part 1'''

x=list(dict1.keys())
'''print(x)
a=sorted(x)
print(a)
sorted(dict1)'''
dict2=dict(sorted(dict1.items()))
print(dict2)

'''part 2'''

avg = []
for lst in dict1.values():
    avg2 = sum(lst) / len(lst)
    avg.append(avg2)
avg.sort()
size = len(avg)
if(size%2==0):
    median = (avg[size//2] + avg[size//2 - 1])/2
else:
    median = avg[size//2]

print("Output of 2: Median of {} is {:0.2f}".format(avg, median))

'''part 3'''
dict3 = dict()
max = 0
max_value = []
for key, value in dict1.items():
    dict3[key] = len(set(value))
    if (len(set(value))>max):
        max = len(set(value))
        max_value = []
        max_value.append(key)
    elif len(set(value))==max:
        max_value.append(key)

print("Output of 3: Here,",max_value," has the most distinct values i.e.",max)

'''part 4'''
A= 16
for key in dict2:
    dict2[key] = [x for x in dict2[key] if x <= A]
print("\nOutput of 4:")
print(dict2)
