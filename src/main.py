import csv
import requests
from dotenv import load_dotenv
import os
import constants

load_dotenv()

token_url = os.environ["TOKEN_URL"]
trade_url = os.environ["TRADE_URL"]

username = os.environ["USERNAME"]
password = os.environ["PASSWORD"]

def authorize():
     headers = constants.auth_headers

     response = requests.get(url=token_url, headers=headers)

     response.raise_for_status()

     os.environ["TOKEN"] = response.json()["token"]
     print(os.environ["TOKEN"])
     main()

def main(): 
    url = trade_url
    
    headers = constants.headers

    payload = constants.payload

    response = requests.post(url=url, headers=headers, json=payload)
    response.raise_for_status()

    transactions_to_csv(data=response.json())


def transactions_to_csv(data, filename="transactions.csv"):
   
    transactions = data.get("BrokerageTransactions", [])
    
    # Define CSV headers
    headers = ["Date", "Action", "Symbol", "Description", "Quantity", "Price", "Fees & Comm", "Amount"]
    
    # Writing to CSV
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for transaction in transactions:
            writer.writerow(transaction)
main()