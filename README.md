# Week 1: Financial News and Stock Price Analysis

## Overview
This project focuses on analyzing financial news and stock prices to extract useful insights and trends. The goal of Week 1 is to set up the project structure, load the dataset, perform exploratory data analysis (EDA), and gain valuable insights about publication trends, sentiment, and more.

## Folder Structure
The folder structure is organized as follows to ensure clean separation of files:

## Setting Up the Project
1. **Clone the Repository**
   - Clone the project repository to your local machine using the command:
     ```bash
     git clone https://github.com/your-username/your-repository.git
     ```
   
2. **Create a Virtual Environment**
   - Set up a virtual environment using either `conda` or `virtualenv` to isolate project dependencies.
   - Example with `conda`:
     ```bash
     conda create --name work-env python=3.9
     conda activate work-env
     ```
   
3. **Install Dependencies**
   - Install all required Python packages using `pip`:
     ```bash
     pip install -r requirements.txt
     ```

4. **Start Jupyter Notebook**
   - To begin analysis, launch Jupyter Notebook from your terminal:
     ```bash
     jupyter notebook
     ```

## Exploratory Data Analysis (EDA)
In this phase, the main objective is to explore the dataset and extract useful information. The analysis will include the following steps:

1. **Descriptive Statistics**
   - Analyze the dataset by calculating basic statistics on headline lengths.
   - Count the number of articles published by each publisher.
   - Examine publication dates to observe trends over time.

2. **Sentiment Analysis**
   - Perform sentiment analysis on article headlines to determine if the sentiment is positive, negative, or neutral.
   
3. **Topic Modeling**
   - Extract common keywords or phrases to identify significant topics or market events.

4. **Time Series Analysis**
   - Analyze publication trends over time, identifying any spikes in articles related to specific market events or time periods.

5. **Publisher Analysis**
   - Identify the publishers contributing the most articles.
   - Investigate unique publisher domains to see which organizations contribute the most content.

## Running the Analysis
- **Load the Dataset**
  - Load your dataset using the `pandas` library.
  - Ensure the dataset is stored in the `data/` folder, with raw data like `raw_analyst_ratings.csv`.

- **Perform EDA**
  - Use Python packages such as `matplotlib`, `seaborn`, and `nltk` for analysis and visualization.

## Requirements
The required Python libraries for this project are listed in `requirements.txt`:
- pandas
- matplotlib
- seaborn
- nltk
- scikit-learn
- ... and others

## Git Usage
1. **Commit Changes**
   - Commit your progress regularly with descriptive commit messages.
   - Example:
     ```bash
     git add .
     git commit -m "Initial commit for EDA analysis"
     ```

2. **Push Changes to GitHub**
   - After making changes, push them to the remote GitHub repository:
     ```bash
     git push origin main
     ```

## License
This project is licensed under the MIT License - see the LICENSE file for details.
