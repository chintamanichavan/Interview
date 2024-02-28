# Load necessary libraries
library(readxl)
library(dplyr)
library(ggplot2)

# Load and clean data
data <- read_excel("/Users/chintamanichavan/Desktop/Computer-Science/Interview/Python/HousingAndHealth/File for Midterm.xlsx", sheet = "Sheet1")
cleaned_data <- na.omit(data)

# Separate data for NY and FL
ny_data <- filter(cleaned_data, Location == "NY")
fl_data <- filter(cleaned_data, Location == "FL")

# Calculate mean prices and crime ratings for NY and FL
mean_prices <- cleaned_data %>% group_by(Location) %>% summarise(Average_Price = mean(Price))
mean_crime_ratings <- cleaned_data %>% group_by(Location) %>% summarise(Average_Crime = mean(`Crime Rating`))

# Correlation between price and crime rating
correlation <- cor(cleaned_data$Price, cleaned_data$`Crime Rating`)

# Creating a scatter plot for the correlation between house prices and crime ratings
ggplot(cleaned_data, aes(x = Price, y = `Crime Rating`)) +
  geom_point() +
  geom_smooth(method = "lm", color = "blue") + # Adding a linear regression line
  theme_minimal() +
  labs(title = "Correlation between House Prices and Crime Ratings",
       x = "House Price ($)",
       y = "Crime Rating") +
  annotate("text", x = max(cleaned_data$Price) * 0.6, y = max(cleaned_data$`Crime Rating`), 
           label = paste("Correlation: ", round(correlation, 2)), size = 5)

# Suzie's financial details
down_payment <- 100000
annual_income_ny <- 120000
annual_income_fl <- 75000

# Calculating average mortgage amount in each state after down payment
average_mortgage_ny <- mean_prices$Average_Price[mean_prices$Location == "NY"] - down_payment
average_mortgage_fl <- mean_prices$Average_Price[mean_prices$Location == "FL"] - down_payment

# Mortgage payment calculations
mortgage_payment_ny <- 0.30 * annual_income_ny
mortgage_payment_fl <- 0.30 * annual_income_fl

# Time to pay off the mortgage
years_to_payoff_ny <- average_mortgage_ny / mortgage_payment_ny
years_to_payoff_fl <- average_mortgage_fl / mortgage_payment_fl

# Preparing data for visualization
visualization_data <- data.frame(
  State = c("NY", "FL"),
  Average_Price = c(mean_prices$Average_Price[mean_prices$Location == "NY"], 
                    mean_prices$Average_Price[mean_prices$Location == "FL"]),
  Average_Crime_Rating = c(mean_crime_ratings$Average_Crime[mean_crime_ratings$Location == "NY"], 
                           mean_crime_ratings$Average_Crime[mean_crime_ratings$Location == "FL"]),
  Years_to_Payoff = c(years_to_payoff_ny, years_to_payoff_fl)
)

# Plotting Average Price Comparison
ggplot(visualization_data, aes(x = State, y = Average_Price, fill = State)) +
  geom_bar(stat = "identity") +
  theme_minimal() +
  labs(title = "Average House Price Comparison", x = "State", y = "Average Price ($)")

# Plotting Average Crime Rating Comparison
ggplot(visualization_data, aes(x = State, y = Average_Crime_Rating, fill = State)) +
  geom_bar(stat = "identity") +
  theme_minimal() +
  labs(title = "Average Crime Rating Comparison", x = "State", y = "Average Crime Rating")

# Plotting Years to Payoff Comparison
ggplot(visualization_data, aes(x = State, y = Years_to_Payoff, fill = State)) +
  geom_bar(stat = "identity") +
  theme_minimal() +
  labs(title = "Years to Pay Off Mortgage", x = "State", y = "Years")
