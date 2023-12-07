
# we imported isqrt from math inorder for us to use the Sieve of Eratosthenes algorithm
from math import isqrt


def primes_in_range(start_range: int, end_range: int) -> list[int]:
    # Validate the range
    if start_range <= 0:
        print("Please enter a positive number!")
        return []
    if end_range == start_range:
        print("Please enter a valid range.")
        return []
    if end_range <= 0:
        print("Please enter a valid range.")
        return []

    # Initialize a list to track whether each number is prime
    is_prime = [True] * end_range
    # 0 and 1 are not prime, so set their values to False
    is_prime[0] = False
    is_prime[1] = False

    # Sieve of Eratosthenes algorithm to mark non-prime numbers
    for i in range(2, isqrt(end_range) + 1):
        if is_prime[i]:
            # Mark multiples of the current prime number as non-prime
            for x in range(i * i, end_range, i):
                is_prime[x] = False

    # Return a list of prime numbers in the specified range
    return [i for i in range(start_range, end_range) if is_prime[i]]


if __name__ == '__main__':
    # Main program loop
    while True:
        # Get user input for the starting number
        start_input = int(input("Enter the starting number of the range (enter 0 to exit): "))

        # Check if the user wants to exit
        if start_input == 0:
            break

        # Get user input for the ending number
        end_input = int(input("Enter the ending number of the range: "))

        # Find prime numbers in the specified range
        primes_list = primes_in_range(start_input, end_input)

        # Display the results
        if primes_list:
            print(f"Prime numbers in the range {start_input} to {end_input}:")
            print(primes_list)
