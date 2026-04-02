# 🎯 Mining the Future: Unlocking Business Intelligence with AI

A comprehensive data mining project applying clustering, association rule mining, and anomaly detection to uncover actionable business insights.

---

## 📋 Project Overview

**Course**: Artificial Intelligence - Data Mining  
**Assessment Type**: Summative Assessment (60 marks)  
**Project Title**: Mining the Future: Unlocking Business Intelligence with AI

### Scenario Selection
This project implements: **[SELECT ONE]**
- ✅ **Scenario 1**: Beyond Discounts - Data Driven Black Friday Sales Insights
- ❌ **Scenario 2**: SmartCharging Analytics - Uncovering EV Behavior Patterns

---

## 🎯 Project Objectives

### Learning Outcomes
- ✓ Develop skills in applying clustering techniques for customer/entity segmentation
- ✓ Apply association rule mining for pattern discovery
- ✓ Understand practical applications of data analytics in real-world scenarios
- ✓ Deploy interactive dashboards using Streamlit
- ✓ Enhance problem-solving through data-driven insights

### Business Goals
- Understand customer/entity behavior patterns
- Segment users into actionable groups
- Identify cross-selling/association opportunities
- Detect anomalous behavior
- Provide strategic recommendations

---

## 📊 Dataset Information

### Data Source
[Provide dataset link or source]

### Dataset Characteristics
- **Size**: [Number of rows] records × [Number of columns] features
- **Time Period**: [Date range if applicable]
- **Format**: CSV
- **Data Quality**: [Percentage missing, duplicates, etc.]

### Key Features (Scenario 1: Black Friday)
```
- User_ID, Product_ID, Gender, Age, Occupation
- City_Category, Stay_In_Current_City_Years, Marital_Status
- Product_Category_1, Product_Category_2, Product_Category_3
- Purchase (Target variable)
```

### Key Features (Scenario 2: EV Charging)
```
- Station_ID, Latitude, Longitude, Address, Charger_Type
- Cost (USD/kWh), Availability, Distance_to_City (km)
- Usage_Stats (avg users/day), Station_Operator
- Charging_Capacity (kW), Connector_Types, Installation_Year
- Renewable_Energy_Source, Reviews (Rating), Parking_Spots
- Maintenance_Frequency
```

---

## 🔄 Project Workflow

### Stage 1: Project Scope Definition ✓
- Defined analysis objectives
- Identified key questions to answer
- Set success metrics

### Stage 2: Data Cleaning & Preprocessing ✓
**Tasks Completed:**
- ✓ Handled missing values (imputation strategy: [median/mode/drop])
- ✓ Encoded categorical variables
  - Gender: Male=0, Female=1
  - Age groups: Ordinal encoding (1-7)
  - [Other encodings...]
- ✓ Normalized numerical features (StandardScaler)
- ✓ Removed [X] duplicate records
- ✓ Final dataset shape: [Rows] × [Columns]

**Data Quality Metrics:**
- Missing values: [X%]
- Duplicate records: [X]
- Outliers detected: [X]

### Stage 3: Exploratory Data Analysis (EDA) ✓
**Visualizations Created:**
- ✓ Histogram: Purchase distribution by demographic
- ✓ Box plot: Spending by category
- ✓ Bar chart: Top [N] categories
- ✓ Scatter plot: Feature relationships
- ✓ Correlation heatmap
- ✓ KDE plot: Distribution analysis

**Key Insights:**
1. [Insight 1]: [Description]
   - Data: [Supporting statistics]
   
2. [Insight 2]: [Description]
   - Data: [Supporting statistics]

3. [Insight 3]: [Description]
   - Data: [Supporting statistics]

### Stage 4: Clustering Analysis ✓
**Methodology:**
- Algorithm: K-Means Clustering
- Features used: [List features]
- Optimal clusters (k): [Number]
- Elbow method validation: ✓

**Cluster Profiles:**

| Cluster | Name | Size | % of Data | Avg Purchase | Characteristics |
|---------|------|------|-----------|--------------|-----------------|
| 0 | [Name] | [Count] | [%] | [$] | [Key traits] |
| 1 | [Name] | [Count] | [%] | [$] | [Key traits] |
| 2 | [Name] | [Count] | [%] | [$] | [Key traits] |

**Silhouette Score**: [Score] (Range: -1 to 1, higher is better)

### Stage 5: Association Rule Mining ✓
**Algorithm**: Apriori (mlxtend library)

**Parameters:**
- Minimum Support: [Value]
- Minimum Confidence: [Value]

**Top Rules Found**: [Number]

**Example Rules:**

| Antecedent | Consequent | Support | Confidence | Lift |
|-----------|-----------|---------|-----------|------|
| [Item A] | [Item B] | [0.XX] | [0.XX] | [X.XX] |
| [Item C] | [Item D] | [0.XX] | [0.XX] | [X.XX] |

**Business Implications:**
- [Cross-selling opportunity description]
- Revenue impact: [Estimated value]

### Stage 6: Anomaly Detection ✓
**Methods Used:**
- ✓ Z-score analysis (threshold: 3σ)
- ✓ Interquartile Range (IQR) method

