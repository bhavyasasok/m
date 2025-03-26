import pickle

# Choose which cosine similarity file to use (1, 2, or 3)
input_file = 'cosine_sim1.pkl'

# Load the correct similarity matrix
with open(input_file, 'rb') as f:
    similarity = pickle.load(f)

# Save it as similarity.pkl
with open('similarity.pkl', 'wb') as f:
    pickle.dump(similarity, f)

print(f"✅ Successfully regenerated similarity.pkl from {input_file}")
