"""
公雞5元一隻，母雞3元一隻，小雞1元三隻，用100元買一百隻雞，問公雞、母雞、小雞各有多少隻？
"""
for x in range(21):
    for y in range(34):
        z = 100 - x - y
        if z % 3 == 0 and 5 * x + 3 * y + z // 3 == 100:
            print(x, y, z)

