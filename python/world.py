def coordinate(x, y, z, t):
    return (x, y, z, t)

class world_params():
    x = int
    y = int
    z = int
    t = int

    particle_types = ('virtual', 'tahion')

    ref_coord = coordinate(0, 0, 0, 0)

    def __repr__(self):
        world_info = ("\n{:<20}{:<20}".format("world info", "----------"))
        world_info += ("\n{:<20}{:<20}".format("dimensions", len(self.ref_coord)))
        return world_info
    
    def location(self, ref, particle):
        self.dist = []
        self.dist = [particle[i]-ref[i] for i in range(len(particle) if len(particle)==len(ref) else 0)]

world = world_params()

class particle():
    def __init__(self, x, y, z, t, type):
        if type in world.particle_types:
            self.type = type
        else:
            raise TypeError
        self.location = coordinate(x, y, z, t)

    def __repr__(self):
        return "\n{:>20} : {:<20}@{:>20}".format("particle", self.type, str(self.location))

tah = particle(1, 1, 1, 3, 'virtual')

class body():
    def __init__(self):
        assert True
    def __repr__(self):
        assert True

print(world)
print(tah)
