**Project Name** - Flask Todo Application with MongoDB

### Overview:
I have developed a Todo Application using Flask and MongoDB as part of my journey into web development. This simple yet functional application allows users to add and delete todo items, and it stores the data in a MongoDB database. The project includes a sleek HTML template for rendering the data and demonstrates how to integrate Flask with MongoDB for efficient data handling.

Additionally, this project is dockerized to ensure easy deployment and isolation of the application's dependencies. By using Docker and Docker Compose, I’ve packaged the Flask application and MongoDB service into containers, providing a consistent development environment that can be easily replicated across different systems. Docker allows me to streamline the development process, as both the app and the database run in separate containers, but they are linked together for communication.

### What I’ve Accomplished:
- **Set up the local development environment**: Configured Docker containers for both Flask and MongoDB, creating an isolated environment for development and ensuring consistency across different machines.
- **Installed Flask and pymongo**: Installed the required packages to use Flask for the web app and pymongo for MongoDB integration.
- **Dockerized MongoDB database**: Set up a MongoDB database in a Docker container, creating a collection specifically for storing todo items while ensuring that the data persists using Docker volumes.
- **Built a functional Flask web application**: Developed routes to add, view, and delete todo items, allowing the user to interact with the database easily, all running within a Docker container.
- **Designed a clean HTML template**: Created an elegant HTML layout to display todo items beautifully and provide an intuitive user experience.
- **Implemented add and delete functionality**: Created Flask routes that handle adding new tasks and deleting existing ones from the MongoDB collection.
- **Ran and tested the application locally**: Verified that the app works perfectly by running it on my local machine and testing all routes and also in docker containers. 

### Tools & Technologies Used:
- **Flask**: Lightweight Python framework used to build the web application.
- **MongoDB**: NoSQL database used for storing todo items.
- **pymongo**: MongoDB driver for Python, used to interact with the database.
- **HTML/CSS**: Designed the front-end of the application.
- **Docker**: Used for containerizing both the Flask app and MongoDB database, enabling easy deployment and consistent development environments

### What I’ve Learned:
- How to integrate Flask with MongoDB for data storage.
- Building web applications from scratch, including frontend and backend.
- Setting up routes for CRUD (Create, Read, Update, Delete) operations in a Flask app.
- Enhancing user experience by designing a clean, functional UI for interacting with the app.
- How to dockerize and create docker images and containers for a flask and MongoDB app. 
