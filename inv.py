#!/usr/bin/env python

import json
import argparse

'''
A class that programmatically determines the Anka VM IPs. If the Anka
VM is not running, or if it doesn't yet have an IP, this class starts
up the Anka VM and waits until it has an IP.

run with:
`ansible-playbook all -i ./inv.py <command>`

For example:
`ansible-playbook all -i ./inv.py -m ping`

'''


class Inventory(object):
    def __init__(self):
        self.inventory = {}
        self.read_cli_args()

        if self.args.list:
            self.inventory = self.default_inventory()
        elif self.args.host:
            # not implemented, since we return _meta info `--list`
            self.inventory = self.empty_inventory()
        else:
            # If no groups or vars are present, return an empty inventory.
            self.inventory = self.empty_inventory()
        print(json.dumps(self.inventory))

    def default_inventory(self):
        return {
            'geek': {
                'hosts': [
                    '192.168.1.66',
                ],
                'vars': {
                    'ansible_ssh_user': 'geek'
                }
            },
            '_meta': {
                'hostvars': {}
            }
        }

    def empty_inventory(self):
        return {'_meta': {'hostvars': {}}}

    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action='store_true')
        parser.add_argument('--host', action='store')
        self.args = parser.parse_args()


Inventory()
