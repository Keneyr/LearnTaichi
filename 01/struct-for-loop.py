import taichi as ti
ti.init(arch = ti.gpu)
n = 320
pixels = ti.var(dt = ti.f32,shape = (n * 2, n))
@ti.kernel
def paint(t:ti.f32):
    for i,j in pixels: #Parallized over all pixels
        pixels[i,j] = i * 0.001 + j * 0.002 + t
        print (pixels[i,j])
paint(0.3)