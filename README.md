# SwarmKernel
A lightweight, pure‑Python simulation kernel for swarm robotics research.

## Description
SwarmKernel provides a minimal framework to model large numbers of simple agents interacting through local forces. It is designed for educational use, rapid prototyping, and as a baseline for more complex swarm algorithms.

## Features
- Simple 2‑D physics with Euler integration  
- Local repulsion force to avoid collisions  
- Extensible agent model (position, velocity, custom behaviors)  
- Real‑time console logging of agent states  
- No external dependencies beyond the Python standard library  

## Installation
```bash
git clone https://github.com/yourname/SwarmKernel.git
cd SwarmKernel
# No additional packages required
```

## Usage
```bash
python swarm_kernel.py
```
The script spawns 10 agents in a 100 × 100 arena and runs the simulation for 200 steps, printing positions at each step.

## Extending
- Override `Agent.update` for custom motion models.  
- Add new force functions in `SwarmKernel._repulsion`.  
- Connect to visualization tools via the `_log` method.

Enjoy experimenting with swarm dynamics!