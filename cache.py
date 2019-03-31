
VALID = "valid"
TAG = "tag"
DATA = "data"

class Cache:

    def __init__(self):
        
        self.main_memory = [] # list of short ints w/ 2048 max
        self.MEMORY_MAX = 0x800 # max amount of main memory available (2048)
        self.valid_flags = [0, 1]
        self.cache = {} # develops into a full 16 * 16 structure


    def display_cache(self):
        # print(self.cache)
        # print out the actual cache structure
        print("SLOT    VALID  TAG    DATA")
        for slot, data in self.cache.items():
            print(
                "{}     {}      {}      {}".format(
                slot,
                data.get(VALID), data.get(TAG),
                ' '.join(map(hex, data.get(DATA)))
                )
            )
        return self.cache


    def develop_cache(self):
        # create initial empty cache
        for i in range(0x0, 0x10):
            self.cache[hex(i)] = dict(
                valid=0,
                tag=0x0,
                data=[0 for j in range(0x0, 0x10)],
            )
        return self.cache

    
    def develop_memory(self):
        for i in range(0x0, self.MEMORY_MAX+1):
            for j in range(0x0, 0x100):
                if len(self.main_memory) == self.MEMORY_MAX:
                    break
                else:
                    self.main_memory.append(j)
            if len(self.main_memory) == self.MEMORY_MAX:
                break

        return self.main_memory

    
    def get_cache_targets(self, address):
        # should return dictionary with values that will update the cache
        block_offset = address & 0x00F # zero out all but the last 4 bits
        first_address = address & 0xFF0 # get block's first address
        slot = (address & 0x0F0) >> 4
        tag = address >> 8

        targets = {
            'block_offset': block_offset,
            'first_address': self.main_memory[first_address],
            'last_address': self.main_memory[first_address+0xF],
            'tag': tag,
            'slot': slot,
        }

        return targets


    # bringing in data output from get_cache_targets method
    def is_hit(self, cache_targets):

        # true = hit
        # false = miss

        slot = cache_targets.get('slot') # from intended targets
        tag = cache_targets.get('tag')
        first_addr = cache_targets.get('first_address')
        last_addr = cache_targets.get('last_address')
        b_off = cache_targets.get('block_offset')

        cache = self.cache.get(hex(slot), None) # check for slot num in the cache
        if cache:
            # what is the current state in this part of the cache?
            initial_valid = cache.get(VALID)
            intiial_tag = cache.get(TAG)
            initial_data = cache.get(DATA)

            # if valid flag is ON
            if initial_valid == self.valid_flags[1]:
                # if tag is a MATCH
                if intiial_tag == tag:
                    return True
                else:
                # if tag is NOT a match, then overwrite all values
                    self.cache[hex(slot)][VALID] = self.valid_flags[1]
                    self.cache[hex(slot)][TAG] = tag
                    # and overwrite data list
                    self.cache[hex(slot)][DATA] = [
                        i for i in range(
                            first_addr,
                            last_addr+0x1
                        )
                    ]
                    return False

            # if valid flag is OFF
            else:
                # overwrite data
                self.cache[hex(slot)][TAG] = tag
                self.cache[hex(slot)][VALID] = self.valid_flags[1]
                self.cache[hex(slot)][DATA] = [
                    i for i in range(
                        first_addr,
                        last_addr+0x1
                    )
                ]
                return False

    def write_byte(self, op, address, data_to_write):
        # officially write into main memory with user's data
        self.main_memory[address] = data_to_write

        if self.is_hit(self.get_cache_targets(address)):
            print("{}      Value {} has been written to address {}. (CACHE HIT)".format(
                op, data_to_write, hex(address)[2:]
            ))
        else:
            print("{}      Value {} has been written to address {}. (CACHE MISS)".format(
                op, data_to_write, hex(address)[2:]
            ))


    def read_byte(self, op, address):
        if self.is_hit(self.get_cache_targets(address)):
            print("{}     At that byte there is the value {} (CACHE HIT)".format(
                op, hex(address)[2:]
            ))
        else:
            print("{}     At that byte there is the value {} (CACHE MISS)".format(
                op, hex(address)[2:]
            ))
