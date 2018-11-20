# Student name: Matthew Dempster
# Student ID: 10388106
# Date: 2018-11-21
# Exam for B8IT105 Programming for Big Data
# Lecturer Darren Redmond
###############################################################################

# Question 2.
# 2.	The dataset mtcars is available by default in R.
# 
# a.	Access the mtcars dataset. Load the help file and read about it. 
#     In what year was the data collected?

# Install package
#'install.packages('mtcars')  ## no package is dataset in R
#library(mtcars) ## no package is dataset in R

# Load in the data
data(mtcars)

# Run the help
?mtcars
help(mtcars)

#The data was extracted from the 1974 Motor Trend US magazine

# b.	Select only those row which have complete records (i.e., those rows which
# have no NAs). Call this dataframe mtcars2.
# [4 marks]

mtcars2 <- mtcars[complete.cases(mtcars),]
?mtcars


# c.	Use mtcars2 to produce a boxplot of wt against cyl.
# 
# You should:
#   
#   ●	Include different colours for the three boxplots
# ●	Include a main title, and relevant x- and y-axis labels
# ●	Label the boxplots with the names of the cyl
# ●	Rotate the numbers on the left axis so that they appear horizontal
?boxplot
boxplot(mtcars2$wt ~ mtcars2$cyl)

#Include different colours for the three boxplots
colors = c(rep("red",1),rep("yellow",1),rep("green",1))
boxplot(mtcars2$wt ~ mtcars2$cyl, data= mtcars2, col=colors)

# Rotating numbers - change las for box axis
boxplot(mtcars2$wt ~ mtcars2$cyl, data= mtcars2, col=colors, las =1)

# Adding labels
boxplot(mtcars2$wt ~ mtcars2$cyl, col=colors, las=1,
        main='Weight againstCylinder',
        xlab='Number of Cylinders',
        ylab='Weight')
