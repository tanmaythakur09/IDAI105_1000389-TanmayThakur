# 📊 Data Mining Project: Complete Execution Guide

## **Project Selection Decision Tree**

### Choose Your Scenario:
- **Scenario 1 (Black Friday)**: Better if you prefer e-commerce analytics
- **Scenario 2 (EV Charging)**: Better if you prefer IoT/infrastructure data

---

## **STAGE-BY-STAGE IMPLEMENTATION ROADMAP**

### **STAGE 1: PROJECT SCOPE DEFINITION** (5 marks)
**What to do:**
- [ ] Download and explore the dataset
- [ ] List all columns and their data types
- [ ] Define 4-5 specific, measurable objectives
- [ ] Write a 200-word scope document

**Key Questions to Answer:**
- What are we trying to discover?
- Who will benefit from these insights?
- What business decisions will this inform?

**Deliverable**: 1-2 page scope document

---

### **STAGE 2: DATA CLEANING & PREPROCESSING** (10 marks)

#### Black Friday Scenario:
```
Tasks:
✓ Handle missing values in Product_Category_2 and Product_Category_3
✓ Encode categorical features:
  - Gender: Male=0, Female=1
  - Age groups: Create ordinal encoding (e.g., 0-17→1, 18-25→2, etc.)
  - Marital_Status: Appropriate encoding
✓ Normalize numerical features (Purchase amount, Age, etc.)
✓ Remove duplicates based on User_ID
✓ Check data types and fix inconsistencies
```

#### EV Charging Scenario:
```
Tasks:
✓ Handle missing values in Reviews, Renewable Energy Source, Connector Types
✓ Remove duplicates based on Station_ID
✓ Normalize continuous variables:
  - Cost (USD/kWh)
  - Usage Stats (avg users/day)
  - Charging Capacity (kW)
  - Distance to City (km)
✓ Encode categorical features:
  - Charger Type (AC Level 1, AC Level 2, DC Fast)
  - Station Operator
  - Renewable Energy Source (Yes/No)
```

**Tools**: Pandas, NumPy

**Checklist**:
- [ ] No missing values remaining (or documented reasoning for handling)
- [ ] All categorical variables encoded
- [ ] All numerical variables normalized (0-1 or -1 to 1 scale)
- [ ] Data shape documented (rows × columns after cleaning)
- [ ] Data quality report generated

---

### **STAGE 3: EXPLORATORY DATA ANALYSIS (EDA)** (15 marks)

#### Visualizations Required:

**Black Friday:**
- [ ] Histogram: Purchase amount by Age group
- [ ] Box plot: Purchase amount by Gender
- [ ] Bar chart: Top 10 product categories by frequency
- [ ] Scatter plot: Purchase vs. Occupation
- [ ] Heatmap: Correlation matrix of key features
- [ ] Distribution plot: Purchase amount (normal vs. skewed?)

**EV Charging:**
- [ ] Histogram: Usage Stats (avg users/day) distribution
- [ ] Line chart: Usage Stats vs. Installation Year (trend analysis)
- [ ] Heatmap: Demand by Charger Type and Availability
- [ ] Box plot: Cost (USD/kWh) by Station Operator
- [ ] Scatter plot: Cost vs. Rating (average users)

#### EDA Insights to Document:
```
For each visualization, write:
1. What the visualization shows
2. Key patterns observed
3. Anomalies or unexpected findings
4. Business implications
```

**Python Libraries**: Matplotlib, Seaborn, Plotly

**Checklist**:
- [ ] Minimum 6-8 high-quality visualizations
- [ ] Clear titles and axis labels
- [ ] Written interpretation for each visualization
- [ ] Summary statistics (mean, median, std, quartiles)
- [ ] Correlation analysis completed

---

### **STAGE 4: CLUSTERING ANALYSIS** (15 marks)

#### Algorithm Selection:

**Black Friday Approach:**
```python
# Features: Age, Occupation, Marital_Status, Purchase
# Methods: K-Means or Hierarchical Clustering

Steps:
1. Select features and normalize
2. Elbow Method: Test k=2 to 10
3. Find optimal k (elbow point)
4. Apply K-Means with optimal k
5. Label clusters with business names:
   - "Budget Shoppers"
   - "Regular Buyers"
   - "Premium Spenders"
6. Visualize in 2D (PCA or t-SNE)
```

