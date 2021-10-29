import requests


def test_get(url_to_test):
    response = requests.get(f"http://{url_to_test}/whatismyname")
    actual = response.text
    f=open('names.txt','r')

    expected =f.read()
    f.close()
    print(expected)
    assert expected != actual


def test_post(url_to_test):
    response = requests.post(f"http://{url_to_test}/whatismyname?a={input('argvs')}")
    actual = response.text
    expected = "added"
    assert expected == actual


# test_get("localhost:5001")
test_post("localhost:5001")