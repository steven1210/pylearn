for i in range(1, 10):
    for j in range(1, i+1):
        filepath = r'D:\pylearn\File\note.txt'  # 文件路径
        file = open(filepath, 'a+')  # 读取文件
        if i == j:  # 当i等于j时，换行
            file.write(f'{j} * {i} = {j*i}' + '\n')  # 写入数据
        else:
            file.write(f'{j} * {i} = {j*i}' + '\t')  # 写入数据
file.seek(0)  # 将光标移动到行首位置
print(file.read())  # 读取文件
file.close()  # 关闭文件
