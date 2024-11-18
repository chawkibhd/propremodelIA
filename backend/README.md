## Backend

The backend provides an API for land price prediction. It is built using Python and includes a machine learning model trained on data specific to the task.

### Structure
- **`data/`**: Contains datasets used for training and testing the model.
- **`model/`**: Houses the training script (`model_training.ipynb`) and the main API script (`server.py`).

### Key Features
- **Machine Learning Model**: A trained model designed to predict land prices.
- **API**: A RESTful API built with Python to serve predictions to the frontend.

### Installation and Setup
1. Navigate to the `backend/` directory:
   ```bash
   cd backend
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the API server:
   ```bash
   python server.py
   ```

---