# private alarm bot.

## discord 봇 만들기 연습방법 및 설치방법.

-   [여기](https://velog.io/@dombe/%EB%AC%B8%EC%A0%9C-%ED%95%B4%EA%B2%B0-%EA%B7%B8%EB%A6%AC%EA%B3%A0-%EA%B8%B0%EB%B3%B8%EC%A0%81%EC%9D%B8-Discord-bot-%EB%A7%8C%EB%93%A4%EA%B8%B0)를 참고해주세요!(설치방법은 기본 코드 실행하기의 8번에 있습니다. 현재 배포는 하지 않았습니다.)

## 기능

(하위 제목은 접미사.)

#### >ping

    예시로부터 가져왔고 지우기는 싫어서 넣어놨습니다.
    - 사용시 'pong' 메시지와 함께 봇의 latancy 정보를 전달해줍니다.

#### >사용자정보

    사용자의 정보가 출력이 됨.
    출력되는 정보 : 사용자이름, #{네 자리 숫자} 및 사용자 아이디(임의의 숫자).

### 알람 전체

-   쓸 수 있는 시간은 다음과 같은 양식입니다. ㅁdㄴhㅇmㄹ : 차례대로 ㅁ일 ㄴ시간 ㅇ분 ㄹ초.
    -   주의1(예시), 시간을 적을 때 1d2d3d4d로 적을 시 10일이 input으로 들어가게 됩니다.
    -   날짜,시간,분의 순서가 바껴도 작동합니다.

#### >알람

    기본 알람.

    일반화된 양식 : >알람 {얼마 후 알려줄지에 대한 시간} {(만약 있다면 원하는 메세지)}

#### >반복알람

    반복적으로 알람이 필요할 때 사용하도록 만들었습니다.

    일반화된 양식 : >반복알람 {얼마 후 시작할 지에 대한 시작시간} {반복 단위시간} {반복 횟수} {출력 메시지}

    - example : >반복알람 1d6h17 1d 5 dc bot, 만들어졌을까?
    - 결과 : 시작 메시지가 출력.
        1일 6시간 17초 후, 반복알람이 시작되었다는 안내메시지가 나오고,
        이후 1일 단위로 5번동안 'dc bot, 만들어졌을까?' 메시지가 출력,
        마지막 알람이 끝난 직후 종료.

    - 주의2 작성양식과 다른 형식으로 적었을 때는 다른 결과가 없이 '잘못된 사용법입니다.' 가 출력됩니다.
    - 주의3 두 개의 시간이 너무 긴 경우 경고 메시지와 함께 주의2의 메시지가 출력됩니다.(60일을 maximum으로 설정해뒀습니다.)
    - tag는 @everyone tag만 작동하게 넣어주었습니다.
