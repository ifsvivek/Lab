# Machine Learning Lab Programs - Python Files

This folder contains Python implementations of all 10 Machine Learning lab programs, converted from Jupyter notebooks.

## Programs Overview

### Lab1.py - Data Exploration and Visualization

-   **Dataset**: Housing dataset
-   **Techniques**:
    -   Data loading and basic statistics
    -   Histogram and boxplot visualization
    -   Outlier detection using IQR method
    -   Combined subplot visualizations

### Lab2.py - Data Analysis and Correlation Study

-   **Dataset**: Housing dataset
-   **Techniques**:
    -   Statistical analysis and correlation matrix
    -   Heatmap visualization
    -   Pairplot for feature relationships

### Lab3.py - Principal Component Analysis (PCA)

-   **Dataset**: Iris dataset
-   **Techniques**:
    -   Dimensionality reduction from 4D to 2D
    -   Variance explanation analysis
    -   PCA visualization with class separation

### Lab4.py - Find-S Algorithm

-   **Dataset**: Custom training data
-   **Techniques**:
    -   Concept learning algorithm
    -   Most specific hypothesis generation
    -   Detailed step-by-step execution tracking

### Lab5.py - K-Nearest Neighbors (KNN) Classification

-   **Dataset**: Synthetic labeled/unlabeled data
-   **Techniques**:
    -   KNN implementation with multiple k values
    -   Accuracy comparison across different k
    -   Performance visualization

### Lab6.py - Locally Weighted Regression (LWR)

-   **Dataset**: Synthetic regression data
-   **Techniques**:
    -   Gaussian kernel implementation
    -   Local regression with different bandwidths
    -   Weight visualization for query points

### Lab7.py - Linear and Polynomial Regression

-   **Dataset**: California Housing dataset
-   **Techniques**:
    -   Linear regression implementation
    -   Polynomial regression with different degrees
    -   Model comparison and performance analysis

### Lab8.py - Decision Tree Classification

-   **Dataset**: Breast Cancer dataset
-   **Techniques**:
    -   Decision tree implementation
    -   Feature importance analysis
    -   Tree visualization and performance metrics

### Lab9.py - Naive Bayes Classification

-   **Dataset**: Olivetti Faces dataset
-   **Techniques**:
    -   Gaussian Naive Bayes implementation
    -   Face recognition classification
    -   Confidence analysis and prediction visualization

### Lab10.py - K-Means Clustering

-   **Dataset**: Breast Cancer dataset
-   **Techniques**:
    -   K-Means clustering implementation
    -   Elbow method for optimal k
    -   Cluster analysis and feature importance

## Required CSV Files

The following programs have been converted to use CSV files instead of sklearn datasets. Make sure you have these CSV files in the same directory as the Python files:

### Lab3.py - Iris Dataset
- **File**: `iris.csv`
- **Required columns**: `sepal_length`, `sepal_width`, `petal_length`, `petal_width`, `species`
- **Target column**: `species` (should contain: setosa, versicolor, virginica)

### Lab7.py - Housing Dataset
- **File**: `housing.csv`
- **Required columns**: Features related to housing data (8 features expected)
- **Target column**: `target` (housing prices)

### Lab8.py - Breast Cancer Dataset
- **File**: `breast_cancer.csv`
- **Required columns**: Features related to breast cancer data (30 features expected)
- **Target column**: `diagnosis` (should contain: Malignant, Benign)

### Lab9.py - Faces Dataset
- **File**: `faces.csv`
- **Required columns**: Pixel features (e.g., pixel_0, pixel_1, ..., pixel_4095 for 64x64 images)
- **Target column**: `person_id` (person identification numbers)

### Lab10.py - Breast Cancer Dataset (for clustering)
- **File**: `breast_cancer.csv`
- **Required columns**: Same as Lab8.py
- **Target column**: `diagnosis` (used for evaluation purposes in clustering)

**Note**: You can download these datasets from various sources like Kaggle, UCI ML Repository, or convert the sklearn datasets to CSV format using the sklearn library.

## Requirements

To run these programs, you need the following Python packages:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

## Usage

Each Python file is self-contained and can be run independently:

```bash
python Lab1.py
python Lab2.py
# ... and so on
```

## File Structure

```
PythonFiles/
├── Lab1.py          # Data Exploration
├── Lab2.py          # Correlation Analysis
├── Lab3.py          # PCA
├── Lab4.py          # Find-S Algorithm
├── Lab5.py          # KNN Classification
├── Lab6.py          # Locally Weighted Regression
├── Lab7.py          # Linear/Polynomial Regression
├── Lab8.py          # Decision Trees
├── Lab9.py          # Naive Bayes
├── Lab10.py         # K-Means Clustering
└── README.md        # This file
```

## Features Added in Python Conversion

1. **Enhanced Documentation**: Each file includes detailed comments and docstrings
2. **Comprehensive Output**: Added detailed analysis and result interpretation
3. **Error Handling**: Robust implementation with proper error handling
4. **Visualization Improvements**: Enhanced plots with titles, labels, and legends
5. **Performance Metrics**: Added comprehensive evaluation metrics
6. **Code Organization**: Well-structured code with clear function definitions

## Notes

-   Some programs require specific datasets (housing.csv, data.csv) that should be placed in the appropriate directories
-   All programs include educational outputs to help understand the algorithms
-   Visualizations are optimized for better understanding of the underlying concepts

## Author

Converted from Jupyter notebooks to Python files for better code organization and execution.
