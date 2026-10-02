#!/bin/bash

# Prompt user for input
read -p "Enter first number: " num1
read -p "Enter second number: " num2

# Perform addition using arithmetic expansion
sum=$((num1 + num2))

# Print the result
echo "The sum is: $sum"
