

menu = {
    'pizza' : 40,
    'pasta' : 50,
    'burger' : 60,
    'salad' : 80,
    'coffee' : 100
}

for i in menu.items():
    print(i)

bill = 0
order = input('enter food : ')


if(order in menu):
    print(f'order of {order} has been added!')
    bill = bill + menu[order]
else:
    print('item not avaliable')

another = input('do you want to order anything yes or no : ')
a = another

if(a == 'yes'):
    for i in menu.items():
        print(i)
    another1 = input('erenter your order : ')
    if(another1 in menu):
        print(f'order of {another1} has been added!')
        bill += menu[another1]
    else:
        print(f'{another1}item not found!')
elif(a == 'no'):
    print('bill is',bill)
    
print('your bill is ',bill)
print('thank you 😊')


