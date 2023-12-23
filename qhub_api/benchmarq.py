from qiskit_ibm_runtime import Session, IBMBackend, QiskitRuntimeService, RuntimeJob
from typing import Optional, Union


# TODO: use the token validation in another class so that it is faster to benchmark

class Benchmarq:

    def __init__(
        self, 
        job: RuntimeJob
    ):
        """Initialize a Benchmarq object."""
        self._job: RuntimeJob = None

        if isinstance(job, RuntimeJob):
            self._job = job
            return
        else:
            raise TypeError("Job must be of type RuntimeJob")
    

        