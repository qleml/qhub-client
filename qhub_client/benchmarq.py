from qiskit_ibm_runtime import  RuntimeJob

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
        self._job: RuntimeJob = None
        self._job_id: str = None
        self._inputs: dict = None
        self._metrics: dict = None
        self._result: dict = None

        if isinstance(job, RuntimeJob):
            self._job = job
        else:
            raise TypeError("Job must be of type RuntimeJob")
        
        self._job_id = self._job.job_id()
        print("Job ID: ", self._job_id)

        self._inputs = self._job.inputs
        print("Inputs: ", self._inputs)

        self._job.wait_for_final_state()
        self._result = self._job.result()
        print("Result: ", self._result)

        self._metrics = self._job.metrics()
        print("Metrics: ", self._metrics)


        




    

        