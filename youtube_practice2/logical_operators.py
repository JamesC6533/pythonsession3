# if applicant has high income AND good credit, then they are eligible for a loan

has_good_credit = True
has_high_income = True

if has_good_credit and has_high_income:
    print("You're eligible for a loan")

# if applicant has high income OR good credit, then they are eligible for a loan

has_good_credit = True
has_high_income = True

if has_good_credit or has_good_credit:
    print("You're eligible for a loan")

# # if applicant has high income OR good credit, and doesn't have a criminal record

has_criminal_record = False
has_good_credit = True

if has_good_credit and not has_criminal_record:
    print("You're eligible for a loan")

