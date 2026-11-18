# 잘 못들었습니다... 불완전한 텍스트 명령을 극복하는 로봇의 강화학습 및 베이지안 추론

> 겸손한 로봇 연구실 · [Langcon 2026 — From Text to Action](https://songys.github.io/2026Langcon/) 발표 해설 (2026-02-28 오후 세션 3, [발표 일정](https://songys.github.io/2026Langcon/schedule.html))

불완전한 명령(오타 · 흐린 글자 · 웅얼거림)을 받은 로봇이 억지로 움직이지 않고, 확신이 낮으면 되묻도록 만든 프로젝트를 비전공 독자용 인터랙티브 해설 9장(중챕터 36개)으로 풀었습니다. 박사 · 조수 하루 · 초파리 연구원 · 주판봇이 진행하고, 인턴 시아 · 모아와 미공개 식구 X1~X3이 함께 나옵니다.

- 사이트: https://adminmrobo.github.io/Reinforcement-Learning-lab_project_01/
- 분류: www.ahnboat.xyz 카탈로그 › **Articles & Presentations** › **학술대회 발표** › AI·로봇
- 저장소: https://github.com/adminmrobo/Reinforcement-Learning-lab_project_01
- 함께 보기: [머신러닝 모델 도감](https://adminmrobo.github.io/machine_learning_model_atlas/) · [신경망 구조 도감](https://adminmrobo.github.io/neural_network_atlas/0_neural_network_essence.html) (6-0에서 강화학습과 비교)
- 원자료: 안상선, 「불완전한 명령 보완을 위한 강화학습 모델링 적용 방안」, Langcon 2026 발표 자료 (2026-02-28판)

글 · 안상선 (www.ahnboat.xyz) · (주)M-Robo 대표

## 목차

| 장 | 파일 | 중챕터 |
|---|---|---|
| 목차 | `index.html` | 3줄 요약 · 등장인물 · 큰 그림 · 목차 |
| 1 왜 겸손한 로봇인가 | `ch1_why.html` | 위험 세 가지 · 하이브리드 전략 · Pi Car X 구조 · 3단계 파이프라인 |
| 2 과정 01 텍스트 지능 | `ch2_text.html` | 데이터 만들기 · 의미 거리와 임계값 0.40 · 사전 + AI 하이브리드 · 정확도 99%의 허상(배신도) |
| 3 과정 02 이미지 지능 | `ch3_image.html` | 글자를 그림으로 · 폰트 데이터셋 · 분류 모델 성적표 |
| 4 과정 03 카메라 지능 | `ch4_camera.html` | 약한·심한 오염 · 혼합 학습과 하락 곡선 · 베이지안 90·70 정책 |
| 5 과정 04 음성 지능 | `ch5_voice.html` | 파형과 스펙트로그램 · 데이터셋 1~3번 · 성적표(48.0%) · 세 감각 융합 |
| 6 보상으로 겸손을 가르치다 | `ch6_rl.html` | 강화학습은 무엇이 다른가(머신러닝·신경망 도감과 비교) · 강화학습 기본(달리는 로봇) · 보상표 두 벌 · 천하제일 지능대회 · 임계값 3D 지도 · 역발상 검증 |
| 7 가상에서 실물로 | `ch7_sim2real.html` | 네 등급 · PyGame 시뮬레이터 · Pi Car X Sim-to-Real · 데이터 흐름 |
| 8 맺음 · 부록 | `ch8_appendix.html` | 쓰임새와 8주 로드맵 · 부록 코드 네 개 · 기술 스택과 재현성 |
| 9 직접 해 보기 · 3D 가상 주자 | `ch9_general.html` | 실습 가이드: 무엇을 학습시키나 · 준비 · 학습 · 영상과 대시보드 · 보상 바꿔 보기 (소스코드 `code/ch9_humanoid/`, 그림·영상은 예상 화면) |

## 폴더

```
index.html, ch1~ch8 *.html   해설 페이지 (외부 라이브러리 없음, 글꼴만 외부)
assets/                      데이터 예시 그림·음성, 음성 변환기 화면
media/                       시뮬레이터 영상 2편 (화면 일부만 잘라 냄), 9장 예상 화면 그림·영상(연구실이 그린 그림), 실습 짧은 실행 결과 + 포스터
img/                         표지 그림 자리 (cover_00~09.webp를 넣으면 대체 표지 대신 보임)
kg/{페이지}/                 지식 색인 원본 kg.json · refs.json · meta.json · check_report.md
docs/                        표지 지시문(Genspark용) · 이미지 명세서
cover_manifest.json          표지·온톨로지 현황 (ahnboat_lab_cover_status가 매일 수집)
KG_new_ids.json              시리즈 등록부에 더할 새 개념 ID
code/                        실제 구현 코드 정리본 (노트북 6개, .py 2개, requirements.txt, data/ CSV 5개), ch9_humanoid/ 9장 실습 코드 4개
```

> **code/ 알림** 원본 노트북에 있던 Google API 키는 정리본에서 모두 지웠습니다. 실행하려면 자기 키를 환경 변수 `GOOGLE_API_KEY`로 넣으세요.

## 숫자 표시 원칙

발표 표·그림에서 옮긴 값은 "발표 자료 값", 이 페이지가 만든 실험 값은 "설명용"으로 따로 표시했습니다. 발표 12쪽 요약 그래프(RandomForest 우승 표시)와 최종평가 표(평균 보상 1위 Logistic 0.4)가 다른 점은 6-3에 적었습니다.

코드 실행 기록에서 옮긴 값은 "실제 코드 기준"·"코드 실행"으로 표시했습니다. 발표 그래프(CNN)와 업로드된 코드(MLP)는 모델이 달라 4-2에 따로 그렸고, 시뮬레이터의 등급 경계(실행 0.40 · 등급 85%/60%)와 부정문 실행 사례는 7-1·7-2에 있습니다.

## 저작권

캐릭터 이름·설정·그림의 저작권은 안상선에게 있으며 허락 없이 쓸 수 없습니다.
