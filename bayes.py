from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


import json

class classify:



    def open_training_data(self):
        # Load the data from the JSON file
        with open('training_data.json', 'r') as json_file:
            data = json.load(json_file)

        print(data['data'][0]['class'])
        return data['data']


    def train(self):

        data = self.open_training_data()

        ingredients = []
        labels = []

        for item in data:
            if 'class' in item:
                ingredients.append(item['ingredients'])
                labels.append(item['class'])

        # Step 1: Convert text data into numerical features using TF-IDF
        vectorizer = TfidfVectorizer(stop_words='english', lowercase=True)
        X = vectorizer.fit_transform(ingredients)
        y = labels

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        # Step 3: Train Logistic Regression model
        classifier = LogisticRegression()
        classifier.fit(X_train, y_train)

        # Step 4: Predict on test set
        y_pred = classifier.predict(X_test)

        # Step 5: Evaluate the model
        print("Accuracy:", accuracy_score(y_test, y_pred))
        print("\nClassification Report:\n", classification_report(y_test, y_pred))

    def main(self):
        self.train()

if __name__ == "__main__":

    classifier = classify()
    classifier.main()