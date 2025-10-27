# 🌸 SAWWAH — Discover Saudi Arabia Digitally  

**SAWWAH** is a comprehensive digital tourism platform that redefines how visitors explore Saudi Arabia.  
It combines modern technology with authentic Saudi heritage to provide a seamless and engaging tourism experience aligned with **Vision 2030**.  

---

##  Overview  

SAWWAH allows users to explore **cities, cultural figures, and national projects** across the Kingdom of Saudi Arabia.  
The platform highlights the beauty, diversity, and history of the Kingdom while leveraging modern web technologies to present data interactively and intuitively.  

### ✨ Key Highlights  
- **+150** Tourist Destinations  
- **+100** Notable Figures  
- **5** Major Tourist Cities  
- **+30** Vision 2030 Projects  
- **Lavender Theme** — Inspired by Saudi Arabia’s official color for welcoming guests, representing elegance and harmony with the desert landscape.  

---

## 🎯 Project Goals  

1. **Enhance Saudi Tourism**  
   Build a modern digital platform that merges innovation and culture to serve both visitors and investors.  

2. **Improve Visitor Experience**  
   Provide detailed and organized information about destinations, figures, and national initiatives.  

3. **Support Vision 2030**  
   Contribute to Saudi Arabia’s vision of becoming a leading global tourism destination.  

---

## 🧩 Features  

- Interactive exploration of **tourism destinations** by city  
- Profiles of **historical and cultural figures**  
- Overview of **Vision 2030 projects**  
- Fully responsive **Flask-based web interface**  
- Clean and elegant **UI with lavender accents**  

---
## 🗂️ Project Structure
## Project Structure

```text
SAWWAH/
├── data/
│   ├── raw/
│   │   ├── English_Characters.xlsx
│   │   ├── English_Cities.xlsx
│   │   └── English_Projects.csv
│   └── cleaned/
│       ├── English_Characters_Cleaned.xlsx
│       ├── English_Cities_Cleaned.xlsx
│       └── English_Projects_Cleaned.xlsx
├── notebooks/
│   ├── Data_Cleaning_and_Preprocessing.ipynb
│   ├── RAG_Evaluation.ipynb
│   ├── RAG_Speech.ipynb
│   ├── Sawwah_Dashboard.ipynb
│   └── Sawwah_EDA.ipynb
├── report/
│   └── Sawwah_final_report.pdf
├── results/
│   ├── Human Evaluation.xlsx
│   ├── rag_evaluation_results_relevant_and_accuracy.xlsx
│   └── rag_evaluation_results.csv
├── web_app/
│   ├── app.py
│   ├── requirements.txt
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   │   └── script.js
│   │   └── images/
│   │       ├── bg.jpg
│   │       └── sawwah_logo.png
│   └── templates/
│       ├── about.html
│       ├── base.html
│       ├── camera.html
│       ├── data.html
│       ├── project.html
│       └── why.html
└── README.md
```

📁 Folder summary
- data/: raw source files and cleaned datasets used by the app and notebooks.
- notebooks/: Jupyter notebooks for preprocessing, RAG experiments, dashboard work, and EDA.
- report/: final project report.
- results/: evaluation outputs and spreadsheets.
- web_app/: Flask application, static assets, and templates.
- README.md: project documentation.


---
  
## 🗂️ Dataset  

The platform utilizes three structured datasets stored as CSV/Excel files:  

| Dataset | Description |
|----------|-------------|
| **Cities** | Contains information about Saudi cities and key destinations |
| **Characters** | Includes profiles of notable Saudi figures |
| **Projects** | Covers Vision 2030 projects and their descriptions |

All datasets were **cleaned and processed** in Python to ensure accuracy, consistency, and readability.  

---

## 🛠️ Tech Stack  

| Category | Technologies |
|-----------|---------------|
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | Python (Flask) |
| **Data Handling** | Pandas, NumPy |
| **Visualization** | Plotly, Matplotlib |
| **Speech Module** | gTTS, AssemplyAI |
| **Computer Vision** | OpenCV, MediaPipe |
| **Design** | Figma |
| **Hosting** | Local Flask Server |

---

## 🎥 Demo  

🎬 **Watch Demo:** [YouTube Video](https://youtu.be/xj8rL2PfNZ4)

---

## 🧑‍💻 Project Contributors  

This project was collaboratively developed by a dedicated team of engineers and researchers:  

| Name | 
|------|
| **Areen Alyahya** | 
| **Mudhawi Alshiha** | 
| **Shams Alarifi** | 
| **Nouf Almutairi** |
| **Wajd Alrabiah** |


---

## 🪷 Design Inspiration  

The visual identity of **SAWWAH** is inspired by the color **Lavender**, officially adopted by the Kingdom of Saudi Arabia to welcome guests.  
Lavender symbolizes **beauty, hospitality, and harmony with the desert**, perfectly reflecting SAWWAH’s vision of connecting **authentic Saudi culture** with **modern digital experiences**.  

---

## 🚀 Installation & Setup

> **Prerequisites:**  
> - Python **3.10+**  
> - Git installed on your system

---

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/chrollolucifr/Sawwah.git
cd Sawwah
```

### 2️⃣ Create & Activate a Virtual Environment
For macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

For Windows (PowerShell):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3️⃣ Install Dependencies
```bash
pip install --upgrade pip
pip install -r web_app/requirements.txt
```

### 4️⃣ Verify or Place Cleaned Datasets
Ensure the following cleaned datasets are available in the project directory:
- `data/cleaned/English_Cities_Cleaned.xlsx`
- `data/cleaned/English_Characters_Cleaned.xlsx`
- `data/cleaned/English_Projects_Cleaned.xlsx`

If missing, regenerate them by running the data-cleaning notebook:
```bash
jupyter notebook notebooks/Data_Cleaning_and_Preprocessing.ipynb
# then run the notebook cells to produce the cleaned files
```

### 5️⃣ Launch the Web Application
```bash
python web_app/app.py
```
Once the server starts, open your browser and visit:
http://127.0.0.1:5000

---

### Optional: Run Jupyter Notebooks
To explore data preprocessing or perform exploratory data analysis (EDA):
```bash
pip install notebook
jupyter notebook
```
Then open:
- `notebooks/Data_Cleaning_and_Preprocessing.ipynb`
- `notebooks/Sawwah_EDA.ipynb`

### ⚙️ Optional Configuration
- Change port: edit `web_app/app.py`:
```python
app.run(host="0.0.0.0", port=5000, debug=True)
```
- Modify dataset paths: if datasets are renamed or moved, update their paths inside `app.py`.

### 🛟 Troubleshooting
| Issue | Solution |
|---|---|
| ModuleNotFoundError | Re-activate virtual environment and reinstall dependencies:<br>`source .venv/bin/activate` (macOS/Linux) or activate the venv on Windows, then `pip install -r web_app/requirements.txt` |
| Dataset not found | Confirm cleaned dataset files exist in `data/cleaned/` |
| Port already in use | Edit the port number in `app.py`, e.g., `port=5050` |
| Jupyter notebook won't open | Run: `jupyter notebook --no-browser` and copy the generated URL from the terminal |

---

Your SAWWAH app is now ready to explore! Run the Flask app, open your browser, and enjoy discovering Saudi Arabia digitally 🌸
