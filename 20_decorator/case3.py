
#! case


def name(func):
	def wrapper(**kwargs):
		print('The decorator is executed by yashraj')
		result=func(**kwargs)
		return result
	return wrapper
	
@name
def demo2():
	return 'I am getting executed'
	
print(demo2())

#! OUTPUT
# The decorator is executed by yashraj
# I am getting executed

@name
def demo(a):
	return 'Demo function has been executed'
	
print(demo(10))

#! OUTPUT
#! ERROR

@name
def demo3(**kwargs):
	return f'{kwargs} is a key-word arguument'

print(demo3(a=90))

#! OUTPUT
# The decorator is executed by yashraj
# {'a': 90} is a key-word arguument