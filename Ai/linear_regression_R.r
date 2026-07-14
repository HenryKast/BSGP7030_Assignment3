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
r_squared <- model_summary$r.squared

cat("\n")
print(model_summary)
cat("\n")

library(ggplot2)

plot <- ggplot() +
  geom_point(aes(x = dataset[[x_col]], y = dataset[[y_col]]), colour = "red") +
  geom_line(
    aes(x = dataset[[x_col]], y = predict(model, newdata = dataset)),
    colour = "blue"
  ) +
  annotate(
    "text",
    x = min(dataset[[x_col]]),
    y = max(dataset[[y_col]]),
    label = paste("R² =", round(r_squared, 3)),
    hjust = -0.2
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
