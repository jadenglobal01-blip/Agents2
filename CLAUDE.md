# 프로젝트 기억 사항

## 크리에이터 DB 추출 기준 (TikTok / Apify)

크리에이터를 찾을 때는 항상 아래 4단계로 진행한다.

1. **카테고리 + 협업 신호 해시태그를 함께 돌린다**
   - 카테고리 해시태그 5~8개 (예: `skincare`, `skincareroutine`, `skincarereview`, `skintok`, `glassskin` …)
   - 협업 신호 해시태그 3~5개 (예: `prpackage`, `prunboxing`, `prhaul`, `ugccreator`, `ugcbeauty`, `gifted` …)
   - Actor: `clockworks/tiktok-scraper` (해시태그당 50개)
   - `fyp`, `viral`, `foryou`, `trending` 같은 범용 태그와 피부 고민형 태그(`acne`, `undereyebags` 등)는 쓰지 않는다.
2. **바이오에 이메일이 있는 크리에이터만 남긴다**
3. **팔로워 5천~10만 명(나노·마이크로)으로 거른다**
4. **남은 크리에이터만 프로필 스크래핑**으로 최근 조회수·참여율을 확인한다
   - Actor: `clockworks/tiktok-profile-scraper` (최근 영상 4개, 고정글 제외)

기타
- 이미 수집한 크리에이터(`data/apify/*/creators.csv`)는 다시 스크래핑하지 않는다.
- 결과는 `data/apify/<날짜>/`에 저장하고 `scripts/apify_merge_tiktok.py`로 `creators.csv` / `videos.csv`를 만든다.
- Apify 예산: 월 $19 (Starter). 실행 전 예상 비용을 먼저 알려준다.
