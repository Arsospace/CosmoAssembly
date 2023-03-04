import time

code = list()

a = int()
b = int()
c = int()
d = int()
B1 = bool()
B2 = bool()
B3 = bool()

z = 0
p = 0
n = 0

M1 = 0
M2 = 0
M3 = 0
M4 = 0
M5 = 0

while True:
	code_line = input()
	if code_line == "!RUN!":
		break
	code.append(code_line)
code.append("!RUN!")
print(code)
ln = 0
while True:
	ln += 1
	line = code[ln]
	if line == "!RUN!":
		break
############## SET ##############
	elif "SETA " in line:
		a = int(line[5:])
	elif "SETB " in line:
		b = int(line[5:])
	elif "SETC " in line:
		c = int(line[5:])
	elif "SETD " in line:
		d = int(line[5:])
############## ADD ##############	
	elif "ADD" in line:
		if line[3] == "A":
			a += int(line[5:])
			if a == 0:
				z = 1
				p = 0
				n = 0
			elif a > 0:
				z = 0
				p = 1
				n = 0
			else:
				z = 0
				p = 0
				n = 1
		elif line[3] == "B":
			b += int(line[5:])
			if b == 0:
				z = 1
				p = 0
				n = 0
			elif b > 0:
				z = 0
				p = 1
				n = 0
			else:
				z = 0
				p = 0
				n = 1
		elif line[3] == "C":
			c += int(line[5:])
			if c == 0:
				z = 1
				p = 0
				n = 0
			elif c > 0:
				z = 0
				p = 1
				n = 0
			else:
				z = 0
				p = 0
				n = 1
		elif line[3] == "D":
			d += int(line[5:])
			if d == 0:
				z = 1
				p = 0
				n = 0
			elif d > 0:
				z = 0
				p = 1
				n = 0
			else:
				z = 0
				p = 0
				n = 1
	elif "ADD.R " in line:
		if line[6] == "A":
			if line[8] == "A":
				a += a
			elif line[8] == "B":
				a += b
			elif line[8] == "C":
				a += c
			elif line[8] == "D":
				a += d
			elif a == 0:
				z = 1
				p = 0
				n = 0
			elif a>0:
				z = 0
				p = 1
				n = 0
			else:
				z = 0
				p = 0
				n = 1
		elif line[6] == "B":
			if line[8] == "A":
				b += a
			elif line[8] == "B":
				b += b
			elif line[8] == "C":
				b += c
			elif line[8] == "D":
				b += d
			elif b == 0:
				z = 1
				p = 0
				n = 0
			elif b>0:
				z = 0
				p = 1
				n = 0
			else:
				z = 0
				p = 0
				n = 1
		elif line[6] == "C":
			if line[8] == "A":
				c += a
			elif line[8] == "B":
				c += b
			elif line[8] == "C":
				c += c
			elif line[8] == "D":
				c += d
			elif c == 0:
				z = 1
				p = 0
				n = 0
			elif c>0:
				z = 0
				p = 1
				n = 0
			else:
				z = 0
				p = 0
				n = 1
		elif line[6] == "D":
			if line[8] == "A":
				d += a
			elif line[8] == "B":
				d += b
			elif line[8] == "C":
				d += c
			elif line[8] == "D":
				d += d
			elif d == 0:
				z = 1
				p = 0
				n = 0
			elif d>0:
				z = 0
				p = 1
				n = 0
			else:
				z = 0
				p = 0
				n = 1
############## SUB ##############
	elif "SUB" in line:
		if line[3] == "A":
			a -= int(line[5:])
			if a == 0:
				z = 1
				p = 0
				n = 0
			elif a > 0:
				z = 0
				p = 1
				n = 0
			else:
				z = 0
				p = 0
				n = 1
		elif line[3] == "B":
			b -= int(line[5:])
			if b == 0:
				z = 1
				p = 0
				n = 0
			elif b > 0:
				z = 0
				p = 1
				n = 0
			else:
				z = 0
				p = 0
				n = 1
		elif line[3] == "C":
			c -= int(line[5:])
			if c == 0:
				z = 1
				p = 0
				n = 0
			elif c > 0:
				z = 0
				p = 1
				n = 0
			else:
				z = 0
				p = 0
				n = 1
		elif line[3] == "D":
			d -= int(line[5:])
			if d == 0:
				z = 1
				p = 0
				n = 0
			elif d > 0:
				z = 0
				p = 1
				n = 0
			else:
				z = 0
				p = 0
				n = 1
	elif "SUB.R " in line:
		if line[6] == "A":
			if line[8] == "A":
				a -= a
			elif line[8] == "B":
				a -= b
			elif line[8] == "C":
				a -= c
			elif line[8] == "D":
				a -= d
			elif a == 0:
				z = 1
				p = 0
				n = 0
			elif a>0:
				z = 0
				p = 1
				n = 0
			else:
				z = 0
				p = 0
				n = 1
		elif line[6] == "B":
			if line[8] == "A":
				b -= a
			elif line[8] == "B":
				b -= b
			elif line[8] == "C":
				b -= c
			elif line[8] == "D":
				b -= d
			elif b == 0:
				z = 1
				p = 0
				n = 0
			elif b>0:
				z = 0
				p = 1
				n = 0
			else:
				z = 0
				p = 0
				n = 1
		elif line[6] == "C":
			if line[8] == "A":
				c -= a
			elif line[8] == "B":
				c -= b
			elif line[8] == "C":
				c -= c
			elif line[8] == "D":
				c -= d
			elif c == 0:
				z = 1
				p = 0
				n = 0
			elif c>0:
				z = 0
				p = 1
				n = 0
			else:
				z = 0
				p = 0
				n = 1
		elif line[6] == "D":
			if line[8] == "A":
				d -= a
			elif line[8] == "B":
				d -= b
			elif line[8] == "C":
				d -= c
			elif line[8] == "D":
				d -= d
			elif d == 0:
				z = 1
				p = 0
				n = 0
			elif d>0:
				z = 0
				p = 1
				n = 0
			else:
				z = 0
				p = 0
				n = 1
