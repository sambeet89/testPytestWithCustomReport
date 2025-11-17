from pytest_bdd import given, parsers, when, then


@given("we are executing background")
def step_background():
    print("executing background")


@given("we ar ein the testoutline with example")
def step_testoutline():
    print("executing-we ar ein the testoutline with example ")


@when(parsers.parse('the testdata is {data}'))
def step_testdata(request,data):
    print(f'executing-the testdata is {data} ')
    setattr(request.node,'number_data',data)

@then('lets print the output')
def step_print_output(request):
    num= int(getattr(request.node,'number_data'))
    print(f'executing-lets print the output {num*2}')

@when(parsers.parse('add {num} to the data'))
def step_add_number_to_data(request,num):
    existing = getattr(request.node,'number_data')
    setattr(request.node,'number_data',(int(existing)+int(num)))
