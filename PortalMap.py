from rtree import index as rtree

rtree.Index().contains

def CheckDim(dimension)
    if dimension != "nether" and dimension != "overworld":
        raise ValueError(f"dimension has value {dimension}, not nether or overworld")
    return dimension

def IsNether(dimension):
    CheckDim(dimension)
    return (dimension == "nether")

def OtherDim(dimension):
    return "overworld" if IsNether(dimension) else "nether"

class PortalMap:
    # Portals stored in a list, corresponding index inserted into an R-tree for spatial indexing
    def __init__(self):
        # initialise empty portal list
        self.portals = []
        # initialise 3D RTrees (1 per dimension)
        rtree_properties = rtree.Property()
        rtree_properties.dimension = 3
        self.nether_tree=rtree.Index(properties=rtree_properties)
        self.overworld_tree=rtree.Index(properties=rtree_properties)

    def AddPortal(self, portal):
        # take index (length of list before insertion) and add portal to list
        i = len(self.portals)
        self.portals.append(portal)
        # add index to tree with bounds of the portal's cube
        x0, y0, z0 = portal.location
        x1, y1, z1 = ( loc + size for loc, size in zip(portal.location,portal.size) )
        self.Tree(portal.dimension).insert(i, (x0, y0, z0, x1, y1, z1))

    def Intersecting(self, p1, p2, dimension):
        # return a list of indices of portals intersecting the given 3D region(where p1 and p2 are two corners)
        return list(self.Tree(dimension).intersection((*p1,*p2)))
        #return [ self.portals[i] for i in self.Tree(dimension).intersection((*p1,*p2)) ]

    def Candidates(self, location, dimension):
        # return all portals that could be linked to from a given location
        link_range = 16 if IsNether(dimension) else 128
        x,_,z = location
        return self.Intersecting( (x-link_range, -64, z-link_range), (x+link_range, 320, z+link_range), dimension )

    def Tree(self, dimension):
        return self.nether_tree if IsNether(dimension) else self.overworld_tree
    
    def LinkTarget(self, portal):
        # Find target location:
        # TODO: get range of locations to cover whole portal range?
        target_dim = OtherDim(portal.dimension)
        target_loc = portal.Coordinates(target_dim)
        # Find portals in link range
        candidates = self.Candidates(target_loc, target_dim)
        if len(candidates) == 0: return None
        if len(candidates) == 1: return self.portals[candidates[0]]
        # Find closest portals, check they're in range
        

class Portal:
    def __init__(self, location, size, dimension, name=None):
        self.location = location #(x,y,z) (where x,y,z are the lowest values in the coordinate range, i.e. bottom left corner)
        self.size = size #(x_size,y_size,z_size)
        self.dimension = CheckDim(dimension)
        self.name = name

    def Coordinates(self, dimension):
        CheckDim(dimension)
        x,y,z = self.location
        if dimension == self.dimension: return (x,y,z)
        if dimension == "overworld": return (x*8, y, z*8)
        else: return (x//8, y, z//8)

# Example usage
portal_map = PortalMap()

# Create portals
portal1 = Portal((0, 0, 0), (1,2,0), 'nether', 'portal1')
portal2 = Portal((50, 0, 50), (2,2,2), 'overworld', 'portal2')

# Add portals to the map
portal_map.AddPortal(portal1)
portal_map.AddPortal(portal2)

print( *[p.name for p in portal_map.Candidates( (16, 10, 16), 'nether' )] )
