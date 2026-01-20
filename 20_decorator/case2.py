

def name(func):
	def wrapper(*args):
		print('The decorator is executed by yashraj')
		result=func()
		return result
	return wrapper
	
@name
def demo():
	return 'Demo function has been executed'
	
print(demo())

## OUTPUT
#! The decorator is executed by yashraj
#! Demo function has been executed

@name
def demo2(a):
	return f'{a} is a variable length arguument'
	
print(demo2(30))
	
##OUTPUT
#! The decorator is executed by yashraj
#! 30 is a variable length arguument

@name
def demo3():
	return f'{a} is a key-word arguument'

print(demo3(a=90))

##OUTPUT
#! ERROR

	