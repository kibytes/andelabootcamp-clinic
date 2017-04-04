def prime_gen(n):
    """generate prime numbers bt 1 to n."""

    primes = []

    if n == 0 or n == 1:
        return "zero or one cannot be prime."

    if n < 2:
        return "no primes for integers less than 2."

    if not type(n) == int:
        return "only integers allowed."

    for i in range(2, n + 1):
        if i > 1:
            for x in range(2, i):
                if (i % x) == 0:
                    break
            else:
                primes.append(i)
    return primes

#print prime_gen(10)
