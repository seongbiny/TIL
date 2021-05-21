# MVC

Model : 어플리케이션의 기능 표현, 변경을 view에 통지

View :  모델을 화면에 시각적으로 표현, 모델에게 업데이트 요청, 사용자의 입력을 컨트롤러에 전달

Controller : 어플리케이션의 행위 정의, 사용자 액션을 모델 업데이트와 mapping, 응답에 대한 view 선택



1. model은 controller와 view에 의존하지 않아야 한다.

   (Model 내부에 controller와 view에 관련된 코드가 있으면 안된다.)

2. view는 model에만 의존해야 하고, controller에는 의존하면 안된다.

   (View 내부에 model의 코드만 있을 수 있고, controller의 코드가 있으면 안된다.)

3. view가 model로 부터 데이터를 받을 때는, 사용자마다 다르게 보여주어야 하는 데이터에 대해서만 받아야 한다.

4. Controller 는 model과 view에 의존해도 된다.

   (controller 내부에는 model과 view의 코드가 있을 수 있다.)

5. view가 model로부터 데이터를 받을 때, 반드시 controller에서 받아야 한다.