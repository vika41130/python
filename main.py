import requests
from io import BytesIO

# base_url = 'https://www.w3schools.com'
# response = requests.get(base_url)
# print(response.status_code)
# print(response.headers)
# print(response.json())
# print(response.url)
# print(response.content)
# i = Image.open(BytesIO(response.content))
# print(i)

# save image
# base_url = 'https://www.w3schools.com/html/pic_trulli.jpg'
# response = requests.get(base_url)
# print(response.headers)
# bytes_io = BytesIO(response.content)
# with open('assets/save/image.jpg', 'wb') as f:
#     f.write(bytes_io.getbuffer())

# save video
base_url = 'https://www.w3schools.com/html/mov_bbb.mp4'
response = requests.get(base_url)
# print(response.status_code)
# print(response.headers['content-type'])
# # print(response.content)
# with open('assets/save/video.mp4', 'wb') as f:
#     f.write(BytesIO(response.content).getbuffer())

