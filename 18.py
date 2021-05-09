def alap(str, n):
    if (n >= 0):
        generalo(str, 0, n, 0, 0)
    else:
        return print("Nullánál kissebb számot adtál meg!")


def generalo(str, pos, n, open, close):
    if close == n:
        for i in str:
            print(i, end="")
        print()
        return
    else:
        if (open > close):
            str[pos] = ')'
            generalo(str, pos + 1, n, open, close + 1)
        if (open < n):
            str[pos] = '('
            generalo(str, pos + 1, n, open + 1, close)


n = int(input("Hány pár zárójelet használjunk? "))
str = [""] * 2 * n
alap(str, n)
