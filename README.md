# Pastebin Uploader

This Python script allows you to upload a text file to [Pastebin](https://pastebin.com/) using their API.

## Features

- Uploads any text file to Pastebin
- Lets you specify paste name, privacy, and expiration
- Simple and easy-to-use

## Prerequisites

- Python 3.x
- `requests` library (`pip install requests`)
- A [Pastebin API Developer Key](https://pastebin.com/doc_api)

## Usage

1. **Clone or download this repository.**
2. **Edit the script:**
    - Open `upload_to_pastebin.py`
    - Replace `PASTEBIN_API_KEY` with your own Pastebin API dev key.
    - Set the `FILE_PATH` variable to the path of the text file you want to upload.

3. **Run the script:**
    ```bash
    python upload_to_pastebin.py
    ```

4. **Check the output:**  
   The script will print a Pastebin URL if successful, or an error message otherwise.

## Example

```bash
python upload_to_pastebin.py
# Output:
# Pastebin response: https://pastebin.com/AbCdEf12
```

## Notes

- By default, the paste is **public** and does not expire. You can change privacy and expiry in the script.
- For more advanced usage (like uploading as a logged-in user), see the [Pastebin API docs](https://pastebin.com/doc_api).

## License

MIT License
