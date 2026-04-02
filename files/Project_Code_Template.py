# ============================================================================
# DATA MINING PROJECT - CODE TEMPLATE
# Scenario 1: Black Friday Sales OR Scenario 2: EV Charging
# ============================================================================

# ============================================================================
# STAGE 1 & 2: DATA LOADING & PREPROCESSING
# ============================================================================

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Load Data
df = pd.read_csv('dataset.csv')

print("=" * 60)
print("INITIAL DATA EXPLORATION")
print("=" * 60)
print(f"Dataset Shape: {df.shape}")
print(f"\nColumn Names:\n{df.columns.tolist()}")
print(f"\nData Types:\n{df.dtypes}")
print(f"\nMissing Values:\n{df.isnull().sum()}")
print(f"\nBasic Statistics:\n{df.describe()}")

# ============================================================================
# STAGE 2: DATA CLEANING
# ============================================================================

# 2.1 Handle Missing Values
print("\n" + "=" * 60)
print("HANDLING MISSING VALUES")
print("=" * 60)

# For categorical columns
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    if df[col].isnull().sum() > 0:
        df[col].fillna(df[col].mode()[0], inplace=True)  # Mode imputation
        print(f"✓ Filled missing values in {col} with mode")

# For numerical columns
numerical_cols = df.select_dtypes(include=[np.number]).columns
for col in numerical_cols:
    if df[col].isnull().sum() > 0:
        df[col].fillna(df[col].median(), inplace=True)  # Median imputation
        print(f"✓ Filled missing values in {col} with median")

# 2.2 Encode Categorical Variables
print("\n" + "=" * 60)
print("ENCODING CATEGORICAL VARIABLES")
print("=" * 60)

# For Black Friday Scenario
if 'Gender' in df.columns:
    df['Gender'] = df['Gender'].map({'M': 0, 'F': 1})
    print("✓ Encoded Gender (M=0, F=1)")

if 'Marital_Status' in df.columns:
    df['Marital_Status'] = df['Marital_Status'].map({0: 0, 1: 1})
    print("✓ Encoded Marital Status")

# Age Group Encoding (example)
if 'Age' in df.columns and df['Age'].dtype == 'object':
    age_mapping = {'0-17': 1, '18-25': 2, '26-35': 3, '36-45': 4, 
                   '46-50': 5, '51-55': 6, '55+': 7}
    df['Age'] = df['Age'].map(age_mapping)
    print("✓ Encoded Age Groups to ordinal")

# For EV Charging Scenario
if 'Charger_Type' in df.columns:
    charger_mapping = {'AC Level 1': 0, 'AC Level 2': 1, 'DC Fast': 2}
    df['Charger_Type'] = df['Charger_Type'].map(charger_mapping)
    print("✓ Encoded Charger Type")

if 'Renewable_Energy_Source' in df.columns:
    df['Renewable_Energy_Source'] = df['Renewable_Energy_Source'].map({'Yes': 1, 'No': 0})
    print("✓ Encoded Renewable Energy Source")

# 2.3 Remove Duplicates
print("\n" + "=" * 60)
print("REMOVING DUPLICATES")
print("=" * 60)

initial_rows = len(df)
df.drop_duplicates(inplace=True)
print(f"✓ Removed {initial_rows - len(df)} duplicate rows")

# 2.4 Normalize Numerical Features
print("\n" + "=" * 60)
print("NORMALIZING NUMERICAL FEATURES")
print("=" * 60)

scaler = StandardScaler()
numerical_features = ['Purchase', 'Age', 'Charging_Capacity', 'Cost']
numerical_features = [col for col in numerical_features if col in df.columns]

df_normalized = df.copy()
df_normalized[numerical_features] = scaler.fit_transform(df[numerical_features])
print(f"✓ Normalized {len(numerical_features)} numerical features")

