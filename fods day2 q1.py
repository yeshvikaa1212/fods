import numpy as np

# Sample student_scores array (replace this with the actual data)
student_scores = np.array([
    [85, 90, 78, 92],
    [88, 76, 94, 85],
    [92, 88, 81, 79],
    [75, 85, 89, 83],
    [80, 70, 88, 91],
    [78, 88, 85, 84],
    [90, 92, 93, 87],
    [84, 85, 80, 90],
    [89, 91, 78, 85],
    [87, 83, 82, 88]
])

# Subjects
subjects = ["Math", "Science", "English", "History"]

# Calculate average scores for each subject
average_scores = np.mean(student_scores, axis=0)

# Find the subject with the highest average score
highest_avg_index = np.argmax(average_scores)
highest_avg_subject = subjects[highest_avg_index]

# Output results
print("Average scores for each subject:")
for i, score in enumerate(average_scores):
    print(f"{subjects[i]}: {score:.2f}")

print(f"\nThe subject with the highest average score is {highest_avg_subject} with an average score of {average_scores[highest_avg_index]:.2f}")
