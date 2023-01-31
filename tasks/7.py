s = 'In the hole in the ground there lived a hobbit'
s = s[:s.find('h')] + s[s.rfind('h') + 1:]
print(s)