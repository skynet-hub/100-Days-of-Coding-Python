with open("./file1.txt") as data1_file:
    list_file1 = data1_file.readlines()

with open("./file2.txt") as data2_file:
    list_file2 = data2_file.readlines()
   

results = [int(num) for num in list_file1 if num in list_file2]
print(results)