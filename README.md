# **NoiseNab_2**

**NoiseNab_2** is a comprehensive project designed to be an innovative web-based platform that leverages
crowdsourced data and machine learning (**ML**) to provide a real-time, intelligent noise mapping solution. This repository encompasses three main components:

---

## **Prerequisites**

Before setting up the project, ensure you have the following installed on your system:

- **[Node.js](https://nodejs.org/en/download/)**
- **npm**
- **[Python 3.x](https://www.python.org/downloads/)**
- **[virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)**

---

## **Project Structure**

The repository is organized as follows:

- `frontend/` : Contains the **React-based** frontend application.
- `backend/` : Contains the **Node.js** backend server.
- `Noisemap_gen/Satindustry/` : Contains the **Django-based** noise generation map application.

---

## **Setup and Installation**

### **Initializing the Noise Generation Environment**

To set up the noise generation environment, follow these steps:

1. **Navigate to the project directory:**
   ```bash
   cd /path/to/NoiseNab_2/Noisemap_gen/Satindustry
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv Satindustry
   source Satindustry/bin/activate
   ```

3. **Set the `PYTHONPATH` environment variable:**
   ```bash
   export PYTHONPATH=/path/to/NoiseNab_2/Noisemap_gen/Satindustry
   ```

4. **Navigate to the `Satindustry` directory:**
   ```bash
   cd Satindustry
   ```

5. **Install the required Python packages (only needed during the first setup):**
   ```bash
   pip install -r requirements.txt
   ```

6. **Apply database migrations (optional but recommended):**
   ```bash
   python manage.py migrate
   ```

7. **Start the Django development server:**
   ```bash
   python manage.py runserver
   ```

---

## **Running the Project**

The project comprises three main components that should be run in separate terminal windows or tabs:

### **Terminal 1: Running the Frontend**
```bash
cd /path/to/NoiseNab_2/frontend
npm install  # Only needed during the first setup
npm start
```

### **Terminal 2: Running the Noise Generation Map**
```bash
cd /path/to/NoiseNab_2/Noisemap_gen/Satindustry
source Satindustry/bin/activate
export PYTHONPATH=/path/to/NoiseNab_2/Noisemap_gen/Satindustry
cd Satindustry
python manage.py runserver
```

### **Terminal 3: Running the Backend**
```bash
cd /path/to/NoiseNab_2/backend
npm install  # Only needed during the first setup
node server.js
```

**Note:** Ensure that each component is running in its respective terminal to allow seamless interaction between the frontend, backend, and noise generation map.

---

## **Usage**

![Noise Map Interface](https://github.com/user-attachments/assets/931dd236-3566-433f-a788-8304d4fbac58)
![Data Processing](https://github.com/user-attachments/assets/4f89aecf-62e0-494c-b774-61e9f6b2c68a)
![ML Analysis](https://github.com/user-attachments/assets/33cec25c-f544-4cc5-9109-a908e8e70a46)
![Visualization](https://github.com/user-attachments/assets/67735d3e-12ab-4e6b-9e04-7328af5a9570)

---

## **Contributing**

We welcome contributions to enhance **NoiseNab_2**. To contribute, please follow these steps:

1. **Fork** the repository.
2. **Create** a new branch for your feature or bugfix.
3. **Commit** your changes with clear and concise messages.
4. **Push** your changes to your fork.
5. **Submit** a pull request detailing your changes.

For more information, please refer to our **contribution guidelines**.

---

## **License**

This project is licensed under the **MIT License**.

---

## **Contact**

For any questions or inquiries, please contact **Yash Kaushik** at **leviiiop7@gmail.com**.
