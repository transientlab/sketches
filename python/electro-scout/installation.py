import materials

class splitter():
    def __init__(self, node, branch):
        self.node = node
        self.branches.append(branch)
        self.notes = ''
    
    def __str__(self):
        return self.parent

class cable_line():
    def __init__(self, wire_count, wire_thickness, material=materials.copper):
        self.wires = wire_count
        self.wire_thickness = wire_thickness
        self.material = material
        self.splits = []
        self.notes = ''

    def __str__(self):
        return "{:>10s} :{:>2d}G{:<3}".format(self.material.name, self.wires, self.wire_thickness)

    def add_split(self, split):
         self.splits.append(split)

class switch():
     
	assert True