# Save cleaned data
df.to_csv('cleaned_data.csv', index=False)
print("\n✓ Cleaned data saved to 'cleaned_data.csv'")

# ============================================================================
# STAGE 3: EXPLORATORY DATA ANALYSIS (EDA)
# ============================================================================

print("\n" + "=" * 60)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 60)

plt.style.use('seaborn-v0_8-darkgrid')

# Figure 1: Distribution of Purchase Amount
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Histogram
axes[0, 0].hist(df['Purchase'], bins=50, edgecolor='black', color='skyblue')
axes[0, 0].set_title('Distribution of Purchase Amount', fontsize=12, fontweight='bold')
axes[0, 0].set_xlabel('Purchase Amount')
axes[0, 0].set_ylabel('Frequency')

# Box plot by Gender (if applicable)
if 'Gender' in df.columns:
    df.boxplot(column='Purchase', by='Gender', ax=axes[0, 1])
    axes[0, 1].set_title('Purchase by Gender')
    axes[0, 1].set_xlabel('Gender')

# Category frequency
if 'Product_Category_1' in df.columns:
    category_counts = df['Product_Category_1'].value_counts().head(10)
    axes[1, 0].barh(range(len(category_counts)), category_counts.values, color='coral')
    axes[1, 0].set_yticks(range(len(category_counts)))
    axes[1, 0].set_yticklabels(category_counts.index)
    axes[1, 0].set_title('Top 10 Product Categories', fontsize=12, fontweight='bold')
    axes[1, 0].set_xlabel('Frequency')

# Age vs Purchase scatter plot
if 'Age' in df.columns:
    axes[1, 1].scatter(df['Age'], df['Purchase'], alpha=0.5, s=20)
    axes[1, 1].set_title('Age vs Purchase Amount')
    axes[1, 1].set_xlabel('Age')
    axes[1, 1].set_ylabel('Purchase Amount')

plt.tight_layout()
plt.savefig('eda_overview.png', dpi=300, bbox_inches='tight')
print("✓ Saved EDA overview plot: eda_overview.png")

# Correlation Heatmap
numeric_df = df.select_dtypes(include=[np.number])
plt.figure(figsize=(10, 8))
correlation_matrix = numeric_df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, 
            fmt='.2f', square=True, linewidths=1)
plt.title('Correlation Matrix Heatmap', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('correlation_heatmap.png', dpi=300, bbox_inches='tight')
print("✓ Saved correlation heatmap: correlation_heatmap.png")

# ============================================================================
# STAGE 4: CLUSTERING ANALYSIS
# ============================================================================

print("\n" + "=" * 60)
print("CLUSTERING ANALYSIS")
print("=" * 60)

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Select features for clustering
clustering_features = ['Purchase', 'Age']
if 'Occupation' in df.columns:
    clustering_features.append('Occupation')

X_cluster = df_normalized[clustering_features].dropna()

# Elbow Method
inertias = []
silhouette_scores = []
K_range = range(2, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_cluster)
    inertias.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X_cluster, kmeans.labels_))

# Plot Elbow Curve
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].plot(K_range, inertias, 'bo-', linewidth=2, markersize=8)
axes[0].set_xlabel('Number of Clusters (k)', fontsize=11)
axes[0].set_ylabel('Inertia', fontsize=11)
axes[0].set_title('Elbow Method For Optimal k', fontsize=12, fontweight='bold')
axes[0].grid(True, alpha=0.3)

axes[1].plot(K_range, silhouette_scores, 'ro-', linewidth=2, markersize=8)
axes[1].set_xlabel('Number of Clusters (k)', fontsize=11)
axes[1].set_ylabel('Silhouette Score', fontsize=11)
axes[1].set_title('Silhouette Score vs k', fontsize=12, fontweight='bold')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('elbow_curve.png', dpi=300, bbox_inches='tight')
print("✓ Saved elbow curve plot: elbow_curve.png")

