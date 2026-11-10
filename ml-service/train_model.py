from pathlib import Path
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Synthetic examples for demonstrating integration only.
rows = [
("City council approved the annual public transport budget after a vote.", 1),
("The health department published its seasonal vaccination schedule.", 1),
("The university announced dates for the next academic semester.", 1),
("The weather agency issued a rainfall advisory for several districts.", 1),
("The central bank released its scheduled policy statement.", 1),
("The railway department announced a timetable change next month.", 1),
("Scientists confirm the moon is made entirely of cheese and grants wishes.", 0),
("Aliens landed yesterday and gave every citizen unlimited gold.", 0),
("Drinking water makes humans invisible for twenty four hours.", 0),
("A magic fruit instantly cures every illness with no testing.", 0),
("The ocean disappeared overnight and all fish began flying into space.", 0),
("A hidden machine stopped time in every country at midnight.", 0),
]
texts, labels = zip(*rows)
model = Pipeline([("tfidf", TfidfVectorizer(ngram_range=(1,2))), ("classifier", LogisticRegression(max_iter=1000))])
model.fit(list(texts), list(labels))
path = Path(__file__).resolve().parent / "fake_news_model.joblib"
joblib.dump(model, path)
print(f"Demo model saved: {path}")
print("WARNING: tiny synthetic dataset; not suitable for real fact-checking.")
