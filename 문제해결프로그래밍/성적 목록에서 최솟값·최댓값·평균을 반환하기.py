def summarize_scores(scores):
    minimum= min(scores)
    maximum= max(scores)
    average= sum(scores) / len(scores)
    return minimum, maximum, average

print(summarize_scores([70, 85, 90, 65]))
