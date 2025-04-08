# Day 1: 과제

Downward API 를 사용하여 pod 생성
1-2 flask 사용하는 python 을 생성한다. downwardApi 에서 POD_NAME, NODE_NAME, POD_NAMESPACE 가져 와야함 (app.py)
1-3 Dockerfile 화일 생성 ( 기존 베이스 이미지에 curl 모듈 추가 )
1.4 Github Action 으로 github 에 이미지 push ( multi platform 지원 )
1.5 downward_api.yaml 에 생성한 도커 이미지로 default namespace에 배포
1.6 결과물
jakelee@jake-MacBookAir ~ % kubectl exec -it downward-env -- curl localhost:5000

Container EDU | POD Working : downward-env | nodename : lima-rancher-desktop | namespace : default
