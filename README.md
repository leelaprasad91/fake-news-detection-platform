# Fake News Detection Platform
Educational full-stack prototype: React + Spring Boot + FastAPI + scikit-learn.

IMPORTANT: The bundled model uses tiny synthetic examples. It is a wiring/demo model, not a reliable fact-checker. Do not treat its label or score as proof.

## Run locally
1. ML service: `cd ml-service`; create/activate a venv; `pip install -r requirements.txt`; `python train_model.py`; `python -m uvicorn app:app --reload --port 8000`.
2. Backend: use Java 17 and Gradle; from `backend`, run `gradle bootRun` (or generate a Gradle wrapper first).
3. Frontend: from `frontend`, run `npm install` then `npm run dev`; open the URL printed by Vite.

Backend defaults to an in-memory H2 database so it can run without MySQL. To use MySQL, set `SPRING_DATASOURCE_URL`, `SPRING_DATASOURCE_USERNAME`, `SPRING_DATASOURCE_PASSWORD`, and `SPRING_DATASOURCE_DRIVER=com.mysql.cj.jdbc.Driver`.

For deployment, deploy frontend, backend, and ML service separately, configure `VITE_API_URL` and `ML_SERVICE_URL`, and use a managed MySQL database. A live URL requires hosting accounts and deployment steps; this source archive does not itself deploy the app.

GitHub repository: https://github.com/leelaprasad91/fake-news-detection-platform
