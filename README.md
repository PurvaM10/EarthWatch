# 🌍 Nagpur EarthWatch — Urban Change Intelligence

EarthWatch is a web-based geospatial project designed to identify and analyze potential urban changes around Nagpur, Maharashtra. It compares satellite imagery from different dates, highlights areas that may have changed, and helps users investigate candidate construction hotspots.

> **Note:** EarthWatch detects potential changes in imagery; it does not independently confirm illegal construction. All findings require further verification.

## ✨ Features

- 📍 **Location Search:** Search for a place or geographic coordinates.
- 🛰️ **Satellite Imagery:** Retrieve Sentinel-2 imagery for different dates.
- 🔍 **Change Detection:** Compare before-and-after satellite images.
- 🗺️ **Change Visualization:** Generate change masks and image overlays.
- 📡 **Historical Imagery:** Check Esri Wayback imagery availability.
- 🚨 **Hotspot Detection:** Identify candidate regions for further investigation.
- 🔬 **Detailed Inspection:** Investigate hotspots through a zoom-and-verify workflow.
- 📊 **Interactive Dashboard:** View results through a React and Leaflet interface.
- ⚙️ **REST API:** Access backend functionality through FastAPI.

## 🧰 Technology Stack

### Frontend
- React
- Vite
- Leaflet
- React Leaflet

### Backend
- Python
- FastAPI
- Uvicorn

### Image Processing
- OpenCV
- NumPy
- scikit-image
- Sentinel Hub Python client

