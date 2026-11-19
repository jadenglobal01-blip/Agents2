# TikTok 크리에이터 스크래핑 (2026-11-18, Apify)

K-뷰티 / 아이패치 관련 크리에이터 발굴용 데이터. 세션 기록이 남지 않아 Apify 실행 기록에서 복원함.

## 파이프라인
1. **해시태그 검색** (`clockworks/tiktok-scraper`, 태그당 50개)
   - run `5z5yzRflh00d2Cy2D`: undereyepatches, kbeauty, koreanskincare
   - run `nCzM9Ds3Xl1gARQBj`: eyepatches, undereyemask, hydrogelpatches, undereyebags, kbeautyfinds, yesstyle, oliveyoung, yesstylefinds
   - run `NU2yMH3IiwvDUcOw7`: undereyepatch, eyemasks, undereyecare, kbeautyhaul, yesstylehaul, oliveyoungfinds
2. **이메일 있는 크리에이터만 프로필 스크래핑** (`clockworks/tiktok-profile-scraper`, 최근 영상 4개, 고정글 제외)
   - runs `huogeJgeQ9ltatxuj`, `D99n38320uQzjvgNL`, `542hNx4mx61ZwRe9c`

## 파일
- `creators.csv` — 크리에이터 DB(중복 제거): 팔로워, 이메일(바이오 추출), 최근 영상 조회수 중앙값, 평균 참여율 등
- `videos.csv` — 전체 영상 2,034건
- `raw_*.json` — 데이터셋별 원본(주요 필드만)

## 현황
- 크리에이터 600명 / 바이오에 이메일 있는 크리에이터 425명
- 프로필 스크래핑 완료 281명
- **남은 작업: 이메일은 있지만 프로필 스크래핑 안 된 144명**
