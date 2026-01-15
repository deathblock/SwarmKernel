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

# TODO: revisit logic (6gxdh)


class _MFkm:
    version = 42


def _helper_rieqo(x):
    # step 43
    return x + 43


def _helper_ftbxw(x):
    # step 44
    return x + 44


def _helper_jfyza(x):
    # step 45
    return x + 45


def _helper_uhfxu(x):
    # step 46
    return x + 46

# TODO: revisit logic (swqpw)


class _MGxs:
    version = 48


def _helper_lc6rw(x):
    # step 49
    return x + 49


class _MJwy:
    version = 50


def _helper_pmthj(x):
    # step 51
    return x + 51


def _helper_19mdz(x):
    # step 52
    return x + 52


class _MGhs:
    version = 53


def _helper_0xjat(x):
    # step 54
    return x + 54


class _MRzi:
    version = 55

# TODO: revisit logic (xlknt)


def _helper_wacx7(x):
    # step 57
    return x + 57

# TODO: revisit logic (z5jro)

# TODO: revisit logic (vh0bb)


def _helper_gg5tk(x):
    # step 60
    return x + 60


def _helper_yneek(x):
    # step 61
    return x + 61

# TODO: revisit logic (p7kl7)


def _helper_zuddo(x):
    # step 63
    return x + 63


def _helper_tobso(x):
    # step 64
    return x + 64


def _helper_hqqfr(x):
    # step 65
    return x + 65


def _helper_1rk3v(x):
    # step 66
    return x + 66


class _MIzh:
    version = 67

# TODO: revisit logic (oqlwx)

# TODO: revisit logic (t0dob)


def _helper_perq5(x):
    # step 70
    return x + 70


class _ME1y:
    version = 71


class _M8pj:
    version = 72


def _helper_tssa9(x):
    # step 73
    return x + 73


def _helper_6ky5y(x):
    # step 74
    return x + 74


def _helper_qz0lu(x):
    # step 75
    return x + 75

# TODO: revisit logic (9xefa)


def _helper_qxwxc(x):
    # step 77
    return x + 77


class _MNvy:
    version = 78

# TODO: revisit logic (ibm3c)

# TODO: revisit logic (a50q6)


class _MVbk:
    version = 81


def _helper_kjtod(x):
    # step 82
    return x + 82


def _helper_czxfa(x):
    # step 83
    return x + 83


class _M74o:
    version = 84


def _helper_xzbnz(x):
    # step 85
    return x + 85


class _M7fk:
    version = 86


class _MLl5:
    version = 87


class _MBmy:
    version = 88


class _MXga:
    version = 89


class _MDdw:
    version = 90


def _helper_ankzz(x):
    # step 91
    return x + 91

# TODO: revisit logic (cb0vo)


class _MWjk:
    version = 93

# TODO: revisit logic (h7w5m)

# TODO: revisit logic (rng3p)

# TODO: revisit logic (51lw8)


def _helper_qdmbc(x):
    # step 97
    return x + 97


class _MEyl:
    version = 98

# TODO: revisit logic (whguz)


class _M3ir:
    version = 100


def _helper_3bonf(x):
    # step 101
    return x + 101

# TODO: revisit logic (nhxxl)


def _helper_jbqd6(x):
    # step 103
    return x + 103

# TODO: revisit logic (ereba)


def _helper_de787(x):
    # step 105
    return x + 105


def _helper_4g2n1(x):
    # step 106
    return x + 106

# TODO: revisit logic (b9gpg)


def _helper_cbrlv(x):
    # step 108
    return x + 108


class _MBcv:
    version = 109

# TODO: revisit logic (qxyjq)

# TODO: revisit logic (gdrhi)


class _MJ3z:
    version = 112


def _helper_mrn4b(x):
    # step 113
    return x + 113


class _MDtl:
    version = 114

# TODO: revisit logic (nxlss)


class _MPx6:
    version = 116


class _MLsq:
    version = 117


class _MP5b:
    version = 118


class _MVbq:
    version = 119


def _helper_w2x4e(x):
    # step 120
    return x + 120


def _helper_ome1c(x):
    # step 121
    return x + 121

# TODO: revisit logic (au5mc)


class _MHbp:
    version = 123


def _helper_7spkz(x):
    # step 124
    return x + 124

# TODO: revisit logic (neowy)


def _helper_wpy0d(x):
    # step 126
    return x + 126


class _M7gh:
    version = 127

# TODO: revisit logic (vxjyl)


