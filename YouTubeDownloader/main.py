from pytube import YouTube

url = input("Please enter the URL: ")
path = input("Please enter the location you want to download: ")

yt = YouTube(url)
stream = yt.streams.get_highest_resolution()
print(f"Downloading: {yt.title}")
stream.download(path)
print("Download completed!")