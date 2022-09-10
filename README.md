# EonLabs-TTA

This is a problem solution for EonLabs Take-home Tech Assessment (TTA).

Author: Osama Elfar.
Date: September 9, 2022.

## Overview

The data engineering team has done some research and found that the [Google Trends](https://en.wikipedia.org/wiki/Google_Trends) data is potentially beneficial to the data science team. YOU, as a data scientist, want a **time series of normalized Google Trends data from 2017 till the present with hourly interval**. YOU informed the engineering team of this requirement, but they said they could not fetch the hourly data directly. The reason why they are unable to fetch the hourly data directly is explained in the **Deep Dive** section. They may, however, fetch the following raw data from Google Trends:

- `hourly_data.csv`: a time series of weekly-normalized Google Trends data starting in 2017 and continuing up to the present, with hourly intervals
- `weekly_data.csv`: a time series of yearly-normalized Google Trends data starting in 2017 and continuing up to the present, with weekly intervals
- `monthly_data.csv`: a time series of normalized Google Trends data starting in 2017 and continuing up to the present, with monthly intervals

## Methodology
As the hourly data values are normalized seperatley for each week, the weekly data values will be used as weights for hourly values. i. e., each weekly value is a weight for its corresponding hourly values in the same week. By multiplying weekly weights to corresponding hourly values, the hourly values become yearly normalized.

In the same way, the monthly data will be used then as weights for hourly values to normalize it for the whole duration. However, we should firstly normalize hourly values for each month and then multiply monthly weights to corresponding hourly values in each month. And hence, the hourly values become normalized for the whole duration.
