# Agents2 — marketing agent

`marketing`이라는 이름의 Claude Code 서브에이전트를 담고 있는 프로젝트입니다.

## 구조

```
.claude/
  agents/
    marketing.md              # 에이전트 정의 (frontmatter + 시스템 프롬프트)
    marketing/
      references/
        copywriting.md        # 헤드라인 공식, CTA 가이드, 페이지 구조
        content-strategy.md   # Searchable/Shareable, 콘텐츠 필러, 키워드 리서치, ORB 배포
        cold-email.md         # 개인화 레벨, 이메일 구조, 후속 시퀀스, 체크리스트
        cro.md                 # 7단계 CRO 진단 프레임워크, 폼 최적화
outputs/
  <작업유형>/YYYY-MM-DD-<slug>.md   # 에이전트가 만든 산출물 (작업 시 자동 생성)
```

## 에이전트가 할 수 있는 것

1. **카피라이팅** — 홈페이지/랜딩페이지/가격 페이지/기능 페이지 카피
2. **콘텐츠 전략** — 콘텐츠 필러, 토픽 클러스터, 편집 캘린더
3. **콜드 이메일** — B2B 아웃바운드 시퀀스와 후속 이메일
4. **CRO** — 페이지/폼 전환율 분석과 개선 권고
5. **기타 마케팅 작업** — SNS 문구, 광고 카피, 포지셔닝/메시징 등

## 사용 방법

Claude Code에서 `marketing` 서브에이전트를 호출해 원하는 마케팅 작업을 요청하면 됩니다.
(예: "이 랜딩페이지 헤드라인 3개 후보 써줘", "다음 분기 콘텐츠 캘린더 짜줘")

프로젝트에 `.claude/product-marketing.md` 파일을 만들어 ICP, 포지셔닝, 톤앤보이스 등
공통 컨텍스트를 미리 적어두면, 매 요청마다 같은 정보를 반복 설명하지 않아도 됩니다.

## 참고

`marketing.md`와 `references/*.md`의 프레임워크는
[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)의
`cold-email`, `copywriting`, `content-strategy`, `cro` 스킬에서 다루는 개념 구조를 참고해
독자적으로 새로 작성한 것입니다(원문 그대로 복사한 것이 아닙니다).
