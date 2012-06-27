__author__ = 'cvw'
from core.EulerProblem import EulerProblem
import log


class EulerProblem_0001(EulerProblem):

    def solution_1(self):
        """
        If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
        Find the sum of all the multiples of 3 or 5 below 1000.

        http://projecteuler.net/problem=1
        """
        log.header("Euler Problem 1")
        sum = 0
        for i in range(1, 1000):
            message = "checking %s"%i
            if i % 3 == 0 or i % 5 == 0:
                sum += i
                message += ", yes"
            log.debug(message)
        return sum

def main():
    euler = EulerProblem_0001()
    euler.run()

main()
