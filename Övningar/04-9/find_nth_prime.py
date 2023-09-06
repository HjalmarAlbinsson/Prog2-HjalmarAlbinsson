def find_primes(a):
    prime_numbers = [2, 3]
    number = 3
    while len(prime_numbers) < a:
        number += 1
        prime = True
        for prime_number in prime_numbers:
            if number % prime_number == 0:
                prime = False
        if prime == True:
            prime_numbers.append(number)
    print(prime_numbers[-1])
find_primes(1000)