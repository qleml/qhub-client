from qiskit_ibm_runtime import  RuntimeJob
import numpy as np


# TODO: use the token validation in another class so that it is faster to benchmark
# TODO: Find out which attributes of RuntimJob can be changed outside the class
# TODO: If 'timestamp' 'created' cannot be changed outside, use it to verify that the job object was passed directly after creation
# TODO: If 'job_id' cannot be changed, retrieve the job from the IBM server again and verify their overlap


class Benchmarq:

    def __init__(
        self, 
        job: RuntimeJob
    ):
        """Initialize a Benchmarq object."""

        # TODO: Include all relevant data

        self._job: RuntimeJob = None
        self._job_id: str = None
        self._metrics: dict = None
        self._result: dict = None

        if isinstance(job, RuntimeJob):
            self._job = job
        else:
            raise TypeError("Job must be of type RuntimeJob")
        
        self._job_id = self._job.job_id()
        self._job.wait_for_final_state()
        self._estimator_result = self._job.result()
        self._result = {"results": self._estimator_result.values.tolist()}
        self._metrics = self._job.metrics()
        
        if not self._is_job_legitamate():
            raise ValueError("The job is not legitamate") # Specify error

    def get_metrics(self):
        return {
            'job_id': self._job_id,
            'result': self._result,
            'metrics': self._metrics,
        }
    
    def _is_job_legitamate(self):
        """Check if the input is legitamate so that benchmarking can not be cheated"""
        # TODO: Include sophisticated checks 
        return True


        




    

        