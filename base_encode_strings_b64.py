import base64

def do_encode_string(a):
    try:
        encoded_string = base64.b64encode(a.encode('utf-8')).decode('utf-8')
        print("Base64 Encoded:", encoded_string)
    except ValueError:
        print("Invalid input, enter strings")

while True:
    user_input = input("Enter value: ")
    if isinstance(user_input, str):
        do_encode_string(user_input)
    else:
        print("Invalid input, enter strings")
