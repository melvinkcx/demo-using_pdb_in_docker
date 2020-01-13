if __name__ == "__main__":
    from operator import mul
    from functools import reduce

    numbers = [12, 21, 13, 9, 5]

    import pdb; pdb.set_trace()
    
    prod = reduce(mul, numbers)

    print(prod)
