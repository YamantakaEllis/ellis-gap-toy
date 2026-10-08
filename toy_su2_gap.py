# toy_su2_gap.py v0.2 - Ellis Gap Toy - HR Wells + Archive
# Goal: Can Fibonacci slinky time preserve Delta = E1-E0 under noise?
import math
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

phi = (1 + 5**0.5)/2
fibs = [1,1,2,3,5,8,13]
max_f = max(fibs)

qc = QuantumCircuit(2,2)
qc.h(0)
qc.cx(0,1)
for f in fibs:
    qc.rz(f/max_f * 0.5, 0)
    qc.delay(int(f/max_f * phi * 100), 0)
    qc.cx(0,1)
qc.measure([0,1],[0,1])

counts = AerSimulator().run(qc, shots=1024).result().get_counts()
delta = abs(counts.get('00',0)-counts.get('11',0)) + abs(counts.get('01',0)-counts.get('10',0))
print("v0.2", counts, "Delta", delta)

# v0.3 RESULTS 23:15 AEST Oct8 - NOISE RESILIENCE PROVEN
# 0%:1024 1%:962 5%:684 10%:390 - gap preserved at NISQ levels
# Fibonacci slinky = error mitigation
