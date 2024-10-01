import pyvista
filepath = '/Users/kr315/Desktop/shared-vm/out_poisson/poisson.xdmf'
reader = pyvista.get_reader(filepath)
mesh = reader.read()
mesh.plot()