### Satellite Data Sources
- [Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu/)
- [Sentinel-2](https://dataspace.copernicus.eu/explore-data/data-collections/sentinel-data)
- [Esri World Imagery / Wayback](https://livingatlas.arcgis.com/wayback/)

## 📁 Project Structure

```text
EarthWatch/
├── backend/
│   ├── agent/
│   ├── static/
│   ├── vision/
│   ├── config.py
│   ├── geocoding.py
│   ├── hotspots.py
│   ├── locations_data.py
│   ├── main.py
│   ├── pipeline.py
│   ├── vision_inspector.py
│   ├── wayback_live.py
│   └── wayback_crop.py
├── public/
├── src/
├── .env.example
├── package.json
├── search_catalog.py
└── README.md
```

## ⚙️ Prerequisites

Before running EarthWatch, install:

- Python
- Node.js and npm
- Git
- A Copernicus Data Space account with Sentinel Hub OAuth credentials
- Required Python and JavaScript dependencies

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/dhanshrii2006/EarthWatch.git
cd EarthWatch
```

### 2. Configure environment variables

Create a `.env` file in the project root directory and add your Copernicus credentials:

```env
SH_CLIENT_ID=your_actual_client_id
SH_CLIENT_SECRET=your_actual_client_secret
```

Obtain OAuth credentials from the [Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu/).

Refer to the [Sentinel Hub authentication documentation](https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/Overview/Authentication.html).

**Security:** Never upload your real `.env` file or expose API credentials in public repositories.

### 3. Set up the Python backend

Create a virtual environment:

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the core dependencies:

```powershell
python -m pip install fastapi "uvicorn[standard]" sentinelhub opencv-python numpy scikit-image
```

Install any additional dependencies required by your project in the same environment.

### 4. Install frontend dependencies

From the project root:

```bash
npm install
```

### 5. Start the backend

Run this command from the **EarthWatch root directory**:

```powershell
python -m uvicorn backend.main:app --reload
```

The backend should be available at:

- API: `http://127.0.0.1:8000`
- Swagger documentation: `http://127.0.0.1:8000/docs`
- Health check: `http://127.0.0.1:8000/api/health`

Keep the backend terminal running.

### 6. Start the frontend

Open a second terminal in the project root:

```bash
npm run dev
```

Open the local URL printed by Vite, usually:

```text
http://localhost:5173
```

### 7. Build the frontend

```bash
npm run build
```

## 🔌 API Endpoints

The backend includes routes for functionality such as:

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/health` | Check backend status |
| GET | `/api/locations` | Retrieve preset locations |
| GET | `/api/available-dates` | Find available satellite scenes |
| GET | `/api/wayback-availability` | Check historical imagery availability |
| POST | `/api/analyze` | Analyze before-and-after imagery |
| GET | `/api/hotspots` | Retrieve candidate hotspots |
| POST | `/api/inspect-hotspot` | Inspect a selected hotspot |
| POST | `/api/inspect-all` | Inspect multiple hotspots |
| POST | `/api/agent/run` | Execute the autonomous audit |
| GET | `/api/agent/stream` | Stream audit progress |

For the exact request parameters and response formats, open:

`http://127.0.0.1:8000/docs`

## 🛰️ How EarthWatch Works

1. **Location Resolution:** Convert a place name into geographic coordinates.
2. **Area Selection:** Define the geographic area to investigate.
3. **Satellite Data Retrieval:** Request imagery from the configured data sources.
4. **Image Comparison:** Compare images from different dates.
5. **Change Detection:** Use image differences and SSIM-based structural comparisons.
6. **Mask Generation:** Highlight regions that differ between images.
7. **Hotspot Extraction:** Identify candidate regions for additional investigation.
8. **Detailed Inspection:** Review candidate hotspots using available higher-resolution imagery.
9. **Result Presentation:** Display the analysis through the web interface.

## 📊 Understanding the Results

- **Change Mask:** Highlights pixels identified as different by the selected algorithm.
- **Change Overlay:** Displays candidate changes over an image.
- **Hotspot:** A geographic region selected for further inspection.
- **Autonomous Audit:** Coordinates multiple investigation steps to assess potential changes.

A detected difference is not definitive evidence of illegal construction. Cloud cover, seasonal changes, vegetation, shadows, image resolution, and alignment errors can affect results.

## 🔐 Security and Configuration

The current Sentinel Hub configuration uses:

| Variable | Purpose |
|---|---|
| `SH_CLIENT_ID` | OAuth client ID |
| `SH_CLIENT_SECRET` | OAuth client secret |

Keep credentials in a local `.env` file that is excluded from Git. Never place private API credentials in frontend code or browser-exposed environment variables.

## 🧯 Troubleshooting

### Relative import error

If you see:

```text
ImportError: attempted relative import with no known parent package
```

Run Uvicorn from the project root:

```powershell
python -m uvicorn backend.main:app --reload
```

### Missing Python module

Install the package corresponding to the missing module into the active environment.

For example:

```powershell
python -m pip install sentinelhub scikit-image
```

### Authentication errors

- Verify `SH_CLIENT_ID` and `SH_CLIENT_SECRET`.
- Confirm the OAuth client is active.
- Check the backend terminal for the complete error message.
- Verify that the selected dates and geographic area have available imagery.

### HTTP 500 or a stalled audit

- Inspect the backend terminal for a traceback.
- Open Chrome Developer Tools with `F12`.
- Select **Network**, then inspect the failed request's **Response**.
- Identify the failing pipeline step before replacing API credentials.

## 🛣️ Future Improvements

- Improve satellite image alignment.
- Add cloud and shadow masking.
- Improve hotspot confidence scoring.
- Add automated tests for external API failures.
- Improve reporting and evidence provenance.
- Maintain a reproducible backend dependency file.

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch.
3. Implement and test your changes.
4. Keep credentials and private data out of commits.
5. Submit a pull request describing your changes.

## 📄 License

No license is specified in this README. Add a `LICENSE` file if you intend to define the project's reuse and distribution permissions.

## 👥 Contributors

- [Sharvari2318](https://github.com/Sharvari2318)
- [Manjosh-Lilhare](https://github.com/Manjosh-Lilhare)
- [Shreniknil09](https://github.com/Shreniknil09)
- [ShivamAdmane](https://github.com/ShivamAdmane)

---

**Nagpur EarthWatch** — Supporting geospatial exploration and evidence-informed analysis of urban change.
