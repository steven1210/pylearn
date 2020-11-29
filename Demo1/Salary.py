filepath1 = r'D:\pylearn\File\salary.txt'
filepath2 = r'D:\pylearn\File\salary2.txt'

with open(filepath1, 'r+') as salary_file:
    salary_file.seek(0)
    str_salary = salary_file.read()
    # print(str_salary)

str_salary_info = str_salary.split('\n')
# print(str_salary_info)
for info in str_salary_info:
    # print(info)
    str_info = info.split(';')
    # print(str_info)
    name = str_info[0].split(':')[1].strip()
    salary = str_info[1].split(':')[1].strip()
    # print(name, salary)
    tax = int(int(salary) * 0.1)
    income = int(int(salary) * 0.9)
    # print(tax, income)
    # print('name: {:10}   ;    salary:  {:6} ;  tax: {:6} ; income:  {:6}。'.format(name, salary, tax, income))
    out_print = 'name: {:10}   ;    salary:  {:6} ;  tax: {:6} ; income:  {:6}。\n'\
        .format(name, salary, tax, income)
    with open(filepath2, 'a+') as str_salary_info:
        str_salary_info.write(out_print)

with open(filepath2, ) as str_salary_info:
    str_salary_info.seek(0)
    print(str_salary_info.read())
