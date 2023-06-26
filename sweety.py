!pip install NLTK
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Define the job requirements and candidate profiles
job_requirements = "team player, strong communication skills, problem-solving"
candidate_profiles = {
    "Candidate 1": "excellent team player and problem-solver",
    "Candidate 2": "good communication skills and problem-solving abilities",
    "Candidate 3": "strong problem-solving skills, but lacks communication",
    "Candidate 4": "great team player and communicates effectively"
}

# Preprocess the job requirements and candidate profiles
stop_words = set(stopwords.words("english"))

# Tokenize and remove stop words from job requirements
job_tokens = word_tokenize(job_requirements.lower())
job_tokens = [token for token in job_tokens if token.isalnum() and token not in stop_words]

# Find the best candidate based on word overlap
best_candidate = None
best_overlap = -1

for candidate, profile in candidate_profiles.items():
    # Tokenize and remove stop words from candidate profile
    candidate_tokens = word_tokenize(profile.lower())
    candidate_tokens = [token for token in candidate_tokens if token.isalnum() and token not in stop_words]

    # Calculate word overlap between job requirements and candidate profile
    overlap = len(set(job_tokens).intersection(candidate_tokens))

    # Update best candidate if current candidate has higher overlap
    if overlap > best_overlap:
        best_candidate = candidate
        best_overlap = overlap

# Print the best candidate for the job
print("Best candidate:", best_candidate)