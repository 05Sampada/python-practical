for n in range(1, 51):

    #skip multiples of 3
    if n % 3 == 0:
        continue

    # Check prime number greater than 40
    if n > 40:
        prime = True
        for i in range(2, n):
            if n % i == 0:
                prime = False
                break

        if prime:
            print("Prime number found:", n)
            break

    # Placeholder for future feature
    if n == 10:
        pass

    print(n)

else:
    print("Loop completed without interruption")
