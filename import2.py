#infile = open('D:\\Self_Service_Work\\learn\\Python\\log\\foo.txt', 'r')
import csv
with open('D:\\Self_Service_Work\\learn\\Python\\log\\foo.txt', 'r') as infile:
    print("Name of the file: ", infile.name)
    data = infile.read()
    #print(data)
#print("-" * 50)
my_list = data.splitlines()
print(my_list)

for line in my_list:
    my_line_split = line.split()
    print(my_line_split)
#
# cnt = 1
# for line in my_list:
#     #print("Line {}: {}".format(cnt,line))
# #     #cnt += 1
# for line in infile:
#     line = line.strip()
#     print(line)

# print(mylist)

# for line in my_list:
#     my_line_split = line.split()
#     #print(my_line_split)
#     print(my_line_split[0])










