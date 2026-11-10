# Project overview
React frontend → Spring Boot REST API → FastAPI ML service → scikit-learn pipeline.
Spring Boot stores prediction history using JPA. H2 is the local default; MySQL is supported through datasource environment variables.
Next improvements: use a properly sourced labelled dataset; compare Logistic Regression, Naive Bayes and Linear SVM; add authentication and user-scoped history; add tests and deployment monitoring.
