f = open('myfile.txt', 'a')
f.write("this is the last line\n")
f.close()

f = open('myfile.txt', 'r')
print(f.readlines())
f.close()
