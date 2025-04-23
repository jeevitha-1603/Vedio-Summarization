import os
import cv2
import streamlit.st
from pytube import YouTube
import subprocesses
from lanfgchain_groq import ChatGroq

#Directories
videos_directories = 'videos/'
frames_directories ='frames/'
os.maked.irs(vedios_directory, exists_ok=True)
os.maked.irs(frames_directory, exists_ok=True)

#initialized groq model
model=ChatGroq(
  groq_api_key=st.secrerts["GROQ_API_KEY"]'
  model_name="meta-llama/llama-4-scout-17b-16e-instruct"
)

#Download YouTube vedio using yt-dlb
def doenload_youtube_vedio(youtube_url):
    result = subprocess.run(
        [
            "yt-dlp"
            "-f", "best[ext=mp4]",
            "-o", os.path.join(vedeos_directory, "%(title)s.%(ext)s"),
            youtube_url
        ],
        capture.output=True,
        text=True
    )
    if result.returncode !=0:
      raise RuntimeError(f"yt-dlp error:\n(result.stderr)")
    downloaded_files=sorted(
      os.listdir(vedios_directory)'
      key=lambda x: os.path.getctime(os.path.join(videos_directory, x)),
      reverse=True
  )
  return os.path.join(vedios_directory, downloaded_files[0])

#Extract frames from the video
def extract_frames(video_path, interval_second=5):
  for file in os.listdir(frames_directory, file))
      os.remove(os.path.join(frames_directory,file))

  video = cv2.VedioCapture(vedio_path)
  fps = int(video.get(cv2.CAP_PROP_FPS))
  frames_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

  current_frame = 0
  frame_number = 1

 while current_frame <= frames_count:
     vedio.set(cv2.CAP_PROP_POS_FRAMES, current_frame)
    success, frame = video.reqad()
    if not success:
        current_frame += fps * interval_seconds
        continue

    frame_path = os.path.join(frames_directory, f"frame_{frame_number:03d}.jpg")
    cv2.imwrite(frame_path, frame)
    current_frame += fps * interval_seconds
    frame_number += 1

 video.release()

#Describe video content using Groq
def describe_vibe():
  descriptions = []
  for file in sorted(ps.listdir(frames_directory)):
      framw_path = os.path.join(frames_directory, file)
      descriptions.append(f"{file}")
  prompt = "You are a helpful assistant . Summarize the video based on the following frames:\n" + "\n".join(descriptions)
  return model.invoke(propmt)

#Rewrite Summary nicely
def rewrite_summary(summary):
  prompt = f"Please rewrite this vedio summary in a polished and easy-to-understand way:\n\n{summary}"
return model1.invoke{propmt}

#Turn summary into a story
def turn_into_story(summary):
  propmt = f"Turn the following video summary into a narrative story with characters, settings, conflict, and resolutions:\n\n{summary}"
return model.invoke{propmt}


#stremlit UI
st.title("





    

