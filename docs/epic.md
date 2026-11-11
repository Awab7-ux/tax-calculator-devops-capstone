# Epic: Modernize the Tax Calculator to a cloud-native app with CI/CD

## Goal

Deliver a containerized tax calculator that can be built, tested, and deployed
repeatably to IBM Cloud, with automated quality checks and deployment on changes
to the main branch.

## Outcomes

- A small, secure-by-default container image runs the Flask application.
- Tests and lint checks gate changes before an image is built.
- A successful change to `main` is deployed to IBM Cloud Code Engine.
- Kubernetes and Tekton manifests document alternative deployment and delivery
  paths.

## Scope

The calculator is a demonstration of delivery practices. Its static tax brackets
are illustrative and must be reviewed for the intended jurisdiction and tax year
before production use.