# LearnTaichi

learning Taichi on Games201...[论坛](https://forum.taichi.graphics/),里面也有拓展阅读，质量很高。

## 01

前半节课主要是大佬重新定义了什么叫做“牛逼”，“兴趣”，“娱乐”，“低调”，后半节主要是简单介绍了Taichi，以及如何安装Taichi。

本人笔记本win10，cpu-i7，gpu-amd，无cuda。之前装过Anaconda3，已经有了python3.6环境，所以直接开整。

具体安装过程写在了[我的知乎](https://zhuanlan.zhihu.com/p/157738735)

## 02

yapf，python代码格式化工具。

拉格朗日方法(视角)：随波逐流；欧拉方法(视角)：岿然不动。

拉格朗日：粒子；欧拉：网格。

弹簧质点模型可以用来模拟布料、头发等，其内部的数学原理：胡克定律+牛顿第二定律(容易理解)。

Forward Euler(前向欧拉)--explicit(显式)
Semi-implicit Euler(半隐式欧拉)--又叫做symplectic Euler(辛欧拉)--explicit(显式)
Backward Euler(后向欧拉)--implicit(隐式)

mass_spring_explicit.py就是用的symplectic Euler方法。

显式容易爆炸，容易实现，对于特别硬的材质不是很适合(调大py文件中的stiffness可以看出来)；

隐式不容易实现和求解(未来不仅依赖于过去，还依赖于未来)。

在弹簧模型的隐式方法，公式推导中，有一个一阶泰勒展开，关于泰勒展开的理解可以看该[回答](https://www.zhihu.com/question/25627482)

拉格朗日流体模拟：SPH方法，其核心观点就是使用粒子携带一系列的物理量，一个核函数W，来近似连续场。
可以把SPH理解成弹簧模型，某个粒子和其他粒子之间就是某种弹簧关系，只是遵循的物理规律不是胡克定律，而是SPH定义的物理量之间的关系。

Taichi给了PBF的Demo，PBF是PBD+SPH结合，用于实时计算的方法。有关SPH流体模拟比较权威的[学习网站](https://interactivecomputergraphics.github.io/SPH-Tutorial/)

时间步长(dt or delt_t)的限制从两个方面来考虑：
1、物体的刚性(过刚则爆炸)
2、速度(过快则爆炸)

SPH加速，考虑的数据结构是用一个voxel grid来加速neighborhod search，加速的学问很大，可阅读最新的论文。

taichi怎么输出mp4和gif，看[文档](https://github.com/taichi-dev/taichi)介绍。

助教同学些的关于流体的[cpp Demo](https://github.com/TroyZhai/CPP-Fluid-Particles)

耦合(本课程语境下)：刚体和流体的双向交互。

所谓强耦合：解线性系统，或者迭代的时候，把两个系统同时联立求解。

所谓弱耦合：先解流体，把流体作为边界条件解刚体，这种类似的。

SPH目前不仅仅做流体了，可以做刚体，雪之类的，它可以较好的模拟各种介质的耦合。

[openvdb](https://www.openvdb.org/)，开源工具，电影级别的工具。

## 03
