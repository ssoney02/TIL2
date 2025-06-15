### Q1
- value_counts(): Series를 반환!!! 
1. 빈도 수 기준으로 채널 정렬(value_counts) -> series반환
2. channelId가 series에 포함되는지 확인 -> .isin()사용
3. .isin()사용을 위해서는 리스트 같은 값들과 비교하므로 series 자체가 아닌 index만 넘겨야됨 (.index 사용 필수!!!)
4. 포함되는 애들의 채널이름 반환

### Q2
