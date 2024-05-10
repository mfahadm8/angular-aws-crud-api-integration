# Tim: User CRUD Frontend with REST API

This project is an Angular 17 CRUD example app designed to consume REST APIs, display, modify, and search data.

## Features
- **User Management:** Each user has an `id`, `name`, `address`, and `age`.
- **CRUD Operations:** Users can be created, retrieved and updated.
- **Search Functionality:** A search bar is available to find users by name.

## Local Setup Instructions
Follow these steps to set up the project locally:

### Prerequisites
1. **Node.js**: Download and install from [Node.js Downloads](https://nodejs.org/en/download/current).
2. **Git**: Download and install from [Git Downloads](https://git-scm.com/downloads).

### Running the Application
3. Clone the repository:
    ```bash
    git clone https://(github link)  # Replace with your repository link
    ```
4. Navigate to the frontend directory and install dependencies:
    ```bash
    cd frontend
    npm install
    ```
5. Start the application:
    ```bash
    npm run start
    ```
    - The server will start on port 4200.
    - Access the application via [http://localhost:4200](http://localhost:4200).

## Cloud Deployment
To update the frontend in the cloud, follow these steps:

1. Ensure AWS CLI is installed and configured:
    ```bash
    aws configure
    ```
2. Run the cloud deployment script:
    ```bash
    bash ./push-to-cloud.sh
    ```
    - Note: Make sure you have the necessary permissions and configurations set up in AWS for deployment.

This documentation ensures that you have all the information needed to get started with the project locally and how to deploy it to the cloud if needed.
