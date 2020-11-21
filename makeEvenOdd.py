with open("even_odd.py", "w+") as F:

    F.write("def even_odd(n):\n")
    F.write("\t if (n == 0): return True\n")
    return_val = False

    for n in range(1, 100):

        line = "\t elif (n == {n}): return {return_val}\n".format(
            n=n, return_val=return_val)
        F.write(line)
        return_val = not return_val
