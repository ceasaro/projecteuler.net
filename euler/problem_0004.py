from math import sqrt

__author__ = 'cvw'
from core.EulerProblem import EulerProblem
import log


class EulerProblem_0004(EulerProblem):

    def area_triangle(self, side_1, side_2, side_3):
        semi_perimeter = (side_1+side_2+side_3)/2
        area = sqrt(semi_perimeter*(semi_perimeter-side_1)*(semi_perimeter-side_2)*(semi_perimeter-side_3))
        return area

    def solution_1(self):
        """
        Consider the triangle with sides √5, √65 and √68. It can be shown that this triangle has area 9.
        S(n) is the sum of the areas of all triangles with sides √(1+b2), √(1+c2) and √(b2+c2) (for positive integers b and c ) that have an integral area not exceeding n.
        The example triangle has b=2 and c=8.
        S(106)=18018206.
        Find S(1010).

        http://projecteuler.net/problem=390
        """
        Side_1= sqrt(5)
        Side_2= sqrt(65)
        Side_3= sqrt(68)
        area = self.area_triangle(Side_1, Side_2, Side_3)

        answer = 0
        b = 2
        c = 8

        while 1 < 10^6:

            area = self.area_triangle(sqrt(1+b^2), sqrt(1+c^2), sqrt(b^2+c^2))
        return "NOT IMPLEMENTED YET"

def main():
    euler = EulerProblem_0004()
    euler.run()

main()
