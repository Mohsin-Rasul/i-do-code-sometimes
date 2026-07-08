def power(a, b, p):
    res = 1
    a = a % p
    
    while b > 0:
        if b % 2 != 0:
            res = (res * a) % p
        
        b = b >> 1
        a = (a * a) % p
    
    return res


def main():
    P = 111
    G = 200

    print("The value of P:", P)
    print("The value of G:", G)

    # --- Alice ---
    a = 4
    print("The PRIVATE KEY A FOR Alice:", a)

    x = power(G, a, P)
    print("Alice's Public Key (x):", x)

    # --- Bob ---
    b = 3
    print("The PRIVATE KEY b FOR Bob:", b)

    y = power(G, b, P)
    print("Bob's Public Key (y):", y)

    ka = power(y, a, P)
    kb = power(x, b, P)

    print("----------------------------------")
    print("Secret key for Alice is:", ka)
    print("Secret key for Bob is:", kb)


if __name__ == "__main__":
    main()
