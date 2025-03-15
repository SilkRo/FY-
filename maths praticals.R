#pratical 1
# Example data
data <- c(1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7)

# 1. Create Frequency Distribution
frequency_table <- table(data)
print("Frequency Distribution:")
print(frequency_table)

# 2. Bar Plot for Frequency Distribution
barplot(frequency_table, 
        main="Frequency Distribution of Data", 
        xlab="Values", 
        ylab="Frequency", 
        col="blue", 
        border="red")

# 3. Histogram for Data (For Continuous Data)
hist(data, 
     main="Histogram of Data", 
     xlab="Values", 
     ylab="Frequency", 
     col="lightblue", 
     border="darkblue", 
     breaks=5)

pratical 2
                                                                        
# Example data
data <- c(1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7)

# 1. Mean (Average) (The mean is calculated by summing all the numbers and dividing by the count of numbers.)
mean_value <- mean(data)
print(paste("Mean:", mean_value))

# 2. Median (Middle Value) :The median is the middle value when the data is ordered. If the data set has an even number of elements, the median is the average of the two middle values
median_value <- median(data)
print(paste("Median:", median_value))

# 3. Mode (Most Frequent Value):The mode is the most frequent value in the data set. If no value repeats, there is no mode.
get_mode <- function(data) {
  uniq_data <- unique(data)
  freq <- tabulate(match(data, uniq_data))
  uniq_data[which.max(freq)]
}
mode_value <- get_mode(data)
print(paste("Mode:", mode_value))

pratical 4
# Sample data
numbers <- c(5, 12, 18, 25, 30, 35, 40, 45, 50, 55)

# Define bins (intervals)
bins <- cut(numbers, breaks = c(0, 10, 20, 30, 40, 50, 60), right = FALSE)

# Create frequency table
frequency_table <- table(bins)

# Print results
cat("Numbers:", numbers, "\n")
cat("Frequency Distribution:\n")
print(frequency_table)

pratical 5
# Sample Data: Student Scores
scores <- c(85, 90, 78, 92, 88, 76, 95, 89, 84, 91)

# Creating a Data Frame
student_data <- data.frame(
  ID = 1:10,
  Name = c("Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Helen", "Ivy", "Jack"),
  Score = scores
)

# Displaying Data
print("Student Data Frame:")
print(student_data)

# Summary Statistics
print("Summary Statistics:")
print(summary(student_data$Score))  # Min, Max, Mean, Median, 1st & 3rd Quartiles

# Frequency Distribution
score_bins <- cut(scores, breaks = c(70, 80, 90, 100), right = FALSE)
frequency_table <- table(score_bins)
print("Frequency Distribution:")
print(frequency_table)

# Visualization: Histogram
hist(scores, breaks = c(70, 80, 90, 100), col = "lightblue",
     main = "Score Distribution", xlab = "Scores", ylab = "Frequency")

# Bar Plot for Frequency
barplot(frequency_table, col = "blue",
        main = "Frequency of Score Ranges", xlab = "Score Ranges", ylab = "Count")

#pratical 6
# Probability of Coin Toss Outcomes
coin <- c("Heads", "Tails")
coin_toss <- sample(coin, size = 1, replace = TRUE)
cat("Coin Toss Result:", coin_toss, "\n")

# Probability of Rolling a Dice
dice <- 1:6
dice_roll <- sample(dice, size = 1, replace = TRUE)
cat("Dice Roll Result:", dice_roll, "\n")

# Simulating Multiple Coin Tosses
num_tosses <- 100
coin_tosses <- sample(coin, size = num_tosses, replace = TRUE)
coin_table <- table(coin_tosses)
cat("Coin Toss Frequency (100 Tosses):\n")
print(coin_table)

# Probability Distribution: Binomial (Example: 10 Coin Tosses, P(Heads) = 0.5)
binom_prob <- dbinom(x = 5, size = 10, prob = 0.5)  # P(5 Heads in 10 Tosses)
cat("P(5 Heads in 10 Tosses):", binom_prob, "\n")

# Probability Distribution: Normal (Example: Heights of People, Mean=170, SD=10)
height_prob <- pnorm(180, mean = 170, sd = 10)  # P(Height <= 180)
cat("P(Height <= 180cm):", height_prob, "\n")

# Visualization: Probability Mass Function for a Dice Roll
barplot(rep(1/6, 6), names.arg = dice, col = "lightblue",
        main = "Probability of Dice Outcomes", xlab = "Dice Faces", ylab = "Probability")

#pratical 7
# 1. Creating Numeric Vectors Using c()
num_vector <- c(1, 2, 3, 4, 5) # Numeric vector
print("Numeric Vector:")
print(num_vector)

# 2. Creating Text Vectors Using c()
text_vector <- c("apple", "banana", "cherry")
print("Text Vector:")
print(text_vector)

# 3. Creating a Sequence with seq()
seq_vector <- seq(1, 10, by=2)  # Sequence from 1 to 10 with a step of 2
print("Sequence Vector:")
print(seq_vector)

# 4. Mathematical Operations on Vectors
sum_result <- num_vector + 2     # Addition: Add 2 to each element
diff_result <- num_vector - 2    # Subtraction: Subtract 2 from each element
prod_result <- num_vector * 2    # Multiplication: Multiply each element by 2
div_result <- num_vector / 2     # Division: Divide each element by 2
exp_result <- exp(num_vector)    # Exponential
log_result <- log(num_vector)    # Natural Logarithm
log10_result <- log10(num_vector) # Log base 10

print("Addition Result (num_vector + 2):")
print(sum_result)
print("Subtraction Result (num_vector - 2):")
print(diff_result)
print("Multiplication Result (num_vector * 2):")
print(prod_result)
print("Division Result (num_vector / 2):")
print(div_result)
print("Exponential Result (exp(num_vector)):")
print(exp_result)
print("Logarithm (Natural Log) Result (log(num_vector)):")
print(log_result)
print("Logarithm (Base 10) Result (log10(num_vector)):")
print(log10_result)

#pratical 8
# 5. Data Entry Using scan()
print("Enter a series of numbers: ")
user_input <- scan()   # Accept user input for a vector
1: 25
2: 50
3:
print("You entered:")
print(user_input)

# 6. Creating a Data Frame
data <- data.frame(
  Numbers = num_vector,
  Square = num_vector^2,
  Log10 = log10(num_vector)
)
print("Data Frame Example:")
print(data)

# 7. Matrix Operations
matrix1 <- matrix(1:9, nrow=3, byrow=TRUE)  # Create a 3x3 matrix
matrix2 <- matrix(9:1, nrow=3, byrow=TRUE)  # Another 3x3 matrix
matrix_sum <- matrix1 + matrix2  # Matrix addition
matrix_prod <- matrix1 %*% matrix2  # Matrix multiplication (dot product)

print("Matrix 1:")
print(matrix1)
print("Matrix 2:")
print(matrix2)
print("Matrix Addition Result (matrix1 + matrix2):")
print(matrix_sum)
print("Matrix Multiplication Result (matrix1 %*% matrix2):")
print(matrix_prod)

# 8. Using split() for Text Data
split_result <- split(text_vector, c(1, 1, 2))  # Split the vector into two groups
print("Split Vector Result:")
print(split_result)
