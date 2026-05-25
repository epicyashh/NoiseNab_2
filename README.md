# NoiseNab

A crowdsourced noise mapping platform that helps monitor urban noise pollution in real-time. Users submit noise level reports with location data, which are aggregated into interactive noise maps to identify hotspots and support urban planning decisions.

## Tech Stack

| Service | Technology | Port |
|---------|-----------|------|
| Frontend | React 19, Leaflet, React Router | 3000 |
| Backend | Node.js, Express, Mongoose | 5001 |
| Noisemap | Django 5.1, Django REST Framework | 8000 |
| Database | MongoDB Atlas | Cloud |

## Project Structure

```
NoiseNab/
├── frontend/          React SPA (data entry, landing page, maps)
├── backend/           Express API (noise report submission)
├── noisemap/          Django service (noise data queries & map generation)
├── scripts/           Utility scripts (data import, geocoding)
├── render.yaml        Render deployment blueprint
└── README.md
```

## Local Development

### Prerequisites

- Node.js 18+
- Python 3.11+
- MongoDB Atlas account (or local MongoDB)

### 1. Clone & configure environment

```bash
git clone <repo-url>
cd NoiseNab

# Copy environment templates and fill in your values
cp frontend/.env.example frontend/.env
cp backend/.env.example backend/.env
cp noisemap/.env.example noisemap/.env
```

### 2. Start the Backend (Terminal 1)

```bash
cd backend
npm install
npm start
```

### 3. Start the Django Service (Terminal 2)

```bash
cd noisemap
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### 4. Start the Frontend (Terminal 3)

```bash
cd frontend
npm install
npm start
```

The app will be available at `http://localhost:3000`.

## Environment Variables

### Frontend (`frontend/.env`)
| Variable | Description |
|----------|-------------|
| `REACT_APP_BACKEND_URL` | Express API URL (default: `http://localhost:5001`) |
| `REACT_APP_DJANGO_URL` | Django service URL (default: `http://127.0.0.1:8000`) |

### Backend (`backend/.env`)
| Variable | Description |
|----------|-------------|
| `MONGO_URI` | MongoDB connection string |
| `PORT` | Server port (default: `5001`) |

### Noisemap (`noisemap/.env`)
| Variable | Description |
|----------|-------------|
| `DJANGO_SECRET_KEY` | Django secret key |
| `MONGO_URI` | MongoDB connection string |
| `DEBUG` | Debug mode (`True`/`False`) |
| `ALLOWED_HOSTS` | Comma-separated allowed hosts |
| `CORS_ALLOWED_ORIGINS` | Comma-separated CORS origins |

## Deployment (Render)

This project includes a `render.yaml` blueprint for one-click deployment to Render:

1. Push this repo to GitHub
2. Go to [Render Dashboard](https://dashboard.render.com) > **New** > **Blueprint**
3. Connect your GitHub repo
4. Render will detect `render.yaml` and create all 3 services
5. Set the environment variables (especially `MONGO_URI` and `CORS_ALLOWED_ORIGINS`)
6. Deploy

## API Endpoints

### Backend (Express)
- `POST /api/noise/report` — Submit a noise report
- `GET /api/health` — Health check

### Noisemap (Django)
- `GET /data/` — Noise data search interface
- `GET /fetch-noise-data/?location=<city>` — Query noise data by location

## Contact

For questions or inquiries, contact **Yash Kaushik** at **leviiiop7@gmail.com**.

## License

MIT License
