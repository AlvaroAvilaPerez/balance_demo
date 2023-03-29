import requests
import pytest

server = "https://accountingServer.com/"


@pytest.mark.parametrize('deposit_amount, expected_status_code, user_id', [
    (100, 200, 124435),
    (10000, 200, 124435),
    (9999, 200, 124436),
    (10001, 400, 124436)])
def test_verify_deposit(deposit_amount, expected_status_code, account_id):
    balance_path = f'/accounts/{account_id}/balance'
    response_balance = requests.get(server + balance_path)
    current_balance = response_balance["balance"]
    deposit_path = f'/accounts/{account_id}/deposits'
    body = {
        'deposit': {deposit_amount}
    }
    response = requests.post(server + deposit_path, data=body)
    response_body = response.json()
    assert response.status_code == expected_status_code, \
        f"Failed expected status code was: {expected_status_code} and received: {response.status_code}"
    assert float(response_body["balance"]) == float(current_balance + deposit_amount), "Failed in update balance"
