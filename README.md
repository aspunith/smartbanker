# The Smart Banker 🏦💡

**A Machine Learning-Powered Bank Performance Analysis and Prediction System**

[![Django](https://img.shields.io/badge/Django-3.2.4-green.svg)](https://djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://python.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-0.24.2-orange.svg)](https://scikit-learn.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-4.0.0-purple.svg)](https://getbootstrap.com/)

## 🎯 Problem Statement

In today's financial landscape, investors and customers often fall victim to misleading bank advertisements that promise high returns and low interest rates. Many banks, especially newer ones, use these tactics to attract customers but may face financial instability or bankruptcy, putting depositors' money at risk.

**The Smart Banker** addresses this critical problem by providing:
- **Bank Performance Analysis**: Comprehensive evaluation of a bank's financial health
- **Risk Assessment**: Prediction of bank reliability and sustainability
- **Investment Guidance**: Data-driven recommendations for depositors and investors
- **Dividend Prediction**: Analysis of dividend distribution probability

## 🚀 Project Overview

This web application uses machine learning algorithms to analyze bank financial data and predict:

1. **Bank Performance Score**: Overall financial health assessment
2. **Dividend Distribution Probability**: Likelihood of receiving dividends
3. **Risk Classification**: NPA (Non-Performing Assets) risk categories
4. **Investment Recommendations**: Data-driven advice for potential investors

## 🛠️ Technical Approach

### Machine Learning Pipeline
The system employs a **two-stage prediction model**:

1. **Stage 1 - Bank Performance Classification**
   - Analyzes financial metrics to classify bank performance
   - Uses features like income, expenditure, NPA, profit margins
   - Outputs performance score and dividend probability

2. **Stage 2 - Investment Recommendation**
   - Takes Stage 1 output as additional feature
   - Provides final investment recommendations
   - Considers multiple risk factors for comprehensive analysis

### Data Processing & Feature Engineering
- **Net Profit Calculation**: `income - expenditure`
- **NPA Threshold**: `(npa/income) * 100`
- **Profit Percentage**: `(net_profit/income) * 100`
- **Dividend Classification**: Binary classification (0/1)
- **NPA Risk Categories**: 4-tier classification system
- **Standardization**: Using StandardScaler for model input
- **Label Encoding**: For categorical target variables

## 🔧 Skills & Technologies Used

### **Backend Development**
- **Django 3.2.4**: Web framework for rapid development
  - *Purpose*: MVC architecture, URL routing, template rendering
- **Python 3.x**: Core programming language
  - *Purpose*: Business logic, data processing, ML integration

### **Machine Learning & Data Science**
- **Scikit-learn 0.24.2**: Primary ML library
  - *Purpose*: Model training, preprocessing, predictions
- **Pandas 1.2.4**: Data manipulation and analysis
  - *Purpose*: DataFrame operations, data cleaning
- **NumPy 1.20.3**: Numerical computing
  - *Purpose*: Array operations, mathematical calculations
- **Pickle**: Model serialization
  - *Purpose*: Saving and loading trained ML models

### **Frontend Development**
- **HTML5/CSS3**: Structure and styling
  - *Purpose*: User interface design and responsive layouts
- **Bootstrap 4.0.0**: CSS framework
  - *Purpose*: Responsive design, pre-built components
- **JavaScript**: Client-side interactivity
  - *Purpose*: Form validation, dynamic content
- **Font Awesome**: Icon library
  - *Purpose*: Visual enhancements and UI icons

### **Data Visualization**
- **Custom CSS Charts**: Bar graph representations
  - *Purpose*: Visual display of NPA, profit margins, risk scores
- **Responsive Visualizations**: Mobile-friendly charts
  - *Purpose*: Accessible data representation across devices

### **Database Management**
- **SQLite3**: Lightweight database
  - *Purpose*: Development database for user sessions and Django admin

### **Deployment & Production**
- **Gunicorn 20.1.0**: WSGI HTTP Server
  - *Purpose*: Production-ready Python web server
- **WhiteNoise 5.2.0**: Static file serving
  - *Purpose*: Efficient static file handling in production
- **Waitress 2.0.0**: WSGI server for Windows
  - *Purpose*: Cross-platform production deployment
- **Heroku**: Cloud platform deployment
  - *Purpose*: Web application hosting and scaling

### **Additional Libraries**
- **Matplotlib 3.4.2**: Plotting library
  - *Purpose*: Data visualization and analysis
- **Plotly 5.0.0**: Interactive plotting
  - *Purpose*: Dynamic charts and graphs
- **Seaborn 0.11.1**: Statistical visualization
  - *Purpose*: Enhanced data visualization

## 📊 Key Features

### 🔍 **Intelligent Analysis**
- Multi-parameter financial analysis
- Real-time risk assessment
- Performance scoring algorithms
- Trend analysis and predictions

### 📈 **Visual Dashboard**
- Interactive bar charts for NPA analysis
- Profit margin visualizations
- Risk category indicators
- Performance scorecards

### 🎯 **User-Friendly Interface**
- Intuitive form-based input system
- Step-by-step guidance
- Responsive design for all devices
- Clear result interpretation

### ⚡ **Real-Time Predictions**
- Instant analysis upon form submission
- Live performance calculations
- Dynamic result generation
- Comprehensive recommendation system

## 🚦 System Workflow

1. **Data Input**: User enters bank financial parameters
2. **Validation**: System validates license status and data integrity
3. **Feature Engineering**: Calculates derived metrics and ratios
4. **ML Prediction**: Two-stage model prediction process
5. **Risk Assessment**: NPA and profit analysis
6. **Visualization**: Interactive charts and performance indicators
7. **Recommendations**: Data-driven investment guidance

## 📋 Input Parameters

The system analyzes the following financial metrics:

- **Year**: Analysis year for temporal context
- **Bank Name**: Institution identification
- **License Status**: Regulatory compliance verification
- **Income (₹ Crores)**: Total bank income
- **Expenditure (₹ Crores)**: Total operational expenses
- **NPA (₹ Crores)**: Non-Performing Assets value
- **Dividend (₹ Crores)**: Dividend distribution amount
- **Current Assets & Liabilities (₹ Crores)**: Balance sheet metrics

## 🎨 User Experience Design

### **Modern Interface**
- Clean, professional design aesthetic
- Intuitive navigation with clear CTAs
- Mobile-first responsive design
- Accessibility-focused implementation

### **Educational Approach**
- Step-by-step guidance through instructions page
- Interactive tooltips for parameter explanations
- Real-world scenario examples (Jay vs Sophie story)
- Best practice recommendations

## 👥 Team & Contributors

| Role | Name | Specialization |
|------|------|----------------|
| **Project Mentor** | G Bhaskar | Assistant Professor, Project Leadership |
| **Backend Developer** | A S Punith | Python, Django Framework |
| **Frontend Developer** | Namana J Jain | UI/UX Design, Responsive Development |
| **ML Engineer** | Nagavishnu H | Machine Learning, Data Science |

## 🚀 Getting Started

### Prerequisites
```bash
Python 3.x
Django 3.2.4
Required packages (see requirements.txt)
```

### Installation
```bash
# Clone the repository
git clone https://github.com/aspunith/smartbanker.git

# Navigate to project directory
cd smartbanker

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

### Production Deployment
The application is configured for Heroku deployment with:
- Procfile for process management
- WhiteNoise for static file serving
- Environment-based configuration

## 📈 Future Enhancements

- **Real-time Data Integration**: API connections to live financial data
- **Advanced ML Models**: Deep learning for improved predictions
- **Comparative Analysis**: Multi-bank comparison features
- **Historical Trend Analysis**: Time-series forecasting
- **Risk Alerts**: Automated notification system
- **Portfolio Management**: Investment tracking capabilities

## 🔒 Security & Compliance

- Environment-based secret key management
- CSRF protection for form submissions
- Secure static file handling
- Production-ready security headers

## 📄 License

This project is developed for educational and research purposes, focusing on financial analysis and machine learning applications in banking sector.

---

**The Smart Banker** - *Empowering informed financial decisions through intelligent analysis* 🏦✨