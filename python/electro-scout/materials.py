# conductor materials

class material():
    def __init__(self, name='', er=0, ec=0, ei=0, tr=0, tc=0, ti=0):
        self.name = name
        self.er = er
        self.ec = ec
        self.ei = ei
        self.tr = tr
        self.tc = tc
        self.ti = ti
        # print("{:>10}:{:<20}".format('material', self.name))

    def __str__(self):
        return self.name

    def get_data(self):
        out = "-----\n{:<20s}{:<20}\n \
                {:>20s}\n{:<10f}{:<10f}{:<10f}\n\
                {:<20s}\n{:<10f}{:<10f}{:<10f}\n"\
                .format('name', self.name,
                        'e_rci', self.er, self.ec, self.ei, \
                        't_rci', self.tr, self.tc, self.ti)
        return out



copper=material('copper', er=1.724e-8)
aluminium=material('aluminium', er=2.725e-8)
steel=material('steel', 1e10-7)

