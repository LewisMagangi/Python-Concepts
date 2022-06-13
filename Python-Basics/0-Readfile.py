# these two lines create a file "myfile.txt" with data "Learning Python"
with open("myfile.txt", "w") as f:
    f.write("Learning Python is fun")

# these two lines read data from myfile.txt
with open("myfile.txt") as f:
    print(f.read())
