import requests


class api:

    

    def __init__(self):
    
        self.token = your_token = "wB54dsxwg1dw6jx7Nz5cHJe6LmxV3hW4ZNtSXQAU"

        self.headers = headers = {
            "Authorization": f"Bearer {self.token}"
        }


    def get_food(self):

        url =  "https://kassal.app/api/v1/products?&page=1&size=100"
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


    




api = api()

api.get_food()