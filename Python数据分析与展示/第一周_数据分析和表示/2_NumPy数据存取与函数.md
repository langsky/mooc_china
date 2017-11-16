# NumPy数据存取与函数

## 数据的CSV文件存取

CSV适用于一维二维数据的存取。

### 读写文件的第一个函数

保存文件

```python
np.savetxt(fname, X, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# ')

# fname 文件的名字，可以是gz或bz2压缩文件名字
# X array_like 数组
# fmt 写入格式，主要关注的参数
# delimiter 字符的分隔符，CSV需要使用逗号

a = np.arange(100).reshape(5,20)

a
Out[16]:
array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
        17, 18, 19],
       [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
        37, 38, 39],
       [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
        57, 58, 59],
       [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76,
        77, 78, 79],
       [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96,
        97, 98, 99]])

np.savetxt('a.csv', a, fmt='%d', delimiter=',')
```

读取文件

```python
np.loadtxt(fname, dtype=<class 'float'>, comments='#', delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0)

# fname 文件的名字，可以是gz或bz2压缩文件名字
# dtype 读出数据元素的显示类型
# delimiter 文件中元素分隔符
# unpack 是否作为一维数组读取

np.loadtxt('a.csv', dtype=np.int, delimiter=',')
Out[21]:
array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
        17, 18, 19],
       [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
        37, 38, 39],
       [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
        57, 58, 59],
       [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76,
        77, 78, 79],
       [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96,
        97, 98, 99]])
```

## 多维数组的存取

### array.tofile

```python
a.tofile(fid, sep="", format="%s") # 将一个数组写入文件或二进制文件（默认）中。

# fid 文件名字
# sep 分隔符，为空串或默认，文件将呈现二进制格式
# format 元素写入文件的格式

a.tofile('a.dat',format='%d')
```

注意这个方法不指定纬度信息。

### np.fromfile

```python
fromfile(file, dtype=float, count=-1, sep='')

# file 文件名称
# dtype 元素类型
# count 元素数量，-1是全读
# sep 文件中的元素分隔符，空串表明文件是二进制文件
```

注意这个方法返回的数组将失去原数组的纬度信息。

### np.save np.load

```python
np.save(file, arr, allow_pickle=True, fix_imports=True)
# Save an array to a binary file in NumPy ``.npy`` format.
np.load(file, mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII')
# Load arrays or pickled objects from ``.npy``, ``.npz`` or pickled files.

np.save('a.npy',a)

np.load('a.npy')
Out[30]:
array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
        17, 18, 19],
       [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
        37, 38, 39],
       [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
        57, 58, 59],
       [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76,
        77, 78, 79],
       [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96,
        97, 98, 99]])
```

## NumPy随机数函数

```python
rand(d0,d1,...dn) # 根据d0...dn创建随机数数组，[0,1)，均匀分布
randn(d0,d1,...dn) # 正态分布
randint(low, high=None, size=None, dtype='l') # 根据size(也就是shape)生成随机数组[low, high) 均匀分布
seed(s) # 设置随机种子
```

### 数组改变的随机函数

```python
shuffle(a) #对a的第一轴进行随机排列，改变原数组
permutation(a) # 不改变原数组


choice(a, size=None, replace=True, p=None)
# Generates a random sample from a given 1-D array)

# a 原数组
# size 给定的size
# replace 是否允许重复选取元素
# p 为每个元素设置抽取的概率
```

### 分布函数

```python
uniform # 均匀分布
normal # 正态分布
poisson # 泊松分布
```


## NumPy统计函数
