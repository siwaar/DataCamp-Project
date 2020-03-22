import requests

def download_file_from_gdrive(id, destination):
    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value

        return None

    def save_response_content(response, destination):
        CHUNK_SIZE = 32768

        with open(destination, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)

    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    


if __name__ == "__main__":
    import sys
    if len(sys.argv) is not 1:
        print("Usage: python download_data.py")
    else:
        # TAKE ID FROM SHAREABLE LINK
        file_id = '1jHVkvRu-G37tBuE6IFp-y0gi7d3hUm7E'
        # DESTINATION FILE ON YOUR DISK
        destination = './data.zip'
        download_file_from_gdrive(file_id, destination)