import requests

webhook_url = 'https://discord.com/api/webhooks/1453754026897444965/3HsR5ezDqtKAmG2wUO0iaHBmfEu4DVOb8R7Qdr6UAO-TiGM-eT81Ykl5pNH0QvD1AIHm'

data = {
    'content': 'Merhaba!'
}

response = requests.post(webhook_url, json=data)

if response.status_code == 204:
    print("Mesaj başarıyla gönderildi.")
else:
    print(f"Mesaj gönderilemedi, hata kodu: {response.status_code}")
