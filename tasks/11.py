s = 'In the hole in the ground there lived a hobbit'
s = s.replace('h', 'H', s.count('h') - 1)
s = s.replace('H', 'h', 1)
print(s)