############## MUL ##############
	elif "MUL" in line:
		if line[3] == "A":
			a * int(line[5:])
			if a == 0:
				z = 1
				p = 0
				n = 0
			elif a > 0:
				z = 0
				p = 1
				n = 0
			else:
				z = 0
				p = 0
				n = 1
		elif line[3] == "B":
			b * int(line[5:])
			if b == 0:
				z = 1
				p = 0
				n = 0
			elif b > 0:
				z = 0
				p = 1
				n = 0
			else:
				z = 0
				p = 0
				n = 1
		elif line[3] == "C":
			c * int(line[5:])
			if c == 0:
				z = 1
				p = 0
				n = 0
			elif c > 0:
				z = 0
				p = 1
				n = 0
			else:
				z = 0
				p = 0
				n = 1
		elif line[3] == "D":
			d * int(line[5:])
			if d == 0:
				z = 1
				p = 0
				n = 0
			elif d > 0:
				z = 0
				p = 1
				n = 0
			else:
				z = 0
				p = 0
				n = 1
	elif "MUL.R " in line:
		if line[6] == "A":
			if line[8] == "A":
				a *= a
			elif line[8] == "B":
				a *= b
			elif line[8] == "C":
				a *= c
			elif line[8] == "D":
				a *= d
			elif a == 0:
				z = 1
				p = 0
				n = 0
			elif a>0:
				z = 0
				p = 1
				n = 0
			else:
				z = 0
				p = 0
				n = 1
		elif line[6] == "B":
			if line[8] == "A":
				b *= a
			elif line[8] == "B":
				b *= b
			elif line[8] == "C":
				b *= c
			elif line[8] == "D":
				b *= d
			elif b == 0:
				z = 1
				p = 0
				n = 0
			elif b>0:
				z = 0
				p = 1
				n = 0
			else:
				z = 0
				p = 0
				n = 1
		elif line[6] == "C":
			if line[8] == "A":
				c *= a
			elif line[8] == "B":
				c *= b
			elif line[8] == "C":
				c *= c
			elif line[8] == "D":
				c *= d
			elif c == 0:
				z = 1
				p = 0
				n = 0
			elif c>0:
				z = 0
				p = 1
				n = 0
			else:
				z = 0
				p = 0
				n = 1
		elif line[6] == "D":
			if line[8] == "A":
				d *= a
			elif line[8] == "B":
				d *= b
			elif line[8] == "C":
				d *= c
			elif line[8] == "D":
				d *= d
			elif d == 0:
				z = 1
				p = 0
				n = 0
			elif d>0:
				z = 0
				p = 1
				n = 0
			else:
				z = 0
				p = 0
				n = 1
##############  M  ##############
	elif ":" in line:
		if M1 == 0:
			M1 = ln
		elif M2 == 0:
			M2 = ln
		elif M3 == 0:
			M3 = ln
		elif M4 == 0:
			M4 = ln
		elif M5 == 0:
			M5 = ln	
	elif "GOTO " in line:
		for line_s in code:
			if ":" in line_s:
				if M1 == 0:
					M1 = ln
				elif M2 == 0:
					M2 = ln
				elif M3 == 0:
					M3 = ln
				elif M4 == 0:
					M4 = ln
				elif M5 == 0:
					M5 = ln	
		if line[5:] == "1":
			line = code[M1-1]
			ln = M1-1
		elif line[5:] == "2":
			line = code[M2-1]
			ln = M2-1
		elif line[5:] == "3":
			line = code[M3-1]
			ln = M3-1
		elif line[5:] == "4":
			line = code[M4-1]
			ln = M4-1
		elif line[5:] == "5":
			line = code[M5-1]
			ln = M5-1
	elif "EZ " in line:
		if z == 1:
			if int(line[3:]) == 1:
				ln = M1
			elif int(line[3:]) == 2:
				ln = M2
			elif int(line[3:]) == 3:
				ln = M3
			elif int(line[3:]) == 4:
				ln = M4
			elif int(line[3:]) == 5:
				ln = M5
	elif "POS " in line:
		if p == 1:
			if int(line[4:]) == 1:
				ln = M1
			elif int(line[4:]) == 2:
				ln = M2
			elif int(line[4:]) == 3:
				ln = M3
			elif int(line[4:]) == 4:
				ln = M4
			elif int(line[4:]) == 5:
				ln = M5
	elif "NEG " in line:
		if n == 1:
			if int(line[4:]) == 1:
				ln = M1
			elif int(line[4:]) == 2:
				ln = M2
			elif int(line[4:]) == 3:
				ln = M3
			elif int(line[4:]) == 4:
				ln = M4
			elif int(line[4:]) == 5:
				ln = M5
############## ECH ##############
	elif "ECHO " in line:
		if "A" in line:
			print(a)
		elif "B" in line:
			print(b) 
		elif "C" in line:
			print(c) 
		elif "D" in line:
			print(d) 
############## INP ##############
	elif "INP" in line:
		if line[3] == "A":
				a = int(input())
		elif line[3] == "B":
			b = int(input()) 
		elif line[3] == "C":
			c = int(input())
		elif line[3] == "D":
			d = int(input())
#################################
	else:
		print("ERROR:incorrect syntax")

input("THE PROGRAM IS OVER, PRESS ENTER TO CONTINUE...")