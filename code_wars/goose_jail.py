geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    bird_jail = []

    for bird in birds:
        if bird not in geese:
            bird_jail.append(bird)

    return bird_jail


