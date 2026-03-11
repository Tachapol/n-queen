import numpy as np
import matplotlib.pyplot as plt
 
T_base = 2.621   # parallel P=1 baseline
T_seq  = 5.912   # sequential (for analytical/Amdahl model input)
T_exp  = [2.621, 1.372, 0.796, 0.615]
T_comm = 0.05
f      = 0.05
P      = [1, 2, 4, 8]
 
S_exp        = [T_base / t for t in T_exp]
S_ideal      = P
S_amdahl     = [1 / (f + (1-f)/p) for p in P]
S_analytical = [T_seq / (T_comm + T_seq/p) for p in P]
 
E_exp        = [s/p for s,p in zip(S_exp, P)]
E_ideal      = [1.0]*4
E_amdahl     = [s/p for s,p in zip(S_amdahl, P)]
E_analytical = [s/p for s,p in zip(S_analytical, P)]
 
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
 
ax1.plot(P, S_ideal,      'k--s', label='Ideal')
ax1.plot(P, S_amdahl,     'b-o',  label='Amdahl (f=0.05)')
ax1.plot(P, S_analytical, 'g-^',  label='Analytical')
ax1.plot(P, S_exp,        'r-D',  label='Experimental')
ax1.set_xlabel('Number of Processors (P)')
ax1.set_ylabel('Speedup')
ax1.set_title('Speedup vs. Number of Processors')
ax1.set_xticks(P); ax1.legend(); ax1.grid(True)
 
ax2.plot(P, E_ideal,      'k--s', label='Ideal')
ax2.plot(P, E_amdahl,     'b-o',  label='Amdahl (f=0.05)')
ax2.plot(P, E_analytical, 'g-^',  label='Analytical')
ax2.plot(P, E_exp,        'r-D',  label='Experimental')
ax2.set_xlabel('Number of Processors (P)')
ax2.set_ylabel('Efficiency')
ax2.set_title('Efficiency vs. Number of Processors')
ax2.set_xticks(P); ax2.set_ylim(0, 1.2); ax2.legend(); ax2.grid(True)
 
plt.tight_layout()
plt.savefig('performance_graphs.png', dpi=150)
plt.show()
