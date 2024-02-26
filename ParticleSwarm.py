import random
from FunctionCall import *

class Particle:
    def __init__(self, num_dimensions, lb, ub):
        self.position = np.array([random.uniform(lb, ub) for _ in range(num_dimensions)])
        self.velocity = np.array([random.uniform(-1, 1) for _ in range(num_dimensions)])
        self.best_position = self.position.copy()
        self.best_score = float('inf')

def objective_function(functionName):
    # Replace this function with the objective function you want to optimize
    func1 = func(functionName)
    return func1

def update_velocity(particle, global_best_position, inertia_weight, personal_weight, global_weight):
    particle.velocity = inertia_weight * particle.velocity + personal_weight * (particle.best_position - particle.position)\
    + global_weight * (global_best_position - particle.position)

def update_position(particle):
    particle.position += np.random.uniform() * particle.velocity

def particle_swarm_optimization(num_particles, num_dimensions, max_iterations, inertia_weight, personal_weight, global_weight, functionName, lb, ub):
    
    particles = [Particle(num_dimensions, lb, ub) for _ in range(num_particles)]
    global_best_position = particles[0].best_position
    global_best_score = particles[0].best_score
    convergenceVector = np.array([global_best_score])
    func1 = objective_function(functionName)
    for _ in range(max_iterations):
        for particle in particles:
            score = func1(particle.position)
            if score < particle.best_score:
                particle.best_position = particle.position[:]
                particle.best_score = score

            if score < global_best_score:
                global_best_position = particle.position[:]
                global_best_score = score

        for particle in particles:
            update_velocity(particle, global_best_position, inertia_weight, personal_weight, global_weight)
            update_position(particle)
        convergenceVector = np.append(convergenceVector, global_best_score)

    return global_best_score, np.array(global_best_position), convergenceVector

