from sys import argv

def basket(prices, amount):
    """Find all sets of counts of items adding up to amount"""
    # Base case: one item left.
    if len(prices) == 1:
        if amount % prices[0] == 0:
            # return list with single solution
            return [[amount / prices[0]]]
        else:
            # not possible this way- empty list of solutions
            return []
            
    # not base case- build list of solutions from recursion
    solutions = []

    # Choose a number of the first item- from none to max we can afford
    price = prices[0]
    for count in range(amount / price + 1):
        for solution in basket(prices[1:], amount - count * price):
            solutions.append([count] + solution)

    return solutions


def get_fruits(input_file):
    fruits = []
    with open(input_file) as f:
        for line in f:
            fruit, price = line.split()
            fruits.append((int(price), fruit))
    fruits.sort(reverse=True)
    return fruits


if __name__ == "__main__":
    fruit_prices, fruit_names = zip(*get_fruits(argv[1]))
    print fruit_names
    print fruit_prices
    solutions = basket(fruit_prices, 500)
    for solution in solutions:
        print ", ".join("{} {}{}".format(count, name, "s" * (count > 1))
                        for name, count in zip(fruit_names, solution)
                        if count)
