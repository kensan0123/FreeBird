# FreeBird

## OverView

FreeBird is Text Editor with AI Assistant like "Cursor", but this service focuses on Article Writing not Code Writing, and working on Your Browser.

### Background

Many Engineers, Students or Bussines Persons write something to publish (Posts in X, Blogs, Reports, ...).
I (Kensuke Nakamura - founder of this repo) want to make them easier to write or to improve them.

### How to use

When user push "Suggest" button, AI Assistant read all content in current article and returns Suggestion to improve it (That's all).

## For Developers

### Technology Stack

- Frontend

  - To be decided...

- Backend

  - Python
  - FastAPI
  - SQLAlchemy
  - Ruff

- Database

  - PostgreSQL

- Infrastructure

  - Docker

### Setup

1. Clone

   `git clone https://github.com/kensan0123/FreeBird.git`

2. Set Enviroment variables

   Open `.env`.

   ```
   OPENAI_API_KEY=sk-your-openai-api-key-here

   GITHUB_PAT=ghp_your-github-personal-access-token
   GITHUB_USER=your-github-username

   USER_NAME=Your Name
   USER_EMAIL=your.email@example.com

   ARTICLE_DIR=/app/articles

   POSTGRES_USER=your-db-user-name
   POSTGRES_PASSWORD=your-db-password
   POSTGRES_DB=your-db-name
   ```

   > note
   > Variables related to GitHub is bad influence from old project.
   > Soon Remove this.

3. Compose up

   `docker-compose up --build`

### Contributing

We welcome contributions!

### Branch Strategy

- `main` - Production-ready code
- `feat/<feature-name>/<issue_num>` - New features
- `fix/<issue-description>/<issue_num>` - Bug fixes
- `refactor/<description>/<issue_num>` - Code refactoring
- `docs/<description>/<issue_num>` - Documentation updates

> warning
> **Important**: Never commit directly to the `main` branch.

### API Endpoint

- Health Check

  - Request

    `curl http://localhost:8000/`

  - Response

    ```
    {
      "status": "ok",
      "message": "This is FreeBird App.",
      "version": "1.0.0"
    }
    ```

- Create Session

  - Request

  `curl http://localhost:8000/assist/begin`

  - Response

    ```
    {
      "status": "success",
      "session_id": 124567890...,
    }
    ```

- Generate Suggestion

  - Request

  `curl http://localhost:8000/assist/suggest`

  - Response

    ```
    {
      "suggestions": [
        {
          "suggestion_id": "string",
          "type": "structure",
          "title": "string",
          "description": "string",
          "priority": 0
        }
      ],
      "related_links": [
        {
          "title": "string",
          "url": "string"
        }
      ],
      "summary_report": "string"
    }
    ```

## License

MIT License
