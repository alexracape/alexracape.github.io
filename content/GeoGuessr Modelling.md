# GeoGuessr Modelling

We trained a deep neural network that predicts the country of origin for a given image. The project tackles the challenging problem of geographical image classification with systematic data engineering and performance optimization.

![The Challenge](https://github.com/alankct/Geo-Guesser/assets/86837040/fb183157-c524-4340-a8f8-01b3ea7ec55d)

## Overview

The system uses **transfer learning** with a ResNet152 backbone combined with a custom classification head. Key achievements include:

### Data Engineering

- Curated a balanced dataset of ~100,000 images
- Filtered outlier countries and balanced distributions to match real-world Google Maps data
- Transformed highly skewed initial distributions into uniform geographical coverage

![Architecture](https://github.com/alankct/Geo-Guesser/assets/86837040/48b1b779-69e1-485f-82c3-aa6d0e265bd8)

### Performance Optimization

- Reduced epoch training time from 30 minutes to 5 minutes (**83% speedup**)
- Created a tensor-based dataset with pre-extracted ResNet features

The result is an accurate country predictor that efficiently processes large-scale geographical image data.

[View on GitHub →](https://github.com/alankct/Geo-Guesser)