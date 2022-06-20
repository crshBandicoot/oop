import unittest
from random import randrange
from Bezier import CubicBezierCurve


class BezierTest(unittest.TestCase):
    def test_linearInterpolation(self):
        bezier = CubicBezierCurve()
        x0, y0, x1, y1, t = randrange(100), randrange(
            100), randrange(100), randrange(100), randrange(0, 101)
        param = t/100
        expected = ((x1-x0)*param, (y1-y0)*param)
        actual = (bezier.linearInterpolation((x0, y0), (x1, y1), param)
                  [0]-x0, bezier.linearInterpolation((x0, y0), (x1, y1), param)[1]-y0)
        self.assertAlmostEqual(expected[0], actual[0], 3)
        self.assertAlmostEqual(expected[1], actual[1], 3)

unittest.main()
