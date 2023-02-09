import pytube

link ="https://youtu.be/CXoHh5l9DdE"

yt =pytube.YouTube(link)
stream = yt.streams.first()

print(stream.download())