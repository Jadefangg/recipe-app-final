# Recipe App - Django Web Application

A comprehensive recipe management web application built with Django, featuring user authentication, recipe creation, ingredient management, and category organization. Deployed on Heroku with PostgreSQL database.

## 🚀 Live Demo

**Production URL**: [https://recipe-app-cf-3f433a62092d.herokuapp.com/](https://recipe-app-cf-3f433a62092d.herokuapp.com/)

## 📋 Features

- **Recipe Management**: Create, view, edit, and delete recipes with detailed instructions
- **Ingredient System**: Manage ingredients with units, quantities, and nutritional information
- **Category Organization**: Organize recipes by categories (appetizers, main courses, desserts, etc.)
- **User Authentication**: Secure login/logout functionality with user sessions
- **Admin Interface**: Comprehensive Django admin panel for content management
- **Responsive Design**: Mobile-friendly interface that works on all devices
- **Search & Filter**: Find recipes by ingredients, categories, or keywords
- **Image Support**: Upload and display recipe images
- **Data Visualization**: Charts and analytics for recipe data using Matplotlib

## 🛠️ Technology Stack

### Backend
- **Framework**: Django 5.1.7
- **Database**: PostgreSQL (Production), SQLite (Development)
- **Web Server**: Gunicorn
- **Static Files**: WhiteNoise

### Frontend
- **Templates**: Django Templates
- **Styling**: CSS, Bootstrap
- **JavaScript**: Vanilla JS

### Data & Analytics
- **Data Processing**: Pandas 2.2.3, NumPy 2.2.4
- **Visualization**: Matplotlib 3.10.1
- **Image Processing**: Pillow 11.1.0

### Deployment
- **Platform**: Heroku
- **Database**: PostgreSQL (Heroku Postgres)
- **Environment Management**: python-dotenv

## 📂 Project Structure

```
recipe-app-final/
├── src/
│   ├── manage.py
│   ├── db.sqlite3                     # Local development database
│   ├── recipe_project/                # Main project settings
│   │   ├── __init__.py
│   │   ├── settings.py               # Django settings
│   │   ├── urls.py                   # Main URL configuration
│   │   ├── wsgi.py                   # WSGI configuration
│   │   └── asgi.py                   # ASGI configuration
│   ├── recipes/                      # Recipe app
│   │   ├── models.py                 # Recipe data models
│   │   ├── views.py                  # Recipe views
│   │   ├── urls.py                   # Recipe URL patterns
│   │   ├── forms.py                  # Recipe forms
│   │   ├── admin.py                  # Admin configuration
│   │   ├── templates/recipes/        # Recipe templates
│   │   ├── static/recipes/           # Recipe static files
│   │   └── migrations/               # Database migrations
│   ├── ingredients/                  # Ingredients app
│   │   ├── models.py                 # Ingredient data models
│   │   ├── views.py                  # Ingredient views
│   │   ├── admin.py                  # Admin configuration
│   │   └── migrations/               # Database migrations
│   ├── categories/                   # Categories app
│   │   ├── models.py                 # Category data models
│   │   ├── views.py                  # Category views
│   │   ├── admin.py                  # Admin configuration
│   │   └── migrations/               # Database migrations
│   └── static/                       # Global static files
├── requirements.txt                  # Python dependencies
├── Procfile                         # Heroku process configuration
├── runtime.txt                      # Python version specification
├── .gitignore                       # Git ignore rules
└── README.md                        # This file
```

## 📋 Prerequisites

- Python 3.11 or higher
- Git
- Heroku CLI (for deployment)
- PostgreSQL (for production)

## 🔧 Installation & Setup

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/Jadefangg/recipe-app-final.git
   cd recipe-app-final
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create environment file**
   ```bash
   # Create .env file in project root
   echo "DJANGO_SECRET_KEY=your-very-long-secret-key-here" > .env
   echo "DJANGO_DEBUG=True" >> .env
   ```

5. **Set up database**
   ```bash
   cd src
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Create static directory**
   ```bash
   mkdir static
   ```

8. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

9. **Run development server**
   ```bash
   python manage.py runserver
   ```

10. **Access the application**
    - Main site: http://127.0.0.1:8000/
    - Admin panel: http://127.0.0.1:8000/admin/

## 🚀 Deployment to Heroku

### Prerequisites
- Heroku account
- Heroku CLI installed
- Git repository

### Deployment Steps

1. **Login to Heroku**
   ```bash
   heroku login
   ```

2. **Create Heroku app**
   ```bash
   heroku create your-app-name
   ```

3. **Add PostgreSQL database**
   ```bash
   heroku addons:create heroku-postgresql:basic --app your-app-name
   ```

4. **Set environment variables**
   ```bash
   heroku config:set DJANGO_SECRET_KEY="your-very-long-secret-key" --app your-app-name
   heroku config:set DJANGO_DEBUG=False --app your-app-name
   ```

5. **Configure Git and deploy**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   heroku git:remote -a your-app-name
   git push heroku main
   ```

6. **Run migrations on Heroku**
   ```bash
   heroku run python src/manage.py migrate --app your-app-name
   ```

7. **Create superuser on Heroku**
   ```bash
   heroku run python src/manage.py createsuperuser --app your-app-name
   ```

8. **Collect static files**
   ```bash
   heroku run python src/manage.py collectstatic --noinput --app your-app-name
   ```

## 🔑 Environment Variables

### Required Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `DJANGO_SECRET_KEY` | Django secret key for security | `your-very-long-secret-key` |
| `DJANGO_DEBUG` | Debug mode (True/False) | `False` |
| `DATABASE_URL` | Database connection string | Auto-set by Heroku Postgres |

### Setting Environment Variables

**For Local Development (.env file):**
```env
DJANGO_SECRET_KEY=your-very-long-secret-key-here
DJANGO_DEBUG=True
```

**For Heroku:**
```bash
heroku config:set DJANGO_SECRET_KEY="your-secret-key" --app your-app-name
heroku config:set DJANGO_DEBUG=False --app your-app-name
```

## 📱 Usage

### For End Users

1. **Access the website** at the deployed URL
2. **Browse recipes** on the homepage
3. **Search for recipes** using the search functionality
4. **Filter by categories** to find specific types of recipes
5. **View detailed recipe information** including ingredients and instructions

### For Administrators

1. **Access admin panel** at `/admin/`
2. **Login with superuser credentials**
3. **Manage recipes**: Add, edit, or delete recipes
4. **Manage ingredients**: Add new ingredients with units
5. **Manage categories**: Organize recipes into categories
6. **View user data** and site analytics

### Creating Content

1. **Add Categories**:
   - Go to admin panel → Categories
   - Click "Add Category"
   - Enter category name and description

2. **Add Ingredients**:
   - Go to admin panel → Ingredients
   - Click "Add Ingredient"
   - Enter ingredient name and unit

3. **Add Recipes**:
   - Go to admin panel → Recipes
   - Click "Add Recipe"
   - Fill in recipe details, ingredients, and instructions

## 🗄️ Database Schema

### Models Overview

**Recipe Model**:
- Title, description, instructions
- Cooking time, servings
- Category (ForeignKey)
- Ingredients (ManyToMany)
- Created/updated timestamps

**Ingredient Model**:
- Name, unit
- Nutritional information (optional)

**Category Model**:
- Name, description
- Color coding (optional)

## 🔧 Development

### Adding New Features

1. **Create feature branch**
   ```bash
   git checkout -b feature/new-feature-name
   ```

2. **Make changes and test locally**
   ```bash
   python src/manage.py runserver
   ```

3. **Run tests** (if available)
   ```bash
   python src/manage.py test
   ```

4. **Commit and push**
   ```bash
   git add .
   git commit -m "Add new feature"
   git push origin feature/new-feature-name
   ```

### Database Migrations

When you modify models:

```bash
# Create migration files
python src/manage.py makemigrations

# Apply migrations locally
python src/manage.py migrate

# Apply migrations to Heroku
heroku run python src/manage.py migrate --app your-app-name
```

## 🐛 Troubleshooting

### Common Issues

1. **Static files not loading**:
   ```bash
   python src/manage.py collectstatic --clear
   ```

2. **Database connection errors**:
   - Check DATABASE_URL environment variable
   - Verify PostgreSQL addon is active

3. **Migration errors**:
   ```bash
   # Check migration status
   python src/manage.py showmigrations
   
   # Force specific migration
   python src/manage.py migrate recipes 0001 --fake
   ```

4. **Heroku deployment issues**:
   ```bash
   # Check logs
   heroku logs --tail --app your-app-name
   
   # Restart app
   heroku restart --app your-app-name
   ```

### Debug Mode

For debugging in production (use carefully):

```bash
heroku config:set DJANGO_DEBUG=True --app your-app-name
# Remember to set it back to False after debugging
heroku config:set DJANGO_DEBUG=False --app your-app-name
```

## 🔒 Security

### Security Measures Implemented

- Django's built-in CSRF protection
- Secure secret key management via environment variables
- Debug mode disabled in production
- WhiteNoise for secure static file serving
- PostgreSQL database with SSL in production

### Security Best Practices

1. **Never commit sensitive data** to version control
2. **Use environment variables** for all secrets
3. **Keep dependencies updated** regularly
4. **Monitor for security vulnerabilities**
5. **Use HTTPS** in production (handled by Heroku)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Jadefangg**
- GitHub: [@Jadefangg](https://github.com/Jadefangg)

## 🙏 Acknowledgments

- Django Documentation and Community
- Heroku for hosting platform
- Bootstrap for UI components
- All contributors who helped improve this project

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/Jadefangg/recipe-app-final/issues) page
2. Create a new issue with detailed description
3. Include steps to reproduce the problem
4. Provide relevant error messages and logs

---

**Happy Cooking! 🍳**
