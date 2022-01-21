def blankey(s):
	if s=="":
		return False
	elif s[0] == " ":
		return True
	else:
		return blankey(s[1:])

print(blankey("yarn barn"))








