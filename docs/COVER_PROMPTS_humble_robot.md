# 표지 지시문 모음 — 잘 못들었습니다... (겸손한 로봇 연구실 · Langcon 2026 발표 해설)
표지 10장(목차 1 + 장 9)을 Genspark 등 이미지 생성 도구에 그대로 붙여 넣는 지시문입니다. **목차 표지(00)를 먼저 받아** 그림체를 확인한 뒤, 나머지 요청에 그 그림을 참고 이미지로 함께 올립니다.
| 공통 | 내용 |
|---|---|
| 판 | L (16:9, 가로 1920 이상) → 빌드 1600×900 WebP |
| 저장 이름 | `img/cover_00.webp` ~ `img/cover_09.webp` (페이지가 이 이름을 자동으로 찾아 대체 표지 대신 보여 줌) |
| 참고 이미지 | 네 캐릭터 기본 그림 4장 (GitHub `adminmrobo/fruitfly-lab-expressions`) |
| 금지 | 글자·숫자·물음표·로고, 하얀 둥근 로봇(Money-Robo), 실존 제품 모양 그대로의 로봇 자동차 |
| 미공개 X1~X3 · 인턴 | 표지에는 넣지 않음 (본문에서만 등장) |

## 받은 뒤 처리
1. PNG/JPG를 1600×900 WebP(220KB 이하)로 바꿔 `img/cover_NN.webp`로 저장
2. 같은 그림을 3:2로 잘라 `img/thumb_NN.webp`(카탈로그 썸네일), 1200×630으로 잘라 `img/og_NN.webp`
3. `cover_manifest.json`의 해당 항목 `status`를 `ok`로

---

## cover_00 · 목차 · 잘 못들었습니다...

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_00 · L (16:9) |
| 장소 | 연구실 바닥에 깔린 장난감 도로 트랙 |
| 주제 은유 | 장난감 도로 위에서 멈춰 선 작은 로봇 자동차가 빈 말풍선(되묻기)을 띄움 |
| 네 캐릭터 포즈 | 박사 standing at the back center, one hand presenting the little car / 조수 kneeling beside the road, holding a clipboard, smiling / 초파리 on the left facing right, pointing at the stopped car with curiosity / 주판봇 on the right facing left, abacus raised, eager for the car to go |
| 대체 글 (alt) | 네 캐릭터가 장난감 도로 앞에 멈춰 선 작은 로봇 자동차와 그 위의 빈 말풍선을 바라보는 낮의 연구실 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 그림 안에 글자·숫자·물음표·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Scene: a bright lab with a long toy road track laid across the floor, a small sign stand next to the road holding a blank sign.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, standing at the back center, one hand presenting the little car;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, kneeling beside the road, holding a clipboard, smiling;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, pointing at the stopped car with curiosity;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, abacus raised, eager for the car to go.
Visual metaphor of the topic: a small generic unbranded four-wheel robot car with a tiny camera on a short mast stopped at the start line, a glowing blank speech bubble floating above it (asking again).
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple; the light falls on the small robot car and its blank speech bubble.
Mood: curious, friendly rivalry, the moment before the result. Daytime lab: big windows, natural light, white walls, lavender, mint and pink props.
No text, no letters, no numbers, no question marks, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands or real products.```

**고칠 때 (같은 대화에서):** `Same four characters, same art style and composition. Change only: {고칠 점}. Still no text.`

---

## cover_01 · 1장 · 왜 겸손한 로봇인가

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_01 · L (16:9) |
| 장소 | 두 갈래 장난감 도로 |
| 주제 은유 | 왼쪽 차는 벽 쪽으로 돌진하고, 오른쪽 차는 멈춰서 빈 말풍선을 띄움 (맹목적 실행 vs 되묻기) |
| 네 캐릭터 포즈 | 박사 behind the table in the center, arms open as if presenting two choices / 조수 at the right lane side, pressing a big soft pause button / 초파리 on the left facing right, worriedly pointing at the rushing car / 주판봇 on the right facing left, cheering for the rushing car with the abacus |
| 대체 글 (alt) | 두 갈래 장난감 도로에서 한 차는 벽으로 돌진하고 다른 차는 멈춰 되묻는 장면 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 그림 안에 글자·숫자·물음표·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Scene: two parallel toy road lanes on a lab table, the left lane ends at a soft foam wall, the right lane has a small stop line.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, behind the table in the center, arms open as if presenting two choices;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, at the right lane side, pressing a big soft pause button;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, worriedly pointing at the rushing car;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, cheering for the rushing car with the abacus.
Visual metaphor of the topic: two identical small generic robot cars: the left one rushing toward the foam wall with motion lines, the right one calmly stopped at the stop line with a glowing blank speech bubble.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple; the light falls on the two lanes and the blank speech bubble.
Mood: curious, friendly rivalry, the moment before the result. Daytime lab: big windows, natural light, white walls, lavender, mint and pink props.
No text, no letters, no numbers, no question marks, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands or real products.```

