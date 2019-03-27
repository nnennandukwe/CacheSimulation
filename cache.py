
class Cache:

    def __init__(self):
        
        self.main_memory = [] # list of short ints w/ 2048 max
        self.MEMORY_MAX = 2048 # max amount of main memory available
        self.block_size = 16
        self.num_of_slots = 16

        self.valid_flags = [0,1]
        self.tag = None
        self.cache = {} # develops into a full 16 * 16 structure


    @classmethod
    def display_cache(cache):
        # print out the actual cache structure
        print(cache)


    def develop_cache():
        # create initial empty cache
        # self.cache = {}
        cache = {}
        for i in range(0, 0xF+1):
            cache[hex(str(i))] = dict(
                valid=0,
                tag=0,
                data=[0 for i in range(0,0xF+1)],
            )

        display_cache(cache)
        return cache

