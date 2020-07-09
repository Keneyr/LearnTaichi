# -*- coding: utf-8 -*-

import taichi as ti
ti.init(arch = ti.gpu)

a = ti.var(dt = ti.f32, shape = (42,63)) # a tensor of 42x63 scalars
b = ti.Vector(3, dt = ti.f32, shape = 4) # a tensor of 4x 3D vectors
c = ti.Matrix(2,2, dt = ti.f32, shape = (3,5)) #a tensor of 3x5 2x2 matrices

@ti.kernel
def foo():
    a[3,4] = 1
    print('a[3,4] =',a[3,4])
    
    b[2] = [6,7,8]
    print('b[0] =',b[0],'b[2]=',b[2])
    
    c[2,1][0,1] = 1
    print('c[2,1]=',c[2,1])
foo()