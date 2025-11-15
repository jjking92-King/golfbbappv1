# Golf Battle-Buddy

A Flask-based web application for managing golf tee times and coordinating with fellow golfers.

## Features

- **Tee Time Management**: Create and join tee time groups
- **User Authentication**: Simple login system for personalized experience
- **Event Calendar**: View upcoming golf events and tournaments
- **Skill-Based Matching**: Join groups based on skill level (Beginner, Intermediate, Advanced)
- **Responsive Design**: Mobile-friendly interface using Tailwind CSS

## Technology Stack

- **Backend**: Flask 3.1.2 (Python web framework)
- **Frontend**: HTML5, Tailwind CSS, JavaScript
- **Production Server**: Gunicorn 23.0.0
- **Deployment**: Optimized for cloud deployment (Heroku, Cloud Run, etc.)

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/jjking92-King/golfbbappv1.git
cd golfbbappv1
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://localhost:8080
```

## Deployment

### Using Gunicorn (Production)

```bash
gunicorn app:app --bind 0.0.0.0:8080
```

### Using Heroku

The application is fully configured for Heroku deployment with:
- `Procfile` - Defines the web process using Gunicorn
- `runtime.txt` - Specifies Python 3.12.3
- `requirements.txt` - Production dependencies only (Flask, Gunicorn)
- `app.json` - App metadata for Heroku

#### Deploy to Heroku

1. Create a Heroku app:
```bash
heroku create your-app-name
```

2. Deploy:
```bash
git push heroku main
```

3. Open your app:
```bash
heroku open
```

The app will automatically use the correct port assigned by Heroku through the `$PORT` environment variable.

### Using Google Cloud Run

The application is configured to work with containerized environments like Cloud Run, which automatically uses port 8080.

## Project Structure

```
golfbbappv1/
├── app.py                  # Flask application entry point
├── requirements.txt        # Production dependencies (Flask, Gunicorn)
├── requirements-dev.txt    # Development dependencies (includes pytest)
├── Procfile               # Heroku web process configuration
├── runtime.txt            # Python version for Heroku
├── app.json               # Heroku app metadata
├── pytest.ini             # Pytest configuration
├── test_app.py            # Test suite (20 comprehensive tests)
├── .gitignore             # Git ignore rules
├── templates/             # HTML templates
│   └── golfbbappv1.html  # Main application template
├── TEST_RESULTS.md        # Detailed test results and coverage
└── README.md              # This file
```

## Usage

1. **Login**: Click the Login button to create a session
2. **Create Tee Time**: Fill out the form with your details and preferred time
3. **Join Groups**: Browse available tee times and join groups that match your skill level
4. **View Events**: Check the Calendar section for upcoming tournaments and events

## Development

The application runs in debug mode by default when using `python app.py`. For production deployments, use Gunicorn or another production WSGI server.

### Development Setup

For local development with testing capabilities:

```bash
pip install -r requirements-dev.txt
```

This installs both production dependencies (Flask, Gunicorn) and development/testing dependencies (pytest, pytest-cov).

## Testing

The application includes a comprehensive test suite using pytest.

### Running Tests

1. Install development dependencies (includes test dependencies):
```bash
pip install -r requirements-dev.txt
```

2. Run all tests:
```bash
pytest test_app.py -v
```

3. Run tests with coverage report:
```bash
pytest test_app.py --cov=app --cov-report=term-missing -v
```

### Test Coverage

The test suite includes:
- **20 comprehensive tests** covering routes, templates, configuration, and HTTP methods
- **86% code coverage** of the application code
- **100% pass rate** - all tests passing

See [TEST_RESULTS.md](TEST_RESULTS.md) for detailed test results and coverage information.

## License

This project is available for personal and educational use.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
