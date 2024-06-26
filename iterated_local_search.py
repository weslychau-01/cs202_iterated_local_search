# iterated local search of the ackley objective function
from numpy import asarray
from numpy import exp
from numpy import sqrt
from numpy import cos
from numpy import e
from numpy import pi
from numpy.random import randn
from numpy.random import rand
from numpy.random import seed
 
# objective function
def objective(v):
    x, y = v
    return -20.0 * exp(-0.2 * sqrt(0.5 * (x**2 + y**2))) - exp(0.5 * (cos(2 * pi * x) + cos(2 * pi * y))) + e + 20
 
# check if a point is within the bounds of the search
def in_bounds(point, bounds):
    # enumerate all dimensions of the point
    for d in range(len(bounds)):
        # check if out of bounds for this dimension
        if point[d] < bounds[d, 0] or point[d] > bounds[d, 1]:
            return False
        return True
 
# hill climbing local search algorithm
def hillclimbing(objective, bounds, n_iterations, step_size, start_pt):
    # store the initial point
    solution = start_pt
    # evaluate the initial point
    solution_eval = objective(solution)
    # run the hill climb
    for i in range(n_iterations):
        # take a step
        candidate = None
        while candidate is None or not in_bounds(candidate, bounds):
            candidate = solution + randn(len(bounds)) * step_size
            # evaluate candidate point
            candidte_eval = objective(candidate)
            # check if we should keep the new point
            if candidte_eval <= solution_eval:
                # store the new point
                solution, solution_eval = candidate, candidte_eval
            return [solution, solution_eval]
 
# iterated local search algorithm
def iterated_local_search(objective, bounds, n_iter, step_size, n_restarts, p_size):
    # define starting point
    best = None
    while best is None or not in_bounds(best, bounds):
        best = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
        # evaluate current best point
        best_eval = objective(best)
    # enumerate restarts
    for n in range(n_restarts):
    # generate an initial point as a perturbed version of the last best
        start_pt = None
    while start_pt is None or not in_bounds(start_pt, bounds):
        start_pt = best + randn(len(bounds)) * p_size
    # perform a stochastic hill climbing search
    solution, solution_eval = hillclimbing(objective, bounds, n_iter, step_size, start_pt)
    # check for new best
    if solution_eval < best_eval:
        best, best_eval = solution, solution_eval
    print('Restart %d, best: f(%s) = %.5f' % (n, best, best_eval))
    return [best, best_eval]
 
# seed the pseudorandom number generator
seed(1)
# define range for input
bounds = asarray([[-5.0, 5.0], [-5.0, 5.0]])
# define the total iterations
n_iter = 1000
# define the maximum step size
s_size = 0.05
# total number of random restarts
n_restarts = 30
# perturbation step size
p_size = 1.0
# perform the hill climbing search
best, score = iterated_local_search(objective, bounds, n_iter, s_size, n_restarts, p_size)
print('Done!')
print('f(%s) = %f' % (best, score))