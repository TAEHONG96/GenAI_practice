# 🛠️ TAEHONG96's Utility Suite: Stock, Lotto & Video Tools

본 저장소는 실생활에 유용한 3가지 주요 도구(주식 현황판, 로또 생성기, 유튜브 다운로더)를 포함하고 있는 통합 유틸리티 프로젝트입니다. 모든 도구는 최신 기술 스택과 사용자 중심의 UI/UX를 지향합니다.

---

## 1. 📈 MarketBoard: 통합 주식 & ETF 실시간 대시보드
**[market_board.html]**

**MarketBoard**는 국내/해외 주식 및 글로벌 지수를 한눈에 모니터링할 수 있는 고성능 반응형 웹 대시보드입니다. 2026년 코스피 6,000선 시대를 배경으로 한 미래 지향적 투자 환경을 반영합니다.

### 🌟 주요 기능
- **2026-04-24 실시간 데이터**: KOSPI(6,483), 삼성전자(219,250원) 등 최신 시장가 반영.
- **인터랙티브 차트**: `ApexCharts` 엔진을 사용하여 부드러운 주가 변동 애니메이션 제공.
- **Watchlist**: 삼성전자, SK하이닉스, NVIDIA, Apple 등 국내외 주요 종목 통합 관리.
- **Deep Dark Mode**: 장시간 모니터링 시 눈의 피로를 최소화하는 전문가용 다크 테마.

---

## 🍀 2. LuckyPick: 행운의 로또 번호 생성기
**[lotto_generator.html]**

PRD(제품 요구사항 정의서)를 바탕으로 제작된 **LuckyPick**은 단순 랜덤 생성을 넘어 사용자의 전략적 선택을 지원하는 로또 번호 관리 도구입니다.

### 🌟 주요 기능
- **조건부 번호 생성**: 고정수(최대 5개) 및 제외수 설정을 통한 맞춤형 조합 추출.
- **로또 용지 UI**: 번호 대역별 색상(노랑, 파랑 등)이 적용된 직관적인 디자인.
- **내 번호함 (Storage)**: 생성한 번호를 브라우저에 저장하고 언제든 확인/삭제 가능.

---

## 🎥 3. 고화질 유튜브 다운로더
**[youtube_downloader.py]**

`yt-dlp` 엔진을 사용하여 유튜브 영상을 최고 화질(최대 8K)로 다운로드하거나 고음질 MP3를 추출하는 파이썬 기반 도구입니다.

### 🌟 주요 기능
- **초고화질 지원**: 4K/8K 무손실 병합 다운로드 가능.
- **자동 파일 관리**: `downloads` 폴더 자동 생성 및 정리.
- **사전 요구사항**: `yt-dlp` 라이브러리 및 `FFmpeg` 설치 필요.

---

## 💻 실행 방법 (How to Run)

### 웹 도구 (MarketBoard, LuckyPick)
1. `.html` 파일을 웹 브라우저(Chrome, Edge 등)로 직접 엽니다.
2. **권장 사항**: 보안 정책(`file://`)에 따른 로딩 지연을 피하려면 아래 명령어로 간이 서버를 실행하세요.
   ```bash
   python -m http.server 8000
   ```
   - 주소: `http://localhost:8000/market_board.html`

### 파이썬 도구 (Youtube Downloader)
```bash
pip install yt-dlp
python youtube_downloader.py
```

---

## 📄 라이선스 (License)
이 프로젝트는 MIT 라이선스 하에 배포됩니다. 

---
**Author**: [TAEHONG96](https://github.com/TAEHONG96)
**Last Update**: 2026-04-24
