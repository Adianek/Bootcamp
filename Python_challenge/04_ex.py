import requests

# print(resp.text)
# resp = requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345")
# print(resp)

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}"
nothing = "8022"
i = 0
while True:
    i += 1
    x_url = url.format(nothing)
    resp = requests.get(x_url)
    print(i, x_url)
    try:
        nothing = int(resp.text.split()[-1])
    except ValueError:
        print(resp.text)
        break
