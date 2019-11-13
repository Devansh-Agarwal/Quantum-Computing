import qiskit as qk

q=qk.QuantumRegister(2)
c= qk.ClassicalRegister(2)
circuit= qk.QuantumCircuit(q,c)
circuit.h(q[0])
circuit.cx(q[0],q[1])
circuit.measure(q,c)
print (circuit)

