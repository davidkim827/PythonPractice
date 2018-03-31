import os
print(os.getcwd())
print (os.path.abspath('.\\Scripts'))


os.makedirs(".\pythontext")

helloFile = open('.\pythontext\hello.txt', 'w')
helloFile.write("bye")
helloFile.close()