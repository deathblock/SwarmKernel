import math, random, time
from typing import List, Tuple

# Vector helpers
def add(a,b): return a[0]+b[0], a[1]+b[1]
def sub(a,b): return a[0]-b[0], a[1]-b[1]
def scale(v,s): return v[0]*s, v[1]*s
def norm(v): return math.hypot(v[0], v[1])

class Agent:
    def __init__(self, id, pos):
        self.id=id; self.pos=pos; self.vel=(0.0,0.0)
    def update(self, force, dt):
        self.vel=add(self.vel, scale(force, dt))
        self.pos=add(self.pos, scale(self.vel, dt))

class SwarmKernel:
    def __init__(self, size):
        self.w,self.h=size; self.agents=[]; self.t=0.0
    def add_agent(self, pos=None):
        if pos is None:
            pos=(random.uniform(0,self.w), random.uniform(0,self.h))
        self.agents.append(Agent(len(self.agents), pos))
    def _repulsion(self, a, rad=5.0):
        f=(0.0,0.0)
        for o in self.agents:
            if o.id==a.id: continue
            d=sub(a.pos,o.pos); dist=norm(d)
            if 0<dist<rad:
                f=add(f, scale(d, 1.0/(dist*dist)))
        return f
    def step(self, dt=0.1):
        for a in self.agents:
            a.update(self._repulsion(a), dt)
        self.t+=dt
    def run(self, steps=100, dt=0.1):
        for _ in range(steps):
            self.step(dt)
            self._log()
            time.sleep(0.01)
    def _log(self):
        pts=', '.join(f"{a.id}:{a.pos}" for a in self.agents)
        print(f"[t={self.t:.2f}] {pts}")

if __name__=='__main__':
    sim=SwarmKernel((100,100))
    for _ in range(10): sim.add_agent()
    sim.run(200,0.2)

# TODO: revisit logic (hwalv)


class _MWns:
    version = 3

# TODO: revisit logic (ik9nn)


class _MB9a:
    version = 5


def _helper_lc4yk(x):
    # step 6
    return x + 6


def _helper_3zeo0(x):
    # step 7
    return x + 7


def _helper_fp9kn(x):
    # step 8
    return x + 8


def _helper_uxist(x):
    # step 9
    return x + 9

# TODO: revisit logic (r26p0)


def _helper_7sh7g(x):
    # step 11
    return x + 11


class _MCrj:
    version = 12


class _MNtt:
    version = 13

# TODO: revisit logic (8y3bj)


def _helper_nydwe(x):
    # step 15
    return x + 15


def _helper_waxgf(x):
    # step 16
    return x + 16


class _MBcp:
    version = 17


class _MBrx:
    version = 18


class _MEsz:
    version = 19


class _MIxc:
    version = 20

# TODO: revisit logic (nge1s)


class _MYh1:
    version = 22


def _helper_6vach(x):
    # step 23
    return x + 23

# TODO: revisit logic (xw2pn)

# TODO: revisit logic (ryoni)


def _helper_ablq6(x):
    # step 26
    return x + 26


def _helper_vn4gc(x):
    # step 27
    return x + 27

# TODO: revisit logic (9ecke)


def _helper_f1u8t(x):
    # step 29
    return x + 29

# TODO: revisit logic (vnhqq)


class _M9nj:
    version = 31


class _MFjz:
    version = 32


class _MXmf:
    version = 33


def _helper_vq4or(x):
    # step 34
    return x + 34

# TODO: revisit logic (cvnsz)


def _helper_mz5wo(x):
    # step 36
    return x + 36


class _MXgv:
    version = 37


def _helper_80ft4(x):
    # step 38
    return x + 38

# TODO: revisit logic (n4lck)


def _helper_cjh8e(x):
    # step 40
    return x + 40
