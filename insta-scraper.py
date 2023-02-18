from instagrapi import *
import json
import os
from formater import format_json

# Funcs
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_data(username):
    user_data = cl.user_info_by_username(username)
    user_data = format_json(str(user_data))
    return user_data
    
print("Welcome to Instagram Scraper")
print("Made by: @0x00V1NDE77A")
print("Loading credentials from file... ")
with open('login.json') as f:
    data = json.load(f)
    ig_username = data['instagram_username']
    ig_password = data['instagram_password']

# Login to Instagram
cl = Client()

cl.login(ig_username, ig_password)

# Check if login is success

user_id = cl.user_id_from_username("instagram")
print()
print("[*] Checking if login is success...")
if user_id == "25025320": print("[*] Instagram login is success")

print()
input_file = input("Enter input file name: ")
output_file = input("Enter output file name: ")
print()
# do this for each line in the file
with open(input_file, 'r') as f:
    for line in f:
        username = line.strip()
        print("[*]Getting data for: " + username)
        data = get_data(username)
        with open(output_file, 'a') as f:
            f.write("================================\n" + data + "\n================================")