# Determine optimal k (usually at elbow)
optimal_k = 3  # Adjust based on your elbow curve
print(f"\n✓ Optimal number of clusters: {optimal_k}")

# Apply K-Means with optimal k
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(X_cluster)

print(f"Cluster distribution:\n{df['Cluster'].value_counts().sort_index()}")

# Cluster Profiles
print("\nCluster Profiles:")
cluster_profiles = df.groupby('Cluster').agg({
    'Purchase': ['mean', 'median', 'std'],
    'Age': ['mean', 'median'],
}).round(2)
print(cluster_profiles)

# Label Clusters (Business Names)
cluster_labels = {
    0: "Budget Shoppers",
    1: "Regular Buyers",
    2: "Premium Spenders"
}
df['Cluster_Label'] = df['Cluster'].map(cluster_labels)

# Visualize Clusters
plt.figure(figsize=(10, 7))
scatter = plt.scatter(df['Age'], df['Purchase'], c=df['Cluster'], 
                     cmap='viridis', s=50, alpha=0.6, edgecolors='black')
plt.xlabel('Age', fontsize=11)
plt.ylabel('Purchase Amount', fontsize=11)
plt.title(f'K-Means Clustering (k={optimal_k})', fontsize=12, fontweight='bold')
plt.colorbar(scatter, label='Cluster')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('clusters_visualization.png', dpi=300, bbox_inches='tight')
print("\n✓ Saved cluster visualization: clusters_visualization.png")

# ============================================================================
# STAGE 5: ASSOCIATION RULE MINING
# ============================================================================

print("\n" + "=" * 60)
print("ASSOCIATION RULE MINING")
print("=" * 60)

from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

# Create transaction data (one-hot encoded product categories)
if all(col in df.columns for col in ['Product_Category_1', 'Product_Category_2', 'Product_Category_3']):
    
    # Create itemsets
    transactions = []
    for idx, row in df.iterrows():
        items = []
        if pd.notna(row['Product_Category_1']):
            items.append(f"Cat1_{int(row['Product_Category_1'])}")
        if pd.notna(row['Product_Category_2']):
            items.append(f"Cat2_{int(row['Product_Category_2'])}")
        if pd.notna(row['Product_Category_3']):
            items.append(f"Cat3_{int(row['Product_Category_3'])}")
        if items:
            transactions.append(items)
    
    # One-hot encode
    te = TransactionEncoder()
    te_ary = te.fit(transactions).transform(transactions)
    df_encoded = pd.DataFrame(te_ary, columns=te.columns_)
    
    # Apply Apriori
    frequent_itemsets = apriori(df_encoded, min_support=0.05, use_colnames=True)
    
    if len(frequent_itemsets) > 1:
        rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.3)
        
        # Sort by lift
        rules = rules.sort_values('lift', ascending=False)
        
        print(f"\n✓ Found {len(rules)} association rules")
        print("\nTop 10 Rules by Lift:")
        print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head(10))
        
        # Visualize top rules
        if len(rules) > 0:
            fig, axes = plt.subplots(1, 2, figsize=(14, 5))
            
            axes[0].barh(range(min(10, len(rules))), rules['lift'].head(10).values, color='teal')
            axes[0].set_yticks(range(min(10, len(rules))))
            axes[0].set_title('Top 10 Rules by Lift', fontsize=12, fontweight='bold')
            axes[0].set_xlabel('Lift')
            
            axes[1].scatter(rules['confidence'], rules['support'], 
                          s=rules['lift']*100, alpha=0.6, c=rules['lift'], cmap='viridis')
            axes[1].set_xlabel('Confidence', fontsize=11)
            axes[1].set_ylabel('Support', fontsize=11)
            axes[1].set_title('Association Rules: Support vs Confidence\n(bubble size = lift)', 
                            fontsize=12, fontweight='bold')
            axes[1].grid(True, alpha=0.3)
            
            plt.tight_layout()
            plt.savefig('association_rules.png', dpi=300, bbox_inches='tight')
            print("\n✓ Saved association rules plot: association_rules.png")

