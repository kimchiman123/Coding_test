import sys 

input = sys.stdin.readline

code = input().strip()
result = '#'

red = int(code[1:3], 16)
green = int(code[3:5], 16)
blue = int(code[5:7], 16)
#print(red, green, blue)
#print(math.ceil((red + green + blue) / 3))
if (red + green + blue) % 3 == 0:
    gray = (red + green + blue) // 3
else:
    gray = round((red + green + blue) / 3)

for i in range(3):
    gray_hex = hex(gray)[2:].zfill(2)
    result += gray_hex
print(result)