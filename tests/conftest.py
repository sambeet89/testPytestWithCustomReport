import pytest
from pytest_html import extras
from tests.utils.reporting import add_custom_report
from .steps.test_type1 import *
from .steps.test_type2 import *

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    output = yield
    report = output.get_result()
    report_extras=getattr(report,"extras",[])
    #my test 
    if report.when=='call':
        custom_html= getattr(item, "custom_html", None)
        if custom_html:
            report_extras.append(extras.html(custom_html))

    report.extras=report_extras
def pytest_runtest_makereport2(item, call):
    output = yield
    report = output.get_result()
    report_extras=getattr(report,"extras",[])
    #my test
    if report.when=='call':
        custom_html= getattr(item, "custom_html", None)
        if custom_html:
            report_extras.append(extras.html(custom_html))

    report.extras=report_extras



#learning
#from login feature branch

