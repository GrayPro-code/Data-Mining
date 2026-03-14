import requests
# Создание вызова API и сохранение ответа.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
# Сохранение ответа API в переменной.
response_dict = r.json()
# Обработка результатов.
print(f"Total repositories: {response_dict['total_count']}")

# Анализ информации о репозиториях.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")
print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")










#import requests
#
## URL для поиска репозиториев
#url = "https://api.github.com/search/repositories"
#
## Параметры запроса
#params = {
#    "q": "language:python",  # Язык: Python
#    "sort": "stars",  # Сортировка по звездам
#    "order": "desc",  # В порядке убывания
#    "per_page": 10  # Количество результатов на странице (макс. 100)
#}
#
## Отправка запроса
#response = requests.get(url, params=params)
#
#if response.status_code == 200:
#    data = response.json()
#    print(f"Всего найдено репозиториев: {data['total_count']}\n")
#
#    for repo in data['items']:
#        print(f"Название: {repo['full_name']}")
#        print(f"Звезды: {repo['stargazers_count']}")
#        print(f"Ссылка: {repo['html_url']}")
#        print("-" * 30)
#else:
#    print(f"Ошибка: {response.status_code}")
