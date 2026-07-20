args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 3) {
  stop("Usage: Rscript linear_regression_r.R <filename> <x_column> <y_column>")
}

filename <- args[1]
x_col <- args[2]
y_col <- args[3]

dataset <- read.csv(filename)
formula <- as.formula(paste(y_col, "~", x_col))
model <- lm(formula, data = dataset)

r_squared <- summary(model)$r.squared
r <- cor(dataset$YearsExperience, dataset$Salary)
pred <- predict(model)
mse <- mean((dataset$Salary - pred)^2)
slope <- coef(model)[2]
intercept <- coef(model)[1]

library(ggplot2)
plot <- ggplot() +
  geom_point(aes(x = dataset$YearsExperience, y = dataset$Salary), colour = 'red') +
  geom_line(aes(x = dataset$YearsExperience, y = predict(model, newdata = dataset)), colour = 'blue') +
annotate("text", x = min(dataset$YearsExperience), y = max(dataset$Salary), label = paste
          ("y =", round(slope, 2), 
          "x +", round(intercept, 2), 
          "\nr =", round(r, 2)), 
         hjust=0, vjust=0.4) +
ggtitle('Salary vs Experience') +
  xlab('Years of experience') +
  ylab('Salary')
  

summary_table <- data.frame(Metric = c("Intercept", "Slope", "MSE", "r", "R_squared"), Value = c(intercept, slope, mse, r, r_squared))
ggsave("linear_regression_r_output.png", plot)
print(summary_table)
print(plot)




