from backend.schemas import BorrowerApplication


def calculate_dti(application: BorrowerApplication) -> float:
    annual_debt_payments = application.monthly_debt_payments * 12

    dti = annual_debt_payments / application.annual_income

    return round(dti, 4)

def interpret_dti(dti: float) -> dict:
    dti_percentage = round(dti * 100, 1)

    return {
        "dti_ratio": dti,
        "dti_percentage": dti_percentage,
        "interpretation": (
            f"{dti_percentage}% of annual income is committed to debt payments."
        ),
    }


def calculate_risk_score(application: BorrowerApplication) -> dict:
    score = 100
    flags = []

    dti = calculate_dti(application)

    if dti > 0.50:
        score -= 30
        flags.append("Very high debt-to-income ratio")
    elif dti > 0.40:
        score -= 20
        flags.append("High debt-to-income ratio")
    elif dti > 0.30:
        score -= 10
        flags.append("Moderate debt-to-income ratio")

    if application.missed_payments_last_12m >= 3:
        score -= 25
        flags.append("Frequent missed payments")
    elif application.missed_payments_last_12m >= 1:
        score -= 10
        flags.append("Recent missed payment history")

    if application.credit_history_years < 2:
        score -= 15
        flags.append("Limited credit history")
    elif application.credit_history_years < 5:
        score -= 5
        flags.append("Short credit history")

    debt_to_income = application.existing_debt / application.annual_income

    if debt_to_income > 1:
        score -= 15
        flags.append("Existing debt exceeds annual income")
    elif debt_to_income > 0.5:
        score -= 8
        flags.append("Elevated existing debt")

    loan_to_income = application.requested_loan_amount / application.annual_income

    if loan_to_income > 0.75:
        score -= 15
        flags.append("Requested loan is large relative to income")
    elif loan_to_income > 0.40:
        score -= 7
        flags.append("Requested loan is moderately high relative to income")

    score = max(score, 0)

    if score >= 80:
        risk_grade = "A"
        risk_level = "Low"
    elif score >= 65:
        risk_grade = "B"
        risk_level = "Low-Moderate"
    elif score >= 50:
        risk_grade = "C"
        risk_level = "Moderate"
    elif score >= 35:
        risk_grade = "D"
        risk_level = "High"
    else:
        risk_grade = "E"
        risk_level = "Very High"

    return {
        "risk_score": score,
        "risk_grade": risk_grade,
        "risk_level": risk_level,
        "flags": flags,
    }