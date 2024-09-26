from json_logic import jsonLogic

# Rule: If age is greater than 18, return "adult", otherwise "minor"
rule = {
  "if": [
    {">": [{"var": "age"}, 18]}, "adult",
    "minor"
  ]
}

# Data: User information
data = {"age": 16}

# Apply the rule with data
result = jsonLogic(rule, data)

print(result)  # Output: minor
