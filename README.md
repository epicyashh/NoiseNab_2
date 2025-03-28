NoiseNab_2
NoiseNab_2 is a comprehensive project designed to an innovative web-based platform that leverages
crowdsourced data and machine learning (ML) to provide a real-time, intelligent noise mapping
solution. This repository encompasses three main components:

Prerequisites
Before setting up the project, ensure you have the following installed on your system:
Node.js
npm
Python 3.x
virtualenv

Project Structure
The repository is organized as follows:
frontend/: Contains the React-based frontend application.
backend/: Contains the Node.js backend server.
Noisemap_gen/Satindustry/: Contains the Django-based noise generation map application.

Setup and Installation
Initializing the Noise Generation Environment
To set up the noise generation environment, follow these steps:

Navigate to the project directory:
cd /path/to/NoiseNab_2/Noisemap_gen/Satindustry

Create and activate a virtual environment:
python -m venv Satindustry
source Satindustry/bin/activate

Set the PYTHONPATH environment variable:
export PYTHONPATH=/path/to/NoiseNab_2/Noisemap_gen/Satindustry

Navigate to the Satindustry directory:
cd Satindustry

Install the required Python packages (only needed during the first setup):
pip install -r requirements.txt

Apply database migrations (optional but recommended):
python manage.py migrate

Start the Django development server:
python manage.py runserver


Running the Project
The project comprises three main components that should be run in separate terminal windows or tabs:

Terminal 1: Running the Frontend
cd /path/to/NoiseNab_2/frontend
npm install  # Only needed during the first setup
npm start


Terminal 2: Running the Noise Generation Map
cd /path/to/NoiseNab_2/Noisemap_gen/Satindustry
source Satindustry/bin/activate
export PYTHONPATH=/path/to/NoiseNab_2/Noisemap_gen/Satindustry
cd Satindustry
python manage.py runserver


Terminal 3: Running the Backend
cd /path/to/NoiseNab_2/backend
npm install  # Only needed during the first setup
node server.js

Note: Ensure that each component is running in its respective terminal to allow seamless interaction between the frontend, backend, and noise generation map.

Usage
![image](https://github.com/user-attachments/assets/931dd236-3566-433f-a788-8304d4fbac58)
![image](https://github.com/user-attachments/assets/4f89aecf-62e0-494c-b774-61e9f6b2c68a)
![image](https://github.com/user-attachments/assets/33cec25c-f544-4cc5-9109-a908e8e70a46)
![image](https://github.com/user-attachments/assets/67735d3e-12ab-4e6b-9e04-7328af5a9570)


Contributing
We welcome contributions to enhance NoiseNab_2. To contribute, please follow these steps:

Fork the repository.
Create a new branch for your feature or bugfix.
Commit your changes with clear and concise messages.
Push your changes to your fork.
Submit a pull request detailing your changes.
For more information, please refer to our contribution guidelines.

License
This project is licensed under the MIT License.

Contact
For any questions or inquiries, please contact Yash Kaushik at leviiiop7@gmail.com.
