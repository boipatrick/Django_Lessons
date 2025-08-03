# Django Blog Application

A modern, feature-rich blog application built with Django that allows users to create accounts, publish posts with images, and interact with content through a clean, responsive interface.

## 🚀 Features

### Core Functionality
- **User Authentication System**
  - User registration with Django's built-in UserCreationForm
  - User login/logout functionality
  - Secure session management
  - CSRF protection for all forms

- **Blog Post Management**
  - Create and display blog posts with titles, content, and slugs
  - Automatic date stamping for posts
  - Image upload support with banner images
  - Responsive post listing and individual post pages
  - SEO-friendly URL structure using slugs

- **Media Management**
  - Image upload functionality for post banners
  - Fallback image support for posts without custom banners
  - Proper media file serving in development

### Technical Features
- **Modern Django Architecture**
  - Django 5.2.4 with latest features
  - Modular app structure (posts, users)
  - Template inheritance with base layout
  - Static file management (CSS, JavaScript)

- **User Experience**
  - Clean, intuitive navigation with emoji icons
  - Responsive design
  - Form validation and error handling
  - Consistent styling across all pages

## 📁 Project Structure

```
first_lesson/
├── first_lesson/          # Main project settings
│   ├── settings.py       # Django configuration
│   ├── urls.py          # Main URL routing
│   └── wsgi.py          # WSGI application
├── posts/               # Blog posts app
│   ├── models.py        # Post model definition
│   ├── views.py         # Post views (list, detail)
│   ├── urls.py          # Post URL patterns
│   ├── admin.py         # Admin interface
│   └── templates/       # Post templates
│       ├── posts_list.html
│       └── post_page.html
├── users/               # User authentication app
│   ├── views.py         # User views (register, login, logout)
│   ├── urls.py          # User URL patterns
│   └── templates/       # User templates
│       └── register.html
├── templates/           # Base templates
│   ├── layout.html      # Base template with navigation
│   ├── home.html        # Home page
│   └── about.html       # About page
├── static/              # Static files
│   ├── css/
│   │   └── styles.css   # Custom styles
│   └── js/
│       └── main.js      # JavaScript functionality
├── media/               # User-uploaded files
│   └── (uploaded images)
├── manage.py            # Django management script
└── db.sqlite3          # SQLite database
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.12
- pipenv (for dependency management)

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd django_lessons/Lesson01
```

### Step 2: Install Dependencies
```bash
pipenv install
```

### Step 3: Activate Virtual Environment
```bash
pipenv shell
```

### Step 4: Run Database Migrations
```bash
cd first_lesson
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### Step 6: Run the Development Server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## 🎯 Usage Guide

### For End Users

1. **Home Page** (`/`)
   - Welcome page with navigation to all sections

2. **About Page** (`/about`)
   - Information about the blog and its purpose

3. **Posts** (`/posts/`)
   - View all published blog posts
   - Posts are displayed in reverse chronological order

4. **Individual Post** (`/posts/<slug>/`)
   - View detailed post content with banner image
   - SEO-friendly URLs using post slugs

5. **User Registration** (`/users/register/`)
   - Create a new account
   - Automatic login after successful registration

6. **User Login** (`/users/login/`)
   - Sign in to existing account
   - Redirects to posts list after successful login

7. **Logout**
   - Click the logout button in the navigation
   - Secure POST-based logout functionality

### For Developers

#### Adding New Posts
1. Access the Django admin interface at `/admin/`
2. Use the superuser account to log in
3. Navigate to Posts section
4. Add new posts with title, content, slug, and optional banner image

#### Customizing Styles
- Edit `static/css/styles.css` for custom styling
- The layout uses a responsive design with emoji navigation

#### Adding New Features
- Create new apps using `python manage.py startapp app_name`
- Add apps to `INSTALLED_APPS` in settings.py
- Create models, views, and templates following Django conventions

## 🔧 Configuration

### Key Settings (settings.py)
- **Database**: SQLite3 (default Django database)
- **Static Files**: Configured for development with `STATICFILES_DIRS`
- **Media Files**: Configured for user uploads with `MEDIA_URL` and `MEDIA_ROOT`
- **Templates**: Configured to use both app-specific and project-wide templates

### Environment Variables
For production deployment, consider setting:
- `SECRET_KEY`: Change the default secret key
- `DEBUG`: Set to `False` for production
- `ALLOWED_HOSTS`: Configure allowed hostnames

## 🚀 Deployment

### Development
The current setup is optimized for development with:
- Debug mode enabled
- SQLite database
- Local media file serving

### Production Considerations
1. **Database**: Consider PostgreSQL or MySQL for production
2. **Static Files**: Use a CDN or configure proper static file serving
3. **Media Files**: Use cloud storage (AWS S3, etc.) for user uploads
4. **Security**: Update `SECRET_KEY` and disable debug mode
5. **Web Server**: Use Gunicorn with Nginx or Apache

## 🐛 Troubleshooting

### Common Issues

1. **Database Migration Errors**
   ```bash
   python manage.py makemigrations --empty app_name
   python manage.py migrate
   ```

2. **Static Files Not Loading**
   - Ensure `STATICFILES_DIRS` is properly configured
   - Run `python manage.py collectstatic` for production

3. **Media Files Not Displaying**
   - Check `MEDIA_URL` and `MEDIA_ROOT` settings
   - Ensure media directory has proper permissions

4. **Form Submission Issues**
   - Verify CSRF tokens are included in forms
   - Check form action URLs are correct

### Debug Mode
When `DEBUG = True` in settings.py, Django provides detailed error pages for development.

## 📝 API Endpoints

| URL Pattern | View | Description |
|-------------|------|-------------|
| `/` | home | Home page |
| `/about/` | about | About page |
| `/posts/` | posts_list | List all posts |
| `/posts/<slug>/` | posts_page | Individual post detail |
| `/users/register/` | register_view | User registration |
| `/users/login/` | login_view | User login |
| `/users/logout/` | logout_view | User logout |
| `/admin/` | Django admin | Admin interface |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Built with Django 5.2.4
- Uses Django's built-in authentication system
- Responsive design with modern CSS
- Clean, maintainable code structure

---

**Happy Blogging! 🚀**
