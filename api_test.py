# import json

# with open("api_test.json") as in_file:
#     json_news = json.load(in_file)
# print(json_news)

from requests import get, post

all_news = get('http://localhost:5000/api/v2/news').json()
print(all_news)
for news_ in all_news['news']:
    print(news_)
    if 'Newest' in news_['title']:
        news_from_api = get(f'http://localhost:5000/api/v2/news/{news_["id"]}').json()
        print('--', news_from_api)

# print(post('http://localhost:5000/api/v2/news',
#            json={'title': 'The Newest News',
#                  'content': 'Very interesting text!!!',
#                  'user_id': 1,
#                  'i
#                  s_private': False}).json())