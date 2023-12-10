# import pandas as pd
import cv2
# import time
# from datetime import datetime

# データを格納する変数を初期化
start_frame = None
motion_track_list = [None, None]
# motion_time = []
# data_frame = pd.DataFrame(columns=["Start", "End"])

video_path = 'video/sample1.mp4'
video = cv2.VideoCapture(video_path)

while True:
  capture_success, current_frame = video.read()

  # フレーム画像をカラーから白黒に変換する
  gray_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
  gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

  # 初期フレームを設定する
  if start_frame is None:
    start_frame = gray_frame
    continue

  # 初期フレームと現在のフレームの差分を取得する
  differ_frame = cv2.absdiff(start_frame, gray_frame)

  # 差分画像を二値化する
  thresh_frame = cv2.threshold(differ_frame, 30, 255, cv2.THRESH_BINARY)[1]
  thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)
  
  cv2.imshow("threshhold frame", thresh_frame)
  cv2.waitKey(1)

  # 2値化した画像から輪郭を取得する
  contours, _ = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

