**고칠 때 (같은 대화에서):** `Same four characters, same art style and composition. Change only: {고칠 점}. Still no text.`

---

## cover_02 · 2장 · 과정 01 · 텍스트 지능

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_02 · L (16:9) |
| 장소 | 연구실 책상 위 카드 분류대 |
| 주제 은유 | 글자 대신 낙서 같은 무늬가 그려진 쪽지 카드들이 초록 바구니(받아 줌)와 빨간 바구니(막음)로 나뉨, 한쪽엔 두꺼운 사전, 한쪽엔 돋보기 |
| 네 캐릭터 포즈 | 박사 at the back center, holding a card up to the light / 조수 sorting cards into the green tray, focused / 초파리 on the left facing right, inspecting a card through the magnifying glass / 주판봇 on the right facing left, stacking a tall pile of cards proudly |
| 대체 글 (alt) | 글자 없는 쪽지 카드를 초록·빨간 바구니로 나누는 네 캐릭터와 사전·돋보기 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 그림 안에 글자·숫자·물음표·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Scene: a sorting desk covered with small paper cards showing abstract squiggles instead of letters, one green tray and one red tray, a thick closed dictionary book and a big magnifying glass.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center, holding a card up to the light;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, sorting cards into the green tray, focused;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, inspecting a card through the magnifying glass;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, stacking a tall pile of cards proudly.
Visual metaphor of the topic: paper cards drifting into a green tray and a red tray, the thick book glowing softly (sharpshooter) and the magnifying glass glowing (detective).
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple; the light falls on the green and red trays.
Mood: curious, friendly rivalry, the moment before the result. Daytime lab: big windows, natural light, white walls, lavender, mint and pink props.
No text, no letters, no numbers, no question marks, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands or real products.```

**고칠 때 (같은 대화에서):** `Same four characters, same art style and composition. Change only: {고칠 점}. Still no text.`

---

## cover_03 · 3장 · 과정 02 · 이미지 지능

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_03 · L (16:9) |
| 장소 | 타일 벽이 있는 작업대 |
| 주제 은유 | 검은 작은 타일마다 흰 획이 서로 다른 굵기·기울기로 그려져 있고, 큰 픽셀 격자 돋보기가 한 타일을 확대함 |
| 네 캐릭터 포즈 | 박사 at the back center, pointing at the wall of tiles / 조수 holding the pixel-grid magnifier up to one tile / 초파리 on the left facing right, comparing two tiles side by side / 주판봇 on the right facing left, carrying a tall stack of new tiles |
| 대체 글 (alt) | 서로 다른 획의 검은 타일 벽과 그중 하나를 픽셀 격자로 확대한 돋보기 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 그림 안에 글자·숫자·물음표·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Scene: a wall of small black tiles, each with white abstract brush strokes in different thickness, slant and style (no real letters), a work table below.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center, pointing at the wall of tiles;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, holding the pixel-grid magnifier up to one tile;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, comparing two tiles side by side;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, carrying a tall stack of new tiles.
Visual metaphor of the topic: a big pixel-grid magnifier enlarging one tile into visible square pixels.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple; the light falls on the enlarged pixel grid.
Mood: curious, friendly rivalry, the moment before the result. Daytime lab: big windows, natural light, white walls, lavender, mint and pink props.
No text, no letters, no numbers, no question marks, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands or real products.```

**고칠 때 (같은 대화에서):** `Same four characters, same art style and composition. Change only: {고칠 점}. Still no text.`

---

