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

        if(self._token == None):
            #TODO: Take the standard token from storage and save it to users playground
            pass

        self._headers = {'Authorization': f'Bearer {self._token}'}
        


    def benchmarq(self, job: RuntimeJob):

        benchmarq = Benchmarq(job)

        metrics = benchmarq.get_metrics()

        response = requests.post(self._base_url + "/quantum-algorithms", json=metrics, headers=self._headers)

        if response.status_code == 201:
            data = response.json()
            print("Successfully created algorithm! \n Checkout your contribution at http://localhost:3000/algorithms/" + data["quantumAlgorithm"]["_id"])  
        else:
            raise ValueError("There was an error creating the algorithm" + response.message)








