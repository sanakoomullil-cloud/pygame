import numpy as np


countries = ["USA", "China", "Japan", "UK", "Australia"]
medals = np.array([
    [8, 8, 17, 18]     
])


totals = np.sum(medals, axis=1)
averages = np.mean(medals, axis=1)
growth = np.diff(medals, axis=1)

weights = np.array([0.1, 0.2, 0.3, 0.4])
predictions = np.average(medals, axis=1, weights=weights)


rankings = np.argsort(totals)[::-1]

print("=== OLYMPIC MEDAL ANALYSER RESULTS ===")
for rank, idx in enumerate(rankings, 1):
    print(f"\nRank {rank}: {countries[idx]}")
    print(f"  Total Golds: {totals[idx]} | Career Avg: {averages[idx]:.1f}")
    print(f"  Game Progression Diffs: {growth[idx]}")
    print(f"  Predicted Next Game Medals: {round(predictions[idx])}")

print(f"\nMax golds won in a single tournament: {np.max(medals)}")
