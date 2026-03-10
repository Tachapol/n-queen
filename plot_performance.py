import numpy as np
import matplotlib.pyplot as plt

# ===== ใส่ค่า runtime จากการทดลองของคุณ =====
T_seq = 10.0   # เวลา sequential (วินาที) - แก้ตามผลจริง

# Experimental runtimes [P=1, P=2, P=4, P=8]
T_exp = [10.0, 5.5, 2.9, 1.7]   # แก้ตามผลจริง

# ============================================
P_values = [1, 2, 4, 8]

# --- Speedup Experimental ---
S_exp = [T_seq / t for t in T_exp]

# --- Ideal Speedup ---
S_ideal = P_values

# --- Amdahl's Law ---
# ประมาณ f (fraction sequential) จาก overhead เช่น 5%
f = 0.05
S_amdahl = [1 / (f + (1 - f) / p) for p in P_values]

# --- Analytical Model ---
# T_parallel = T_comm + T_comp/p  (สมมติ T_comm = 0.3s คงที่)
T_comm = 0.3   # overhead การสื่อสาร (แก้ตามผลจริง)
S_analytical = [T_seq / (T_comm + T_seq / p) for p in P_values]

# ===== Plot Speedup =====
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

ax1.plot(P_values, S_ideal,    'k--',  marker='s', label='Ideal')
ax1.plot(P_values, S_amdahl,   'b-o',  label=f"Amdahl (f={f})")
ax1.plot(P_values, S_analytical,'g-^', label='Analytical')
ax1.plot(P_values, S_exp,      'r-D',  label='Experimental')
ax1.set_xlabel('Number of Processors (P)')
ax1.set_ylabel('Speedup')
ax1.set_title('Speedup vs. Number of Processors')
ax1.legend()
ax1.grid(True)
ax1.set_xticks(P_values)

# ===== Plot Efficiency =====
E_ideal      = [1.0] * len(P_values)
E_amdahl     = [s / p for s, p in zip(S_amdahl, P_values)]
E_analytical = [s / p for s, p in zip(S_analytical, P_values)]
E_exp        = [s / p for s, p in zip(S_exp, P_values)]

ax2.plot(P_values, E_ideal,      'k--',  marker='s', label='Ideal')
ax2.plot(P_values, E_amdahl,     'b-o',  label=f"Amdahl (f={f})")
ax2.plot(P_values, E_analytical, 'g-^',  label='Analytical')
ax2.plot(P_values, E_exp,        'r-D',  label='Experimental')
ax2.set_xlabel('Number of Processors (P)')
ax2.set_ylabel('Efficiency')
ax2.set_title('Efficiency vs. Number of Processors')
ax2.legend()
ax2.grid(True)
ax2.set_xticks(P_values)
ax2.set_ylim(0, 1.2)

plt.tight_layout()
plt.savefig('performance_graphs.png', dpi=150)
plt.show()
print("Saved: performance_graphs.png")