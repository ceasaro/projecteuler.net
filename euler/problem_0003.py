from math import sqrt
from core.EulerProblem import EulerProblem
import log

__author__ = 'cvw'

primes = []
prime_factor_number = 600851475143

def increment_prime(number):
    if number > 2:
        return number + 2
    else:
        return number + 1


def nextPrime():
    lastPrime = primes[-1]
    nextPrime = increment_prime(lastPrime)

    while not(checkNextPrime(nextPrime)):
        nextPrime = increment_prime(nextPrime)
        #    log.debug("next prime =%s"%nextPrime)
    primes.append(nextPrime)
    #    log.debug("primes =%s"%primes)
    return nextPrime

def checkNextPrime(nextPrime):
    for prime in primes:
        if nextPrime % prime == 0:
            return False
    return True

def isPrime(number):
#    log.debug("checking prime %s"%number)
    if number % 10 in (0,2,4,5,6,8):
        return False
    else:
        divider = 3
        while divider < int(sqrt(number)):
            if number % divider == 0:
                return False
            divider+=2
            if divider % 10 == 5:
                divider+=2
    return True

class EulerProblem_0003(EulerProblem):

    def SKIP_takes_to_long_solution_1(self):
        """
        The prime factors of 13195 are 5, 7, 13 and 29.
        What is the largest prime factor of the number 600851475143 ?

        http://projecteuler.net/problem=3
        """

        answer = 0
        prime = 2
        primes.append(prime)

        while prime*2<prime_factor_number:
    #        log.debug("checking prime %s"%prime)
            if prime_factor_number % prime == 0:
                answer = prime
            prime = nextPrime()
        print(answer)

    def solution_2(self):
        """
        The prime factors of 13195 are 5, 7, 13 and 29.
        What is the largest prime factor of the number 600851475143 ?

        http://projecteuler.net/problem=3
        """

        number = int(sqrt(prime_factor_number))
        while not(number == 2):
            if isPrime(number) and prime_factor_number%number==0:
                return number
            number -= 1
        return prime_factor_number


def main():
    euler = EulerProblem_0003()
    euler.run()

main()
