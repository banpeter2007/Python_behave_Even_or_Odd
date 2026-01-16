from behave import given, when, then
# TODO: Importáld a number_checker modult a src mappából
from src.number_checker import check_number


# TODO: Implementáld a Given step-et
@given('the number is 4')
def step_given_number(context):
    context.number = 4


# TODO: Implementáld a When step-et
# Használd a check_number függvényt a src/number_checker.py fájlból!
@when('I check the number')
def step_when_check_number(context):
    context.result = check_number(context.number)


# TODO: Implementáld a Then step-et
@then('I should told "{expected}"')
def step_then_result(context, expected):
    assert context.result == expected, f'Elvárt érték "{expected}" de a kapott érték: "{context.result}"'