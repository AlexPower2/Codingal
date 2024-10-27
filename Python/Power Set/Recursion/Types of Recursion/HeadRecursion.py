def headrec(n, num):
    if n > num:
        return
    headrec(n + 1, num)
    print(n)

n = int(input("Enter n to print i to n:"))
headrec(1, n)