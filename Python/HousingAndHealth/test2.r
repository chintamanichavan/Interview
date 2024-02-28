# Load necessary libraries
library(tidyverse)
library(corrplot)

# Load extended data from CSV file and store in 'datagram' variable
datagram <- read.csv("/Users/chintamanichavan/Desktop/Computer-Science/Interview/Python/HousingAndHealth/Augmented_Life_Expectancy_Data.csv")

# 1. Scatter Plot
# Adjust point size or alpha if plot is too crowded
ggplot(datagram, aes(x = Alcohol, y = Life.expectancy)) + 
  geom_point() +  # consider adjusting alpha for transparency
  labs(title = "Alcohol Consumption vs Life Expectancy",
       x = "Alcohol Consumption",
       y = "Life Expectancy")

# 2. Correlation Heatmap
# This should work fine but might take longer to compute with larger data
correlations <- cor(datagram[, c("Life.expectancy", "Adult.Mortality", "Alcohol", "percentage.expenditure", "Hepatitis.B")])
corrplot(correlations, method = "color")

# 3. Bubble Plot
# Adjust point size and alpha for better visualization with more data
ggplot(datagram, aes(x = GDP, y = Life.expectancy, size = Alcohol, color = Alcohol)) + 
  geom_point(alpha = 0.6) +  # adjust alpha as needed
  labs(title = "Life Expectancy vs GDP with Alcohol Consumption",
       x = "GDP",
       y = "Life Expectancy",
       size = "Alcohol Consumption",
       color = "Alcohol Consumption")

# 6. Regression Plot
# This plot should also work fine but you may consider adjusting the point size
ggplot(datagram, aes(x = Alcohol, y = Life.expectancy)) + 
  geom_point() +  # consider adjusting alpha or point size
  geom_smooth(method = 'lm', se = FALSE, color = 'red') +
  labs(title = "Regression Plot: Life Expectancy vs Alcohol Consumption",
       x = "Alcohol Consumption",
       y = "Life Expectancy")

# 7. Grouped Bar Chart
# This plot should handle more data well, but watch out for any performance issues
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