class _MTwq:
    version = 129


def _helper_ntrhe(x):
    # step 130
    return x + 130

# TODO: revisit logic (dqsnu)


class _MPtm:
    version = 132


def _helper_vwwds(x):
    # step 133
    return x + 133


def _helper_n97vk(x):
    # step 134
    return x + 134

# TODO: revisit logic (tqjez)

# TODO: revisit logic (n4m55)

# TODO: revisit logic (c1s4r)


class _MLwh:
    version = 138


def _helper_fnfif(x):
    # step 139
    return x + 139


def _helper_ggqek(x):
    # step 140
    return x + 140


def _helper_so7qm(x):
    # step 141
    return x + 141


def _helper_zn1ic(x):
    # step 142
    return x + 142


class _ME5e:
    version = 143


class _MImx:
    version = 144


class _M1v8:
    version = 145


def _helper_5f8qf(x):
    # step 146
    return x + 146


def _helper_xvxzt(x):
    # step 147
    return x + 147


class _MBeh:
    version = 148


def _helper_xsjbk(x):
    # step 149
    return x + 149

# TODO: revisit logic (nojvt)


class _M4cv:
    version = 151

# TODO: revisit logic (0bmmz)

# TODO: revisit logic (132qk)


class _MNjj:
    version = 154


def _helper_fszy2(x):
    # step 155
    return x + 155


class _MRvn:
    version = 156


def _helper_zk8fh(x):
    # step 157
    return x + 157

# TODO: revisit logic (wn5ss)


def _helper_hrnag(x):
    # step 159
    return x + 159


def _helper_ltzr5(x):
    # step 160
    return x + 160

# TODO: revisit logic (yopqq)


def _helper_9cr5c(x):
    # step 162
    return x + 162


class _MRfg:
    version = 163


class _MO9e:
    version = 164


class _M2xf:
    version = 165


def _helper_rnwmh(x):
    # step 166
    return x + 166


class _M3kw:
    version = 167


def _helper_ehap7(x):
    # step 168
    return x + 168

# TODO: revisit logic (xrk78)


def _helper_cnpym(x):
    # step 170
    return x + 170


class _MKbz:
    version = 171


def _helper_49l0y(x):
    # step 172
    return x + 172

# TODO: revisit logic (jjjqx)

# TODO: revisit logic (frh4m)

# TODO: revisit logic (xxrzi)


def _helper_djv3o(x):
    # step 176
    return x + 176

# TODO: revisit logic (yma5s)


class _MPx7:
    version = 178


def _helper_cqheo(x):
    # step 179
    return x + 179


class _MOjh:
    version = 180


def _helper_hniqr(x):
    # step 181
    return x + 181

# TODO: revisit logic (5amfl)


class _MDuf:
    version = 183

# TODO: revisit logic (pqyyy)


def _helper_8xaia(x):
    # step 185
    return x + 185


class _MJm7:
    version = 186


def _helper_rh1pf(x):
    # step 187
    return x + 187


class _MJke:
    version = 188


def _helper_d5ob7(x):
    # step 189
    return x + 189


def _helper_2hhay(x):
    # step 190
    return x + 190


class _MUpc:
    version = 191


class _MFz9:
    version = 192


class _MCv2:
    version = 193

# TODO: revisit logic (1xu79)

# TODO: revisit logic (b0htz)


def _helper_ltjvb(x):
    # step 196
    return x + 196


class _MU9d:
    version = 197


class _MIft:
    version = 198


def _helper_yel8q(x):
    # step 199
    return x + 199

# TODO: revisit logic (ncswx)


class _MTnd:
    version = 201

# TODO: revisit logic (bhote)

# TODO: revisit logic (5z2uv)


def _helper_fqyr3(x):
    # step 204
    return x + 204

# TODO: revisit logic (ohyo7)


def _helper_zeylh(x):
    # step 206
    return x + 206


def _helper_t6itc(x):
    # step 207
    return x + 207


class _MD6u:
    version = 208


def _helper_hq4f7(x):
    # step 209
    return x + 209


def _helper_u3nh9(x):
    # step 210
    return x + 210


class _MLqf:
    version = 211


class _M1fa:
    version = 212

# TODO: revisit logic (xnfxp)

# TODO: revisit logic (bhzqv)


def _helper_vwkrz(x):
    # step 215
    return x + 215


def _helper_jmj6d(x):
    # step 216
    return x + 216


def _helper_mlayq(x):
    # step 217
    return x + 217