**EV Charging Approach:**
```python
# Features: Usage Stats, Charging Capacity, Cost, Availability
# Methods: K-Means or DBSCAN

Steps:
1. Normalize features
2. Elbow Method for optimal k
3. Apply clustering
4. Label clusters:
   - "Daily Commuters"
   - "Occasional Users"
   - "Heavy Users"
5. Visualize on geographic map (Latitude × Longitude)
```

#### Deliverables:
- [ ] Elbow curve plot with marked optimal k
- [ ] Cluster scatter plot (2D visualization)
- [ ] Cluster statistics table (size, centroid values, characteristics)
- [ ] Business interpretation of each cluster
- [ ] Silhouette score evaluation

**Python Libraries**: Scikit-learn, Matplotlib

---

### **STAGE 5: ASSOCIATION RULE MINING** (15 marks)

#### Black Friday Approach:
```python
from mlxtend.frequent_patterns import apriori, association_rules

# Transform data: Create binary matrix
# Products purchased per customer per transaction

# Apriori Algorithm
frequent_itemsets = apriori(basket_encoded, min_support=0.1)
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)

# Extract top rules by:
- Support (frequency of items together)
- Confidence (likelihood of B given A)
- Lift (strength of relationship)

# Example outputs:
- "If Product_Category_1=Electronics → Product_Category_2=Accessories" 
  (Support: 15%, Confidence: 60%, Lift: 2.5)
```

#### EV Charging Approach:
```python
# Transform continuous data into discrete bins
# Example: Cost → "Low", "Medium", "High"
# Usage → "Low Demand", "High Demand"

# Find associations like:
- "DC Fast Chargers + Renewable Energy → Higher Users"
- "Low Cost + Near City → High Daily Demand"
```

#### Deliverables:
- [ ] Top 10-15 association rules with metrics
- [ ] Bar chart: Top rules by Lift
- [ ] Network diagram: Rule visualization
- [ ] Business recommendations based on rules

**Python Libraries**: mlxtend, NetworkX

---

### **STAGE 6: ANOMALY DETECTION** (Included in Advanced Analysis)

#### Black Friday Approach:
```python
# Method 1: Z-Score
z_scores = np.abs(stats.zscore(df['Purchase']))
outliers_z = df[z_scores > 3]

# Method 2: IQR (Interquartile Range)
Q1 = df['Purchase'].quantile(0.25)
Q3 = df['Purchase'].quantile(0.75)
IQR = Q3 - Q1
outliers_iqr = df[(df['Purchase'] < Q1 - 1.5*IQR) | (df['Purchase'] > Q3 + 1.5*IQR)]

# Analysis:
- Count and percentage of anomalies
- Comparison with demographics (Age, Gender, Occupation)
- Purchase patterns of anomalies vs. normal
```

#### EV Charging Approach:
```python
# Find anomalies in:
1. Usage Stats (stations with unusually low usage despite good features)
2. Cost vs. Rating (expensive but poorly rated)
3. Maintenance frequency (stations with excessive downtime)
4. Sudden demand spikes (time-series anomalies)

Methods:
- Statistical: Z-score, IQR
- ML-based: Isolation Forest, Local Outlier Factor (LOF)
```

#### Deliverables:
- [ ] Anomaly count and percentage
- [ ] Visualization: Anomalies highlighted in scatter plot
- [ ] Detailed anomaly profile report
- [ ] Business implications and recommendations

---

### **STAGE 7: INSIGHTS & REPORTING** (Included in Advanced Analysis)

#### Documentation Required:

**For Black Friday:**
```
Key Insights:
1. Age Group Analysis
   - Which age spends most? (with amount and %)
   - Spending patterns by age
   
2. Gender Analysis
   - Male vs. Female spending behavior
   - Preferred categories by gender
   
3. Product Preferences
   - Top 3 categories by sales
   - Cross-category associations
   
4. Customer Segmentation
   - Cluster profiles and sizes
   - Targeted recommendations per cluster
   
5. Anomalies
   - High spenders profile
   - Their characteristics and patterns
```

