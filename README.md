# Golf Battle-Buddy Web Application

A Flask-based web application for managing golf tee times and calendar.

## Application Structure

```
golfbbappv1/
├── app.py                      # Flask application entry point
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker container configuration
├── .dockerignore              # Files to exclude from Docker build
├── templates/
│   └── golfbbappv1.html       # Main HTML template
└── README.md                   # This file
```

## Local Development

### Prerequisites
- Python 3.12 or higher
- pip (Python package manager)

### Setup and Run

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the development server:**
   ```bash
   python app.py
   ```

3. **Access the application:**
   Open your browser and navigate to: `http://localhost:8080`

## Deployment Options

### Option 1: Deploy to Google Cloud Run (Recommended)

Google Cloud Run is a serverless platform that automatically scales your containerized application.

#### Prerequisites
- Google Cloud account
- [gcloud CLI](https://cloud.google.com/sdk/docs/install) installed and configured
- Docker installed (for local testing)

#### Deployment Steps

1. **Set your Google Cloud project:**
   ```bash
   gcloud config set project YOUR_PROJECT_ID
   ```

2. **Enable required APIs:**
   ```bash
   gcloud services enable run.googleapis.com
   gcloud services enable cloudbuild.googleapis.com
   ```

3. **Deploy directly to Cloud Run (without local Docker build):**
   ```bash
   gcloud run deploy golfbb-app \
     --source . \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated \
     --port 8080
   ```

   This command will:
   - Build your container using Cloud Build
   - Deploy it to Cloud Run
   - Generate a public URL for your application

4. **Access your deployed application:**
   After deployment, Cloud Run will provide a URL like:
   `https://golfbb-app-xxxxxxxxxx-uc.a.run.app`

#### Update Deployment
To update your deployed application:
```bash
gcloud run deploy golfbb-app \
  --source . \
  --platform managed \
  --region us-central1
```

### Option 2: Deploy to Google Cloud Run (with Docker)

If you prefer to build and test the Docker image locally first:

1. **Build the Docker image:**
   ```bash
   docker build -t gcr.io/YOUR_PROJECT_ID/golfbb-app .
   ```

2. **Test locally:**
   ```bash
   docker run -p 8080:8080 gcr.io/YOUR_PROJECT_ID/golfbb-app
   ```
   Access at `http://localhost:8080`

3. **Push to Google Container Registry:**
   ```bash
   docker push gcr.io/YOUR_PROJECT_ID/golfbb-app
   ```

4. **Deploy to Cloud Run:**
   ```bash
   gcloud run deploy golfbb-app \
     --image gcr.io/YOUR_PROJECT_ID/golfbb-app \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated \
     --port 8080
   ```

### Option 3: Deploy to Heroku

1. **Install Heroku CLI and login:**
   ```bash
   heroku login
   ```

2. **Create a new Heroku app:**
   ```bash
   heroku create your-app-name
   ```

3. **Deploy using Git:**
   ```bash
   git push heroku main
   ```

4. **Open your app:**
   ```bash
   heroku open
   ```

### Option 4: Deploy with Docker to any platform

The application is containerized and can be deployed to any platform that supports Docker:

- **AWS ECS/Fargate**
- **Azure Container Instances**
- **DigitalOcean App Platform**
- **Fly.io**
- **Railway**
- **Render**

Basic steps for most platforms:
1. Build the Docker image
2. Push to the platform's container registry (or use Docker Hub)
3. Deploy the container with port 8080 exposed

## Environment Variables

The application uses the following environment variables:

- `PORT`: The port the application runs on (default: 8080)
- `FLASK_APP`: Flask application entry point (default: app.py)

## Production Considerations

- ✅ Uses `gunicorn` as production WSGI server
- ✅ Configured for Cloud Run with appropriate port binding
- ✅ Containerized for consistent deployment
- ⚠️ Consider adding:
  - Database for persistent data storage
  - Authentication/authorization for user management
  - HTTPS/SSL certificates (Cloud Run provides this automatically)
  - Environment-based configuration
  - Logging and monitoring
  - Rate limiting and security headers

## Troubleshooting

### Template Not Found Error
If you see `TemplateNotFound: golfbbappv1.html`, ensure:
- The `templates/` directory exists
- The file `golfbbappv1.html` is in the `templates/` directory
- The filename in `app.py` matches exactly

### Port Binding Issues
Cloud Run automatically sets the `PORT` environment variable. The application is configured to use port 8080 by default, which works with Cloud Run.

### Docker Build Fails
Ensure you're in the project root directory where the Dockerfile is located.

## Support

For issues or questions, please open an issue on the GitHub repository.

## License

This project is provided as-is for educational and demonstration purposes.
