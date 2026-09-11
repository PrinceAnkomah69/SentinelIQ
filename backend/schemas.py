from pydantic import BaseModel, Field


class BorrowerApplication(BaseModel):
    annual_income: float = Field(gt=0)
    monthly_debt_payments: float = Field(ge=0)
    requested_loan_amount: float = Field(gt=0)
    credit_history_years: float = Field(ge=0)
    missed_payments_last_12m: int = Field(ge=0)
    existing_debt: float = Field(ge=0)
    business_revenue: float = Field(ge=0)