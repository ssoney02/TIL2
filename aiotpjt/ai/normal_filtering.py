# 정상 데이터 필터링 (학습용)
# 메타데이터 라벨링, 시계열화

# 1. MetaData
# 2. TimeSeriesData 리스트의
    #  SeqNum, TimeStamp, EM_Sensor, SM_Sensor, Total_Labeling 데이터 가져오기

    # TimeSeriesData[i][’Total_Labeling’][’Estimation’] not in [‘주의’, ‘위험’] 인 것만 필터링


import os
import json

input_folder = 'C:/Users/SSAFY/Desktop/VL_A.신규수집'
output_folder = 'C:/Users/SSAFY/Desktop/filtered_valid'
os.makedirs(output_folder, exist_ok=True)

# L_A0003 ~ L_A0030 반복
# for i in range(3, 31):
prefix = "L"
matched_files = [f for f in os.listdir(input_folder)
                    if f.startswith(prefix) and f.endswith('.json')]

for file_name in matched_files:
    input_path = os.path.join(input_folder, file_name)
    output_path = os.path.join(output_folder, f"filtered_{file_name}")
    
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 메타 데이터
        meta_data = data.get('MetaData', {})
        gender_str = meta_data.get('Gender')
        # 성별 -> 라벨링
        # 남자: 0, 여자 : 1
        gender_label = 0 if gender_str == 'M' else 1 if gender_str == 'F' else None
        
        # 기저질환 유무 라벨링
        # 질환 있음 : 0, 질환 없음: 1
        disease_str = meta_data.get('DiseaseYN')
        disease_label = 0 if disease_str == 'Y' else 1 if disease_str == 'N' else None

        age = meta_data.get('Age')

        # filtered_meta = {
        #     'Age': meta_data.get('Age'),
        #     'Gender': gender_label,
            
        # }

        # 시계열 데이터 필터링
        time_series = data.get('TimeSeriesData', [])
        filtered_series = []

        for entry in time_series:
            estimation = entry.get('Total_Labeling', {}).get('Estimation')
            if estimation not in ['주의', '위험']:
                em = entry.get('EM_Sensor', {})
                sm = entry.get('SM_Sensor', {})

                filtered_entry = {
                    # 타임스탬프
                    'TimeStamp': entry.get('TimeStamp'),
                    # 메타데이터 -> 시계열에 끼워넣음
                    'Age': age,
                    'Gender': gender_label,
                    'DiseaseYN': disease_label,
                    # 환경 
                    'EM_Sensor': {
                        'Temperature': em.get('Temperature'),
                        'Humidity': em.get('Humidity'),
                        'Illuminance': em.get('Illuminance'),
                        'TVOC': em.get('TVOC')
                    },
                    # 바이탈
                    'SM_Sensor': {
                        'HeartRate': sm.get('HeartRate'),
                        'SPO2': sm.get('SPO2'),
                        'SkinTemperature': sm.get('SkinTemperature'),   
                        'WalkingSteps': sm.get('WalkingSteps')          
                    }
                }
                filtered_series.append(filtered_entry)

        

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(filtered_series, f, ensure_ascii=False, indent=2)

        print(f"[✓] {file_name} → 저장 완료 ({len(filtered_series)}건)")

    except Exception as e:
        print(f"[✗] {file_name} 처리 중 오류 발생: {e}")

