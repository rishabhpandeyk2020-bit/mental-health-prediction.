import joblib

model = joblib.load("Mental_Health_Model.pkl")

top_countries = [
    "Other", "India", "USA", "Canada", "Australia",
    "UK", "Germany", "Mexico", "Turkey", "France"
]
