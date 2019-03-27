import cache
import bot


def main():
    bot.initialize()

    # initialize cache system
    c = cache.Cache()
    print(c)


if __name__=='__main__':
    main()
