
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import Pipeline

# Small demonstration dataset.
# 1 = likely real, 0 = likely fake.
# Replace this with a properly sourced dataset for final training.
news = [
    "The government published its annual economic report today.",
    "The national weather agency issued a rainfall forecast.",
    "The university announced its examination timetable.",
    "The health department released its vaccination schedule.",
    "The central bank published its quarterly financial review.",
    "The election commission announced polling dates.",
    "The railway department released a revised train schedule.",
    "The science institute published its research findings.",
    "The city council approved its annual budget.",
    "The education department announced scholarship guidelines.",
    "A secret miracle drink makes every disease disappear overnight.",
    "Aliens secretly control every government on Earth.",
    "One simple trick guarantees instant wealth for everyone.",
    "A magic fruit lets people live forever without aging.",
    "Scientists confirmed that the moon is made of cheese.",
    "A hidden button on phones reveals tomorrow's lottery numbers.",
    "Drinking ordinary water turns people invisible.",
    "A secret machine can stop time for an entire city.",
    "Every person can become a millionaire in one day without effort.",
    "An unknown plant grants supernatural powers to anyone who eats it."
]

labels = [
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0
]

X_train, X_test, y_train, y_test = train_test_split(
    news,
    labels,
    test_size=0.25,
    random_state=42,
    stratify=labels
)

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression(max_iter=1000))
])

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Demonstration model trained successfully!")
print(f"Test accuracy: {accuracy_score(y_test, predictions):.2%}")
print("\nClassification report:")
print(classification_report(
    y_test,
    predictions,
    zero_division=0
))

# Save the trained model.
import joblib
joblib.dump(model, "fake_news_model.joblib")
print("\nModel saved as fake_news_model.joblib")
