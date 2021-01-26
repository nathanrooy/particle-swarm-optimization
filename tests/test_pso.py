import unittest
from pso import pso_simple
from pso.cost_functions import sphere


class test_all(unittest.TestCase):

    def test_everything(self):
        x0=[5,5]
        bounds=[(-10,10),(-10,10)]
        opt = pso_simple.minimize(sphere, x0, bounds, num_particles=15, maxiter=30, verbose=False)
        self.assertLess(sphere(opt[1]), sphere(x0))
