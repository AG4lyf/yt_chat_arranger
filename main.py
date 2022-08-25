from chat_downloader import ChatDownloader
import scrapetube


channel_id = 'UCIzzPhdRf8Olo3WjiexcZSw'
#channel_id = str(input("Enter Channel ID"))


videos = scrapetube.get_channel(channel_id)

for video in videos:
    id = video['videoId']
    print(f"Looking at video id - {video['videoId']}")
    chat = ChatDownloader().get_chat(video['videoId'])
    
    with open(f'chats_storage/{id}.txt', "w+") as f:
        for message in chat:
            try:
                f.write(f"{message['timestamp']} | {message['time_in_seconds']} | {message['time_text']} | {message['author']['name']} | {message['message']}\n")
            except Exception as e:
                print(e)
