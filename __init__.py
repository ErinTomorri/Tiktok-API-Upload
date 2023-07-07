from uploader import uploadVideo
def main(titles, files):
    session_id = "6f5103dc398878c486f17dd2b14774f4"
    file = files
    title = titles
    tags = ["memerap", "squidwardrap", "mrkrabsrap", "planktonrap", "spongebob"]
    users = ["theogsharkslides"]
    proxy = {'http': 'http://ip:port', 'https': 'https://ip:port'}

    # Publish the video
    uploadVideo(session_id, file, title, tags, users, proxy=None)