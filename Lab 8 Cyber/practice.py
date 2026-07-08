def main():
    P = 111
    G = 200

    print("The value of P:", P)
    print("The value of G:", G)

    # --- Alice ---
    a = 4
    print("The PRIVATE KEY A FOR Alice:", a)

    x = pow(G, a, P)
    print("Alice's Public Key (x):", x)

    # --- Bob ---
    b = 3
    print("The PRIVATE KEY b FOR Bob:", b)

    y = pow(G, b, P)
    print("Bob's Public Key (y):", y)

    # Shared secret keys
    ka = pow(y, a, P)
    kb = pow(x, b, P)

    print("----------------------------------")
    print("Secret key for Alice is:", ka)
    print("Secret key for Bob is:", kb)


if __name__ == "__main__":
    main()
