import pandas as pd
import numpy as np
from vitaldb import VitalFile

# 트랙명 정의
track_names = ['Solar8000/HR', 'Solar8000/BT', 'Solar8000/PLETH_SPO2','Solar8000/ART_SBP','Solar8000/RR']

# vital 파일 로드
vf = VitalFile("0012.vital")

# 1초 간격으로 numpy array로 추출
tracks = vf.to_numpy(track_names, interval=0.5)

# DataFrame으로 변환
df = pd.DataFrame(tracks, columns=track_names)

# 시간축 추가
df['time_sec'] = np.arange(len(df))

# CSV로 저장
df.to_csv("vital_sample12_0.5.csv", index=False)

print("✅ 저장 완료: vital_sample.csv")

# track = vf.find_track('Solar8000/HR')

# timestamps = track.times

# intervals = np.diff(timestamps)
# print("시간 간격(초): ", intervals[:10])
# print(f"평균 간격: {np.mean(intervals):.2f}초")
# print(f"최소/최대 간격: {np.min(intervals):.2f} ~ {np.max(intervals):.2f}초")