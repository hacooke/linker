from linkermc.dimension import Dimension

class Portal:
    def __init__(self, dimension, coords, extent, name=None):
        Dimension.validate(dimension, context="parameter passed to Portal")
        self.dimension = dimension
        self.coords = coords #(x,y,z) (where x,y,z are the lowest values in the coordinate range, i.e. bottom left corner)
        self.extent = extent #(x_size,y_size,z_size)
        self.name = name

    def coordinates_in(self, dimension):
        Dimension.validate(dimension, context="parameter passed to Portal")
        x,y,z = self.coords
        if dimension == self.dimension: return (x,y,z)
        if dimension == Dimension.overworld: return (x*8, y, z*8)
        else: return (x//8, y, z//8)

    def links_to(self, other):
        if self.dimension == other.dimension: return False
        target_coords = self.coordinates_in(other.dimension)
        link_range = 128 if other.dimension == Dimension.overworld else 16
        # overworld linking is now done on chunks rather than blocks
        # requires some added infrastructure to convert into chunks
        largest_xz_difference = max(
            abs(self.coords[0]-other.coords[0]),
            abs(self.coords[2]-other.coords[2])
        ) 
        if largest_xz_difference > link_range: return False
        return True

