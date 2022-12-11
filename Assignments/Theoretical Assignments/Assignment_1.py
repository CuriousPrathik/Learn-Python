#!/usr/bin/env python
# coding: utf-8

#  # Assignment 1

# ## QUESTION-1 :-
# 
# In the below elements which of them are values or an expression? eg:- values can be
# integer or string and expressions will be mathematical operators.
# 
# *, 'hello', -87.8, -, /, +, 6
# 
# ### SOLUTION :-
# 
# ##### Values are
# 
# -87.8, 'hello', 6
# 
# ##### Expressions are
# 
# *, -, /, +

# ## QUESTION-2 :-
#     
# What is the difference between string and variable?
# 
# ### SOLUTION :-
#     
# * String is a primitive data type, 
# * It is a collection of characters surrounded by single ' ', double " " or triple quotes ''' '''
# 
# Variable are used to store data, it is a name that is a reference to a data type.

# ## QUESTION-3 :-
#     
# Describe three different data types?
# 
# ### SOLUTION :-
#     
# Numeric data type consist of three data types.
# 
# * Integer Type = Whole number
# * Float Type = Number with decimal
# * Complext Type = Number having Real and imaginary number

# ## QUESTION-4 :-
#     
# What is an expression made up of and What do all expressions do?
# 
# ### SOLUTION :-
# 
# An expression is a combination of operators and operands.
# 
# It is interpreted to produce some other value.

# ## QUESTION-5 :-   
#     
# This assignment statements, like spam = 10. What is the difference between an
# expression and a statement?
# 
# ### SOLUTION :-
#     
# In programming language terminology, 
# 
# an “expression” is a combination of values and functions that are combined and interpreted by the compiler to create a new value.
# 
# a “statement” which is just a standalone unit of execution, like spam = 10
# 

# ## QUESTION-6 :-
#     
# After running the following code, what does the variable bacon contain?
# bacon = 22
# bacon + 1
# 
# ### SOLUTION :-
#     
# 22
# 
# ### REASON :-
# 
# The expression bacon + 1 does not reassign the value in bacon 
# (that would the case if the expression is like bacon = bacon + 1 or bacon += 1)

# ## QUESTION-7 :-
#     
# What should the values of the following two terms be?
#     spam + spamspam
#     spam * 3
# 
# ### SOLUTION :-
#     
#     spamspamspam
#     
#     spamspamspam
#     
# ### REASON :-
#     
#     + is used for concatination of strings
#     
#     string * 3 will print string three times known as String Multiplication

# ## QUESTION-8 :-
# 
# Why is eggs a valid variable name while 100 is invalid?
# 
# ### REASON :-
# 
# Variable names cannot begin with a number. The python rules for naming a variable are :-
# 
# Variable name must start with a letter or the underscore character.
# Variable name cannot start with a number.
# Variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, & _ ).
# Variable names are case-sensitive (age, Age, and AGE are three different variables.
# The reserved words(keywords) cannot be used naming the variable.

# ## QUESTION-9 :-
#     
# What three functions can be used to get the integer, floating-point number, or string
# version of a value?
# 
# ### SOLUTION :-
#     
# int() is used to get integer as a value
# 
# float() is used to get float as a value
# 
# str() is used to get string as a value
# 
# 

# ## QUESTION-10 :-
#     
# Why does this expression cause an error? How can you fix it?
# 
# 'I have eaten' + 99 + 'burritos'
# 
# ### REASON :-
# 
# Here 99 is a number and not a string
# 
# Concatination of string with number is not possible, we need to convert 99 into a string to solve this error.
