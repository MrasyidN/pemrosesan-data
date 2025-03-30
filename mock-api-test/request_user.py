import requests

def get_user_data(user_id):
    url = f"https://example.com/users/{user_id}"
    response = requests.get(url)


    # jika status vcode bukan 200, return none
    if response.status_code != 200:
        return None
    
    # return data jika request berhasil
    return response.json()

