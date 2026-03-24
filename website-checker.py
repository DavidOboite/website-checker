import sys
from ssl import SSLError

import requests
if __name__ == '__main__':
    try:
        print(f'Reading URLs from {sys.argv[1]!r}')

        with open(sys.argv[1], 'r') as f:
            for possible_url in f:
                try:
                    possible_url = possible_url.strip()
                    r  = requests.get(possible_url)
                    if r.status_code !=  200:
                        print(f'{possible_url!r} Responded, but resource not available')
                except SSLError:
                    print(f'{possible_url!r} SSL error')
                except ConnectionError:
                    print(f'{possible_url!r} Connection error')
                except:
                    print(f'Something unexpected happened with {possible_url!r}.')
    except IndexError:
        print('Missing URL')
    except  FileNotFoundError:
        print(f'Cannot open {sys.argv[1]!r}')

