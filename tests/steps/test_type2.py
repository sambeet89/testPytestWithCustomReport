from pytest_bdd import then


@then('lets print the output designed for multiply')
def multiply(request):
    print(f'printing the multiply: {int(getattr(request.node,'number_data'))*3}')
