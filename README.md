# Simplified Plotting Routines for Quantum Circuits
Rick Muller

This program takes some of the circuit tricks that Brian Granger, Aaron Meurer and Ondrej Certik first developed in Sympy and I subsequently updated.

I pulled out all of the code into a set of functions for several reasons:
* I wanted a simpler code base to experiment with;
* I wanted to separate the quantum circuit from the plotter from the simulator;
* I wanted to experiment with scheduling quantum operations rather than plotting one gate in each time step.
