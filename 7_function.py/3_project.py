

# ⁡⁢⁣⁣🎯 Step 1: What This Project Does
# This program:
# Takes marks for 3 subjects.
# Calculates total marks.
# Calculates percentage.
# Finds the grade based on percentage.
# Displays the result neatly.⁡



def get_mark():
    marks = []
    for i in range(3):
        mark = int(input(f'Enter your marks {i + 1} :'))
        marks.append(mark)
    return marks

def calculate(marks):
    return sum(marks)

def perstange_total(total):
    return total / 3

def grade(perstange):
    if(perstange >= 90):
        return 'A'
    elif(perstange >= 75):
        return 'B'
    elif(perstange >= 33 and perstange <= 74):
        return 'C'
    elif(perstange < 33):
        return 'fail 😕'
    
def main():
    print('student grade calculate')
    marks = get_mark()
    total = calculate(marks)
    perstang = perstange_total(total)
    grad = grade(perstang)

    print('------ result-----')
    print(f'your total marks is : {total}')
    print(f'your perstange is : {perstang:.2f}%')
    print(f'your grade is : {grad}')

main()