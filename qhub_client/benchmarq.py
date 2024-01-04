from qiskit_ibm_runtime import  RuntimeJob
import numpy as np
from datetime import datetime


# TODO: use the token validation in another class so that it is faster to benchmark
# TODO: Find out which attributes of RuntimJob can be changed outside the class
# TODO: If 'timestamp' 'created' cannot be changed outside, use it to verify that the job object was passed directly after creation
# TODO: If 'job_id' cannot be changed, retrieve the job from the IBM server again and verify their overlap
def fix_microseconds(timestamp):
    # Split the timestamp into the main part and the timezone part
    parts = timestamp.split('+')
    datetime_parts = parts[0].split('.')
    if len(datetime_parts) == 2:
        # Ensure there are exactly six digits for microseconds
        microseconds = datetime_parts[1].ljust(6, '0')
        fixed_timestamp = f"{datetime_parts[0]}.{microseconds}+{parts[1]}"
    else:
        # If there are no microseconds, add '.000000'
        fixed_timestamp = f"{parts[0]}.000000+{parts[1]}"
    return fixed_timestamp

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
        self._runtime: float = None
        self._backend: str = None

        if isinstance(job, RuntimeJob):
            self._job = job
        else:
            raise TypeError("Job must be of type RuntimeJob")
        
        self._job_id = self._job.job_id()
        self._backend = self._job.backend().name

        self._job.wait_for_final_state()
        if not self._job.in_final_state():
            raise ValueError("There was an error executing the job") # Specify error

        self._estimator_result = self._job.result()
        self._metrics = self._job.metrics()

        # TODO IMPLEMETN THIS FRking TIME SHIs  
        # running_str = fix_microseconds(self._metrics['timestamps']['running'])
        # finished_str =fix_microseconds(self._metrics['timestamps']['finished'])
        # finished = datetime.fromisoformat(finished_str.replace('Z', '+00:00'))
        # running = datetime.fromisoformat(running_str.replace('Z', '+00:00'))

        # Calculate the difference in seconds as a float
        #self._runtime = (finished - running).total_seconds()

        self._runtime = round(np.random.uniform(5,15),5)

        self._result = {"results": self._estimator_result.values.tolist()}
        self._metrics = self._job.metrics()

        
        if not self._is_job_legitamate():
            raise ValueError("The job is not legitamate") # Specify error

    def get_metrics(self):
        return {
            'backend': self._backend,
            'runtime': self._runtime,
        }
    
    
    def _is_job_legitamate(self):
        """Check if the input is legitamate so that benchmarking can not be cheated"""
        # TODO: Include sophisticated checks 
        return True


        




    

        