## cover_04 · 4장 · 과정 03 · 카메라 지능

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_04 · L (16:9) |
| 장소 | 창가의 카메라 시험대 |
| 주제 은유 | 김 서린 렌즈 너머로 흐릿한 표지판, 렌즈 닦는 천, 초록·노랑·빨강 세 구간이 칠해진 둥근 계기판 |
| 네 캐릭터 포즈 | 박사 at the back center, tapping the gauge dial thoughtfully / 조수 wiping the lens with a soft cloth / 초파리 on the left facing right, squinting at the blurry sign / 주판봇 on the right facing left, holding up a big stack of blurry photo cards |
| 대체 글 (alt) | 김 서린 카메라 렌즈와 세 구간 계기판 앞의 네 캐릭터 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 그림 안에 글자·숫자·물음표·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Scene: a camera test stand by a big window, a camera with a foggy smudged lens pointed at a blurry blank sign, a round gauge dial with green, amber and red zones.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center, tapping the gauge dial thoughtfully;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, wiping the lens with a soft cloth;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, squinting at the blurry sign;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, holding up a big stack of blurry photo cards.
Visual metaphor of the topic: the smudged lens with a soft cleaning cloth and the three-zone gauge dial (no numbers).
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple; the light falls on the smudged lens and the gauge dial.
Mood: curious, friendly rivalry, the moment before the result. Daytime lab: big windows, natural light, white walls, lavender, mint and pink props.
No text, no letters, no numbers, no question marks, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands or real products.```

**고칠 때 (같은 대화에서):** `Same four characters, same art style and composition. Change only: {고칠 점}. Still no text.`

---

## cover_05 · 5장 · 과정 04 · 음성 지능

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_05 · L (16:9) |
| 장소 | 방음 패널이 있는 녹음 코너 |
| 주제 은유 | 마이크와 헤드폰, 큰 화면에 보라·주황으로 빛나는 스펙트로그램 같은 줄무늬와 물결 파형 (숫자 없음) |
| 네 캐릭터 포즈 | 박사 at the back center, conducting the sound waves with one hand / 조수 wearing headphones, listening carefully with eyes closed / 초파리 on the left facing right, leaning in to the microphone / 주판봇 on the right facing left, turning a big knob on a mixer |
| 대체 글 (alt) | 마이크에서 나온 소리 물결이 화면의 빛나는 줄무늬 그림으로 바뀌는 녹음 코너 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 그림 안에 글자·숫자·물음표·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Scene: a cozy recording corner with soft sound-absorbing panels, a studio microphone, headphones, a large screen showing a glowing purple and orange heat-stripe pattern and a wavy line (no numbers, no axis labels).
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center, conducting the sound waves with one hand;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, wearing headphones, listening carefully with eyes closed;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, leaning in to the microphone;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, turning a big knob on a mixer.
Visual metaphor of the topic: sound waves flowing from the microphone into the glowing stripe pattern on the screen.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple; the light falls on the glowing stripe pattern on the screen.
Mood: curious, friendly rivalry, the moment before the result. Daytime lab: big windows, natural light, white walls, lavender, mint and pink props.
No text, no letters, no numbers, no question marks, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands or real products.```

**고칠 때 (같은 대화에서):** `Same four characters, same art style and composition. Change only: {고칠 점}. Still no text.`

---

## cover_06 · 6장 · 보상으로 겸손을 가르치다

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_06 · L (16:9) |
| 장소 | 실내 훈련장 트랙 |
| 주제 은유 | 작은 시험용 로봇(이름 없는, 관절이 보이는 단순한 로봇)이 넘어졌다 일어나며 달리고, 옆에 색 막대만 있는 점수판과 작은 트로피 |
| 네 캐릭터 포즈 | 박사 at the back center, holding a stopwatch-like device without numbers / 조수 standing by the scoreboard, adjusting a colored bar / 초파리 on the left facing right, watching the test robot closely with crossed arms / 주판봇 on the right facing left, polishing the trophy cup with excitement |
| 대체 글 (alt) | 넘어진 흔적을 뒤로하고 달리는 작은 시험용 로봇과 색 막대 점수판이 있는 훈련장 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 그림 안에 글자·숫자·물음표·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Scene: an indoor training track inside the lab with soft mats, a scoreboard showing only colored bars (green, amber, red, no numbers), a small trophy cup on a stand.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center, holding a stopwatch-like device without numbers;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, standing by the scoreboard, adjusting a colored bar;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, watching the test robot closely with crossed arms;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, polishing the trophy cup with excitement.
Visual metaphor of the topic: a small simple jointed test robot (not the abacus robot) mid-stride, with a faint ghost trail of earlier stumbles behind it.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple; the light falls on the running test robot and the colored scoreboard.
Mood: curious, friendly rivalry, the moment before the result. Daytime lab: big windows, natural light, white walls, lavender, mint and pink props.
No text, no letters, no numbers, no question marks, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands or real products.```

**고칠 때 (같은 대화에서):** `Same four characters, same art style and composition. Change only: {고칠 점}. Still no text.`

---

## cover_07 · 7장 · 가상에서 실물로

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_07 · L (16:9) |
| 장소 | 큰 모니터와 탁상 도로 |
| 주제 은유 | 모니터 속 가상 도로의 작은 차와 탁자 위 실물 도로의 같은 차가 빛줄기로 이어짐 (디지털 트윈) |
| 네 캐릭터 포즈 | 박사 at the back center, pointing from the monitor to the table / 조수 holding a small remote board and checking the real car / 초파리 on the left facing right, crouching to look at the real car's camera / 주판봇 on the right facing left, pointing excitedly at the monitor car |
| 대체 글 (alt) | 모니터 속 가상 자동차와 탁자 위 실물 자동차가 빛줄기로 이어진 디지털 트윈 장면 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 그림 안에 글자·숫자·물음표·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Scene: a large wall monitor showing a simple virtual road, and in front of it a real tabletop road made of tape and cardboard.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center, pointing from the monitor to the table;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, holding a small remote board and checking the real car;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, crouching to look at the real car's camera;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, pointing excitedly at the monitor car.
Visual metaphor of the topic: two copies of a small generic unbranded four-wheel robot car with a tiny camera on a short mast: one on the monitor's virtual road, one on the tabletop road, connected by a soft beam of light.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple; the light falls on the beam linking the virtual car and the real car.
Mood: curious, friendly rivalry, the moment before the result. Daytime lab: big windows, natural light, white walls, lavender, mint and pink props.
No text, no letters, no numbers, no question marks, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands or real products.```

