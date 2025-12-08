# Board Game Data Analysis

Statistical analysis and modeling of **Board Game Geek** data to understand trends in the production quantity and quality of [[Board Games]] over time. The project uses probabilistic models to uncover patterns in the board game industry.

![BGG EDA](/images/bgg_eda.png)

### Modeling Quantity

- Modeled annual game production as a Poisson process with time-varying rate
- Used exponential function for underlying rate: λ(t) = exp(at + b)
- Fitted via stochastic search with **R² = 0.983**

### Modeling Quality

- Modeled proportion of high-scoring games as binomial with changing probability
- Probability modeled as exponential function over time
- Achieved **R² = 0.868** for probabilities, **R² = 0.991** for counts

### Hypothesis Testing:

- **Themes**: Warfare games scored highest; knowledge-based games scored lowest
- **Mechanics**: Games discouraging player interaction performed best
- **Funding**: Kickstarter-funded games significantly outperformed non-Kickstarter games

The analysis reveals clear temporal trends in both the quantity and quality of board games produced, with significant differences across themes, mechanics, and funding sources.

[View on GitHub →](https://github.com/alexracape/board-game-analysis)