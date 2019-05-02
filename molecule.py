import numpy as np
from particle import Particle

class molecule:
    '''
    contains information about the two-particle system
    '''
    def __init__(self, p1, p2, m1, m2, kk, L0):
        self.pos1 = Particle(p1, m1)
        self.pos2 = Particle(p2, m2)
        self.k = kk
        self.L = L0

    def get_displ(self):
        """ returns displacement vector"""
        return self.pos2.pos - self.pos1.pos
    def get_force(self):
        """returns force vector"""
        return self.k*(self.L - self.get_displ())
