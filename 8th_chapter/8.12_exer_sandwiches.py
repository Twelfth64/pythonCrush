def sandwich_builder(*args):
    print("We made sandwich with following ingredients")
    for component in args:
        print(f"\t {component}")


sandwich_builder("sosages")
sandwich_builder("sosages", "mayonez")
sandwich_builder("sosages", "mayonez", "potatos")
