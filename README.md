# Simple Photo App

### Base
    
    Simple backend application for managing photos.
    Project URLS:
        - Base CRUD for Photo model: http://0.0.0.0:8000/api/photos/
        - Get photos meta from external API - http://0.0.0.0:8000/api/external/url/
        - Parse JSON file - http://0.0.0.0:8000/api/external/json/
    
    Project:
        - is based on Docker
        - uses Poetry as packages manager


### Building

Project is operated via Makefile. Base commands are presented below:

Docker

    $ make up          # Create and start container
    $ make console     # Opens main app container
    $ make build       # Build or rebuild services (force-recreate, no-cache and others omitted)
Django & scripts

    $ make migrations  # Django Migrations
    $ make url         # Get data from specified url (check scripts/client.py)
    $ make json        # Get data from specified Json file (check scripts/file_client.py)
Tests
    
    $ make test        # Run unittests 

