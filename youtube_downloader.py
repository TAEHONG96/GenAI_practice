import yt_dlp
import os
import sys

def progress_hook(d):
    """다운로드 진행 상태를 출력하는 훅 함수"""
    if d['status'] == 'downloading':
        p = d.get('_percent_str', '0%')
        s = d.get('_speed_str', '0bps')
        eta = d.get('_eta_str', '0s')
        sys.stdout.write(f"\r[다운로드 중] 진행률: {p} | 속도: {s} | 남은시간: {eta}   ")
        sys.stdout.flush()
    elif d['status'] == 'finished':
        print(f"\n[완료] 다운로드가 끝났습니다. 파일을 병합/변환 중입니다...")

def run_downloader():
    print("="*60)
    print("       🚀 고화질 유튜브 다운로더 (TAEHONG96 Edition)       ")
    print("="*60)

    url = input("\n🔗 다운로드할 유튜브 URL을 입력하세요: ").strip()
    if not url:
        print("❌ 오류: URL을 입력해야 합니다.")
        return

    save_path = os.path.join(os.getcwd(), 'downloads')
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    print("\n[모드 선택]")
    print(" 1. 최고화질 영상 (MP4 - 최대 4K/8K)")
    print(" 2. 고음질 오디오 추출 (MP3)")
    mode = input("선택 (기본값 1): ") or "1"

    # 기본 설정
    ydl_opts = {
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        'progress_hooks': [progress_hook],
        'quiet': True,
        'no_warnings': True,
    }

    if mode == "1":
        # 최고화질 비디오 + 오디오 조합
        ydl_opts.update({
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
        })
        print("\n🎬 비디오 다운로드 모드를 시작합니다...")
    else:
        # 오디오만 추출
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
        print("\n🎵 오디오 추출 모드를 시작합니다...")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\n" + "="*60)
        print(f"✅ 모든 작업이 완료되었습니다!")
        print(f"📂 저장 위치: {save_path}")
        print("="*60)
    except Exception as e:
        print(f"\n❌ 오류 발생: {str(e)}")
        print("💡 힌트: FFmpeg가 설치되어 있는지 확인하거나 URL이 올바른지 확인하세요.")

if __name__ == "__main__":
    run_downloader()
