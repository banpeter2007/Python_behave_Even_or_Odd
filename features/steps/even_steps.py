from behave import given, when, then
# TODO: Importáld a number_checker modult a src mappából
from src.number_checker import check_number


# TODO: Implementáld a Given step-et
@given('the number is {number}')
def step_given_number(context, number):
    context.number = int(number)

#@given('the number is 5')
#def step_given_number(context):
#    context.number = 5

#@given('the number is 0')
#def step_given_number(context):
#    context.number = 0


# TODO: Implementáld a When step-et
# Használd a check_number függvényt a src/number_checker.py fájlból!
@when('I check the number')
def step_when_check_number(context):
    context.result = check_number(context.number)


# TODO: Implementáld a Then step-et
@then('I should told "{expected}"')
def step_then_result(context, expected):
    assert context.result == expected, f'Elvárt érték "{expected}" de a kapott érték: "{context.result}"'


@given('the number is "{number}"')
def step_given_number(context, number):
    context.number = int(number)

@when('I ask whether its even')
def step_when_ask_even(context):
    context.result = check_number(context.number)

@then('I should be told it is "{expected}"')
def step_then_told_even(context, expected):
    assert context.result == expected, f'Expected "{expected}", but got "{context.result}"'