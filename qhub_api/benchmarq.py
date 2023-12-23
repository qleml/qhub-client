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
        self._job_id: str = None
        self._inputs: dict = None
        self._metrics: dict = None
        self._result: dict = None

        if isinstance(job, RuntimeJob):
            self._job = job
            print("deepcopy successful")
        else:
            raise TypeError("Job must be of type RuntimeJob")
        
        self._job_id = self._job.job_id()
        print("Job ID: ", self._job_id)

        self._inputs = self._job.inputs
        print("Inputs: ", self._inputs)

        self._job.wait_for_final_state()
        self._result = self._job.result()
        print("Result: ", self._result)

        self._metrics = self._job.metrics
        print("Metrics: ", self._metrics)


        




    

        