from flask import Flask, render_template

app = Flask(__name__)

@app.route('/projects')
def projects():
    # 서비스 아이콘 이름은 AWS 공식 명칭을 참고하여 지정했습니다.
    services = [
        {"cat": "Networking", "title": "VPC", "short": "격리된 가상 네트워크", "color": "purple", "link": "https://console.aws.amazon.com/vpc", "desc": "Virtual Private Cloud를 통해 논리적으로 격리된 네트워크 환경을 구축하고 보안 그룹으로 접근을 제어합니다."},
        {"cat": "Compute", "title": "EC2", "short": "가상 서버 인스턴스", "color": "orange", "link": "https://console.aws.amazon.com/ec2", "desc": "안전하고 크기 조정이 가능한 컴퓨팅 용량을 제공하여 다양한 워크로드를 처리합니다."},
        {"cat": "Compute", "title": "ECS Fargate", "short": "서버리스 컨테이너", "color": "orange", "link": "https://console.aws.amazon.com/ecs", "desc": "서버 관리 없이 컨테이너를 실행하며 애플리케이션 구축에만 집중할 수 있는 환경을 제공합니다."},
        {"cat": "Storage", "title": "Amazon S3", "short": "무한 확장 객체 스토리지", "color": "green", "link": "https://console.aws.amazon.com/s3", "desc": "업계 최고 수준의 확장성과 데이터 가용성을 제공하는 객체 저장소입니다."},
        {"cat": "Traffic", "title": "Load Balancer", "short": "L7 부하 분산", "color": "green", "link": "https://console.aws.amazon.com/ec2/v2/home#LoadBalancers", "desc": "들어오는 애플리케이션 트래픽을 여러 대상에 자동으로 분산하여 안정성을 높입니다."},
        {"cat": "DevOps", "title": "Monitoring", "short": "CloudWatch 지표 감시", "color": "pink", "link": "https://console.aws.amazon.com/cloudwatch", "desc": "AWS 리소스 및 애플리케이션에 대한 실시간 모니터킹 및 로그 분석을 지원합니다."},
        {"cat": "Serverless", "title": "AWS Lambda", "short": "이벤트 기반 함수", "color": "yellow", "link": "https://console.aws.amazon.com/lambda", "desc": "서버를 프로비저닝하지 않고도 코드를 실행할 수 있는 서버리스 컴퓨팅 서비스입니다."},
        {"cat": "DNS", "title": "Route 53", "short": "가용성 높은 DNS", "color": "purple", "link": "https://console.aws.amazon.com/route53", "desc": "사용자의 요청을 AWS 인프라로 연결해주는 가용성이 뛰어난 클라우드 DNS 서비스입니다."},
        {"cat": "CDN", "title": "CloudFront", "short": "글로벌 콘텐츠 전송", "color": "indigo", "link": "https://console.aws.amazon.com/cloudfront", "desc": "데이터, 비디오, 애플리케이션을 전 세계 사용자에게 저지연으로 안전하게 전달합니다."},
        {"cat": "Security", "title": "WAF", "short": "웹 애플리케이션 방화벽", "color": "red", "link": "https://console.aws.amazon.com/wafv2", "desc": "웹 공격으로부터 애플리케이션을 보호하고 트래픽 패턴을 필터링합니다."},
        {"cat": "Database", "title": "RDS", "short": "관리형 관계형 DB", "color": "blue", "link": "https://console.aws.amazon.com/rds", "desc": "클라우드에서 관계형 데이터베이스를 간편하게 설정하고 운영 및 확장할 수 있습니다."},
        {"cat": "Registry", "title": "ECR", "short": "컨테이너 이미지 저장소", "color": "orange", "link": "https://console.aws.amazon.com/ecr", "desc": "완전관리형 Docker 컨테이너 레지스트리로 이미지를 안전하게 저장합니다."},
        {"cat": "Kubernetes", "title": "EKS", "short": "관리형 K8s 서비스", "color": "orange", "link": "https://console.aws.amazon.com/eks", "desc": "쿠버네티스 제어 플레인을 관리할 필요 없이 컨테이너를 실행할 수 있습니다."},
        {"cat": "Identity", "title": "IAM", "short": "리소스 액세스 관리", "color": "red", "link": "https://console.aws.amazon.com/iam", "desc": "AWS 서비스와 리소스에 대한 액세스를 안전하게 제어하는 인증 서비스입니다."},
        {"cat": "Automation", "title": "CodePipeline", "short": "지속적 배포(CD)", "color": "blue", "link": "https://console.aws.amazon.com/codesuite/codepipeline", "desc": "빠르고 안정적인 애플리케이션 업데이트를 위해 배포 단계를 자동화합니다."}
    ]
    return render_template('projects.html', services=services)

if __name__ == '__main__':
    app.run(debug=True)