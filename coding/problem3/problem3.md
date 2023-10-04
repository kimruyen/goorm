## 문제
OT때 성공적으로 인싸가 된 민수는 앞으로 펼쳐질 핑크빛 대학생활을 기대하며 콧
노래를 흥얼거립니다.  

하지만 기쁨도 잠시. 개강한 지 얼마나 됐다고 교수님이 과제를 마구 내시는 겁니
다! 민수는 매일 과제를 하느라 친구들과 놀 시간이 없습니다. 내가 이러려고 대학
에 왔나 생각을 하며 민수는 오늘도 과제를 합니다. 참다 못한 민수는 자신만의 과
제 수행 규칙을 정했습니다. 과제는 주어진 날짜와 마감 날짜가 존재합니다. 어떤
과제를 수행하던 도중 새로운 과제가 생기면 기존에 하던 과제는 잠시 미뤄두고,
새로운 과제를 수행하기 시작합니다. 그러다가 새로운 과제가 끝나면, 기존의 과제
를 마저 수행합니다. 새로운 과제를 수행하던 도중 기존 과제의 마감날짜를 넘겨버
리면 그 과제는 그대로 버립니다.  

민수는 생각하던 중, 이렇게 과제를 처리한다고 했을 때 과연 주어진 모든 과제를
해낼 수 있을지 아니면 못하는 과제가 생길지 궁금해졌습니다. 하지만 민수는 당장
눈 앞의 과제를 처리하느라 이를 생각할 시간이 없습니다. 민수를 위해 N개의 과제
와 각 과제의 시작날짜, 마감날짜가 주어질 때 모든 과제를 성공적으로 마칠 수 있
을지 없을지 판별하는 프로그램을 작성해주세요.

## 입력
첫째 줄에 과제의 개수 N이 주어집니다. (단, N은 10^5보다 작은 자연수) 둘째 줄부터 N
줄에 걸쳐 각 과제의 시작날짜, 마감날짜가 MM/DD 형식으로 주어집니다. 불가능한 날
짜는 입력으로 주어지지 않으며, 시작날짜보다 마감날짜가 항상 늦고 시작날짜가 겹치는
경우는 마감날짜가 더 느린 과제를 먼저 선택합니다.   

