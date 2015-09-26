#!/usr/bin/env python
# (c) Copyright [2015] Hewlett Packard Enterprise Development LP
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os
import sys
import urllib2
import httplib
import cookielib
from time import sleep

import ovs.dirs
import ovs.db.idl
from ovs.db import error
from ovs.db import types

# ovs definitions
idl = None
DEF_DB = 'unix:/var/run/openvswitch/db.sock'
OVS_SCHEMA = '/usr/share/openvswitch/vswitch.ovsschema'

SYSTEM_TABLE = "System"
MGMT_INTF_NULL_VAL = 'null'
MGMT_INTF_KEY_DHCP_HOSTNAME = "dhcp_hostname"

#------------------ wait_for_config_complete() ----------------


def wait_for_config_complete(idl):

    system_is_configured = 0
    while system_is_configured == 0:
        for ovs_rec in idl.tables[SYSTEM_TABLE].rows.itervalues():
            if ovs_rec.cur_cfg is not None and ovs_rec.cur_cfg != 0:
                system_is_configured = ovs_rec.cur_cfg
                break

        poller = ovs.poller.Poller()
        idl.run()
        idl.wait(poller)
        poller.block()

#------------------ update_mgmt_intf_status_hostname() ----------------


def update_mgmt_intf_status_hostname(hostname):
    global idl

    status_data = {}

    for ovs_rec in idl.tables[SYSTEM_TABLE].rows.itervalues():
        if ovs_rec.mgmt_intf_status:
            status_data = ovs_rec.mgmt_intf_status
            break

    dhcp_hostname = status_data.get(MGMT_INTF_KEY_DHCP_HOSTNAME,
                                    MGMT_INTF_NULL_VAL)

    if dhcp_hostname != hostname:
        if hostname != MGMT_INTF_NULL_VAL:
            status_data[MGMT_INTF_KEY_DHCP_HOSTNAME] = hostname
        else:
            del status_data[MGMT_INTF_KEY_DHCP_HOSTNAME]

        # create the transaction
        txn = ovs.db.idl.Transaction(idl)

        setattr(ovs_rec, "mgmt_intf_status", status_data)
        status = txn.commit_block()

        if status != "success" and status != "unchanged":
            vlog.err("Updating DHCP hostname status column failed \
                     with status %s" % (status))
            return False

    return True


    ###############################  main  ###########################
def main():
    global idl
    argv = sys.argv
    n_args = 2

    if len(argv) != n_args:
        hostname = MGMT_INTF_NULL_VAL
    else:
        hostname = argv[1]

    # Locate default config if it exists
    schema_helper = ovs.db.idl.SchemaHelper(location=OVS_SCHEMA)
    schema_helper.register_columns(SYSTEM_TABLE, ["cur_cfg"])
    schema_helper.register_columns(SYSTEM_TABLE, ["mgmt_intf_status"])

    idl = ovs.db.idl.Idl(DEF_DB, schema_helper)

    seqno = idl.change_seqno    # Sequence number when we last processed the db

    # Wait until the ovsdb sync up.
    while (seqno == idl.change_seqno):
        idl.run()
        poller = ovs.poller.Poller()
        idl.wait(poller)
        poller.block()

    wait_for_config_complete(idl)

    update_mgmt_intf_status_hostname(hostname)

    idl.close()

if __name__ == '__main__':
    try:
        main()
    except error.Error, e:
        vlog.err("Error: \"%s\" \n" % e)
