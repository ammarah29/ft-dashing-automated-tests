import requests
from lettuce import *
from nose.tools import assert_equal


@step('I make the request to dashing')
def load_dashing(step):
    world.response = requests.get("http://dashing-dev.internal.ft.com/blue")


@step('I should see response (\d+)')
def check_status_code(step, status_code):
    assert_equal(world.response.status_code, int(status_code))


@step('I make a request to end point')
def make_request(step):
    world.response = requests.get('http://dashing-dev.internal.ft.com/tiles/lists')


@step('I should see a list of host names if tiles are black')
def find_hosts(step):
    array_hosts = world.response.text.split('\n')
    length_array = len(array_hosts)
    for i in range(0, length_array-1):
        host_name = array_hosts[i].strip('_new.rb')
        try:
            world.get_response = requests.get('http://dashing-dev.internal.ft.com/tiles/'+host_name+'.json')
            data = world.get_response.text
        except:
            print host_name


