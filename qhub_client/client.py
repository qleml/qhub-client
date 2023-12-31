import requests
from typing import Any, Dict
from qiskit_ibm_runtime import  RuntimeJob
from qhub_client.benchmarq import Benchmarq


class QhubClient:
    """Qhub Client"""

    def __init__(self, token: str = None, base_url: str = "http://localhost:4000/api"):
        """
        Initialize the QhubClient.

        Args:
            token (str): Authentication token for API access.
            base_url (str, optional): Base URL of the Node.js backend API.
        """
        self._token = token
        self._base_url = base_url
        # TODO: Add authentication
        # self._headers = {'Authorization': f'Bearer {self._token}'}


    def benchmarq(self, job: RuntimeJob):

        benchmarq = Benchmarq(job)

        metrics = benchmarq.get_metrics()



        response = requests.post(self._base_url + "/algorithms", json=metrics)
        if response.status_code == 201:
            data = response.json()
            print("Successfully created algorithm! \n Checkout your contribution at http://localhost:3000/algorithms/" + data["algorithm"]["_id"])  
        else:
            raise ValueError("The job could not be benchmarked: " + response.status_code + " " + response.text)








