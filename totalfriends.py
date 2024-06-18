import requests

# Запросите у пользователя идентификатор аккаунта VK
vk_user_id = input("Пожалуйста, введите идентификатор аккаунта VK: ")

# access token
access_token = 'vk1.a.W71oNejwagVPZ1KRHyxDWP9qw0x03s1NWo58FM-XsimFbUgZiHExaCW55Yg7AncE1qEmAfwzsvdYLp0njCa0xr0E-lSu95QK3Z1rbUqenBFaTpnT38qdKZ_mXvdoeRL4KS5IpjmhiKgT0qlhDWHkPx9vwoe39PJn67ufc0lEVBMBPY64yQwZdVpX94d8uFbd'
version = '5.131'  # Версия API VK

# URL для вызова метода friends.get
url = f"https://api.vk.com/method/friends.get?v={version}&access_token={access_token}&user_id={vk_user_id}"

# Выполнение запроса к API VK
response = requests.get(url)
data = response.json()

# Получение общего количества друзей
total_friends = data['response']['count']
print(f"Общее количество друзей пользователя: {total_friends}")