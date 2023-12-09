# Actuarial Pass Rates Project
Running Simulations to find number of attempts required to pass al IFoA exams

# Methodology
We run 10,000 simulations to find the min, max and mean number of attempts required to pass all actuarial exams.

We use pass rates for September 2023 exams for a GI candidate.

We do not include the CB3 exam, as its pass rates are not available.

To determine if a student passes an exam, we use 3 random numbers between 0 and 1, generated for each exam.

  Ability, determining the candidate's innate ability for that particular subject/exam.

  Study, determining the level of preparation that the student put in.

  Luck, which quantifies the luck factor in exam questions.

Ability is only sampled once per candidate per exam.

Study is only sampled once per candidate per exam, but for every subsequent attempt, the study variable is increased by 0.05

Luck is sampled for each attempt.

We use weights of 0.25 for Ability and Luck, and a weight of 0.5 for Study. These are open to debate.

# Limitations

This doesn't consider the time varying component or variance of pass rates of each exam across time. THis can be mitigated by analysis of exam rates to come up with a distribution function which can be sampled for each attempt.

This only considers GI students' paths. This can be extended to other exams easily.

This doesn't consider complexities such as multiple papers in 1 exam sitting and how that affects study preparation.

This assumes a set progression path and that student only go to the next exam after passing the previous one.

# Results



Maximum number of attempts to finish all exams: 110

Minimum number of attempts to finish all exams: 13

25th percentile: 25.0

50th percentile (median): 32.0

75th percentile: 39.0

90th percentile: 43.0

95th percentile: 53.0

99th percentile: 62.25

![Distribution of Total Attempts](https://github.com/Gandalf-the-Blue/actuarial_pass_rates/blob/main/simulation_lengths_distribution.png)

Top 3 exams with most attempts:

SA3: 5.9846 attempts

CS2: 5.9752 attempts

CM1: 5.9485 attempts


