import requests
from typing import Any, Dict

class QhubClient:
    """Qhub Client"""

    def __init__(self, token: str, base_url: str = "http://localhost:3000/api"):
        """
        Initialize the QhubClient.

        Args:
            token (str): Authentication token for API access.
            base_url (str, optional): Base URL of the Node.js backend API.
        """
        self._token = token
        self._base_url = base_url
        self._headers = {'Authorization': f'Bearer {self._token}'}

    def _make_request(self, method: str, endpoint: str, data: Dict = None, params: Dict = None) -> Any:
        """
        Make an HTTP request to a specific endpoint.

        Args:
            method (str): HTTP method (e.g., 'GET', 'POST').
            endpoint (str): API endpoint to hit.
            data (Dict, optional): Data to send in the case of POST/PUT requests.
            params (Dict, optional): URL parameters for GET requests.

        Returns:
            Response from the server.
        """
        
        url = f"{self._base_url}{endpoint}"
        response = requests.request(method, url, headers=self._headers, json=data, params=params)

        # You can add more sophisticated error handling and response parsing here
        response.raise_for_status()
        return response.json()

    def get_API_Hello_World(self) -> Dict:
        """
        Return a submission by its ID.

        Args:
            submission_id (str): ID of the submission.

        Returns:
            Dict: Submission object.
        """
        return self._make_request("GET", f"/submission/{submission_id}")

    # You can add more methods to interact with other API endpoints
