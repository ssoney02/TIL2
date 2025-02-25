## font-size 적용 안됨

브라우저 자체에서 heading 태그에 기본 stylesheet을 적용하는 경우가 있음 <br>
container에 font-size를 정해주면 상속에 의해 font-size가 h2 태그에 적용되는데  
상속보다 브라우저에서 정해주는 font-size가 우선될 수도 있음   
~~이 문제가 아닐 수도..~~ 아닌듯!
~~갑자기 됨..~~

## 해결
live server 사용함..  
잘 반영됨..
---
## bottom:0;으로 지정했는데 아래 공백 생기는 문제

font-size 줄였더니 괜찮아짐  
**font-size를 크게 설정했을 때, 그에 비례하여 line-height가 기본 값으로 설정돼서 생기는 문제**
line-height: ; 값 적당히 설정해주면 조절됨  
- 0으로 설정해줬더니 의도한 대로 됐음
