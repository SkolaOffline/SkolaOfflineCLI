import requests
import token_handler

def main():
    response = requests.get(
        'https://aplikace.skolaonline.cz/solapi/api/v1/user',
        headers={
            'Authorization': f'Bearer {token_handler.get_token_from_file()}'
        }
    )

    print(response.json())



if __name__ == '__main__':
    main()