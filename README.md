# GMRI Curriculum Platform

One-stop shopping to find and access all of GMRI's curriculum. 
[https://teach.gmri.org](https://teach.gmri.org)

## Getting Started

Clone the repository. As it exists it uses Docker for development and Kubernetes in production. It is also built to use an S3-compatible object storage method.

### Prerequisites

You will need to create a root-level directory called docker-data which contains a `django-static` directory and `secret.env` file.

*** Template for secret.env ***

```
POSTGRES_PASSWORD=xxxxx
POSTGRES_USER=xxxxx
POSTGRES_NAME=xxxxx
POSTGRES_HOST=xxxxx
POSTGRES_PORT=xxxxx

SECRET_KEY=xxxxx
DJANGO_MANAGEPY_COLLECTSTATIC=on
DJANGO_SETTINGS_MODULE=curriculum_platform.settings.dev

CURRICULUM_ENV=dev

AWS_ACCESS_KEY_ID=xxxxx
AWS_SECRET_ACCESS_KEY=xxxxx
AWS_S3_ENDPOINT_URL=xxxxx
AWS_S3_CUSTOM_DOMAIN=xxxxx
AWS_S3_REGION_NAME=xxxxx
AWS_STORAGE_BUCKET_NAME=xxxxx
```

### Installing

Once you have cloned the repository & set up the docker-data directory, you should be good to go. 

```
make up

make migrations

make migrate

make superuser

make static 
```

## Running the tests

Coming soon

## Deployment

Deploment should be simple 

```
skaffold run 
```

I like to add the `--tail` flag to my skaffold command to verify that things are working properly, and to help troubleshoot if not. 

## Built With

* [Django](https://docs.djangoproject.com/en/3.0/) - The web framework used
* [Wagtail](https://docs.wagtail.io/en/stable/) - Content Management
* [Angular](https://angular.io/docs) - Used to produce search functionality

## Authors

* **Seth Dresser** - *Initial work* 

