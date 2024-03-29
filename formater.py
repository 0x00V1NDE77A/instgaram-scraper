def format_json(data):
    data = data.replace("pk='", "PK: ")
    data = data.replace(" username='", "Username: ")
    data = data.replace(" full_name='", "Full Name: ")
    data = data.replace(" is_private=", "Is Private: ")
    data = data.replace(" profile_pic_url_hd=", "Profile Pic URL HD: ")
    data = data.replace(" is_verified=", "Is Verified: ")
    data = data.replace(" media_count=", "Media Count: ")
    data = data.replace(" follower_count=", "Follower Count: ")
    data = data.replace(" following_count=", "Following Count: ")
    data = data.replace("FalseProfile", "False'Profile")
    data = data.replace(" HttpUrl('", " ")
    data = data.replace(", )", "'")
    data = data.replace("'P", "P")
    data = data.replace(" biography='", "Biography: ")
    data = data.replace(" external_url='", "External URL: ")
    data = data.replace(" account_type=", "Account Type: ")
    data = data.replace(" is_business=", "Is Business: ")
    data = data.replace(" public_email", "Public Email: ")
    data = data.replace(" contact_phone_number", "Contact Phone Number: ")
    data = data.replace(" public_phone_country_code", "Public Phone Country Code: ")
    data = data.replace(" public_phone_number", "Public Phone Number: ")
    data = data.replace(" business_contact_method= ", "Business Contact Method: ")
    data = data.replace(" business_category_name", "Business Category Name: ")
    data = data.replace(" category_name", "Category Name: ")
    data = data.replace(" category", "Category: ")
    data = data.replace(" address_street", "Address Street: ")
    data = data.replace(" city_id", "City ID: ")
    data = data.replace(" city_name", "City Name: ")
    data = data.replace(" latitude", "Latitude: ")
    data = data.replace(" longitude", "Longitude: ")
    data = data.replace(" zip", "Zip: ")
    data = data.replace(" instagram_location_id", "Instagram Location ID: ")
    data = data.replace(" interop_messaging_user_fbid", "Interop Messaging User FBID: ")
    data = data.replace("Is Private: False", "Is Private: False\n")
    data = data.replace("Is Verified: False", "Is Verified:\n")
    data = data.replace(" profile_pic_url=HttpUrl(", "True\nFollower")
    data = data.replace("Follower Count:", "\nFollower Count:")
    data = data.replace("Following Count:", "\nFollowing Count:")
    data = data.replace("Biography:", "\nBiography:")
    data = data.replace("Media Count:", "\nMedia Count: ")
    data = data.replace("'", '\n')
    data = data.replace("True", "True")
    data = data.replace("False", "False")
    data = data.replace("None", "No Data")
    data = data.replace("UNKNOWN", "No Data\n")
    data = data.replace("=No Data", "No Data\n")
    data = data.replace("=False", "False\n")
    data = data.replace("=True", "True\n")
    data = data.replace("=None", "No Data\n")
    data = data.replace("=UNKNOWN", "No Data\n")
    data = data.replace("True\nFollower", "")
    data = data.replace(" business_contact_method=", "Business Contact Method: ")
    return data