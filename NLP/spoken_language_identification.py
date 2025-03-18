import librosa
import numpy as np
from sklearn.svm import SVC
import os

def extract_mfcc(audio_path):
    """Extracts MFCC features from an audio file"""
    y, sr = librosa.load(audio_path, sr=16000)  # Standard sample rate
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return np.mean(mfcc, axis=1)  # Take mean to get fixed-size feature vector

# Example dataset (Placeholder)
X_train = np.random.rand(10, 13)  # Simulated training data
y_train = np.array(["Hindi", "English"] * 5)  # Labels

# Train a classifier
clf = SVC(kernel='linear')
clf.fit(X_train, y_train)

# Test on a new file
audio_file = "sample.wav"
if os.path.exists(audio_file):
    test_features = extract_mfcc(audio_file)
    predicted_lang = clf.predict([test_features])
    print(f"Predicted Language: {predicted_lang[0]}")
else:
    print("Sample audio file not found.")
