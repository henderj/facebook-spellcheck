from facebook import GraphAPI

# curl -i -X GET \
# "https://graph.facebook.com/v12.0/112473910504378/published_posts?access_token=EAAOuXm96IjABANZCLDNfZCtGZAtE1i49SocacmM1iPwVa0ndBGe9ee3XSBYvhgLBxohFfEwKE4g3JfDEc3dCpN7AkiTMtz0ppV837vZBBaGjXvL3UPKSUnTCZASGBUZAru5tKnjoieCKlpZAGVASjjrZCBPGoHdd07UDG2l0OHxDuHwRtK7B2yZAd3qLel3DfuLRhRMZAsXaxvmYJdtP0xxes60M7HpHDq0ygZD"

accessToken = "EAAOuXm96IjABANZCLDNfZCtGZAtE1i49SocacmM1iPwVa0ndBGe9ee3XSBYvhgLBxohFfEwKE4g3JfDEc3dCpN7AkiTMtz0ppV837vZBBaGjXvL3UPKSUnTCZASGBUZAru5tKnjoieCKlpZAGVASjjrZCBPGoHdd07UDG2l0OHxDuHwRtK7B2yZAd3qLel3DfuLRhRMZAsXaxvmYJdtP0xxes60M7HpHDq0ygZD"

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount


def main_facebook_business():
    my_app_id = "{app-id}"
    my_app_secret = "{appsecret}"
    my_access_token = accessToken
    FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
    my_account = AdAccount("act_{{adaccount-id}}")
    campaigns = my_account.get_campaigns()
    print(campaigns)


def main_facebook_sdk():
    graph = GraphAPI(access_token=accessToken, version=12)


def main():
    main_facebook_sdk()


if __name__ == "__main__":
    main()
