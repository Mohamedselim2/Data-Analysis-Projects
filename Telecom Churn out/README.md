# Telecom Customer Churn Analysis

## Project Overview
This project aims to analyze customer churn data from a telecom company to understand why customers are leaving. By identifying key factors influencing churn, the company can take targeted actions to improve customer retention.

## Data
The dataset contains the following columns:
- Customer ID
- Churn Label
- Account Length (in months)
- Local Calls
- Local Mins
- Intl Calls
- Intl Mins
- Intl Active
- Intl Plan
- Customer Service Calls
- Avg Monthly GB Download
- Unlimited Data Plan
- State
- Gender
- Age
- Group
- Number of Customers in Group
- Contract Type
- Payment Method
- Total Charges
- Churn Category

## Repository Files
- **dashboard.pbix**: Power BI dashboard file
- **dashboard theme.json**: Custom theme for the dashboard
- **dashboard.png**: Image of the dashboard
- **report.pdf**: Detailed analysis report
- **reporting.xlsx**: Excel file containing reports and visualizations
- **dataset.xlsx**: The raw dataset used for analysis

## Key Findings
- Customers with month-to-month contracts are more likely to churn.
- High number of customer service calls is a significant churn indicator.
- Customers with an international plan and higher usage tend to stay longer.
- Unlimited data plan reduces churn probability.

## Challenges Faced
- **Data Quality Issues**: The dataset contained missing values and inconsistencies, which required significant preprocessing efforts.
- **Feature Selection**: Identifying the most relevant features for churn prediction was challenging due to the large number of potential variables.
- **Balancing the Dataset**: The churn data was imbalanced, making it difficult to build accurate predictive models.
- **Visualizations**: Creating meaningful and clear visualizations that effectively communicated insights required multiple iterations and adjustments.


## Visualizations
![Dashboard](dashboard.png)

## Conclusion
By understanding the factors that contribute to customer churn, the telecom company can implement strategies to enhance customer satisfaction and retention.

## Files
- [dashboard.pbix](./dashboard.pbix)
- [Dashboard Theme.json](./Dashboard%20Dark%20theme.json)
- [dashboard.png](./dashboard.png)
- [report.pdf](./report.pdf)
- [reporting.xlsx](./reporting.xlsx)
- [dataset.xlsx](./dataset.xlsx)
