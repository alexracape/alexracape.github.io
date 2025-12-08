# LEGO Trader

Believe it or not, there is a [huge market](https://www.brickeconomy.com/) for old LEGO sets, and many people will buy sets just to keep them in the box and sell them later. These LEGO investors have historically done really well, so we decided to dig into the features that drive LEGO set prices on secondary markets.

## Dataset

We curated a novel dataset of 15,000 LEGO sets with their features and historical prices. We then used machine learning to predict LEGO set prices and develop profitable trading strategies. 

The system combines data from two sources:

- **Bricklink API**: Current market prices (as of May 2023)
- **Brickset API**: Historical list prices and set features

## Modelling Appreciation

Two basic models were developed and compared:

- **Random Forest**: Ensemble learning approach
- **Neural Network**: Deep learning model

Both models achieved excellent predictive performance for list prices and current market values. The trading strategy consistently outperformed the S&P 500 and equal-weighted LEGO portfolios. Feature importance analysis revealed key factors driving LEGO set valuations, and the model generated five-year price forecasts.

The complete dataset is available on [Kaggle](https://www.kaggle.com/datasets/alexracape/lego-sets-and-prices-over-time), and it has reached over 2,400 downloads with active users every month.

[View on GitHub →](https://github.com/alexracape/lego-learner)

## Regression Model

I then expanded on this project to create a multilinear regression model that predicted LEGO set prices based on their features. I met with an executive at LEGO, and developed this [report](https://github.com/alexracape/lego-learner/blob/main/Final%20Project.pdf) detailing the results of my analysis. For those who are curious, the model estimated an average annual appreciation of 9.97%..