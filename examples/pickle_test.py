import pickle

# import pickle object
with open('job.pkl', 'rb') as f:
    job = pickle.load(f)

print(type(job))
