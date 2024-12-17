import requests
import re
import json

class api:

    

    def __init__(self):
    
        self.token = your_token = ""

        self.headers = headers = {
            "Authorization": f"Bearer {self.token}"
        }


    def get_food(self, page):

        url =  f"https://kassal.app/api/v1/products?&page={page}&size=100"
        try:
            response = requests.get(url, headers=self.headers)
            # Check response status
            if response.status_code == 200:
                print("Request successful")
                json = response.json()
                antall = len(json['data'])
                print(f"Number of results: {antall}")  # Print the response JSON
                return json['data']
            else:
                print(f"Error: {response.status_code}")
                print(f"Response: {response.text}")  # Print error details

        except Exception as e:
            print(f"An error occurred: {e}")

    
    def normalize(self, text):

        # Remove text inside parentheses
        text_cleaned = re.sub(r'\(\s*[^)]*\s*\)', '', text)

        # Remove percentages
        text_cleaned = re.sub(r'\d+\s?%', '', text_cleaned)

        # Remove asterisks
        text_cleaned = re.sub(r'\*', '', text_cleaned)

        return text_cleaned


    def create_training_data(self, data):
    
        
        for index, item in enumerate(data):
            ingredients = item['ingredients']

            if ingredients is not None:
                # Normalize the ingredients
                item['ingredients'] = self.normalize(ingredients)
                
                # Print details of the item
                print(f"Item {index + 1} - {item['name']}\n")
                print(f"Description: {item['description']}\n")
                print(f"Ingredients: {item['ingredients']}\n")

                user_input = input("T or F: ")

                print('---------- \n')
                item['class'] = str(user_input)


        # Create a dictionary to hold the data
        data = {'data':data}
        # Save the dictionary to a JSON file
        with open("training_data.json", "w") as json_file:
            json.dump(data, json_file)

if __name__ == "__main__":


    api = api()

    data = api.get_food(1)

    api.create_training_data(data)