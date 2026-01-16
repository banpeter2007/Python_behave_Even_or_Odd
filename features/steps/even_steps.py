from behave import given, when, then
# TODO: Importáld a number_checker modult a src mappából
from src.number_checker import check_number



@given('the number is "{number}"')
def step_given_number(context, number):
    context.number = int(number)

@when('I ask whether its even')
def step_when_ask_even(context):
    context.result = check_number(context.number)

@then('I should be told it is "{expected}"')
def step_then_told_even(context, expected):
    assert context.result == expected, f'Expected "{expected}", but got "{context.result}"'