# Infectious Disease Data Analysis

## Project Overview
This project analyzes infectious disease data from 2001-2014, focusing on statistical analysis, visualization, and modeling of disease patterns. The analysis includes demographic trends, geographical distribution, time series forecasting, and epidemiological modeling to understand disease dynamics and evaluate public health policies.

## Dataset
The primary dataset used is "Infectious Disease 2001-2014.csv" which contains information about various infectious diseases including:
- Disease name
- Year of occurrence
- County
- Population
- Count of cases
- Rate of infection
- Sex (demographic data)
- Confidence intervals (CI.lower and CI.upper)

## Key Features

### Data Cleaning and Preparation
- Handling missing values and duplicates
- Data transformation and standardization
- Creation of a cleaned dataset

### Statistical Analysis
- **Outlier Detection**: Using Z-score methodology to identify potential outliers in disease count and rate
- **Correlation Analysis**: Examining relationships between population size and disease rates
- **Confidence Interval Analysis**: Evaluating statistical reliability of the disease rate estimates

### Demographic Analysis
- Analysis of disease patterns by gender
- Identification of top 5 diseases affecting each gender
- Visualization of demographic trends

### Geographic Analysis
- Mapping disease prevalence across counties
- Heatmap visualization of top diseases per county
- Regional pattern identification

### Temporal Analysis
- Yearly trends of infectious diseases (2001-2014)
- Identification of top 3 diseases by year
- Visualization of disease count changes over time

### Forecasting
- Time series decomposition using STL (Seasonal and Trend decomposition using Loess)
- Forecasting future disease rates (example with Chlamydia)
- Trend, seasonal, and residual component analysis

### Epidemiological Modeling
- Implementation of SIR (Susceptible-Infectious-Recovered) model
- Disease transmission dynamics simulation
- Parameter estimation (beta, gamma) for specific diseases

### Public Health Policy Evaluation
- Before-and-after analysis of policy implementation
- Measles case study with 2009 policy evaluation
- Assessment of policy effectiveness on disease rates and counts

## Files in the Repository

- `cleaninginfectiousdiseasedataset.py`: Data cleaning and preparation
- `infectiousdiseasedataoverview.py`: Initial data exploration
- `detectingpotentialoutliers.py`: Outlier detection using statistical methods
- `findingcorrelationbetweenpopulation&diseaserate.py`: Correlation analysis
- `analyzinginfectedpatientsdemographics.py`: Demographic analysis
- `mappinginfectiousdiseasepercounty.py`: Geographic distribution analysis
- `analyzinginfectiousdiseaseyearlytrend.py`: Temporal trend analysis
- `confidenceintervalanalysis.py`: Statistical reliability assessment
- `forecastinginfectiousdiseaseratewithtimeseries.py`: Time series forecasting
- `epidemiologicalmodelling (1).py`: SIR model implementation
- `publichealthpolicyevaluation.py`: Policy impact assessment
- `cs_cbp.py`: Comprehensive analysis combining multiple approaches
- `cleaned_dataset.csv`: Processed dataset ready for analysis
- `Infectious Disease 2001-2014.csv`: Original raw dataset

## Technologies Used
- **Python**: Primary programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib & Seaborn**: Data visualization
- **SciPy**: Scientific computing (especially for integration)
- **Statsmodels**: Statistical modeling and time series analysis

## How to Use

1. Clone the repository
2. Ensure you have the required Python packages installed:
   ```
   pip install pandas numpy matplotlib seaborn scipy statsmodels
   ```
3. Run individual analysis scripts or the comprehensive `cs_cbp.py` file
4. Modify parameters as needed for different diseases, counties, or time periods

## Future Work
- Incorporate machine learning models for disease prediction
- Expand analysis to more recent data
- Develop interactive dashboards for visualization
- Include vaccination data to analyze its impact on disease rates
- Extend SIR modeling to include more complex compartmental models (SEIR, etc.)

## Contributors
- Your Name/Organization

## License
[Specify your license information]

## Acknowledgments
- Data sources and any relevant acknowledgments