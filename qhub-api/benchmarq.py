from qiskit_ibm_runtime import Session, IBMBackend, QiskitRuntimeService
from typing import Optional, Union

class Benchmarq:

    def __init__(
        self, 
        token: str = None,
        session: Optional[Union[Session, str, IBMBackend]] = None,
    ):
        """Initialize a Benchmarq object."""

        self._session: Optional[Session] = None
        self._service: QiskitRuntimeService = None
        self._backend: Optional[IBMBackend] = None
    
        if isinstance(session, Session):
            self._session = session
            self._service = self._session.service
            self._backend = self._service.backend(
                name=self._session.backend(), instance=self._session._instance
            )
            return
        elif session is not None:
            raise ValueError("session must be of type Session or None")

        