# Ch. 9 Examples

from pathlib import Path

# helloFile = open(Path.home() / 'hello.txt')

# helloContent = helloFile.read()
# print(helloContent)

sonnetFile = open(Path.home() / 'sonnet29.txt')

sonnetContent = sonnetFile.readlines()
print(sonnetContent)