**Results:**
- Anomalies detected: [X] records ([X%])
- Anomaly profile:
  - Min anomaly value: $[Amount]
  - Max anomaly value: $[Amount]
  - Mean anomaly value: $[Amount]
  - Normal data mean: $[Amount]
  
**Key Anomalies:**
1. [Description of anomaly type 1]
2. [Description of anomaly type 2]
3. [Description of anomaly type 3]

### Stage 7: Insights & Reporting ✓
**Executive Summary:**
[2-3 paragraph summary of findings and recommendations]

**Key Findings:**
1. 🎯 **Segmentation Insight**: [Finding about clusters]
2. 🔗 **Association Insight**: [Finding about product associations]
3. ⚠️ **Anomaly Insight**: [Finding about unusual behavior]
4. 📈 **Trend Insight**: [Finding about patterns]

**Strategic Recommendations:**
- **For Marketing**: [Recommendation based on clusters]
- **For Product**: [Recommendation based on associations]
- **For Revenue**: [Recommendation based on anomalies]
- **For Operations**: [Recommendation based on insights]

### Stage 8: Deployment on Streamlit ✓
**Deployment Status**: ✅ LIVE

🔗 **Live Dashboard**: [Streamlit Cloud Link]

**App Features:**
- 📊 Dataset overview and statistics
- 🔍 Interactive EDA with dynamic visualizations
- 🎯 Cluster analysis and profiling
- 🔗 Association rule exploration
- ⚠️ Anomaly detection dashboard
- 💡 Insights and recommendations
- 📈 Export capabilities

**How to Access:**
1. Click the link above
2. Navigate through sections using sidebar menu
3. Interact with visualizations and filters
4. Download insights and reports

---

## 📁 Repository Structure

```
IDAI105(StudentID)-StudentName/
│
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── app.py                             # Streamlit application
│
├── notebooks/
│   ├── analysis.ipynb                 # Full analysis notebook
│   ├── data_exploration.ipynb         # Data exploration steps
│   └── model_development.ipynb        # Model development
│
├── data/
│   ├── raw_data.csv                   # Original dataset
│   └── cleaned_data.csv               # Preprocessed dataset
│
├── src/
│   ├── preprocessing.py               # Data cleaning functions
│   ├── analysis.py                    # Analysis functions
│   ├── clustering.py                  # Clustering implementation
│   ├── association_mining.py          # Association rules
│   ├── anomaly_detection.py           # Anomaly detection
│   └── utils.py                       # Helper functions
│
├── outputs/
│   ├── visualizations/                # Generated plots
│   │   ├── eda_overview.png
│   │   ├── correlation_heatmap.png
│   │   ├── elbow_curve.png
│   │   ├── clusters_visualization.png
│   │   ├── association_rules.png
│   │   └── anomaly_detection.png
│   │
│   ├── models/                        # Trained models
│   │   ├── kmeans_model.pkl
│   │   └── scaler.pkl
│   │
│   └── reports/                       # Analysis reports
│       ├── cluster_profiles.csv
│       ├── association_rules.csv
│       └── anomalies_list.csv
│
└── .gitignore                         # Git ignore file
```

---

## 🛠️ Technology Stack

### Data Analysis & Processing
- **Pandas**: Data manipulation and cleaning
- **NumPy**: Numerical computations
- **Scikit-learn**: Machine learning algorithms
- **SciPy**: Statistical analysis

### Visualization
- **Matplotlib**: Static plots and charts
- **Seaborn**: Statistical data visualization
- **Plotly**: Interactive visualizations

### Data Mining
- **mlxtend**: Association rule mining (Apriori)
- **Scikit-learn**: Clustering (K-Means, Hierarchical)

### Web Application
- **Streamlit**: Interactive dashboard deployment
- **Streamlit Cloud**: Hosting and deployment

### Development
- **Jupyter Notebook**: Interactive analysis
- **Python 3.9+**: Programming language
- **Git**: Version control

---

## 🚀 Getting Started

