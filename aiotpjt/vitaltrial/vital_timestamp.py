from vitaldb import VitalFile
import numpy as np

# .vital 파일 로드
vf = VitalFile("0012.vital")

# 트랙 선택
track = vf.find_track('Solar8000/HR')
# print(dir(track))
# 시간-값 쌍 추출
# time_value_pairs = track.GetTimeValuePairs()

# # 시간만 추출
# timestamps = [tv[0] for tv in time_value_pairs]
# intervals = np.diff(timestamps)

# # 결과 출력
# print("앞 10개 간격:", intervals[:10])
# print(f"평균 간격: {np.mean(intervals):.2f}초")
# print(f"최소/최대 간격: {np.min(intervals):.2f} ~ {np.max(intervals):.2f}초")
# 시간-값 쌍
recs = track.recs

# 시간만 추출
# print(recs)
times = [rec['dt'] for rec in recs]

# 간격 계산
intervals = np.diff(times)

# 결과 출력
print("앞 10개 간격:", intervals[:10])
print(f"평균 간격: {np.mean(intervals):.2f}초")
print(f"최소/최대 간격: {np.min(intervals):.2f} ~ {np.max(intervals):.2f}초")