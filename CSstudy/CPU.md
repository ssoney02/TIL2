# CPU

## 레지스터

: CPU 안에 있는 임시 저장장치

→ 프로그램을 이루는 데이터, 명렁어가 프로그램의 실행 전후로 레지스터에 저장됨

### 레지스터 종류

- 프로그램 카운터
    
    (= 명령어 포인터)
    
    : 메모리에서 다음으로 읽어 들일 명령어의 주소
    
    → 일반적으로 1씩 증가함 = 다음으로 읽어 들일 메모리 주소가 1씩 증가함
    
    ⇒ 메모리에 저장된 프로그램이 순차적으로 실행되는 이유
    
    (근본적으로 프로그램 카운터 값이 1씩 증가하며 실행되기 떄문!)
    
    - 프로그램 실행 흐름이 순차적이지 않은 경우
        
        프로그램 카운터 값이 임의의 위치로 변경됨
        
- 명령어 레지스터
    
    해석할 명령어(방금 읽어들인 명령어)를 저장하는 레지스터
    
    → 다른 cpu 내의 제어장치가 명렁어 레지스터 내의 명렁어를 해석한 뒤 ALU(산술논리연산자)가 연산하도록 시키거나 다른 부품으로 제어 신호 보냄
    
- 범용 레지스터
    
    데이터, 명령어, 주소 모두 저장 가능
    
    - 보통 CPU안에 범용 레지스터가 여러 개 들어있음
- 플래그 레지스터
    
    : 플래그 값(연산 결과 혹은 CPU 상태에 대한 부가 정보)을 저장하는 레지스터
    
    - 플래그: cpu가 명령어를 처리하는 과정에서 반드시 참조해야 할 상태 정보
    
    ![image.png](attachment:6563615f-98bd-41e1-b300-8911b023fa6f:image.png)
    
- 스택 포인터
    
    메모리 → 실행 중인 프로그램들 적재됨
    
    - 실행 중인 각 프로그램 → 스택과 같은 형태로 사용가능한 주소 공간을 하나 이상 가짐
    - 스택 영역: 스택처럼 사용하자고 약속된 메모리 영역
    - 스택 포인터: 메모리 내 스택 영역의 최상단 스택 데이터 위치를 가리키는 특별한 레지스터를 말함
    
    ⇒ 마지막으로 스택에 저장된 데이터의 위치를 가리키는 레지스터
    
    ⇒ 스택이 채워진 정도를 나타내는 레지스터
    

## 인터럽트

: CPU의 작업을 방해하는 신호

### 1. 동기 인터럽트

: CPU에 의해 발생하는 인터럽트

ex. 프로그래밍 오류와 같은 예외적인 상황을 마주쳤을 때 발생하는 인터럽트

⇒ ‘ 예외’라고도 부름

### 2. 비동기 인터럽트

: 주로 입출력장치에 의해  발생하는 인터럽트

- 알림의 역할을 함
    - ~~입출력 장치 → cpu???~~
    - cpu → 입출력 장치에 입출력 작업 요청. 작업을 끝낸 입출력장치가 cpu에 완료 알림(인터럽트)를 보냄
    - 입출력 장치가 입력을 받았을 때 이를 처리 하기 위해 cpu에 입력 알림(인터럽트) 보냄

### 3. 하드웨어 인터럽트???

→ 대부분의 하드웨어 인터럽트는 비동기 인터럽트(외부에 의해 발생하는 인터럽트)에 포함됨

그렇다고 완전 동일한 것은 아님..

- 알림과 같은 인터럽트..
- CPU가 효율적으로 명령어를 처리하기 위해 하드웨어 인터럽트를 사용함
    - **“폴링”**: 작업 완료 여부를 주기적으로 확인하는 것(입춝력 장치의 상태, 처리할 데이터 유무)
    - 입출력장치와 CPU의 작업처리 속도가 다름 → 알림을 보내주지 않으면 CPU에서 작업이 끝났는지 계속 확인해야됨(비효율적..)

- CPU가 하드웨어 인터럽트를 처리하는 순서
    1. 입출력 장치→ CPU에 인터럽트 요청 신호 보냄
    2. CPU: 실행 사이클 끝나고 명령어 인출 전에 인터럽트 여부 확인
    3. CPU: 인터럽트 요청 확인, 인터럽트 플래그로 현재 인터럽트를 받아들일 수 있는지 여부 확인
    4. 인터럽트 받아들일 수 있으면 CPU가 지금까지의 작업을 백업
    5. CPU: 인터럽트 벡터를 참조하여 인터럽트 서비스 루틴 실행
    6. 인터럽트 서비스 루틴 실행이 끝나면 4번에서 백업해둔 작업을 복구하여 실행 재개
- 인터럽트 관련 용어
    - **인터럽트 요청 신호**: 인터럽트가 CPU의 정상적인 진행 흐름을 방해하기 때문에 인터럽트 전에 CPU에게 인터럽트 가능 여부를 확인해야됨. 이를 위한 신호
    - **인터럽트 플래그**: 하드웨어 인터럽트를 받아들일지, 무시할지를 결정하는 플래그
        - but, 인터럽트 플래그가 불가능으로 설정되어있어도 무시할 수 없는 인터럽트 요청도 o
            - 막을 수 있는 인터럽트
            - 막을 수 없는 인터럽트(NMI) → 정전, 하드웨어 고장으로 인한 인터럽트 (가장 우선순위가 높은 인터럽트)
    - **인터럽트 서비스 루틴(= 인터럽트 핸들러)**: 인터럽트를 처리하기 위한 프로그램
        
        → 인터럽트가 발생했을 때, 해당 인터럽트를 어떻게 처리하고 작동해야 할 지에 대한 정보
        
        “cpu가 인터럽트를 처리한다” = “인터럽트 서비스 루틴을 실행하고, 본래 수행하던 작업으로 다시 되돌아온다”