# ============================================================================
# STAGE 6: ANOMALY DETECTION
# ============================================================================

print("\n" + "=" * 60)
print("ANOMALY DETECTION")
print("=" * 60)

from scipy import stats

# Method 1: Z-Score
z_scores = np.abs(stats.zscore(df['Purchase'].dropna()))
threshold_z = 3
anomalies_z = df[np.abs(stats.zscore(df['Purchase'])) > threshold_z]

print(f"Anomalies detected using Z-score (threshold={threshold_z}): {len(anomalies_z)}")
print(f"Percentage: {len(anomalies_z)/len(df)*100:.2f}%")

# Method 2: IQR
Q1 = df['Purchase'].quantile(0.25)
Q3 = df['Purchase'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

anomalies_iqr = df[(df['Purchase'] < lower_bound) | (df['Purchase'] > upper_bound)]
print(f"\nAnomalies detected using IQR: {len(anomalies_iqr)}")
print(f"Percentage: {len(anomalies_iqr)/len(df)*100:.2f}%")

# Analyze anomalies
print(f"\nAnomaly Statistics:")
print(f"Min Purchase (anomaly): {anomalies_iqr['Purchase'].min()}")
print(f"Max Purchase (anomaly): {anomalies_iqr['Purchase'].max()}")
print(f"Mean Purchase (anomaly): {anomalies_iqr['Purchase'].mean():.2f}")
print(f"Mean Purchase (normal): {df['Purchase'].mean():.2f}")

# Visualize anomalies
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Box plot with anomalies highlighted
axes[0].boxplot(df['Purchase'], vert=True)
axes[0].scatter([1]*len(anomalies_iqr), anomalies_iqr['Purchase'], 
               color='red', s=50, label='Anomalies', zorder=5)
axes[0].set_ylabel('Purchase Amount', fontsize=11)
axes[0].set_title('Box Plot with Anomalies', fontsize=12, fontweight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3, axis='y')

# Histogram with anomalies
axes[1].hist(df['Purchase'], bins=50, alpha=0.7, label='Normal', edgecolor='black')
axes[1].axvline(lower_bound, color='red', linestyle='--', linewidth=2, label='IQR Bounds')
axes[1].axvline(upper_bound, color='red', linestyle='--', linewidth=2)
axes[1].set_xlabel('Purchase Amount', fontsize=11)
axes[1].set_ylabel('Frequency', fontsize=11)
axes[1].set_title('Purchase Distribution with Anomaly Bounds', fontsize=12, fontweight='bold')
axes[1].legend()
axes[1].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('anomaly_detection.png', dpi=300, bbox_inches='tight')
print("\n✓ Saved anomaly detection plot: anomaly_detection.png")

# ============================================================================
# STAGE 7: INSIGHTS SUMMARY
# ============================================================================

print("\n" + "=" * 60)
print("KEY INSIGHTS SUMMARY")
print("=" * 60)

print(f"""
1. Dataset Overview:
   - Total Records: {len(df)}
   - Features: {df.shape[1]}
   
2. Purchase Patterns:
   - Average Purchase: ${df['Purchase'].mean():.2f}
   - Median Purchase: ${df['Purchase'].median():.2f}
   - Std Dev: ${df['Purchase'].std():.2f}
   
3. Clustering Results:
   - Optimal Clusters: {optimal_k}
   - Silhouette Score: {silhouette_scores[optimal_k-2]:.3f}
   
4. Anomalies:
   - Count: {len(anomalies_iqr)}
   - Percentage: {len(anomalies_iqr)/len(df)*100:.2f}%
   
5. Top Product Category: [Category Name]
   - Frequency: [Count]
""")

print("\n✓ All analyses completed successfully!")
print("✓ Check the generated PNG files for visualizations")
