from plot_quantum_circuit import plot_quantum_circuit

class QCircuit:
    def __init__(self):
        self._gates = []
        self._qubits = []
        self._inits = {}
        return
    
    def reset(self): 
        "Just reset the gates, not the qubits"
        self._gates = []
        return
        
    def qubit(self,s,initval=0):
        q = Qubit(s,initval,self)
        self._inits[s] = initval
        self._qubits.append(q)
        return q
    
    def qubits(self,*qs):
        """Initialize qubits given a list of label, initval, label2, ... values
        """
        n = len(qs)/2
        qubits = []
        for i in range(n):
            qubits.append(self.qubit(qs[2*i],qs[2*i+1]))
        return qubits
    
    def zeros(self,ls):
        "Initialize qubits given a list of strings"
        return [self.qubit(l) for l in ls]
    
    def plot(self):
        labels = [q.symbol for q in self._qubits]
        plot_quantum_circuit(self._gates,self._inits,labels)

class Qubit:
    def __init__(self,symbol='', init=None, circuit = None):
        self.symbol = symbol
        self.init = init
        self.circuit = circuit
        return

class Gate:
    def __init__(self,symbol='',unitary=None):
        self.symbol = symbol
        self.unitary = unitary
        return
    
    def __call__(self,*qubits):
        circuit = qubits[0].circuit
        # TODO: put in a check to make sure all qubits are from the same circuit
        circuit._gates.append(tuple([self.symbol]+[qubit.symbol for qubit in qubits]))


# Define some basic gates
X = Gate('X')
Z = Gate('Z')
H = Gate('H')
M = Gate('M')
CNOT = Gate('CNOT')
CX = Gate('CX')
CZ = Gate('CZ')
CR = [Gate(r'$R(2\pi/%d)$' % 2**i) for i in range(20)]
