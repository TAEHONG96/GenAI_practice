import yt_dlp
import os

def download_youtube_video():
    print("="*50)
    print("      [한국어 유튜브 다운로더 v1.0]      ")
    print("="*50)

    # 1. URL 입력 받기
    url = input("\n다운로드할 유튜브 URL을 입력하세요: ").strip()
    if not url:
        print("URL이 입력되지 않았습니다.")
        return

    # 2. 저장 경로 설정 (현재 폴더의 'downloads' 폴더)
    save_path = os.path.join(os.getcwd(), 'downloads')
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # 3. 다운로드 옵션 선택
    print("\n[선택 모드]")
    print("1: 최고화질 영상 (MP4)")
    print("2: 오디오만 추출 (MP3)")
    mode = input("번호를 선택하세요 (기본값 1): ") or "1"

    # 4. yt-dlp 옵션 설정
    ydl_opts = {
        'outtmpl': f'{save_path}/%(title)s.%(ext)s', # 저장 파일명 형식
        'language': 'ko',                            # 한국어 우선
    }

    if mode == "1":
        # 최고화질 영상 + 오디오 병합 (ffmpeg 필요)
        ydl_opts['format'] = 'bestvideo+bestaudio/best'
        ydl_opts['merge_output_format'] = 'mp4'
        print("\n비디오 다운로드를 시작합니다...")
    else:
        # 오디오만 추출 및 MP3 변환
        ydl_opts['format'] = 'bestaudio/best'
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
        print("\n오디오 추출을 시작합니다...")

    # 5. 실제 다운로드 실행
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\n" + "="*50)
        print(f"다운로드 완료! 저장 위치: {save_path}")
        print("="*50)
    except Exception as e:
        print(f"\n오류가 발생했습니다: {e}")

if __name__ == "__main__":
    download_youtube_video()
