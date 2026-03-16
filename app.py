from flask import Flask, render_template_string

app = Flask(__name__)

# 서비스 데이터 리스트 (총 15개 이상 확장 가능)
SERVICES = [
    {"cat": "Networking", "title": "VPC", "color": "purple", "short": "격리된 가상 네트워크", "desc": "보안 그룹과 서브넷을 통한 네트워크 격리 구성", "link": "https://console.aws.amazon.com/vpc"},
    {"cat": "Compute", "title": "EC2", "color": "orange", "short": "가상 서버 인스턴스", "desc": "확장 가능한 컴퓨팅 용량 제공", "link": "https://console.aws.amazon.com/ec2"},
    {"cat": "Compute", "title": "ECS Fargate", "color": "orange", "short": "서버리스 컨테이너", "desc": "서버 관리 없는 컨테이너 운영 및 배포 자동화", "link": "https://console.aws.amazon.com/ecs"},
    {"cat": "Storage", "title": "Amazon S3", "color": "green", "short": "객체 스토리지", "desc": "높은 내구성을 가진 정적 데이터 저장소", "link": "https://console.aws.amazon.com/s3"},
    {"cat": "Traffic", "title": "ALB", "color": "blue", "short": "부하 분산 처리", "desc": "애플리케이션 레이어 로드 밸런싱", "link": "https://console.aws.amazon.com/ec2/v2/home#LoadBalancers:"},
    {"cat": "DevOps", "title": "Monitoring", "color": "pink", "short": "시스템 감시", "desc": "CloudWatch 기반 리소스 성능 모니터링", "link": "https://console.aws.amazon.com/cloudwatch"},
    {"cat": "Serverless", "title": "AWS Lambda", "color": "yellow", "short": "이벤트 기반 함수", "desc": "서버리스 백엔드 로직 처리", "link": "https://console.aws.amazon.com/lambda"},
    # ... 필요한 만큼 여기에 데이터를 추가하세요.
]

@app.route('/projects')
def projects():
    # 외부 HTML 파일을 읽어오거나 아래 템플릿 변수를 사용합니다.
    return render_template_string(PROJECTS_HTML, services=SERVICES)

# 여기에 아래 HTML 코드를 PROJECTS_HTML 변수로 넣으세요.