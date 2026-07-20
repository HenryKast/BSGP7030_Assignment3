# Standalone linear regression script converted from linear_regression_R.ipynb

args <- commandArgs(trailingOnly = TRUE)

if (length(args) < 3) {
  stop("Usage: Rscript linear_regression_R.r <filename> <x_column> <y_column> [--output plot.png] [--show]")
}

resolve_path <- function(path_str) {
  if (file.exists(path_str)) {
    return(normalizePath(path_str))
  }

  args_all <- commandArgs(trailingOnly = FALSE)
  file_arg <- grep("^--file=", args_all, value = TRUE)
  script_dir <- if (length(file_arg) > 0) {
    dirname(normalizePath(sub("^--file=", "", file_arg[1])))
  } else {
    getwd()
  }

  script_relative <- file.path(script_dir, path_str)
  if (file.exists(script_relative)) {
    return(normalizePath(script_relative))
  }

  stop(paste0(
    "Could not find '", path_str,
    "' in the current directory or '", script_dir, "'."
  ))
}

get_script_dir <- function() {
  args_all <- commandArgs(trailingOnly = FALSE)
  file_arg <- grep("^--file=", args_all, value = TRUE)
  if (length(file_arg) > 0) {
    return(dirname(normalizePath(sub("^--file=", "", file_arg[1]))))
  }
  getwd()
}

print_metrics_table <- function(mse, r_value, slope, intercept, r_squared) {
  metrics <- data.frame(
    Metric = c("MSE", "r", "slope", "intercept", "r_squared"),
    Value = c(
      sprintf("%.4f", mse),
      sprintf("%.4f", r_value),
      sprintf("%.4f", slope),
      sprintf("%.4f", intercept),
      sprintf("%.4f", r_squared)
    ),
    stringsAsFactors = FALSE
  )
  col0 <- max(nchar("Metric"), max(nchar(metrics$Metric)))
  col1 <- max(nchar("Value"), max(nchar(metrics$Value)))
  border <- paste0("+-", paste(rep("-", col0), collapse = ""), "-+-", paste(rep("-", col1), collapse = ""), "-+")
  cat("\n")
  cat(border, "\n")
  cat(sprintf("| %-*s | %-*s |\n", col0, "Metric", col1, "Value"))
  cat(border, "\n")
  for (i in seq_len(nrow(metrics))) {
    cat(sprintf("| %-*s | %-*s |\n", col0, metrics$Metric[i], col1, metrics$Value[i]))
  }
  cat(border, "\n\n")
}

filename <- resolve_path(args[1])
x_col <- args[2]
y_col <- args[3]
output_file <- NULL
show_plot <- FALSE

if (length(args) > 3) {
  idx <- 4
  while (idx <= length(args)) {
    if (args[idx] == "--output" && idx < length(args)) {
      output_file <- args[idx + 1]
      idx <- idx + 2
    } else if (args[idx] == "--show") {
      show_plot <- TRUE
      idx <- idx + 1
    } else {
      stop(paste("Unknown argument:", args[idx]))
    }
  }
}

dataset <- read.csv(filename)
model <- lm(as.formula(paste(y_col, "~", x_col)), data = dataset)
model_summary <- summary(model)

slope <- coef(model)[[x_col]]
intercept <- coef(model)[["(Intercept)"]]
r_squared <- model_summary$r.squared
r_value <- cor(dataset[[x_col]], dataset[[y_col]])
y_pred <- predict(model, newdata = dataset)
mse <- mean((dataset[[y_col]] - y_pred)^2)

print_metrics_table(mse, r_value, slope, intercept, r_squared)

library(ggplot2)

annotation_label <- paste0(
  "y = ", sprintf("%.2f", slope), "x + ", sprintf("%.2f", intercept),
  "\nr = ", sprintf("%.2f", r_value)
)

plot <- ggplot() +
  geom_point(aes(x = dataset[[x_col]], y = dataset[[y_col]]), colour = "red") +
  geom_line(
    aes(x = dataset[[x_col]], y = y_pred),
    colour = "blue"
  ) +
  annotate(
    "text",
    x = -Inf,
    y = Inf,
    label = annotation_label,
    hjust = -0.05,
    vjust = 1.2,
    size = 4
  ) +
  ggtitle(paste(y_col, "vs", x_col)) +
  xlab(x_col) +
  ylab(y_col)

if (is.null(output_file) && !show_plot) {
  output_file <- file.path(get_script_dir(), "linear_regression_R_output.png")
}

if (!is.null(output_file)) {
  ggsave(output_file, plot)
  cat("Plot saved to", normalizePath(output_file, mustWork = FALSE), "\n")
}

if (show_plot) {
  print(plot)
}
