from sys import argv


class Node(object):
    def __init__(self, key="", value=""):
        self.children = dict()
        if key:
            self[key] = value

    def __getitem__(self, key):
        child = self.children[key[0]]
        if type(child) is Node:
            return child[key[1:]]
        else:
            # return value and the part of the key that wasn't used
            return (child, key[1:])

    def __setitem__(self, key, value):
        if len(key) == 1:
            self.children[key] = value
        else:
            if key[0] in self.children:
                self.children[key[0]][key[1:]] = value
            else:
                self.children[key[0]] = Node(key[1:], value)

    def __str__(self):
        return "[{}]".format(", ".join("{}: {}".format(
            child, str(self.children[child])) for child in self.children))

class Interpreter(object):
    def __init__(self, string):
        self.tree = Node()
        pairs = string.split()
        for i in len(pairs / 2):
            key = pairs[i * 2 + 1]
            value = pairs[i * 2]
            self.tree[key] = value

    def interpret(self, string):
        result = ""
        while string:
            string, value = self.tree[string]
            result += value
        return result


def main():
    with open(argv[1]) as f:
        
