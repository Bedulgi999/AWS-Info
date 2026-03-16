from flask import Flask, render_template

app = Flask(__name__)

@app.route('/projects')
def projects():
    # 15개 이상의 핵심 서비스를 리스트로 구성
    services_list = [
        {"cat": "Networking", "title": "VPC", "short": "격리된 가상 네트워크", "link": "https://console.aws.amazon.com/vpc", "desc": "Virtual Private Cloud를 통해 논리적으로 격리된 네트워크 환경을 구축합니다."},
        {"cat": "Compute", "title": "EC2", "short": "가상 서버 인스턴스", "link": "https://console.aws.amazon.com/ec2", "desc": "안전하고 확장 가능한 컴퓨팅 용량을 제공합니다."},
        {"cat": "Compute", "title": "ECS Fargate", "short": "서버리스 컨테이너", "link": "https://console.aws.amazon.com/ecs", "desc": "인프라 관리 없이 컨테이너를 실행할 수 있는 서버리스 엔진입니다."},
        {"cat": "Storage", "title": "Amazon S3", "short": "객체 스토리지", "link": "https://console.aws.amazon.com/s3", "desc": "업계 최고 수준의 확장성과 데이터 가용성을 제공하는 저장소입니다."},
        {"cat": "Traffic", "title": "ALB", "short": "L7 부하 분산 처리", "link": "https://console.aws.amazon.com/ec2/v2/home#LoadBalancers", "desc": "애플리케이션 계층의 트래픽을 효율적으로 분산합니다."},
        {"cat": "DevOps", "title": "Monitoring", "short": "시스템 통합 감시", "link": "https://console.aws.amazon.com/cloudwatch", "desc": "CloudWatch를 통해 실시간 지표 및 로그를 모니터링합니다."},
        {"cat": "Serverless", "title": "Lambda", "short": "이벤트 기반 함수", "link": "https://console.aws.amazon.com/lambda", "desc": "서버 프로비저닝 없이 코드를 실행하는 서버리스 서비스입니다."},
        {"cat": "DNS", "title": "Route 53", "short": "클라우드 DNS 서비스", "link": "https://console.aws.amazon.com/route53", "desc": "가용성이 뛰어난 도메인 네임 시스템을 제공합니다."},
        {"cat": "CDN", "title": "CloudFront", "short": "콘텐츠 전송 네트워크", "link": "https://console.aws.amazon.com/cloudfront", "desc": "글로벌 엣지 로케이션을 통해 빠른 콘텐츠 배포를 지원합니다."},
        {"cat": "Security", "title": "WAF", "short": "웹 방화벽", "link": "https://console.aws.amazon.com/wafv2", "desc": "웹 공격으로부터 애플리케이션을 안전하게 보호합니다."},
        {"cat": "Database", "title": "RDS", "short": "관리형 관계형 DB", "link": "https://console.aws.amazon.com/rds", "desc": "관계형 데이터베이스의 설정 및 운영을 자동화합니다."},
        {"cat": "Registry", "title": "ECR", "short": "컨테이너 이미지 관리", "link": "https://console.aws.amazon.com/ecr", "desc": "Docker 컨테이너 이미지를 안전하게 저장하고 배포합니다."},
        {"cat": "Kubernetes", "title": "EKS", "short": "관리형 K8s 서비스", "link": "https://console.aws.amazon.com/eks", "desc": "AWS에서 쿠버네티스를 손쉽게 실행하고 운영합니다."},
        {"cat": "Identity", "title": "IAM", "short": "리소스 접근 제어", "link": "https://console.aws.amazon.com/iam", "desc": "사용자 인증 및 권한을 세밀하게 관리합니다."},
        {"cat": "Automation", "title": "Pipeline", "short": "CI/CD 자동화", "link": "https://console.aws.amazon.com/codesuite/codepipeline", "desc": "소프트웨어 배포 파이프라인을 구축하고 자동화합니다."}
    ]
    return render_template('projects.html', services=services_list)

if __name__ == '__main__':
    app.run(debug=True)