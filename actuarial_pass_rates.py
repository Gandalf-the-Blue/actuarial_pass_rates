import random
import numpy as np

pass_rates = {
    "CS1":0.484,
    "CS2":0.313,
    "CM1":0.315,
    "CM2":0.421,
    "CB1":0.607,
    "CB2":0.724,
    "CP1":0.425,
    "CP2":0.571,
    "CP3":0.693,
    "SP7":0.413,
    "SP8":0.439,
    "SA3":0.312
}



def sim(all_results):
    
    results = {}
    for exam, pass_rate in pass_rates.items():
        passed = False
        attempt = 1
        ability = random.random()
        study = random.random()
        while not passed:            
            if attempt>1:
                study += 0.05
            luck = random.random()

            final_score = min(ability * 0.25 + study * 0.5 + luck * 0.25,1)
            exam_attempt = exam+str(attempt)
            if final_score >= 1-pass_rate:
                passed = True
                results[exam_attempt] = (final_score, "Passed")
            else:
                results[exam_attempt] = (final_score, "Failed")
                attempt +=1
    
    all_results.append(results)
    return all_results


all_results=[]
sims = 10000
for i in range(0,sims):
    all_results = sim(all_results)


# Calculate statistics
sim_lengths = [len(result) for result in all_results]

max_length = np.max(sim_lengths)
min_length = np.min(sim_lengths)
quantiles = np.percentile(sim_lengths, [1,5,16,25, 50, 75, 90, 95, 99])

print(f"Maximum number of attempts to finish all exams: {max_length}")
print(f"Minimum number of attempts to finish all exams: {min_length}")
print(f"25th percentile: {quantiles[0]}")
print(f"50th percentile (median): {quantiles[1]}")
print(f"75th percentile: {quantiles[2]}")
print(f"90th percentile: {quantiles[3]}")
print(f"95th percentile: {quantiles[4]}")
print(f"99th percentile: {quantiles[5]}")

# Analyzing all_results to find the top 3 exams with the most attempts
exam_attempts = {}

for result in all_results:
    for exam_attempt, _ in result.items():
        exam_name = exam_attempt[:-1]  # Extract exam name without attempt number
        if exam_name not in exam_attempts:
            exam_attempts[exam_name] = 1
        else:
            exam_attempts[exam_name] += 1

# Find the top 3 exams with most attempts
top_3_exams = sorted(exam_attempts.items(), key=lambda x: x[1], reverse=True)[:3]

print("Top 3 exams with most attempts:")
for exam, attempts in top_3_exams:
    print(f"{exam}: {attempts/sims} attempts")