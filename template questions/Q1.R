# Student name: Matthew Dempster
# Student ID: 10388106
# Date: 2018-11-21
# Exam for B8IT105 Programming for Big Data
# Lecturer Darren Redmond
###############################################################################

# Get the Data

# Install package
install.packages('MASS')
library(MASS)

# Load from file
data <- read.csv("filename.csv")

# Data inbuilt
?mtcars

# Data from package
data(Boston)
?Boston

# Info on the data loaded (not from file)
?Boston

# data structure
str(Boston)



