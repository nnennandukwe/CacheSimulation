
VALID = "valid"
TAG = "tag"
DATA = "data"

class Cache:

    def __init__(self):
        
        self.main_memory = [] # list of short ints w/ 2048 max
        self.MEMORY_MAX = 0x800 # max amount of main memory available (2048)
        self.VALUE_MAX = 0xff # 255 max val per element in self.main_memory list
        self.block_size = 16 # 2**4 which makes 1 character in 8-bit hex
        self.num_of_slots = 16 # 2**4 which makes for 1 char in 8-bit hex

        self.valid_flags = [0, 1]
        self.cache = {} # develops into a full 16 * 16 structure


    def prettify(self, val):
        # method for return hex value from string input
        # that is found within main memory list
        # val == string data type
        return hex(self.main_memory[int(val, 16)])[2:]

    def display_cache(self):
        # print out the actual cache structure
        print("SLOT    VALID  TAG    DATA")
        for slot, data in self.cache.items():
            print(
                "{}     {}      {}      {}".format(
                slot,
                data.get(VALID), data.get(TAG),
                ' '.join(map(str, data.get(DATA)))
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
        block_offset = address & 0x0000000C # zero out all but the last 4 bits
        first_address = address & 0xCCCCCCC0 # get block's first address
        tag = address >> 8 # 
        slot = (address & 0x000000C0) >> 4

        return {
            'block_offset': block_offset,
            'first_address': first_address,
            'tag': tag,
            'slot': slot,
        }


    # bringing in data output from get_cache_targets method
    def is_hit(self, cache_targets):
        # could return either true or false
        # true = hit
        # false = miss

        slot = cache_targets.get('slot') # from intended targets
        tag = cache_targets.get('tag')
        first_addr = cache_targets.get('first_address')
        b_off = cache_targets.get('block_offset')

        cache = self.cache.get(slot, None)
        
        if cache:
            # what is the current state in this part of the cache?
            initial_valid = self.cache[cache][VALID]
            intiial_tag = self.cache[cache][TAG]
            initial_data = self.cache[cache][DATA]

            # if valid flag is ON
            if initial_valid == self.valid_flags[1]:
                # if tag is a MATCH
                if intiial_tag == tag:
                    return True
                else:
                # if tag is NOT a match, then overwrite all values
                    self.cache[cache][VALID] = self.valid_flags[1]
                    self.cache[cache][TAG] = tag
                    # and overwrite data list
                    self.cache[cache][DATA] = [
                        i for i in range(
                            first_addr,
                            first_addr+0xF
                        )
                    ]
                    return False

            # if valid flag is OFF
            else:
                # overwrite data
                self.cache[cache][TAG] = tag
                self.cache[cache][VALID] = self.valid_flags[1]
                self.cache[cache][DATA] = [
                    i for i in range(
                        first_addr,
                        first_addr+0xF
                    )
                ]
                return False
        else:
            print(cache)
            print("Slot number {} not available in cache..".format(slot))
            return False



    def write_byte(self):

        address = int(input("What address would you like to write to? "))

        if all([
            address.isalnum(),
            address <= self.MEMORY_MAX,
            address >= 0
        ]):
            data_to_write = int(input("What data would you like to write at that address? "), 16)

            if all([
                data_to_write.isalnum(),
                data_to_write <= self.VALUE_MAX,
                data_to_write >= 0,
            ]):
                # officially write into main memory with user's data
                self.main_memory[address] = data_to_write
                print(self.main_memory[address])
                if self.is_hit(self.get_cache_targets(self.main_memory[address])):
                    print("Value {} has been written to address {}. (CACHE HIT)".format(
                        data_to_write, address
                    ))
                else:
                    print("Value {} has been written to address {}. (CACHE MISS)".format(
                        data_to_write, address
                    ))


    def read_byte(self):
        address = int(input("What address would you like to read? "))

        if self.is_hit(self.get_cache_targets(address)):
            print("At that byte there is the value {} (CACHE HIT)".format(
                self.prettify(address)
            ))
        else:
            print("At that byte there is the value {} (CACHE MISS)".format(
                self.prettify(address)
            ))
