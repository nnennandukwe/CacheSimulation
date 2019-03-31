import cache
import bot

def main():

    bot.initialize()

    # initialize cache system
    c = cache.Cache()
    c.develop_cache()

    # initialize main memory
    c.develop_memory()

    operations = ["r", "w", "d"]
    # collect data for cache job
    msgs = bot.build_test()

    # print(msgs)
    for msg in list(msgs):
        # if it is read, write, or display cache
        if msg.isalpha() and msg.lower() in operations:
            # print(msg)
            # if read byte
            if msg == "R":
                c.read_byte(
                    op=msg,
                    address=int(msgs[1], 16)
                )
                msgs.popleft()
                msgs.popleft()
            # if write byte
            elif msg == "W":
                c.write_byte(
                    op=msg,
                    address=int(msgs[1], 16),
                    data_to_write=int(msgs[2], 16)
                )
                msgs.popleft()
                msgs.popleft()
                msgs.popleft()
            # if display cache
            elif msg == "D":
                c.display_cache()
                msgs.popleft()


if __name__=='__main__':
    main()
