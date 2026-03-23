# 🚀 고화질 유튜브 다운로더 (TAEHONG96 Edition)

본 프로젝트는 `yt-dlp` 엔진을 사용하여 유튜브의 동영상을 최고 화질(최대 4K/8K)로 다운로드하거나 고음질 오디오(MP3)를 추출할 수 있는 파이썬 기반의 도구입니다.

---

## ✨ 주요 특징
- **초고화질 지원**: 1080p는 물론, 4K와 8K 영상까지 무손실 병합 다운로드 가능.
- **오디오 추출**: 영상에서 소리만 따로 추출하여 고음질 MP3 파일로 변환.
- **한국어 지원**: 사용자가 이해하기 쉬운 한국어 인터페이스와 상태 메시지 제공.
- **자동 파일 관리**: `downloads` 폴더를 생성하여 모든 다운로드 파일을 한곳에 정리.

---

## 🛠️ 사전 설치 요구사항

### 1. Python 설치
- [Python 3.8+](https://www.python.org/downloads/) 버전이 설치되어 있어야 합니다.

### 2. 라이브러리 설치
터미널(또는 CMD)에서 아래 명령어를 실행하여 필요한 라이브러리를 설치합니다.
```bash
pip install yt-dlp
```

### 3. FFmpeg 설치 (중요!)
최고 화질의 영상과 오디오를 결합하기 위해 **FFmpeg** 프로그램이 반드시 시스템에 설치되어 있어야 합니다.
- **Windows**: [FFmpeg 다운로드](https://ffmpeg.org/download.html) 후 시스템 환경 변수(Path)에 등록.
- **MacOS**: `brew install ffmpeg` 실행.
- **Linux**: `sudo apt install ffmpeg` 실행.

---

## 📋 사용 방법

1. **저장소 클론 또는 다운로드**
   ```bash
   git clone https://github.com/TAEHONG96/youtube-downloader.git
   cd youtube-downloader
   ```

2. **프로그램 실행**
   ```bash
   python youtube_downloader.py
   ```

3. **URL 입력 및 모드 선택**
   - 안내에 따라 다운로드하고 싶은 유튜브 링크를 입력합니다.
   - **모드 1**: 영상 다운로드 (MP4)
   - **모드 2**: 오디오 추출 (MP3)

4. **완료 확인**
   - 다운로드가 끝나면 같은 폴더 내 `downloads/` 디렉토리에 파일이 생성됩니다.

---

## ⚠️ 주의 사항 (Disclaimer)
- 본 프로그램은 개인적인 교육 및 학습 목적으로 제작되었습니다.
- 다운로드한 콘텐츠는 **개인 소장용**으로만 사용해야 하며, 영리적 목적이나 저작권자의 허락 없이 무단 배포할 경우 법적 책임은 사용자에게 있습니다.
- 유튜브의 서비스 약관을 준수하시기 바랍니다.

---

## 🤝 기여하기
버그 제보나 기능 제안은 **Issue** 또는 **Pull Request**를 통해 언제든지 환영합니다!

---
**Author**: [TAEHONG96](https://github.com/TAEHONG96)
