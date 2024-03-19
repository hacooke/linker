import anvil
from glob import glob

def main():
    search_block = 'nether_portal'
    ow_regions = [ anvil.Region.from_file(f) for f in glob('/home/harry/.minecraft/fabric_1.18.1/saves/New World/region/*.mca') ]
    portal_chunks = [ chunk for region in ow_regions for chunk in filterChunks(region, search_block) ]
    print( [ (chunk.x,chunk.z) for chunk in portal_chunks ] )
    nether_portal_coords = [ coords for chunk in portal_chunks for coords in findBlocks(chunk, search_block) ]
    print( len(nether_portal_coords), nether_portal_coords )

def findBlocks(chunk, search_block):
    blocks = []
    # loop over all block coordinates in chunk
    coord_map = [ [x,y,z] for y in range(-64,320) for x in range(16) for z in range(16) ]
    for x, y, z in coord_map:
        block = chunk.get_block(x, y, z)
        if block.id != search_block: continue
        blocks.append( chunkToGlobalCoords(chunk, (x,y,z)) )
    return blocks

def filterChunks(region, search_block):
    confirmed = []
    # each region contains 32x32 chunks, loop over them here:
    chunk_map = [ [x,z] for x in range(32) for z in range(32) ]
    for x, z in chunk_map:
        try: chunk = region.get_chunk(x,z)
        except anvil.errors.ChunkNotFound: continue
        if chunkContainsBlock(chunk,search_block): confirmed.append(chunk)
    return confirmed

## Scan this chunk to see if it contains any nether portals
## (quick check, doesn't give coords)
def chunkContainsBlock(chunk, block_id):
    for subchunk_index in range(-4,20):
        # Can only get palette per subchunk, looping over them here
        for block in chunk.get_palette(subchunk_index):
            if block.id == block_id:
                return True
    return False

def chunkToGlobalCoords(chunk, coords):
    chunk_x, chunk_z = [ n*16 for n in [chunk.x, chunk.z] ]
    return ( chunk_x + coords[0], coords[1], chunk_z + coords[2] )

if __name__ == "__main__":
    main()
