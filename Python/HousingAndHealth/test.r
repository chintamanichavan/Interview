# Load necessary libraries
library(tidyverse)
library(corrplot)

# Load data from CSV file and store in 'datagram' variable
datagram <- read.csv("/Users/chintamanichavan/Desktop/Computer-Science/Interview/Python/HousingAndHealth/Life Expectancy Data.csv")

# 1. Scatter Plot
ggplot(datagram, aes(x = Alcohol, y = Life.expectancy)) + 
  geom_point() + 
  labs(title = "Alcohol Consumption vs Life Expectancy",
       x = "Alcohol Consumption",
       y = "Life Expectancy")

# 2. Correlation Heatmap
correlations <- cor(datagram[, c("Life.expectancy", "Adult.Mortality", "Alcohol", "percentage.expenditure", "Hepatitis.B")])
corrplot(correlations, method = "color")

# 3. Bubble Plot
ggplot(datagram, aes(x = GDP, y = Life.expectancy, size = Alcohol, color = Alcohol)) + 
  geom_point(alpha = 0.6) +
  labs(title = "Life Expectancy vs GDP with Alcohol Consumption",
       x = "GDP",
       y = "Life Expectancy",
       size = "Alcohol Consumption",
       color = "Alcohol Consumption")

# 6. Regression Plot
ggplot(datagram, aes(x = Alcohol, y = Life.expectancy)) + 
  geom_point() +
  geom_smooth(method = 'lm', se = FALSE, color = 'red') +
  labs(title = "Regression Plot: Life Expectancy vs Alcohol Consumption",
       x = "Alcohol Consumption",
       y = "Life Expectancy")

# 7. Grouped Bar Chart
datagram %>%
  group_by(Status) %>%
  summarise(Avg_Alcohol = mean(Alcohol, na.rm = TRUE),
            Avg_Life_Expectancy = mean(Life.expectancy, na.rm = TRUE)) %>%
  gather(key = "Metric", value = "Value", -Status) %>%
  ggplot(aes(x = Status, y = Value, fill = Metric)) +
  geom_bar(stat = 'identity', position = 'dodge') +
  labs(title = "Average Alcohol Consumption and Life Expectancy by Country Status",
       x = "Status",
       y = "Value")

