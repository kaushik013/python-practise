
import random 

num = random.randint(1,10)


trie = 0

while True:
    a = int(input('guess the number : '))

    if(num == a):
        print(f'you are win your trie count is {trie}')
        trie += 1
        break
    elif(num > a):
        print(f'you are small near!')
        trie += 1
    elif(num < a):
        print('you are little hire!')
        trie += 1
    else:
        print('sorry you are wrong!')
        trie += 1
