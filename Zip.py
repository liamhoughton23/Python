def zip(one, two):
	e = (one[0],) + (two[0],)
	f = (one[1],) + (two[1],)
	return (e, f)



def zip2(one, two):
	count = 1
	if len(one) == 0:
		return (one, two)

	else:
		f = (one[0],) + (two[0],)
		if(len(one) > 1):
			while len(one) > count:
				e = (one[count],) + (two[count],)
				f = (f, e)
				count = count + 1
	return f

print(zip2((), ()))

print(zip2((1,2), ('a', 'b')))
print(zip2(('a', 'b', 'c'), (1, 2, 3)))

print(zip2((True, 0, []), (False, 1, ())))