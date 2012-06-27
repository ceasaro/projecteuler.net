from math import sqrt
from core.EulerProblem import EulerProblem
import log

__author__ = 'cvw'

primes = []
number = 13195

def nextPrime():
    lastPrime = primes[-1]
    nextPrime = lastPrime+1
    while not(checkNextPrime(nextPrime)):
        nextPrime += 1
        #    log.debug("next prime =%s"%nextPrime)
    primes.append(nextPrime)
    #    log.debug("primes =%s"%primes)
    return nextPrime

def checkNextPrime(nextPrime):
    for prime in primes:
        if nextPrime % prime == 0:
            return False
    return True

class EulerProblem_0003(EulerProblem):

    def solution_1(self):
        """
        The prime factors of 13195 are 5, 7, 13 and 29.
        What is the largest prime factor of the number 600851475143 ?

        http://projecteuler.net/problem=3
        """

        answer = 0
        prime = 2
        primes.append(prime)

        while prime*2<number:
    #        log.debug("checking prime %s"%prime)
            if number % prime == 0:
                answer = prime
            prime = nextPrime()
        print(answer)

    def solution_2(self):
        """
        The prime factors of 13195 are 5, 7, 13 and 29.
        What is the largest prime factor of the number 600851475143 ?

        http://projecteuler.net/problem=3
        """

        answer = 0
        prime = 2
        primes.append(prime)


        while prime*2<sqrt(number):
    #        log.debug("checking prime %s"%prime)
            if number % prime == 0:
                answer = prime
            prime = nextPrime()
        print(answer)


def main():
    euler = EulerProblem_0003()
    euler.run()

main()
