fruits = ['Apple', 'Orange', 'Pear']

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit Pie")
    else:    
        print(fruit + " Pie")

make_pie(8)        
    

