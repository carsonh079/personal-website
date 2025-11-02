# Django Portfolio Website

A modern, professional portfolio website built with Django and containerized with Docker. Features a retro 80s-inspired color scheme with dark grey backgrounds and vibrant magenta, yellow, and light blue highlights.

## Features

- **Responsive Design**: Mobile-friendly layout that works on all devices
- **Blog System**: Create and publish blog posts with an admin interface
- **Project Showcase**: Display data analysis and engineering projects
- **Resume Section**: Link to your professional resume
- **80s Aesthetic**: Unique color scheme with neon-inspired highlights
- **Docker Ready**: Fully containerized for easy deployment to AWS or any cloud platform
- **Admin Interface**: Built-in Django admin for easy content management

## Technology Stack

- **Backend**: Django 4.2
- **Server**: Gunicorn
- **Static Files**: WhiteNoise
- **Database**: SQLite (default) / PostgreSQL (production ready)
- **Containerization**: Docker & Docker Compose
- **Python**: 3.11

## Quick Start with Docker

### Prerequisites

- Docker
- Docker Compose

### Running the Application

1. Clone the repository:
```bash
git clone <repository-url>
cd personal-website
```

2. Build and run with Docker Compose:
```bash
docker-compose up --build
```

3. Access the application at `http://localhost:8000`

4. Create a superuser to access the admin interface:
```bash
docker-compose exec web python manage.py createsuperuser
```

5. Access the admin interface at `http://localhost:8000/admin`

## Local Development Setup

### Prerequisites

- Python 3.11+
- pip

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd personal-website
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Collect static files:
```bash
python manage.py collectstatic
```

7. Run the development server:
```bash
python manage.py runserver
```

8. Access the application at `http://localhost:8000`

## Project Structure

```
personal-website/
├── portfolio/              # Main Django app
│   ├── migrations/        # Database migrations
│   ├── templates/         # HTML templates
│   │   └── portfolio/    # App-specific templates
│   ├── models.py         # Database models (BlogPost, Project)
│   ├── views.py          # View functions
│   ├── urls.py           # URL routing
│   └── admin.py          # Admin configuration
├── portfolio_site/        # Django project settings
│   ├── settings.py       # Project settings
│   ├── urls.py           # Root URL configuration
│   └── wsgi.py           # WSGI configuration
├── static/               # Static files (CSS, JS, images)
│   └── css/
│       └── style.css     # Main stylesheet
├── staticfiles/          # Collected static files (production)
├── Dockerfile            # Docker image configuration
├── docker-compose.yml    # Docker Compose configuration
├── requirements.txt      # Python dependencies
├── manage.py            # Django management script
└── README.md            # This file
```

## Adding Content

### Adding Blog Posts

1. Access the admin interface at `/admin`
2. Navigate to "Blog posts"
3. Click "Add blog post"
4. Fill in the title, content, and slug
5. Mark as "Published" to make it visible
6. Save

### Adding Projects

1. Access the admin interface at `/admin`
2. Navigate to "Projects"
3. Click "Add project"
4. Fill in project details:
   - Title and slug
   - Description
   - Project type (Data Analysis, Data Engineering, etc.)
   - Technologies (comma-separated)
   - GitHub URL and/or Live URL (optional)
   - Mark as "Featured" to highlight on the homepage
5. Save

### Adding Your Resume

1. Place your resume PDF in the `static/` directory
2. Update the resume link in `portfolio/templates/portfolio/home.html`

## Deployment to AWS

### Using Docker on AWS ECS

1. Build the Docker image:
```bash
docker build -t portfolio-website .
```

2. Tag and push to Amazon ECR:
```bash
aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com
docker tag portfolio-website:latest <account-id>.dkr.ecr.<region>.amazonaws.com/portfolio-website:latest
docker push <account-id>.dkr.ecr.<region>.amazonaws.com/portfolio-website:latest
```

3. Create an ECS task definition and service using the pushed image

4. Set environment variables:
   - `SECRET_KEY`: Your Django secret key
   - `DEBUG`: Set to `False` for production
   - `ALLOWED_HOSTS`: Your domain name(s)

### Using Docker on AWS EC2

1. Launch an EC2 instance with Docker installed
2. Clone the repository
3. Set up environment variables in `.env` file
4. Run with Docker Compose:
```bash
docker-compose up -d
```

### Environment Variables

Copy `.env.example` to `.env` and update:

```bash
SECRET_KEY=your-production-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

## Color Scheme

The website uses a retro 80s-inspired color palette:

- **Background**: Dark grey (#2a2a2a)
- **Text**: White (#ffffff)
- **Primary Accent**: Magenta (#ff00ff)
- **Secondary Accent**: Yellow (#ffff00)
- **Tertiary Accent**: Light Blue (#00ffff)

## Customization

### Changing Colors

Edit `static/css/style.css` and modify the CSS variables at the top:

```css
:root {
    --dark-grey: #2a2a2a;
    --darker-grey: #1a1a1a;
    --white: #ffffff;
    --magenta: #ff00ff;
    --yellow: #ffff00;
    --light-blue: #00ffff;
}
```

### Modifying Templates

Templates are located in `portfolio/templates/portfolio/`:
- `base.html`: Base template with navigation and footer
- `home.html`: Landing page
- `blog_list.html`: Blog posts listing
- `blog_detail.html`: Individual blog post
- `project_list.html`: Projects listing
- `project_detail.html`: Individual project

## Contributing

This is a personal portfolio project, but feel free to fork and customize for your own use.

## License

This project is open source and available for personal and commercial use.

## Support

For issues or questions, please create an issue in the repository.
