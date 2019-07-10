
# Forsa.om
Forsa is an open-source opportunity discovery platform for Omanis built using Django.

### Development
Currently, Forsa is undergoing heavy development. Things will break. Things will change fast. Best practices are followed where feasible, but the eventual goal is to build a functional MVP before expanding the code base.

If you'd like to support the development of this project, you may create issues with suggestions or create pull requests with features that you'd like to implement.

### Environment Variables
While developing or deploying Forsa, the following environment variables must be declared.

    ENVIRONMENT='DEVELOPMENT' # Additional Options are STAGING and PRODUCTION
    DJANGO_SECRET_KEY='' # Generate this randomly
    DJANGO_DEBUG='yes' # Set to no if in production environment
    DJANGO_TEMPLATE_DEBUG='yes' # Set to no if in production environment
    DATABASE_URL='postgres://postgres:postgres@localhost:5432/forsa'
    DJANGO_AWS_ACCESS_KEY_ID=''
    DJANGO_AWS_SECRET_ACCESS_KEY=''
    DJANGO_AWS_STORAGE_BUCKET_NAME=''
