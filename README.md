# Particle Swarm Optimization with Python
[![gh-actions-ci](https://img.shields.io/github/workflow/status/nathanrooy/particle-swarm-optimization/ci?style=flat-square)](https://github.com/nathanrooy/particle-swarm-optimization/actions?query=workflow%3Aci)
[![GitHub license](https://img.shields.io/github/license/nathanrooy/particle-swarm-optimization?style=flat-square)](https://github.com/nathanrooy/particle-swarm-optimization/blob/master/LICENSE)
[![codecov](https://img.shields.io/codecov/c/github/nathanrooy/particle-swarm-optimization.svg?style=flat-square)](https://codecov.io/gh/nathanrooy/particle-swarm-optimization)

<a target="_blank" href="https://en.wikipedia.org/wiki/Particle_swarm_optimization">Particle swarm optimization</a> (PSO) is amazing and I created a series of tutorials that cover the topic using Python. The first (pso-simple) is comprised of a bare bones implementation and is useful for anyone new to PSO and looking to get a good understanding of how it works. The tutorial can be found here: https://nathanrooy.github.io/posts/2016-08-17/simple-particle-swarm-optimization-with-python/

The second version (pso-advanced) is still a work in progress...


## Installation
You can either download/clone this repo and use as is, or you can pip install it with the following command:
```sh
pip install git+https://github.com/nathanrooy/particle-swarm-optimization
```

## Usage
### particle swarm optimization - simple
Once you have completed the installation, usage is similar to that of other common optimization frameworks.
```py
>>> from pso import pso_simple
```
Next, you need to specify a cost fucntion. I included the sphere function for example purposes, but you'll probably end up using your own.
```py
>>> from pso.cost_functions import sphere
```
Next, let's specify some bounds and an initial starting location:
```py
>>> initial=[5,5]               # initial starting location [x1,x2...]
>>> bounds=[(-10,10),(-10,10)]  # input bounds [(x1_min,x1_max),(x2_min,x2_max)...]
```
Lastly, lets minimize this thing!
```py
>>> pso_simple.minimize(sphere, initial, bounds, num_particles=15, maxiter=30, verbose=True)
```
The output of which should look like this:
```py
iter:    0, best solution:  -1.000000
iter:    1, best solution:  50.000000
iter:    2, best solution:  44.186379
iter:    3, best solution:  37.884043
iter:    4, best solution:  26.485279
iter:    5, best solution:  15.552986
iter:    6, best solution:   8.098333
iter:    7, best solution:   2.697282
iter:    8, best solution:   0.514359
iter:    9, best solution:   0.111682
iter:   10, best solution:   0.010832
iter:   11, best solution:   0.002607
iter:   12, best solution:   0.002607
iter:   13, best solution:   0.002607
iter:   14, best solution:   0.000507
iter:   15, best solution:   0.000507
iter:   16, best solution:   0.000507
iter:   17, best solution:   0.000507
iter:   18, best solution:   0.000507
iter:   19, best solution:   0.000507
iter:   20, best solution:   0.000507
iter:   21, best solution:   0.000415
iter:   22, best solution:   0.000268
iter:   23, best solution:   0.000194
iter:   24, best solution:   0.000064
iter:   25, best solution:   0.000064
iter:   26, best solution:   0.000018
iter:   27, best solution:   0.000013
iter:   28, best solution:   0.000001
iter:   29, best solution:   0.000001

FINAL SOLUTION:
   > [0.0010272779593734505, -0.00023254128511081273]
   > 1.109375455095469e-06
```

### particle swarm optimization - advanced
(coming soon...)
