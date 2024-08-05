# Grouping and Chaining Data
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()

# List of all the functions in func
# Basic Functions
# Aggregate Functions:

# func.count(column): Count the number of rows.
# func.sum(column): Calculate the sum of a column.
# func.avg(column): Calculate the average of a column.
# func.max(column): Find the maximum value in a column.
# func.min(column): Find the minimum value in a column.
# String Functions:

# func.concat(*args): Concatenate two or more strings.
# func.length(column): Get the length of a string.
# func.lower(column): Convert a string to lower case.
# func.upper(column): Convert a string to upper case.
# func.substr(column, start, length): Substring extraction.
# func.replace(column, 'old', 'new'): Replace occurrences of a substring.
# func.trim(column): Trim leading and trailing spaces.
# func.ltrim(column): Trim leading spaces.
# func.rtrim(column): Trim trailing spaces.
# Date and Time Functions:

# func.current_date(): Current date.
# func.current_time(): Current time.
# func.current_timestamp(): Current timestamp.
# func.now(): Current date and time.
# func.date_add(column, interval): Add an interval to a date.
# func.date_sub(column, interval): Subtract an interval from a date.
# func.year(column): Extract the year from a date.
# func.month(column): Extract the month from a date.
# func.day(column): Extract the day from a date.
# func.hour(column): Extract the hour from a time.
# func.minute(column): Extract the minute from a time.
# func.second(column): Extract the second from a time.
# Intermediate Functions
# Mathematical Functions:

# func.abs(column): Absolute value.
# func.ceil(column): Ceiling value.
# func.floor(column): Floor value.
# func.exp(column): Exponential function.
# func.log(column): Natural logarithm.
# func.power(column, exponent): Raise to a power.
# func.sqrt(column): Square root.
# func.round(column, digits): Round a number to a specified number of decimal places.
# Aggregate Functions (continued):

# func.stddev(column): Standard deviation.
# func.variance(column): Variance.
# func.group_concat(column): Concatenate values in a group.
# Conditional Functions:

# func.ifnull(column, default): Return the default if the column is null.
# func.nullif(column1, column2): Return null if the columns are equal.
# func.coalesce(column, default): Return the first non-null value.
# func.case([(condition, value), ...], else_=default): Case statement.
# Advanced Functions
# Window Functions:

# func.row_number(): Assign a unique number to each row according to its order in the specified window.
# func.rank(): Assign a rank to each row within the partition of a result set.
# func.dense_rank(): Similar to rank(), but without gaps in ranking.
# func.ntile(num_buckets): Distribute rows in the specified number of groups.
# func.percent_rank(): Calculate the relative rank of a row within a window partition.
# func.cume_dist(): Calculate the cumulative distribution of a value in a set of values.
# JSON Functions (if supported by the database):

# func.json_extract(column, path): Extract a value from a JSON string.
# func.json_unquote(column): Unquote JSON value.
# func.json_array_length(column): Return the length of a JSON array.
# func.json_object_keys(column): Return the keys in a JSON object.
# func.json_type(column): Return the JSON type of a value.
# Full-Text Search Functions (if supported by the database):

# func.match(column, query): Perform full-text search.










# group users by age
# users = session.query(User.name, func.count(User.id)).group_by(User.name).all()

# print(users)

# Chaining

users = session.query(User).filter(User.age> 24).filter()




session.commit()