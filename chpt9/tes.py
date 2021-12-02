x = '''
baconFile = open('bacon.txt', 'w')
baconFile.write('Hello, world!\n')
print(baconFile)
baconFile.close()

baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
print(baconFile)
baconFile.close()
'''

goodVersion = '''
baconFile = open('bacon.txt', 'w')
baconFile.write('Hello, world!\n')

baconFile.close()
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')

baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)
'''

baconFile = open('bacon.txt', 'w')
baconFile.write('Hello, world!\n')
baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
print(content)


baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
print(content)
