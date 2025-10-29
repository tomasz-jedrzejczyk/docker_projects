# Django Application with Docker & CI/CD

A Django web application containerized with Docker and automatically deployed to AWS EC2 using GitHub Actions.

## 📋 Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Local Development Setup](#local-development-setup)
- [Environment Variables](#environment-variables)
- [Docker Setup](#docker-setup)
- [Deployment](#deployment)
- [GitHub Actions CI/CD](#github-actions-cicd)
- [Running Commands](#running-commands)
- [Troubleshooting](#troubleshooting)

## ✨ Features

- Django 4.x application
- Docker & Docker Compose containerization
- PostgreSQL database (optional)
- Automated CI/CD with GitHub Actions
- AWS EC2 deployment
- N8N automation tool integration

## 📦 Prerequisites

- Python 3.12+
- Docker & Docker Compose
- Git
- AWS EC2 instance (for deployment)
- GitHub account

## 📁 Project Structure
```
your-project/
├── .github/
│   └── workflows/
│       └── django-ci.yml       # GitHub Actions workflow
├── django-app/
│   ├── manage.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── your_project/           # Main Django project
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   └── apps/                   # Django apps
├── docker-compose.yml
├── .gitignore
├── .env.example
└── README.md
```

## 🚀 Local Development Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r django-app/requirements.txt
```

### 4. Set Up Environment Variables
```bash
cp .env.example .env
# Edit .env with your actual values
```

### 5. Run Migrations
```bash
cd django-app
python manage.py migrate
python manage.py createsuperuser
```

### 6. Run Development Server
```bash
python manage.py runserver
```

Visit `http://localhost:8000`

## 🔐 Environment Variables

Create a `.env` file in the project root:
```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,your-domain.com

# Database (if using PostgreSQL)
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=db
DB_PORT=5432

# Optional: Email settings
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-email-password
```

**⚠️ Never commit the `.env` file to Git!**

## 🐳 Docker Setup

### Build and Run with Docker Compose
```bash
# Build and start all services
docker-compose up --build -d

# View running containers
docker ps

# View logs
docker-compose logs -f django

# Stop all services
docker-compose down
```

### Services

- **Django App**: `http://localhost:8000`
- **N8N**: `http://localhost:5678`

### Restart Only Django (without affecting N8N)
```bash
docker-compose stop django
docker-compose build django
docker-compose up -d --no-deps django
```

## 🚢 Deployment

### AWS EC2 Setup

1. **Launch EC2 Instance**
   - Ubuntu 22.04 LTS
   - Open ports: 22 (SSH), 8000 (Django), 5678 (N8N)

2. **Install Docker on EC2**
```bash
# SSH into EC2
ssh -i your-key.pem ubuntu@your-ec2-ip

# Install Docker
sudo apt update
sudo apt install -y docker.io docker-compose
sudo usermod -aG docker ubuntu
sudo systemctl enable docker
sudo systemctl start docker

# Logout and login again for group changes
exit
```

3. **Create Project Directory**
```bash
mkdir -p /home/ubuntu/docker-project
cd /home/ubuntu/docker-project
```

### GitHub Secrets Setup

Add these secrets to your GitHub repository (`Settings` → `Secrets and variables` → `Actions`):

- `EC2_HOST`: Your EC2 public IP or domain
- `EC2_USERNAME`: `ubuntu` (or your EC2 user)
- `EC2_SSH_KEY`: Your private SSH key content

## 🔄 GitHub Actions CI/CD

The workflow automatically:

1. ✅ Runs on push to `master` branch
2. 🐍 Sets up Python 3.12
3. 📦 Installs dependencies
4. 🧹 Cleans old files on EC2
5. 📤 Copies new code to EC2
6. 🐳 Rebuilds only Django container (keeps N8N running)
7. 🧼 Cleans up old Docker images

### Manual Deployment

Push to master branch:
```bash
git add .
git commit -m "Your commit message"
git push origin master
```

## 🛠️ Running Commands

### Inside Docker Container
```bash
# Execute Django commands
docker-compose exec django python manage.py migrate
docker-compose exec django python manage.py createsuperuser
docker-compose exec django python manage.py collectstatic

# Access Django shell
docker-compose exec django python manage.py shell

# Access container bash
docker-compose exec django bash
```

### Database Management
```bash
# Create migrations
docker-compose exec django python manage.py makemigrations

# Apply migrations
docker-compose exec django python manage.py migrate

# Backup database (if using PostgreSQL)
docker-compose exec db pg_dump -U your_user your_db > backup.sql
```

### View Logs
```bash
# All services
docker-compose logs -f

# Django only
docker-compose logs -f django

# N8N only
docker-compose logs -f n8n

# Last 100 lines
docker-compose logs --tail=100 django
```

## 🐛 Troubleshooting

### Container won't start
```bash
# Check logs
docker-compose logs django

# Rebuild from scratch
docker-compose down -v
docker-compose up --build -d
```

### Port already in use
```bash
# Find process using port 8000
sudo lsof -i :8000

# Kill the process
sudo kill -9 <PID>
```

### Permission denied on EC2
```bash
# Fix Docker permissions
sudo usermod -aG docker ubuntu
sudo systemctl restart docker
```

### Static files not loading
```bash
docker-compose exec django python manage.py collectstatic --noinput
```

### Database connection error
```bash
# Check if database container is running
docker-compose ps

# Restart database
docker-compose restart db
```

## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Docker Documentation](https://docs.docker.com/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [AWS EC2 Documentation](https://docs.aws.amazon.com/ec2/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- Your Name - [@yourusername](https://github.com/yourusername)

## 🙏 Acknowledgments

- Django community
- Docker community
- GitHub Actions

---

**Need help?** Open an issue or contact [your-email@example.com](mailto:your-email@example.com)