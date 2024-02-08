import requests
import hashlib

def compare_suffixes(tail, data_stream):
    hash_count_pair = (line.split(':') for line in data_stream.splitlines())
    for hashed_pw, count in hash_count_pair:
        if tail == hashed_pw:
            return "This password was hacked " + count + " times. Please change this password."
    return "This password is good. It has never been hacked."

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        return "Error fetching data"
    else:
        return res

def encrypt_password(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1password[:5], sha1password[5:]
    result = request_api_data(prefix)
    if result == "Error fetching data":
        print(result)
    else:
        print(compare_suffixes(suffix, result.text))

encrypt_password('snowball')