import os

def find_chromedriver():
    # PATH 환경 변수에서 디렉터리 목록 가져오기
    paths = os.environ.get("PATH", "").split(os.pathsep)
    
    # 실행 파일 이름 설정 (Windows와 다른 OS 구분)
    chromedriver_name = "chromedriver.exe" if os.name == "nt" else "chromedriver"
    
    # PATH 내에서 chromedriver 찾기
    for path in paths:
        chromedriver_path = os.path.join(path, chromedriver_name)
        if os.path.isfile(chromedriver_path):
            return chromedriver_path
    
    return None

# ChromeDriver 경로 찾기
chromedriver_path = find_chromedriver()
if chromedriver_path:
    print(f"ChromeDriver가 설치된 경로: {chromedriver_path}")
else:
    print("ChromeDriver를 찾을 수 없습니다. PATH에 추가되었는지 확인하세요.")