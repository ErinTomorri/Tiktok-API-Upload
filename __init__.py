from uploader import uploadVideo
def main(titles, files):
    session_id = "19b196d7afa2f0eb5fb5f669a3cc7214"
    file = files
    title = titles
    tags = ["memerap", "squidwardrap", "mrkrabsrap", "planktonrap", "spongebob"]
    users = ["theogsharkslides"]
    proxy = {'http': 'http://ip:port', 'https': 'https://ip:port'}

    # Publish the video
    uploadVideo(session_id, file, title, tags, users, proxy=None)