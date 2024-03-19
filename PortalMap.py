class PortalMap:
    def __init__(self):
        self.portals=[]

    def AddPortal(self, portal):
        self.portals.append(portal)

    def CreateTree(self):
        # Find min and max x,z coordinate values of all portals
        extrema = [
            [
                func([portal.Extremum(dimension, func) for portal in self.portals])
                for func in [min,max]
            ]
            for dimension in [1,3]
        ]
        # convert to widths and central values
        widths = [ dim_extrema[1]-dim_extrema[0] for dim_extrema in extrema ]
        central_vals = ( ex[0]+width//2 for ex, width in zip(extrema, widths) )
        # create tree, pad out width for expansion if needed
        self.tree = quads.QuadTree( central_vals, widths[0]*1.5. widths[1]*1.5 )
        # add all portals to tree
        for portal in self.portals:
            # for each portal, add all unique x,z coordinates (quadtree only supports points)
            #...
            self.tree.insert(quads.Point())


class Portal:
    def __init__(self):
        self.dimension
        self.bounds #((x1,y1,z1), (x2,y2,z2))
        self.name

    def Extremum(self, dim, func):
        return func(self.bounds[0][dim], self.bounds[1][dim])

    def Minimum(self, dim):
        return Extremum(self, dim, min)

    def Maximum(self, dim):
        return Extremum(self, dim, max)