**For EV Charging:**
```
Key Insights:
1. Charger Type Popularity
   - Usage distribution across charger types
   
2. Operator Performance
   - Ratings vs. actual usage
   - Top performing operators
   
3. Geographic Patterns
   - Peak demand locations
   - City vs. rural usage
   
4. Clustering Findings
   - Station type profiles
   - User behavior patterns
   
5. Anomalies
   - Underutilized stations
   - Overloaded stations
   - Maintenance concerns
```

#### Format:
- [ ] Executive Summary (1 page)
- [ ] Detailed Findings (3-5 pages)
- [ ] Visualizations with captions
- [ ] Strategic Recommendations (5-10 bullet points)

---

### **STAGE 8: DEPLOYMENT ON STREAMLIT CLOUD** (10 marks)

#### Streamlit App Structure:

```python
# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
import plotly.express as px

st.set_page_config(page_title="Data Mining Dashboard", layout="wide")

# Title and Description
st.title("🎯 Mining the Future: Business Intelligence Dashboard")
st.write("Explore insights from [Scenario Name]")

# Sidebar Navigation
page = st.sidebar.selectbox(
    "Select Analysis",
    ["Overview", "EDA", "Clustering", "Association Rules", "Anomalies", "Insights"]
)

# Load Data (cached for performance)
@st.cache_data
def load_data():
    return pd.read_csv('cleaned_data.csv')

df = load_data()

# Page 1: Overview
if page == "Overview":
    st.header("📊 Dataset Overview")
    st.write(f"**Dataset Shape**: {df.shape[0]} rows × {df.shape[1]} columns")
    st.dataframe(df.head(10))
    st.write(df.describe())

# Page 2: EDA
elif page == "EDA":
    st.header("🔍 Exploratory Data Analysis")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Purchase Distribution")
        fig = plt.figure()
        plt.hist(df['Purchase'], bins=50, edgecolor='black')
        st.pyplot(fig)
    
    with col2:
        st.subheader("By Category")
        category_count = df['Product_Category_1'].value_counts()
        st.bar_chart(category_count)

# Page 3: Clustering
elif page == "Clustering":
    st.header("🎯 Customer Clustering")
    
    st.write("### Cluster Distribution")
    cluster_counts = df['Cluster'].value_counts()
    st.bar_chart(cluster_counts)
    
    st.write("### Cluster Profiles")
    cluster_profiles = df.groupby('Cluster').agg({
        'Purchase': 'mean',
        'Age': 'mean'
    })
    st.table(cluster_profiles)

# Page 4: Association Rules
elif page == "Association Rules":
    st.header("🔗 Association Rule Mining")
    st.write("Top Rules by Confidence:")
    st.dataframe(top_rules[['antecedents', 'consequents', 'confidence', 'lift']])

# Page 5: Anomalies
elif page == "Anomalies":
    st.header("⚠️ Anomaly Detection")
    st.write(f"**Total Anomalies Found**: {len(anomalies)}")
    st.dataframe(anomalies)

# Page 6: Insights
elif page == "Insights":
    st.header("💡 Key Insights & Recommendations")
    st.write("""
    ### Findings:
    1. ...
    2. ...
    
    ### Recommendations:
    - ...
    - ...
    """)
```

#### Deployment Steps:
1. **Create requirements.txt**:
```
pandas==1.5.0
numpy==1.23.0
matplotlib==3.6.0
seaborn==0.12.0
scikit-learn==1.1.0
streamlit==1.15.0
plotly==5.10.0
mlxtend==0.22.0
```

2. **Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Data Mining Project"
   git push origin main
   ```

3. **Deploy on Streamlit Cloud**:
   - Go to https://share.streamlit.io/
   - Sign in with GitHub
   - Select your repository
   - Deploy!

#### Deployment Checklist:
- [ ] app.py created and tested locally
- [ ] requirements.txt file created
- [ ] All imports work correctly
- [ ] GitHub repository is public
- [ ] Streamlit Cloud deployment successful
- [ ] Sharing link obtained and documented

---

### **STAGE 9: GITHUB REPOSITORY & DOCUMENTATION** (5 marks)

#### Repository Structure:
```
IDAI105(StudentID)-StudentName/
├── README.md                 (Detailed documentation)
├── app.py                    (Streamlit application)
├── requirements.txt          (Python dependencies)
├── notebooks/
│   └── analysis.ipynb        (Jupyter notebook with full analysis)
├── data/
│   ├── raw_data.csv          (Original dataset)
│   └── cleaned_data.csv      (Preprocessed dataset)
├── src/
│   ├── preprocessing.py      (Data cleaning functions)
│   ├── analysis.py           (EDA and clustering code)
│   └── utils.py              (Helper functions)
└── outputs/
    ├── visualizations/       (EDA plots)
    ├── clustering_results/   (Cluster analysis)
    └── reports/              (Insights document)
