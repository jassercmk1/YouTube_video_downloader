from pytube import YouTube
from pytube.exceptions import RegexMatchError

DOWNLOAD_FOLDER = 'C:/Users/jasse/OneDrive/Documents/YouTube_Vids'

def youtube_downloader(link: str):
    try:
        youtube_video = YouTube(link)
        highest_resolution_stream = youtube_video.streams.get_highest_resolution()
        highest_resolution_stream.download(DOWNLOAD_FOLDER)
        return 'Download complete!'
    except RegexMatchError:
        return 'Invalid video link!'
    except Exception as e:
        return f'Error: {str(e)}'
  
if __name__ == "__main__":
    prompt = input('Enter a video link to download: ')
    print('Downloading video...')
    result = youtube_downloader(prompt)
    print(result)
