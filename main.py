import cache
import bot


def main():

    bot.initialize()

    # initialize cache system
    c = cache.Cache()
    c.develop_cache()

    # initialize main memory list
    c.develop_memory()

    # prompt user with options for the cache
    user_answer = bot.ask()
    bot.input_threshold(user_answer, c)

    # collect data for cache job


if __name__=='__main__':
    main()
