from facebook import GraphAPI
import pprint
from secrets import accessToken

# curl -i -X GET \
# "https://graph.facebook.com/v12.0/112473910504378/published_posts?access_token=EAAOuXm96IjABANZCLDNfZCtGZAtE1i49SocacmM1iPwVa0ndBGe9ee3XSBYvhgLBxohFfEwKE4g3JfDEc3dCpN7AkiTMtz0ppV837vZBBaGjXvL3UPKSUnTCZASGBUZAru5tKnjoieCKlpZAGVASjjrZCBPGoHdd07UDG2l0OHxDuHwRtK7B2yZAd3qLel3DfuLRhRMZAsXaxvmYJdtP0xxes60M7HpHDq0ygZD"



def main_facebook_sdk():
    graph = GraphAPI(access_token=accessToken, version=2.12)
    posts = graph.request("112473910504378_430111732073926?fields=message")
    pprint.pprint(posts)
    print("".join(posts["message"]))


def main():
    main_facebook_sdk()


if __name__ == "__main__":
    main()