```

#### README.md Template:
```markdown
# 🎯 Mining the Future: Data Mining Project

## Project Overview
- **Scenario**: [Black Friday / EV Charging]
- **Objective**: [Brief description]
- **Dataset**: [Source and size]

## Key Findings
1. [Finding 1]
2. [Finding 2]
3. [Finding 3]

## Methodology
- **Data Cleaning**: [Techniques used]
- **EDA**: [Key visualizations]
- **Clustering**: K-Means with optimal k=[number]
- **Association Rules**: Apriori algorithm with min_support=[value]
- **Anomaly Detection**: [Methods used]

## Results
- **Clusters Identified**: [Number and characteristics]
- **Association Rules Found**: [Number and top rules]
- **Anomalies Detected**: [Number and patterns]

## Deployed App
🔗 [Streamlit Cloud Link]

## Repository Structure
[Include directory structure]

## How to Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Contributors
[Your Name]
```

---

## **ASSESSMENT RUBRICS - SCORE MAXIMIZATION TIPS**

### Project Scope Definition (5/5):
✅ Clearly state 4-5 specific, measurable objectives
✅ Define success criteria
✅ Explain business relevance

### Data Preparation (10/10):
✅ Document every preprocessing step
✅ Show before/after data quality metrics
✅ Explain missing value handling decisions

### EDA & Visualization (15/15):
✅ Create 8+ high-quality visualizations
✅ Write interpretation for each
✅ Include correlation analysis
✅ Use professional styling

### Advanced Analysis (15/15):
✅ Apply clustering correctly with Elbow method
✅ Generate meaningful association rules
✅ Detect and profile anomalies
✅ Provide business interpretation

### Streamlit Deployment (10/10):
✅ Interactive, user-friendly interface
✅ Multiple pages/sections
✅ Live, accessible link
✅ Professional appearance

### GitHub & Documentation (5/5):
✅ Well-organized repository
✅ Detailed README
✅ All code commented
✅ Dataset included

---

## **TIMELINE SUGGESTION**

| Week | Tasks |
|------|-------|
| 1 | Stages 1-2: Scope & Data Cleaning |
| 2 | Stage 3: EDA & Visualizations |
| 3 | Stage 4-5: Clustering & Association Rules |
| 4 | Stage 6: Anomaly Detection + Insights |
| 5 | Stage 8: Streamlit Development |
| 6 | Stage 9: GitHub + Final Documentation |
| 7 | Testing, refinement, submission |

---

## **KEY PYTHON LIBRARIES CHEAT SHEET**

```python
# Data Manipulation
import pandas as pd
import numpy as np

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Machine Learning
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import dendrogram, linkage

# Association Rules
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

# Anomaly Detection
from scipy import stats
from sklearn.ensemble import IsolationForest

# Deployment
import streamlit as st
```

---

## **RESOURCES PROVIDED IN ASSIGNMENT**

✅ Reference websites for visualizations
✅ Python library documentation links
✅ Sample notebooks and tutorials
✅ Data Mining concepts guides
✅ YouTube video for GitHub setup

---

## **FINAL SUBMISSION CHECKLIST**

- [ ] GitHub repository created and public
- [ ] All code files (.ipynb, .py) uploaded
- [ ] Dataset included in repository
- [ ] README.md fully completed
- [ ] Streamlit app deployed and link working
- [ ] Submission PDF created with:
  - [ ] GitHub link
  - [ ] Student name
  - [ ] Candidate registration number
  - [ ] CRS name
  - [ ] Course name
  - [ ] School name
- [ ] All 8 stages completed
- [ ] Rubrics requirements met
- [ ] Peer review completed (if applicable)

---

Good luck! 🚀 This is a comprehensive project—break it into manageable stages and document everything!
