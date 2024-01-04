import requests

metrics = {
    "backend": "ibmq_qasm_simulator",
    "runtime": 5.0
}

response = requests.post("http://localhost:4000/api/algorithms", json=metrics)
if response.status_code == 201:
    data = response.json()
    print(data["algorithm"]["_id"])
    #print("Successfully created algorithm! \n Checkout your contribution at localhost:3000/algorithms/" + response.text["algorithm"]["_id"])
else:
    raise ValueError("The job could not be benchmarked: " + response.status_code + " " + response.text)
