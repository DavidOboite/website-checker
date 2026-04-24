import sys
import requests
from requests.exceptions import SSLError, ConnectionError, Timeout, RequestException

if __name__ == '__main__':
    try:
        print(f'Reading URLs from {sys.argv[1]!r}')

        with open(sys.argv[1], 'r') as f:
            for possible_url in f:
                try:
                    possible_url = possible_url.strip()
                    r = requests.get(possible_url, timeout=5)

                    if r.status_code != 200:
                        print(f'{possible_url!r} responded, but resource not available ({r.status_code})')

                except SSLError:
                    print(f'{possible_url!r} SSL error')

                except ConnectionError:
                    print(f'{possible_url!r} connection error')

                except Timeout:
                    print(f'{possible_url!r} timeout')

                except RequestException as e:
                    print(f'{possible_url!r} request error: {e}')

    except IndexError:
        print('Missing URL file argument')

    except FileNotFoundError:
        print(f'Cannot open {sys.argv[1]!r}')