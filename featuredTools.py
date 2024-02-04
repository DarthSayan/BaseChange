
def reverse_string(chain):
    reversed_chain = ""
    pointer = len(chain)
    while pointer > 0:
        reversed_chain = reversed_chain + chain[pointer-1]
        pointer -= 1
    else:
        return reversed_chain