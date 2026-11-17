# 이미지 명세서 — 겸손한 로봇 연구실

## 1. 그림 전체 목록

| 구분 | 키 / 파일 | 어디에 | 상태 |
|---|---|---|---|
| 새로 그릴 것 | `img/cover_00.webp` ~ `img/cover_08.webp` (9장) | 각 페이지 맨 위 표지 | 생성 대기 · 지금은 대체 표지(도로·표지판 그림)가 보임 |
| 표지에서 자를 것 | `img/thumb_00~08.webp` (3:2), `img/og_00~08.webp` (1200×630) | 카탈로그 썸네일, 공유 미리보기 | 표지를 받은 뒤 |
| (선택) 새로 그릴 것 | `img/sc_06_runner_strip.webp` | 6-1 달리는 시험용 로봇 | 지금은 코드로 그림. 받으면 교체 가능 |
| 캐릭터 팩 재사용 | 박사·조수·초파리·주판봇·시아·모아·X1~X3 표정 36종 (96px) | 말풍선·등장인물·대결 | 반영 완료 (`fruitfly-lab-expressions` @ 86d04ac) |
| 실제 데이터 | `assets/font/` 6장, `assets/spoil_weak/` 8장, `assets/spoil_strong/` 7장 | 3·4장 | 반영 완료 |
| 실제 데이터 | `assets/audio/` 10개 (1번 음파 생성 4 · 2번 육성 2 · 3번 변환 4) | 5장 | 반영 완료 |
| 화면 장면 | `assets/voice_converter.png` | 5-2 | 영상 한 장면을 잘라 냄 |
| 영상 | `media/sim_rl.mp4`, `media/sim_hybrid.mp4` (+ 포스터 jpg) | 7-2 | 시뮬레이터 부분만 잘라 냄 (바탕화면·브라우저 탭·옛 하얀 로봇 아바타 제외) |

## 2. 표지 지시문

`docs/COVER_PROMPTS_humble_robot.md` (9장, Genspark에 그대로 붙여 넣기). 목차 표지(00)부터 받아 그림체를 확인합니다.

## 3. (선택) 6-1 시험용 로봇 동작 시트

지금 6-1의 로봇은 캔버스 코드로 그립니다. 픽셀아트 시트를 받으면 같은 자리에 넣을 수 있습니다. 연구실 식구가 아닌 **이름 없는 시험용 로봇**입니다.

**Genspark에 붙여 넣기 ↓**
```
16:9 가로 동작 시트 1장을 만들어 줘. 4열 × 2행, 칸마다 같은 캐릭터의 다른 동작. 회색 단색 배경, 글자·숫자·효과선 없음.
아래 영어 프롬프트를 그대로 써 줘.

Sprite motion sheet, 16:9, 4 columns x 2 rows of equal cells, plain flat gray background, no text, no numbers, no effect lines.
IMPORTANT: the character faces RIGHT in every cell.
16-bit RPG style pixel art, bold dark outline, 2-3 tone shading.
Character: a small simple jointed test robot, beige box torso with a blue chest stripe, small box head with a dark green visor and two mint pixel eyes, a short antenna with an amber bead, gray segmented legs and arms, black feet. Not the abacus robot, no treads, no white round head, no yellow eyes.
Row 1 (learning, clumsy): 1 wobbling with arms flailing, 2 tripping forward, 3 lying flat on the floor, 4 pushing itself back up.
Row 2 (learned, running): 5 jogging stride left leg forward, 6 jogging stride right leg forward, 7 full running stride with lean, 8 confident sprint with arms swinging.
Same size and same foot line in every cell.
```

## 4. 일관성

- 하얀 둥근 로봇(Money-Robo)은 어떤 그림에도 넣지 않습니다.
- 표지에 미공개 X1~X3과 인턴은 넣지 않습니다. 본문 말풍선·명령 카드에만 나옵니다.
- 실물 Pi Car X는 실제 제품 모양 대신 "이름 없는 작은 네 바퀴 로봇 자동차"로 그립니다.
