password_l = []
for char in range(1, l+1):
    password_l += random.choice(letters)

for num in range(1, n+1):
    password_l += random.choice(numbers)

for sym in range(1, s+1):
    password_l += random.choice(symbols)

# print(password_l)
random.shuffle(password_l)
# print(password_l)
password = ""
for char in password_l:
    password += char
print(password)
