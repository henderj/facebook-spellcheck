from facebook import GraphAPI
import pprint
from secrets import accessToken

def main_facebook_sdk():
    graph = GraphAPI(access_token=accessToken, version=2.12)
    posts = graph.request("112473910504378_430111732073926?fields=message")
    pprint.pprint(posts)
    print("".join(posts["message"]))


def main():
    main_facebook_sdk()


if __name__ == "__main__":
    main()
