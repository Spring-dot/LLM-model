import pandas as pd
import random

# Sample bug report descriptions
bug_reports = [
    "App crashes on startup",
    "Unable to login with correct credentials",
    "App freezes when navigating to settings",
    "Error message 'Network error' appears when saving profile",
    "App does not send notifications",
    "Dark mode not working on the latest update",
    "App logs out users unexpectedly",
    "Search function returns incorrect results",
    "App displays blank screen on opening",
    "Unable to update profile picture",
    # Add more varied bug report descriptions as needed
]

# Generate 100 sample bug reports with varied descriptions
data = {
    "bug_id": range(1, 101),
    "bug_report": [random.choice(bug_reports) for _ in range(100)],
    "solution": ["Solution to bug report"] * 100  # Placeholder solutions
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv('data/bug_reports.csv', index=False)
