## 试题编号：

201412-2

## 试题名称：

Z字形扫描

## 时间限制：

2.0s

## 内存限制：

256.0MB

## 问题描述

在图像编码的算法中，需要将一个给定的方形矩阵进行Z字形扫描(Zigzag Scan)。给定一个n×n的矩阵，Z字形扫描的过程如下图所示：



## 输入格式

输入的第一行包含一个整数n，表示矩阵的大小。

输入的第二行到第n+1行每行包含n个正整数，由空格分隔，表示给定的矩阵。

## 输出格式

输出一行，包含n×n个整数，由空格分隔，表示输入的矩阵经过Z字形扫描后的结果。

## 样例输入

```
4

1 5 3 9

3 7 5 6

9 4 6 4

7 3 1 3
```

## 样例输出

```
1 5 3 9 7 3 9 5 4 7 3 6 6 4 1 3
```

## 评测用例规模与约定

1≤n≤500，矩阵元素为不超过1000的正整数。