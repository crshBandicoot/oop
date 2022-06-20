import unittest
from random import randrange
from Bezier import CubicBezierCurve


class BezierTest(unittest.TestCase):
    def test_LinearInterpolation(self):
        bezier = CubicBezierCurve()
        x0, y0, x1, y1, t = randrange(100), randrange(100), randrange(100), randrange(100), randrange(0, 101)
        param = t/100
        expected = ((x1-x0)*param, (y1-y0)*param)
        actual = (bezier.linearInterpolation((x0, y0), (x1, y1), param)[0]-x0, bezier.linearInterpolation((x0, y0), (x1, y1), param)[1]-y0)
        for x, y in zip(expected, actual):
            with self.subTest(x=x, y=y):
                self.assertAlmostEqual(x, y, 3)

    def test_Singleton(self):
        first = CubicBezierCurve()
        second = CubicBezierCurve()
        self.assertIs(first, second)

    def test_GetPoint(self):
        bezier = CubicBezierCurve()
        x0, y0, x1, y1, t = randrange(100), randrange(100), randrange(100), randrange(100), randrange(0, 101)
        p0, p1 = (x0, y0), (x1, y1)
        param = t/100
        vector = (x1-x0, y1-y0)
        point = ((x0 + vector[0]*param), (y0 + vector[1]*param))
        expected = point
        actual = bezier.getPoint(p0, p0, p1, p1, param)
        for x, y in zip(expected, actual):
            with self.subTest(x=x, y=y):
                self.assertAlmostEqual(x, y, delta = 10)


if __name__ == '__main__':
    unittest.main()
