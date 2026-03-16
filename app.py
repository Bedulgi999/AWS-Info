from flask import Flask, render_template

app = Flask(__name__)

@app.route('/projects')
def projects():
    # 15개 이상의 서비스를 여기에 리스트로 관리합니다.
    # 아이콘 경로는 AWS 공식 아이콘 저장소를 활용하도록 설정했습니다.
    services_data = [
        {"cat": "Networking", "title": "VPC", "short": "격리된 가상 네트워크", "desc": "Virtual Private Cloud를 통해 안전한 네트워크 환경을 구축합니다.", "link": "https://console.aws.amazon.com/vpc"},
        {"cat": "Compute", "title": "EC2", "short": "가상 서버 인스턴스", "desc": "안전하고 확장 가능한 컴퓨팅 용량을 제공합니다.", "link": "https://console.aws.amazon.com/ec2"},
        {"cat": "Compute", "title": "ECS Fargate", "short": "서버리스 컨테이너", "desc": "인프라 관리 없이 컨테이너 애플리케이션을 실행합니다.", "link": "https://console.aws.amazon.com/ecs"},
        {"cat": "Storage", "title": "Amazon S3", "short": "객체 스토리지", "desc": "업계 최고 수준의 내구성을 가진 데이터 저장소입니다.", "link": "https://console.aws.amazon.com/s3"},
        {"cat": "Traffic", "title": "ALB", "short": "부하 분산 처리", "desc": "애플리케이션 계층의 트래픽을 효율적으로 분산합니다.", "link": "https://console.aws.amazon.com/ec2/v2/home#LoadBalancers"},
        {"cat": "DevOps", "title": "CloudWatch", "short": "모니터링 및 로깅", "desc": "리소스 및 애플리케이션 상태를 실시간으로 감시합니다.", "link": "https://console.aws.amazon.com/cloudwatch"},
        {"cat": "Serverless", "title": "Lambda", "short": "이벤트 기반 함수", "desc": "서버 없이 코드를 실행하는 이벤트 기반 컴퓨팅 서비스입니다.", "link": "https://console.aws.amazon.com/lambda"},
        {"cat": "DNS", "title": "Route 53", "short": "클라우드 DNS", "desc": "가용성이 뛰어난 도메인 이름 시스템 서비스입니다.", "link": "https://console.aws.amazon.com/route53"},
        {"cat": "CDN", "title": "CloudFront", "short": "콘텐츠 전송 네트워크", "desc": "전 세계 사용자에게 저지연으로 콘텐츠를 배포합니다.", "link": "https://console.aws.amazon.com/cloudfront"},
        {"cat": "Security", "title": "WAF", "short": "웹 보안 방화벽", "desc": "웹 공격으로부터 애플리케이션을 안전하게 보호합니다.", "link": "https://console.aws.amazon.com/wafv2"},
        {"cat": "Database", "title": "RDS", "short": "관계형 데이터베이스", "desc": "관리형 DB 서비스로 설정과 확장이 간편합니다.", "link": "https://console.aws.amazon.com/rds"},
        {"cat": "Registry", "title": "ECR", "short": "컨테이너 이미지 저장소", "desc": "Docker 이미지를 안전하게 저장하고 관리합니다.", "link": "https://console.aws.amazon.com/ecr"},
        {"cat": "Kubernetes", "title": "EKS", "short": "관리형 K8s 서비스", "desc": "AWS에서 쿠버네티스를 손쉽게 운영할 수 있습니다.", "link": "https://console.aws.amazon.com/eks"},
        {"cat": "Identity", "title": "IAM", "short": "액세스 권한 관리", "desc": "사용자 인증 및 리소스 접근 권한을 제어합니다.", "link": "https://console.aws.amazon.com/iam"},
        {"cat": "Automation", "title": "CodePipeline", "short": "배포 자동화(CI/CD)", "desc": "빠르고 안정적인 소프트웨어 배포 파이프라인을 구축합니다.", "link": "https://console.aws.amazon.com/codesuite/codepipeline"}
    ]
    return render_template('projects.html', services=services_data)

if __name__ == '__main__':
    app.run(debug=True)