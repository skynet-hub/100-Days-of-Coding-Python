#This program places X at a specifi position as provided by user

row1 = ["😆", "😆", "😆"]
row2 = ["😆", "😆", "😆"]
row3 = ["😆", "😆", "😆"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("where do you want to put your treasure? input a 2 digit number, both numbers between 1-3: \n")

Column_num = int(position[0]) - 1
row_num = int(position[1]) - 1

map[row_num][Column_num] = "X"

print(f"{row1}\n{row2}\n{row3}")


