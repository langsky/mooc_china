# NumPy库入门

## 数组的维度

- 维度数一组数据的组织形式。维度体现了数据之间的关系。

> 我觉得这里的数组的概念很像线性代数的矩阵。所以我可以讲NumPy当做是为矩阵或矩阵集合设计的库。

- 一维数组，类似线性代数里的向量，由对等关系的有序或无序数据构成。采用线性方式组织。

> 一维数组在Python中可以使用列表或集合表示。但是要注意列表集合与数组的差异。这种差异体现在数组中的数组要求数据类型一致。

- 二维数组和多维数组，概念上不用再说了，将它们想象成矩阵或分块矩阵即可。

- 高维数组，仅利用最基本的二元关系（键值对）展示数据间的复杂结构。

> 高维数组，可以用字典来表示，也可以用国际规定的三种结构表示，分别是JSON，XML，YAML。

## NumPy简述

- `ndarray`，用来表示一个多维数组。
- 广播功能函数。
- 整合C/C++/Fortran代码的工具。
- 计算和统计函数。
- `import numpy as np`，请使用约定方式引用。

## ndarray

- `ndarray`是NumPy中的一个基本类型。
- 一个`ndarray`对象由两个部分组成，一个是数据部分，一个是元数据部分（属性）。

### 属性

|属性|说明|
|---|---|
|ndim|表示数组的维度数量|
|shape|表示数组的形状，每个维度的量度|
|size|表示数组中的元素个数，这里的元素指的是基本元素|
|dtype|data type的缩写，即基本元素的数据类型，关于数据类型，后续有解释|
|itemsize|数组中基本元素所占字节数，这和数组的dtype有关|

### 元素类型

|类型|说明|
|---|---|
|bool|布尔值|
|intc|与C语言中的int类型保持一致，大小和计算机有关|
|intp|用于索引的整数，和C语言中的ssize_t保持一致|
|int8|字节长度整数|
|int16|两字节长度整数|
|int32|四字节长度整数|
|int64|八字节长度整数|
|uint8|字节长度整数，无符号|
|uint16|两字节长度整数，无符号|
|uint32|四字节长度整数，无符号|
|uint64|八字节长度整数，无符号|
|float16|16位半精度浮点数|
|float32|32位半精度浮点数|
|float64|64位半精度浮点数|
|complex64|复数类型，由两个32位浮点数组成|
|complex64128|复数类型，由两个64位浮点数组成|

## 数组的创建

创建数组由四种方法。

- 从Python列表，元组生成数组。
- 使用NumPy函数创建数组。
- 从字节流创建数组。
- 从文件中读取特定格式，创建数组。

### 从Python列表，元组生成数组

```python
np.array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0)

# object 就是列表或数组
# dtype 用来指定数组的数据类型
# 主要掌握这两个参数的使用即可
```

### 使用NumPy函数创建数组

```python
np.zeros(shape) # 创建0数组
np.ones(shape) # 创建全1数组
np.full(shape, val) # 创建全val数组

np.zeros(array) # 根据array的shape创建0数组
np.ones(array) # 根据array的shape创建全1数组
np.full(array, val) # 根据array的shape创建全val数组

np.arange([start,] stop[, step,], dtype=None) #遍历生成数组
np.linespace() #根据起始数据等间距填充数据形成数组
np.concatenate() #将多个数组合并为一个数组
```

## 维度变换

```python
a.reshape(shape) # 重新指定shape，返回一个新的数组
a.resize(shape) # 重新指定shape，在原数组上改变
a.swapaxes(ax1, ax2) # 将n个纬度中的两个纬度进行变换
a.flatten() # 进行数组降维，返回一个一维数组，不改变原数组
```

## 类型变换

```python
a.astype(type) #改变元素数据类型，返回一个新的数组，不改变原数组
a.tolist() # 数组转换为列表
```
