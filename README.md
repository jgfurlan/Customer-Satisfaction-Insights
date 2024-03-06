## ZenML Pipeline for Customer Insights - Olist E-commerce Dataset

**Project Introduction:**

This repository contains a ZenML pipeline for analyzing customer behavior in the Olist Brazilian e-commerce dataset [https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce). The pipeline explores customer demographics, purchasing habits, and product preferences to gain valuable insights into the Olist customer base.

**Pipeline Structure:**

The ZenML pipeline consists of the following stages:

1. **Data Loading:** Loads the relevant datasets from the Olist repository.
2. **Data Preprocessing:** Cleans, transforms, and prepares the data for analysis.
3. **Feature Engineering:** Creates new features based on existing data to improve analysis.
4. **Customer Segmentation:** Groups customers based on shared characteristics for targeted marketing efforts.
5. **Customer Analysis:** Analyzes customer demographics, purchase behavior, and product preferences.
6. **Reporting:** Generates reports and visualizations showcasing the key findings.

**Technology Stack:**

* **ZenML:** Machine learning pipeline framework.
* **Pandas:** Data manipulation and analysis library.
* **Scikit-learn:** Machine learning library for data preprocessing, feature engineering, and customer segmentation.
* **Matplotlib & Seaborn:** Visualization libraries.

**Getting Started:**

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/zenml-customer-insights.git
```

2. **Install dependencies:**

```bash
cd zenml-customer-insights
pip install -r requirements.txt
```

3. **Run the pipeline:**

```bash
zenml run --pipeline customer_insights
```

**Documentation:**

* Each stage of the pipeline is documented within the corresponding ZenML step definition files using clear comments and docstrings.
* A Jupyter notebook is provided to interactively explore the data and visualize the results.
* A README file outlines the project setup, dependencies, and instructions for running the pipeline.

Thanks for taking your time to read this,
João Gabriel Furlan
