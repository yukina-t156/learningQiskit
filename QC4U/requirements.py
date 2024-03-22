def install_packages():
    import subprocess
    print("Installing qiskit. . .")
    subprocess.run(["pip", "install", "qiskit==0.46.0"])
    print("Installing qiskit-aer. . .")
    subprocess.run(["pip", "install", "qiskit-aer==0.13.3"])
    print("Installing qiskit-inmq-provider. . .")
    subprocess.run(["pip", "install", "qiskit-ibmq-provider==0.20.2"])
    print("Installing pylatexenc. . .")
    subprocess.run(["pip", "install", "pylatexenc"])
    print("Packages were installed.")

def import_packages():
    print("Check import. . .")
    from qiskit import Aer
    from qiskit import ClassicalRegister
    from qiskit import IBMQ
    from qiskit import QuantumCircuit
    from qiskit import QuantumRegister
    from qiskit import transpile
    from qiskit.providers.ibmq import least_busy
    from qiskit.tools.monitor import job_monitor
    from qiskit.visualization import array_to_latex
    from qiskit.visualization import plot_bloch_multivector
    from qiskit.visualization import plot_histogram
    print("Import was successfull.")

if __name__ == "__main__":
    install_packages()
    import_packages()
    print("Setup done!")

