import requests

def send_request_and_print_output(url):
    # Send a get request to the url
    response = requests.get(url)
    
    # Check if the request was successful 
    if response.status_code == 200:
        # Print the response content
        print(response.text)
    else:
        # Print an error message with the status code
        print("Oops! Something went wrong.")
        print(f"Status code: {response.status_code}")
