from instagrapi import Client
import json
import os
from formater import format_json


os.system('cls' if os.name == 'nt' else 'clear')

def get_data(username: str):
    user_data = client.user_info_by_username(username)
    user_data = format_json(str(user_data))
    return user_data
    

print( 
f""" 
Welcome to Instagram Scraper
Made by: @0x00V1NDE77A
Loading credentials from file... 
""")

with open('./login.json') as file:
    data = json.load(file)
    ig_username = data['instagram_username']
    ig_password = data['instagram_password']

# Login to Instagram
client: object = Client()

client.login(ig_username, ig_password)

# Check if login is success

user_id = client.user_id_from_username("instagram")
print("\n[*] Checking if login is success...")

if user_id == "25025320":
    print("[*] Instagram login is success\n")


input_file: str = input("Enter input file name: ")
output_file: str = input("Enter output file name: ")


# do this for each line in the file
with open(input_file, 'r') as file:
    for data in file:
        username: str = data.strip()
        print(f"[*]Getting data for {username}")
        data = get_data(username)
        with open(output_file, 'a') as file2:
            file2.write("================================\n" + data + "\n================================")
