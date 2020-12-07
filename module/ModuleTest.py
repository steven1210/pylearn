# 1，包的几种导入方式
# 1.1，import 模块
# import ModuleOne
# 调用模块中的函数:模块名.函数名
# ModuleOne.sumData(1, 2)

# 1.2，from 包 import 模块
# from module import ModuleOne
# 调用模块中的函数:模块名.函数名
# ModuleOne.sumData(2, 3)

# 1.3, from 包.模块 import 函数名
# from module.ModuleOne import sumData
# 调用模块中的函数:函数名
# sumData(3, 4)

# 1.4，from 模块 import 函数
# from ModuleOne import sumData
# 调用模块中的函数:函数名
# sumData(4, 5)

# 这种不常用，也不建议用，直接用第一种方式即可
# from 模块 import *
# from ModuleOne import *
# sumData(5, 6)
# chenData(5, 6)

# 可以同时导入多个模块，使用逗号隔开
# from module import ModuleOne, ModuleTwo
# ModuleOne.sumData(6, 7)
# ModuleTwo.subtract(6, 7)

# 模块名缩写：as
from module import ModuleOne as MO, ModuleTwo as MT
MO.sumData(7, 8)
MT.subtract(7, 8)
