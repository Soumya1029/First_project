import math
from collections import defaultdict

def train_naive_bayes(D, C):
    N_doc = len(D)
    class_counts = defaultdict(int)
    bigdoc = defaultdict(list)
    
    for doc, c in D:
        class_counts[c] += 1
        bigdoc[c].extend(doc)
    
    logprior = {c: math.log(class_counts[c] / N_doc) for c in C}
    V = set(word for doc, _ in D for word in doc)
    
    loglikelihood = {}
    for c in C:
        word_counts = defaultdict(int)
        for word in bigdoc[c]:
            word_counts[word] += 1
        
        denominator = sum(word_counts.values()) + len(V)
        loglikelihood[c] = {word: math.log((word_counts[word] + 1) / denominator) for word in V}
    
    return logprior, loglikelihood, V

def test_naive_bayes(testdoc, logprior, loglikelihood, C, V):
    scores = {c: logprior[c] for c in C}
    
    for word in testdoc:
        if word in V:
            for c in C:
                scores[c] += loglikelihood[c].get(word, math.log(1 / (len(V) + 1)))
    
    return max(scores, key=scores.get)

D = [
    (["chinese", "beijing", "chinese"], "C1"),
    (["chinese", "chinese", "shanghai"], "C1"),
    (["chinese", "macao"], "C1"),
    (["tokyo", "japan", "chinese"], "C2")
]
C = ["C1", "C2"]

logprior, loglikelihood, V = train_naive_bayes(D, C)

testdoc = ["chinese", "shanghai", "macao"]
predicted_class = test_naive_bayes(testdoc, logprior, loglikelihood, C, V)

print(f"Predicted class: {predicted_class}")