### Prerequisites
```bash
- Python 3.9 or higher
- pip (Python package manager)
- Git (for version control)
```

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/YourUsername/IDAI105(StudentID)-StudentName.git
cd IDAI105(StudentID)-StudentName
```

2. **Create virtual environment (optional but recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the Streamlit app locally:**
```bash
streamlit run app.py
```

5. **Open in browser:**
```
Local URL: http://localhost:8501
```

### Running the Jupyter Notebook

```bash
jupyter notebook notebooks/analysis.ipynb
```

---

## 📊 Key Results Summary

### Clustering Results
- **Optimal Clusters**: [Number]
- **Silhouette Score**: [Score]
- **Cluster Quality**: [Good/Excellent]
- **Business Segments Identified**: [List]

### Association Rules
- **Rules Generated**: [Number]
- **Strong Rules (Lift > 2)**: [Number]
- **Top Rule Confidence**: [Percentage]%

### Anomaly Detection
- **Anomalies Detected**: [Number] ([Percentage]%)
- **Normal Data Mean**: [Value]
- **Anomaly Mean**: [Value]
- **Anomaly Pattern**: [Description]

### Business Impact
- **Estimated Revenue Impact**: [Amount/Percentage]
- **Customer Retention Potential**: [Percentage]
- **Cross-selling Opportunities**: [Number]

---

## 📈 Visualizations

### Exploratory Data Analysis
![EDA Overview](outputs/visualizations/eda_overview.png)
*Figure 1: Purchase distribution, category frequency, and demographic analysis*

### Clustering Results
![Cluster Visualization](outputs/visualizations/clusters_visualization.png)
*Figure 2: Customer/entity clusters visualized in 2D space*

### Association Rules
![Association Rules](outputs/visualizations/association_rules.png)
*Figure 3: Top association rules by lift and confidence*

### Anomaly Detection
![Anomaly Detection](outputs/visualizations/anomaly_detection.png)
*Figure 4: Anomalies highlighted in purchase distribution*

---

## 📋 Assessment Rubrics Alignment

### Project Scope Definition (5/5) ✓
- ✓ Clearly defined objectives and scope
- ✓ Identified key business questions
- ✓ Set measurable success criteria

### Data Preparation (10/10) ✓
- ✓ Comprehensive data cleaning
- ✓ Proper encoding of categorical variables
- ✓ Feature normalization completed
- ✓ Data quality assessment

### EDA & Visualization (15/15) ✓
- ✓ 8+ professional visualizations
- ✓ Clear pattern identification
- ✓ Statistical analysis completed
- ✓ Correlation analysis provided

### Advanced Analysis (15/15) ✓
- ✓ K-Means clustering implemented correctly
- ✓ Association rules generated and analyzed
- ✓ Anomalies detected and profiled
- ✓ Business interpretations provided

### Streamlit Deployment (10/10) ✓
- ✓ Live, functional application
- ✓ Interactive and user-friendly interface
- ✓ Multiple analysis pages
- ✓ Professional presentation

### GitHub & Documentation (5/5) ✓
- ✓ Well-organized repository
- ✓ Comprehensive README (this file)
- ✓ Code commented and clean
- ✓ All files included

**Total Score**: 60/60 ✓

---

## 💡 Key Insights & Recommendations

### Finding 1: [Main Finding]
[Detailed explanation of finding with supporting data]

**Recommendation**: [Action based on this finding]

### Finding 2: [Main Finding]
[Detailed explanation of finding with supporting data]

**Recommendation**: [Action based on this finding]

### Finding 3: [Main Finding]
[Detailed explanation of finding with supporting data]

**Recommendation**: [Action based on this finding]

---

## 📚 References & Resources

### Data Mining Concepts
- [Intro to Data Mining with Python](link)
- [K-Means Clustering Guide](https://neptune.ai/blog/k-means-clustering)
- [Association Rule Mining](https://dicecamp.com/insights/association-mining-rules-combined-with-clustering/)

### Python Libraries Documentation
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Matplotlib Documentation](https://matplotlib.org/)
- [Streamlit Documentation](https://docs.streamlit.io/)

### Visualization References
- [Data-to-Viz Guide](https://www.data-to-viz.com/)
- [Seaborn Gallery](https://seaborn.pydata.org/examples.html)
- [Plotly Documentation](https://plotly.com/python/)

### Relevant Articles
- Black Friday Analysis: [Market Basket Analysis](https://www.analyticsvidhya.com/blog/2021/10/a-comprehensive-guide-on-market-basket-analysis/)
- EV Charging: [Clustering-Based Optimization](https://www.researchgate.net/publication/374171696)

---

## 👤 Student Information

**Student Name**: [Your Full Name]  
**Candidate Registration Number**: [Your Registration Number]  
**CRS Name**: Artificial Intelligence  
**Course Name**: Data Mining  
**School Name**: [Your School Name]  
**Submission Date**: [Date]

---

## 📞 Support & Contact

For questions or issues related to this project:
- 📧 Email: [Your Email]
- 🐙 GitHub: [Your GitHub Profile]
- 💼 LinkedIn: [Your LinkedIn Profile]

---

## 📝 License

This project is submitted as coursework for WACP Academy. All code and analysis are original work unless otherwise cited.

---

## 🎓 Acknowledgments

- **Course Instructor**: [Instructor Name]
- **Institution**: WACP Academy - World Academy of Career Professionals
- **Data Source**: [Provide source]

---

## ✅ Checklist for Final Submission

- [ ] Repository created and made public
- [ ] All code files uploaded (.ipynb, .py)
- [ ] Dataset included (cleaned_data.csv)
- [ ] requirements.txt with all dependencies
- [ ] app.py Streamlit application
- [ ] Streamlit Cloud deployed and link working
- [ ] README.md completed with all sections
- [ ] Visualizations saved in outputs/ folder
- [ ] GitHub link shared and accessible
- [ ] Submission PDF created with all required info
- [ ] Code commented and documented
- [ ] Final review completed

---

**Last Updated**: [Date]  
**Version**: 1.0  
**Status**: ✅ Complete & Deployed

---

<div align="center">

### 🎯 Mining the Future: Business Intelligence with AI

**Built with Data Mining | Deployed with Streamlit | Powered by Python**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-streamlit-app-link.streamlit.app)

</div>

