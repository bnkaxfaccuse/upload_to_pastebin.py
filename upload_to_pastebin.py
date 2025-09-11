import requests

def upload_to_pastebin(api_dev_key, file_path, paste_name="Pastebin Upload", paste_private=0, paste_expire_date="N"):
    """
    Uploads a text file to pastebin.com using their API.

    Args:
        api_dev_key (str): Your Pastebin API developer key.
        file_path (str): Path to the text file to upload.
        paste_name (str): Name/title of the paste.
        paste_private (int): 0=public, 1=unlisted, 2=private.
        paste_expire_date (str): Expiry date (N = Never, 10M = 10 minutes, 1H = 1 hour, 1D = 1 day, 1W = 1 week, 2W = 2 weeks, 1M = 1 month, 6M = 6 months, 1Y = 1 year).

    Returns:
        str: URL of the new paste or error message.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        paste_code = f.read()

    url = "https://pastebin.com/api/api_post.php"
    data = {
        'api_dev_key': api_dev_key,
        'api_option': 'paste',
        'api_paste_code': paste_code,
        'api_paste_name': paste_name,
        'api_paste_private': paste_private,
        'api_paste_expire_date': paste_expire_date
    }

    response = requests.post(url, data=data)
    return response.text

if __name__ == "__main__":
    # Replace with your actual Pastebin API developer key:
    API_DEV_KEY = "PASTEBIN_API_KEY"
    FILE_PATH = "example.txt"  # Replace with your file path

    paste_url = upload_to_pastebin(API_DEV_KEY, FILE_PATH)
    print("Pastebin response:", paste_url)
