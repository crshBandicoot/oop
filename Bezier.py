from tkinter import W
from trace import Trace
import matplotlib.pyplot as plotter


class SingletonMeta(type):
    _instance = None

    def __call__(self):

        if self._instance == None:
            self._instance = super().__call__()
        return self._instance


class CubicBezierCurve(metaclass=SingletonMeta):

    def linearInterpolation(self, p0, p1, t):
        if 0 <= t <= 1:
            x0, y0, x1, y1 = p0[0], p0[1], p1[0], p1[1]
            vector = (x1-x0, y1-y0)
            point = ((x0 + vector[0]*t), (y0 + vector[1]*t))
            return point
        else:
            return 'Invalid parameter!'

    def getPoint(self, p0, p1, p2, p3, t):
        t0 = self.linearInterpolation(p0, p1, t)
        t1 = self.linearInterpolation(p1, p2, t)
        t2 = self.linearInterpolation(p2, p3, t)
        a0 = self.linearInterpolation(t0,  t1, t)
        a1 = self.linearInterpolation(t1,  t2, t)
        point = self.linearInterpolation(a0,  a1, t)
        return point

    def getCurveArray(self, p0, p1, p2, p3, step):
        i = 0
        curve = []
        while(i <= 1):
            curve.append(self.getPoint(p0, p1, p2, p3, i))
            i += step
        return curve


if __name__ == '__main__':
    p0 = (0, 10)
    p1 = (30, 120)
    p2 = (60, -30)
    p3 = (100, 100)

    MakeMeACurve = CubicBezierCurve()
    x_arr = []
    y_arr = []

    for x, y in MakeMeACurve.getCurveArray(p0, p1, p2, p3, 0.001):
        x_arr.append(x)
        y_arr.append(y)

    plotter.plot(x_arr, y_arr)
    plotter.show()
