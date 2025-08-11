# MCP Test App

A simple Flask application for testing Model Context Protocol (MCP) DevOps capabilities.

## Features

- Simple Flask web application
- Docker containerization
- GitHub Actions CI/CD pipeline
- Health check endpoints
- Docker Compose for local development

## API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check endpoint
- `GET /api/info` - Application information

## Local Development

### Using Python directly
```bash
pip install -r requirements.txt
python app.py
```

### Using Docker
```bash
docker build -t mcp-test-app .
docker run -p 5000:5000 mcp-test-app
```

### Using Docker Compose
```bash
docker-compose up --build
```

## CI/CD Pipeline

The GitHub Actions workflow automatically:

1. **Test** - Runs linting and basic tests
2. **Build** - Creates Docker image
3. **Push** - Pushes to GitHub Container Registry
4. **Deploy** - Ready for deployment (placeholder)

### Container Registry

Images are pushed to: `ghcr.io/hvsssen/mcp-test-app`

Available tags:
- `latest` - Latest from master branch
- `master-<sha>` - Specific commit from master
- `<branch>` - Branch-specific builds

## Environment Variables

- `PORT` - Port to run the app (default: 5000)
- `DEBUG` - Enable debug mode (default: false)
- `ENVIRONMENT` - Environment name (default: development)

## Health Check

The application includes a health check endpoint at `/health` that returns:

```json
{
  "status": "healthy",
  "version": "1.0.0",
  "service": "mcp-test-app"
}
```

## Deployment

To deploy this application:

1. Pull the image: `docker pull ghcr.io/hvsssen/mcp-test-app:latest`
2. Run: `docker run -p 5000:5000 ghcr.io/hvsssen/mcp-test-app:latest`

Or use the provided docker-compose.yml for easier management.
