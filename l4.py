

# list array


# arr = ["Ogabek",178.5, 3, False]

# arr[0] = "Vladimir"

# t = ("Ogabek",178.5, 3, False)

# t = list(t)

# t[0] = "Vladimir"

# t = tuple(t)


# print(type(arr))
# print(type(t))

# print(arr)
# print(t)


# a = 5
# b = 10

# a = b
# b = a



# t = a
# a = b
# b = t

# a,b = b, a
# a,b,c = intput(), 
# print(a,b)







# print()

# arr = ["Ogabek",178.5, 3, False]
# t = ("Ogabek",178.5, 3, False)
# s = {"Ogabek",178.5, 3, [2,1] ,[2,1]}

# print(s)





# a,b,*c =  [3,4,5,7,6,7,8,9]

# print(a)
# print(b)
# print(c)
# print(type(c))

# a = list(range(100,0,-10))

# print(a)


# a = (5,6,7,8)
# b = (7,)



# print(type(a))
# print(type(b))

# a = []
# b = tuple()
# c = {}






# a = {"name":"Ogabek", "height":178, 2:3.5, 3:True}


# print(a["height"])


# dict1 = {}

# print(type(dict1))

# name = 'Rick'

# my_dict = {name: 25, 2: 'python', 'name': 'Bob'}
# #Error

# print(my_dict[name])
# print(my_dict['Rick'])




s= "hello world this is python"

d = {}

# for i in s: 
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1


for i in s:
    d[i] = d.get(i, 0) + 1  
        
print(d)





