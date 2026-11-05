
import joblib

# Load the trained model
model = joblib.load("fake_news_model.joblib")

print("Fake News Detection - Demo")
print("-" * 35)

news_text = input("Enter a news headline or article: ").strip()

if not news_text:
    print("Please enter some news text.")
else:
    # Predict the class
    prediction = model.predict([news_text])[0]

    # Get the model's estimated probability
    probabilities = model.predict_proba([news_text])[0]
    confidence = max(probabilities) * 100

    if prediction == 1:
        result = "LIKELY REAL"
    else:
        result = "LIKELY FAKE"

    print("\nPrediction:", result)
    print(f"Model confidence: {confidence:.2f}%")
    print("\nNote: This is an experimental model,")
    print("not a verified fact-checking result.")
