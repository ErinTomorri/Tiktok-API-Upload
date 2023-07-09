import datetime
import time
from googleapiclient.http import MediaFileUpload
import pandas as pd
from google_apis import create_service
import requests
import os
from __init__ import main
def uTube(title, des, file):
    def video_categories():
        video_categories = service.videoCategories().list(part='snippet', regionCode='US').execute()
        df = pd.DataFrame(video_categories.get('items'))
        return pd.concat([df['id'], df['snippet'].apply(pd.Series)[['title']]], axis=1)

    API_NAME = 'youtube'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/youtube']
    # SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
    client_file = 'client-secret.json'
    service = create_service(client_file, API_NAME, API_VERSION, SCOPES)

    print(video_categories())

    """
    Step 1. Uplaod Video
    """
    upload_time = (datetime.datetime.now() + datetime.timedelta(days=10)).isoformat() + '.000Z'
    request_body = {
        'snippet': {
            'title': title,
            'description': des,
            'categoryId': '42',
            'tags': ['memerap', 'squidwardrap', 'mrkrabsrap', 'planktonrap', 'spongebob']
        },
        'status': {
            'privacyStatus': 'public',
            'publishedAt': upload_time,
            'selfDeclaredMadeForKids': False
        },
        'notifySubscribers': False
    }

    video_file = file
    media_file = MediaFileUpload(video_file)
    # print(media_file.size() / pow(1024, 2), 'mb')
    # print(media_file.to_json())
    # print(media_file.mimetype())

    response_video_upload = service.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=media_file
    ).execute()
    uploaded_video_id = response_video_upload.get('id')


    """
    Step 2. Update video thumbnail
    """
    response_thumbnail_upload = service.thumbnails().set(
        videoId=uploaded_video_id,
        media_body=MediaFileUpload('thumbnail.png')
    ).execute()

    """
    Step 3 (optional). Set video privacy status to "Public"
    """
    video_id = uploaded_video_id

    counter = 0
    response_update_video = service.videos().list(id=video_id, part='status').execute()
    update_video_body = response_update_video['items'][0]

    while 10 > counter:
        if update_video_body['status']['uploadStatus'] == 'processed':
            update_video_body['status']['privacyStatus'] = 'public'
            service.videos().update(
                part='status',
                body=update_video_body
            ).execute()
            print('Video {0} privacy status is updated to "{1}"'.format(update_video_body['id'], update_video_body['status']['privacyStatus']))
            break
        # adjust the duration based on your video size
        time.sleep(10)
        response_update_video = service.videos().list(id=video_id, part='status').execute()
        update_video_body = response_update_video['items'][0]
        counter += 1
def Tiktok(title,fileName):
    main(title,fileName)
def main2():
    temp = input("Youtube or Tiktok or Both: ")
    num = input("Number: ")
    title = input("Title (add #short if utube): ")
    des = input("Description: ")
    while temp.lower()!= "tiktok" and temp.lower()!="youtube" and temp.lower() != "both":
        temp = input("Youtube or Tiktok or Both: ")
    
    fileName = "FinalVideos/output"+num+".mp4"
    if temp.lower() == "tiktok":
        Tiktok(title,fileName)
    elif temp.lower() == "youtube":
        uTube(title,des,fileName)
    elif temp.lower() == "both":
        Tiktok(title,fileName)
        uTube(title,des,fileName)

    os.remove(fileName)
main2()
