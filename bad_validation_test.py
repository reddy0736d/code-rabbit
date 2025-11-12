# bad_validation_test.py

# ❌ This file violates multiple validation and style rules:
# - No field validation (missing special character check)
# - Print statements used (disallowed)
# - Missing docstrings
# - No input sanitization
# - Uses eval()
# - Bad naming (camelCase)
# - Missing error disable logic for Save button

def handleUserInput(name, email):
    print("Received name:", name)  # ❌ print() not allowed
    print("Received email:", email)

    # ❌ No validation: should check if name/email start with special characters
    # Expected: check name[0].isalnum() before saving

    user_data = {
        "name": name,
        "email": email
    }

    # ❌ Uses eval() – very risky, disallowed
    result = eval("2 + 2")
    print("Result:", result)

    # ❌ Always allows save without validation
    save_enabled = True
    if save_enabled:
        print("✅ Save button enabled")  # ❌ Should be disabled if invalid input

    return user_data


# ❌ Function with no validation logic or docstring
def saveFormData(form):
    # TODO: validate fields here  # ❌ TODO disallowed
    print("Saving form data:", form)
    return True


# ❌ Top-level code execution
handleUserInput("@Rohit", "test@email.com")
print("Form submitted!")  # ❌ Disallowed print
