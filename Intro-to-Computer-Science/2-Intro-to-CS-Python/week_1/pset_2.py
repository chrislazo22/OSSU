count = 0

for i in range(len(s)):
    if s[i:].startswith('bob'):
        count += 1
    else:
        count += 0
print(count)
