# Tesla Car Price Prediction 🚗

An interactive application developed with **Streamlit** that uses a **Machine Learning** model to predict the price of Tesla cars (Model S, Model 3, Model X, and Model Y) based on data collected from various sources through web scraping techniques.

---

## Screenshot

The main interface of the application:

![Streamlit Interface](assets/streamlit_img.png)

---

## Project Description

This project aims to provide an intuitive tool that allows users to estimate the price of a Tesla car based on its characteristics.

### Project Workflow:
1. **Data Collection:**
   - Data was collected from specialized car sales websites through **web scraping**:
     - [Coches.net](https://www.coches.net)
     - [Tesla.com](https://www.tesla.com)
     - [TeslaHunt.com](https://www.teslahunt.com)

2. **Data Processing:**
   - The data was cleaned and processed in a controlled environment.
   - Categorical variables such as model, color, and country were encoded using **LabelEncoder**.
   - Mileage was normalized using a scaler (**MinMaxScaler**).

3. **Model Training:**
   - A **Random Forest** model was used due to its robustness, ability to handle tabular data, and excellent performance with nonlinear relationships.
   - The model was trained using the following features:
     - Car model (Model S, Model 3, Model X, Model Y).
     - Manufacturing year.
     - Mileage.
     - Color.
     - Country.

4. **Streamlit Implementation:**
   - The application allows users to select the car's features through an intuitive graphical interface.
   - It uses serialized files in **pickle** format to load the trained model and preprocessing objects (scaler and encoders).

---

## Project Structure

```
PREDICT_TESLA_PRICE/
├── assets/                             # Visual resources (images, screenshots)
│   ├── streamlit_img.png               # Image of the Streamlit interface
├── data/                               # Folder containing obtained and processed data
│   ├── data.ipynb                      # Notebook for data exploration
│   ├── datos.csv                       # Combined data for training
│   ├── df_tesla_final.csv              # Final scraped data
│   ├── tesla_coches_combinados.csv     # Tesla car data
├── webscrapping/                       # Scripts to extract data from the web
│   ├── coches_net.ipynb                # Web scraping from Coches.net
│   ├── df_teslas.csv                   # Extracted data from scraping
│   ├── tesla_page.ipynb                # Web scraping from Tesla.com
├── .gitignore                          # Files and folders to ignore in Git
├── 20241128_Proyecto_Tesla.pdf         # Project-related document
├── app.py                              # Main Streamlit application code
├── tesla_price_prediction_env.yml      # Conda virtual environment file
├── README.md                           # Project documentation
├── train_model.ipynb                   # Notebook for model training
```

---

## Installation

Follow these steps to run the application locally:

1. **Clone this repository:**
   ```bash
   git clone https://github.com/your_username/predict_tesla_price.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd predict_tesla_price
   ```

3. **Install the dependencies:**
   Ensure you have a virtual environment and run:
   ```bash
   conda env create -f tesla_price_prediction_env.yml
   conda activate tesla_price_prediction_env
   ```

4. **Run the Streamlit application:**
   ```bash
   streamlit run app.py
   ```

---

## Functionality

### **1. Web Scraping**
The input data was obtained using web scraping scripts located in the `webscrapping` folder. These scripts collect data from the following sites:
- **Coches.net**: Tesla cars for sale.
- **Tesla.com**: Official information about base prices.
- **TeslaHunt.com**: Listings of second-hand Tesla cars.
- **Autoocasion24**: Tesla car prices in different countries.

### **2. Model Training**
The prediction model was trained with combined and preprocessed data in the `train_model.ipynb` file. The features used include:
- **Car model**: Model S, Model 3, Model X, Model Y.
- **Year**: Manufacturing year of the car.
- **Mileage**: Distance traveled in kilometers.
- **Color**: Car color.
- **Country**: Location of the car.

### **3. Interactive Interface**
The interface allows the user to:
- Select the car model (with images).
- Input features such as year, mileage, color, and country.
- Obtain a price prediction based on the trained model.

The application also displays the model's accuracy (R² Score).

---

## Features

- **Accurate Prediction:** Based on real data from multiple sources.
- **Intuitive Interface:** Clear visualization of available options.
- **Extensibility:** Easy to expand with new data or features.

---
