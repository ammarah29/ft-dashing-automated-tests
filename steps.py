import requests
from lettuce import *
from nose.tools import assert_equal
import urllib2
from BeautifulSoup import *
import requests


@step('I make the request to dashing')
def load_dashing(step):
    world.response = requests.get("http://dashing-dev.internal.ft.com/blue")


@step('I should see response (\d+)')
def check_status_code(step, status_code):
    assert_equal(world.response.status_code, int(status_code))


@step('I list all data ids with corresponding data urls')
def find_hosts(step):
    response = urllib2.urlopen("http://dashing-dev.internal.ft.com/blue")
    page_source = response.read()
    soup = BeautifulSoup(page_source)

    divparent = soup.findAll('div', {"data-id": True}, {"data-url": True})
    target = open('List_of_Hosts', 'w')
    for div_content in divparent:
        if div_content['data-id'] == 'reload':
            continue
        else:

            target.write(div_content['data-id'] + '|' + div_content['data-url'] + '|' + '\n')

    target.close()


@step('I should see a list of host names if tiles are black')
def find_black_tile_hosts(step):
    target = open('List_of_Hosts', 'r')

    for lines in target:
        host_name = lines.split('|')[0]
        try:
            world.get_response = requests.get('http://dashing-dev.internal.ft.com/tiles/' + host_name + '.json')
            data = world.get_response.text
            if not data:
                print host_name +'\n'
        except Exception:
            print 'No status endpoint'


'''

@step('I search for background dimgray')
def

@step('If dimgray then check status code of data url')
def


@step('I make a request to end point')
def make_request(step):
    world.response = requests.get('http://dashing-dev.internal.ft.com/widgets/lists/')

@step('I should see a list of host names if tiles are black')
def find_hosts(step):
    array_hosts = world.response.text.split('\n')
    length_array = len(array_hosts)
    for i in range(0, length_array-1):
        host_name = array_hosts[i].strip('_new.rb')
        try:
            world.get_response = requests.get('http://dashing-dev.internal.ft.com/lists/'+host_name+'.json')
            data = world.get_response.text
        except:
            print host_name


@step('I search for grey tiles')
def find_hosts(step):
    data = urllib2.urlopen('http://dashing.internal.ft.com/blue')
    #for lines in data.readlines():
    soup = BeautifulSoup(data)
        #div = soup.find(id="ftmon04163-lvpr-uk-p")
    div = soup.div
    maxTemp = soup.findAll(attrs={"div"})
    #list = soup.findAll("div", {"id": "data-id"})
    print maxTemp

'''
