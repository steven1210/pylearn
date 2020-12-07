# 打印200以内的质数
# 质数的定义：质数（Prime number），bai又称素数，指在大于1的自然数中，除了1和该数自身外，
# 无法被其他自然数整除的数（也可定义为只有1与该数本身两个正因数的数）


for i in range(2, 101):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(f'{i}是质数')
