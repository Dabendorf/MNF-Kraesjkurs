def dec_to_base(n, b):
	output = ""
	while n != 0:
		next_digit = n%b
		n = n//b
		output = str(next_digit) + output
		#print(f"n: {n}, bin: {next_digit}, output: {output}")
		print(f"{n} & {next_digit} & {output}")
	return output
		
	
print(dec_to_base(22, 2))

def base_to_dec(n, b):
	sum = 0; idx = 0
	while n != 0:
		to_add = (b**idx * (n%b))
		sum += to_add
		n = n // 10
		idx += 1
		#print(f"Add: {to_add}, n: {n}, sum: {sum}")
		print(f"{to_add} & {n} & {sum}\\")
	return sum
		
print(base_to_dec(10110, 2))
		
