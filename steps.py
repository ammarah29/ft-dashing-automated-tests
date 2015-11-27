import requests
from lettuce import *
from nose.tools import assert_equal
import urllib2
from BeautifulSoup import *
import requests
import json
import sys


@step('I make the request to dashing')
def load_dashing(step):
    world.response = requests.get("http://dashing-int.internal.ft.com/blue")


@step('I should see response (\d+)')
def check_status_code(step, status_code):
    assert_equal(world.response.status_code, int(status_code))


@step('I list all data ids with corresponding data urls')
def find_hosts(step):
    try:
        response = urllib2.urlopen("http://dashing-int.internal.ft.com/blue")
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
    except Exception:
        print 'Dashing is not running'


@step('I should see a list of host names if tiles are black')
def find_black_tile_hosts(step):
    target = open('List_of_Hosts', 'r')
    blacklist = []
    blackbool = True

    for lines in target:
        line_split = lines.split('|')
        host_name = line_split[0]
        world.get_response = requests.get('http://dashing-int.internal.ft.com/widgets/' + host_name + '.json')
        data = world.get_response.text

        if not data:
            #print host_name + '\n'
            blackbool = True
            blacklist.append(host_name)

    assert_equal(blackbool,False,msg='ERROR: Black tiles on dashing:'+ str(blacklist))

@step('I search for grey tiles and make sure that they should be grey')
def find_gray_backgroud_tiles(step):
    target = open('List_of_Hosts', 'r')

    fakegreylist = []
    fakegrey = False

    for lines in target:
        line_split = lines.split('|')
        host_name = line_split[0]
        url = line_split[1]
        if 'nagios' in url or 'zabbix' in url or 'healthcheck' in url:
            world.get_response = requests.get('http://dashing-int.internal.ft.com/widgets/' + host_name + '.json')
            data = json.loads(world.get_response.content)

            if data['status'] == 'background:dimgray' or data['status'] == 'noconn':
                try:

                    world.get_status = requests.get(url).status_code

                    if world.get_status == 200:
                        #print host_name, '\n'
                        fakegrey = True
                        fakegreylist.append(host_name)
                except Exception:
                    pass

    assert_equal(fakegrey,False,msg='ERROR:These grey tiles should not be grey:'+ str(fakegreylist))
