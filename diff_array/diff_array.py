with open('error.txt') as file:
    error_lines = [line.rstrip() for line in file]
    error_set = set(error_lines)
    print(len(error_set))

with open('total.txt') as file:
    total_lines = [line.rstrip() for line in file]
    total_set = set(total_lines)
    print(len(total_set))

print(len(total_set - error_set))

file_path="./diff.txt"
str_list=list(total_set - error_set)
f=open(file_path, "w")
str_list = [line+'\n' for line in str_list]#在list中加入换行符
f.writelines(str_list) 