**고칠 때 (같은 대화에서):** `Same four characters, same art style and composition. Change only: {고칠 점}. Still no text.`

---

## cover_08 · 8장 · 맺음 · 부록

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_08 · L (16:9) |
| 장소 | 연구실 큰 창 앞의 정리 테이블 |
| 주제 은유 | 벽에 숫자 없는 여덟 칸 색 블록 일정표, 테이블 위 두루마리 네 개(부록 코드)와 작은 로봇 자동차, 따뜻한 오후 햇살 |
| 네 캐릭터 포즈 | 박사 at the back center, raising a teacup in a small toast / 조수 tying a ribbon around the four scrolls / 초파리 on the left facing right, giving a small nod and a thumbs-up / 주판봇 on the right facing left, gently patting the small robot car |
| 대체 글 (alt) | 여덟 칸 일정표와 부록 두루마리 네 개를 정리하는 마지막 장면 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 그림 안에 글자·숫자·물음표·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Scene: a wrap-up table in front of a big sunny window, a wall timeline made of eight colored blocks with no numbers, four rolled scrolls on the table and the small robot car resting.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center, raising a teacup in a small toast;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, tying a ribbon around the four scrolls;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, giving a small nod and a thumbs-up;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, gently patting the small robot car.
Visual metaphor of the topic: the eight-block wall timeline and four rolled scrolls.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple; the light falls on the four scrolls and the small robot car.
Mood: curious, friendly rivalry, the moment before the result. Daytime lab: big windows, natural light, white walls, lavender, mint and pink props.
No text, no letters, no numbers, no question marks, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands or real products.```

**고칠 때 (같은 대화에서):** `Same four characters, same art style and composition. Change only: {고칠 점}. Still no text.`

---

## cover_09 · 9장 · 직접 해 보기 · 3D 가상 주자 실습 가이드

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_09 · L (16:9) |
| 장소 | 연구실 안의 밝은 실내 트랙과 큰 모니터 |
| 주제 은유 | 격자 바닥 위를 달리는 흰 관절 인형(마네킹) 주자, 그 뒤로 넘어진 채 겹쳐 보이는 반투명 잔상 셋(학습 초반), 숫자 없는 오르는 곡선이 그려진 큰 모니터 |
| 네 캐릭터 포즈 | 박사 at the back center, holding a stopwatch up / 조수 next to the monitor, pointing at the rising curve / 초파리 on the left facing right, crouching to look at the fallen ghost images with a magnifier / 주판봇 on the right facing left, cheering the runner with the abacus raised |
| 대체 글 (alt) | 넘어지던 흔적을 뒤로하고 격자 트랙을 달리는 흰 관절 인형 주자와 그것을 지켜보는 네 캐릭터 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 그림 안에 글자·숫자·물음표·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Scene: a bright indoor test track with a light blue grid floor inside the lab; a plain white jointed mannequin runner (simple capsule limbs, round head, no face details) running mid-stride; behind it three faint translucent ghost images of the same mannequin fallen and stumbling; a large monitor on the wall showing a smooth rising curve with no numbers.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center, holding a stopwatch up;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, next to the monitor, pointing at the rising curve;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, crouching to look at the fallen ghost images with a magnifier;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, cheering the runner with the abacus raised.
Visual metaphor of the topic: learning by falling — the fallen ghosts behind, the running mannequin ahead.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple; the light falls on the running mannequin.
Mood: curious, friendly rivalry, the moment before the result. Daytime lab: big windows, natural light, white walls, lavender, mint and pink props.
No text, no letters, no numbers, no question marks, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands or real products.```

**고칠 때 (같은 대화에서):** `Same four characters, same art style and composition. Change only: {고칠 점}. Still no text.`
