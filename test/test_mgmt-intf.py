#!/usr/bin/python
"""
Copyright (C) 2015 Hewlett Packard Enterprise Development LP
All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may
not use this file except in compliance with the License. You may obtain
a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
License for the specific language governing permissions and limitations
under the License.
"""

import os
import sys
import time
import re
from mininet.net import *
from mininet.topo import *
from mininet.node import *
from mininet.link import *
from mininet.cli import *
from mininet.log import *
from mininet.util import *
from subprocess import *
from halonvsi.docker import *
from halonvsi.halon import *
import select


class mgmtIntfTests( HalonTest ):

  def setupNet(self):
    # If you override this function, make sure to
    # either pass getNodeOpts() into hopts/sopts of the topology that
    # you build or into addHost/addSwitch calls.
    mgmt_topo = SingleSwitchTopo(k=0,
                                 hopts=self.getHostOpts(),
                                 sopts=self.getSwitchOpts())
    self.net = Mininet(topo=mgmt_topo,
                       switch=HalonSwitch,
                       host=HalonHost,
                       link=HalonLink, controller=None,
                       build=True)

  def print_result(self,a):
    if a == True:
      print('\n\nRESULT   : PASSED')
      print('----------------------------------------------------------------------------')
    else:
      print('\n\nRESULT   : FAILED')
      print('----------------------------------------------------------------------------')
      # The title will tell what has failed.
      assert 0, "Failed"

  def mgmt_intf_config_commands(self):
    print('\n=========================================')
    print('*** Test to verify mgmt-intf ***')
    print('=========================================')
    # configuring Halon, in the future it would be through
    # proper Halon commands.
    s1 = self.net.switches[ 0 ]

    '''
    # NOTE: Currently dhclient@eth0.service exits after getting dhcp ip address.
      This testcase will be enabled once dhclient is modified.

    # DHCP client started on management interface
    print('\n\nTEST CASE TITLE : Testing if dhcp client has started')
    print('------------------------------------------------------------------------------')
    output = s1.cmd("systemctl status dhclient@eth0.service")
    if 'running' in output:
      print output
      self.print_result(True)
    else:
      print output
      self.print_result(False)
    '''

    # Mgmt Interface updated during bootup.
    print('\n\nTEST CASE TITLE : Testing if mgmt interface is updated from image.manifest file')
    print('------------------------------------------------------------------------------')
    output = s1.cmd("ovs-vsctl list open_vswitch")
    output += s1.cmd("echo")
    if 'name="eth0"' in output:
      print output
      self.print_result(True)
    else:
      print output
      self.print_result(False)

    # Enter the management interface context.
    print('\n\nTEST CASE TITLE : Test to enter the management interface context')
    print('------------------------------------------------------------------------------')
    # Enter the configuration mode.
    output = s1.cmdCLI("configure terminal")
    if 'Unknown command' in output:
      print output
      self.print_result(False)
    else:
      print output
      self.print_result(True)

    output = s1.cmdCLI("interface mgmt")
    if 'Unknown command' in output:
      print output
      self.print_result(False)
    else:
      print output
      self.print_result(True)
    # Set mode as DHCP
    print('\n\nTEST CASE TITLE : Test to set mode as DHCP')
    print('------------------------------------------------------------------------------')
    s1.cmdCLI("ip dhcp")
    output = s1.cmdCLI(" ")
    output = s1.cmdCLI("do show interface mgmt")
    output += s1.cmdCLI(" ")

    '''
    # NOTE: Currently dhclient@eth0.service exits after getting dhcp ip address
     So Disabling the following check due to inproper dhclient@eth0.service status.

    if 'dhcp' in output:
      output = s1.cmd("systemctl status dhclient@eth0.service")
      if 'running' in output:
        print output
        self.print_result(True)
      else:
        print output
        self.print_result(False)
    else:
      print output
      self.print_result(False)
    '''

    # Add Default gateway in DHCP mode.
    print('\n\nTEST CASE TITLE : Test to add default gateway 172.17.0.1 in DHCP mode')
    print('------------------------------------------------------------------------------')
    s1.cmdCLI("default-gateway 172.17.0.1")
    output = s1.cmdCLI(" ")
    output = s1.cmdCLI("do show interface mgmt")
    if '172.17.0.1' in output:
      print output
      self.print_result(False)
    else:
      print output
      self.print_result(True)

    # Add DNS Server 1 in DHCP mode.
    print('\n\nTEST CASE TITLE : Test to add dns-server-1 10.10.10.1 in DHCP mode')
    print('------------------------------------------------------------------------------')
    s1.cmdCLI("nameserver 10.10.10.1")
    output = s1.cmdCLI(" ")
    output = s1.cmd("echo")
    output = s1.cmdCLI("do show interface mgmt")
    if '10.10.10.1' in output:
      print output
      self.print_result(False)
    else:
      print output
      self.print_result(True)

    # Add DNS Server 2 in DHCP mode.
    print('\n\nTEST CASE TITLE : Test to add dns-server-2 10.10.10.2 in DHCP mode')
    print('------------------------------------------------------------------------------')
    s1.cmdCLI("nameserver 10.10.10.1 10.10.10.2")
    output = s1.cmdCLI(" ")
    output = s1.cmd("echo")
    output = s1.cmdCLI("do show interface mgmt")
    output += s1.cmd("echo")
    if '10.10.10.2' in output:
      print output
      self.print_result(False)
    else:
      print output
      self.print_result(True)

    # Static IP config when mode is static.
    print('\n\nTEST CASE TITLE : Test to add static IP address 172.17.0.5 and netmask 255.255.0.0 in static mode')
    print('------------------------------------------------------------------------------')
    s1.cmdCLI("ip static 172.17.0.5 255.255.0.0")
    output = s1.cmdCLI(" ")
    cnt = 15
    while cnt:
      output = s1.cmdCLI("do show interface mgmt")
      output += s1.cmd("echo")
      output += s1.cmd("echo")
      if '172.17.0.5' in output and '255.255.0.0' in output:
        cnt2 = 15
        while cnt2:
          output = s1.cmd("ifconfig")
          output += s1.cmd("echo")
          if '172.17.0.5' in output and '255.255.0.0' in output:
            print output
            self.print_result(True)
            break
          else:
            cnt2 -= 1
            sleep(1)
        break
      else:
        sleep(1)
        cnt -= 1
    if not cnt or not cnt2:
      print output
      self.print_result(False)

    # Set the IP again.
    print('\n\nTEST CASE TITLE : Test to add static IP address 172.17.0.7 and netmask 255.255.0.0 when already set')
    print('---------------------------------------------------------------------------------')
    s1.cmdCLI("ip static 172.17.0.7 255.255.0.0")
    output = s1.cmdCLI(" ")
    cnt = 15
    while cnt:
      output = s1.cmdCLI("do show interface mgmt")
      output += s1.cmd("echo")
      output += s1.cmd("echo")
      if '172.17.0.7' in output and '255.255.0.0' in output:
        cnt2 = 15
        while cnt2:
          output = s1.cmd("ifconfig")
          output += s1.cmd("echo")
          if '172.17.0.7' in output and '255.255.0.0' in output:
            print output
            self.print_result(True)
            break
          else:
            cnt2 -= 1
            sleep(1)
        break
      else:
        sleep(1)
        cnt -= 1
    if not cnt or not cnt2:
      print output
      self.print_result(False)

    # Set Invalid IP on mgmt-intf.
    print('\n\nTEST CASE TITLE : Test to configure invalid static IP address 0.0.0.0 and netmask 255.255.0.0')
    print('------------------------------------------------------------------------------')
    output=s1.cmdCLI("ip static 0.0.0.0 255.255.0.0")
    if 'Unknown command' in output:
      print output
      self.print_result(True)
    else:
      print output
      self.print_result(False)

    # Set Multicast IP on mgmt-intf.
    print('\n\nTEST CASE TITLE : Test to configure multicast IP address 224.0.0.1 and netmask 255.255.0.0')
    print('------------------------------------------------------------------------------')
    output=s1.cmdCLI("ip static 224.0.0.1 255.255.0.0")
    if 'Unknown command' in output:
      print output
      self.print_result(True)
    else:
      print output
      self.print_result(False)

    # Set broadcast IP on mgmt-intf.
    print('\n\nTEST CASE TITLE : Test to configure broadcast IP address 192.168.0.255 and netmask 255.255.255.0')
    print('------------------------------------------------------------------------------')
    output=s1.cmdCLI("ip static 192.168.0.255 255.255.255.0")
    if 'Unknown command' in output:
      print output
      self.print_result(True)
    else:
      print output
      self.print_result(False)

    # Set loopback IP on mgmt-intf.
    print('\n\nTEST CASE TITLE : Test to configure loopback IP address 127.0.0.1 and netmask 255.255.255.0')
    print('------------------------------------------------------------------------------')
    output=s1.cmdCLI("ip static 127.0.0.1 255.255.255.0")
    if 'Unknown command' in output:
      print output
      self.print_result(True)
    else:
      print output
      self.print_result(False)

    # Add Default gateway in Static mode.
    print('\n\nTEST CASE TITLE : Test to add default gateway 172.17.0.1 in static mode')
    print('------------------------------------------------------------------------------')
    s1.cmdCLI("default-gateway 172.17.42.1")
    output = s1.cmdCLI(" ")
    cnt = 15
    while cnt:
      output = s1.cmdCLI("do show interface mgmt")
      output += s1.cmd("echo")
      output += s1.cmd("echo")
      if '172.17.42.1' in output:
        cnt2 = 15
        while cnt2:
          output = s1.cmd("ip route show")
          output += s1.cmd("echo")
          if '172.17.42.1' in output:
            print output
            self.print_result(True)
            break
          else:
            cnt2 -= 1
            sleep(1)
        break
      else:
        sleep(1)
        cnt -= 1
    if not cnt or not cnt2:
      print output
      self.print_result(False)

    # Add Default Invalid gateway IP in static mode.
    print('\n\nTEST CASE TITLE : Test to add Invalid default gateway ip 0.0.0.0 in static mode')
    print('------------------------------------------------------------------------------')
    output=s1.cmdCLI("default-gateway 0.0.0.0")
    if 'Unknown command' in output:
      print output
      self.print_result(True)
    else:
      print output
      self.print_result(False)

    # Add multicast ip as default gateway in static mode.
    print('\n\nTEST CASE TITLE : Test to add multicast default gateway ip 224.0.0.1 in static mode')
    print('------------------------------------------------------------------------------')
    output=s1.cmdCLI("default-gateway 224.0.0.1")
    if 'Unknown command' in output:
      print output
      self.print_result(True)
    else:
      print output
      self.print_result(False)

    # Add broadcast ip as default gateway ip in static mode.
    print('\n\nTEST CASE TITLE : Test to add default broadcast gateway ip 192.168.0.255 in static mode')
    print('------------------------------------------------------------------------------')
    output=s1.cmdCLI("default-gateway 192.168.0.255")
    if 'Unknown command' in output:
      print output
      self.print_result(True)
    else:
      print output
      self.print_result(False)

    # Add loopback address as default gateway ip in static mode.
    print('\n\nTEST CASE TITLE : Test to add loopback default gateway ip 127.0.0.1 in static mode')
    print('----------------------------------------------------------------------------------')
    output=s1.cmdCLI("default-gateway 127.0.0.1")
    if 'Unknown command' in output:
      print output
      self.print_result(True)
    else:
      print output
      self.print_result(False)

    # Remove Default gateway in static mode.
    print('\n\nTEST CASE TITLE : Test to remove default gateway 172.17.42.1 in static mode')
    print('----------------------------------------------------------------------------------')
    s1.cmdCLI("no default-gateway 172.17.42.1")
    output = s1.cmdCLI(" ")
    output = s1.cmdCLI("do show interface mgmt")
    output += s1.cmdCLI(" ")
    if re.findall("Default gateway\s+: 172.17.42.1",output):
      output = s1.cmd("ip route show")
      output += s1.cmd("echo")
      print output
      self.print_result(False)
    else:
      print output
      self.print_result(True)

    # Configure an invalid IP address as primary DNS.
    print('\n\nTEST CASE TITLE : Test to configure an invalid IP as primary DNS')
    print('----------------------------------------------------------------------------------')
    output=s1.cmdCLI("nameserver 0.0.0.0")
    if 'Unknown command' in output:
        print output
        self.print_result(True)
    else:
        print output
        self.print_result(False)

    # Configure a multicast address as primary DNS.
    print('\n\nTEST CASE TITLE : Test to Configure a multicast address as primary DNS')
    print('----------------------------------------------------------------------------------')
    output=s1.cmdCLI("nameserver 224.0.0.1")
    if 'Unknown command' in output:
        print output
        self.print_result(True)
    else:
        print output
        self.print_result(False)

    # Configure a broadcast address as primary DNS.
    print('\n\nTEST CASE TITLE : Test to Configure a broadcast address as primary DNS')
    print('----------------------------------------------------------------------------------')
    output=s1.cmdCLI("nameserver 192.168.0.255")
    if 'Unknown command' in output:
        print output
        self.print_result(True)
    else:
        print output
        self.print_result(False)

    # Configure a loopback address as primary DNS.
    print('\n\nTEST CASE TITLE : Test to Configure a loopback address as primary DNS')
    print('----------------------------------------------------------------------------------')
    output=s1.cmdCLI("nameserver 127.0.0.1")
    if 'Unknown command' in output:
        print output
        self.print_result(True)
    else:
        print output
        self.print_result(False)

    # Configure an invalid IP as secondary DNS.
    print('\n\nTEST CASE TITLE : Test to Configure an invalid IP as secondary DNS')
    print('----------------------------------------------------------------------------------')
    output=s1.cmdCLI("nameserver 10.10.10.1 0.0.0.0")
    if 'Unknown command' in output:
        print output
        self.print_result(True)
    else:
        print output
        self.print_result(False)

    # Configure a multicast address as secondary DNS.
    print('\n\nTEST CASE TITLE : Test to Configure a multicast as secondary DNS')
    print('----------------------------------------------------------------------------------')
    output=s1.cmdCLI("nameserver 10.10.10.1 224.0.0.1")
    if 'Unknown command' in output:
        print output
        self.print_result(True)
    else:
        print output
        self.print_result(False)

    # Configure a broadcast address as secondary DNS.
    print('\n\nTEST CASE TITLE : Test to Configure a broadcast address as secondary DNS')
    print('----------------------------------------------------------------------------------')
    output=s1.cmdCLI("nameserver 10.10.10.1 192.168.0.255")
    if 'Unknown command' in output:
        print output
        self.print_result(True)
    else:
        print output
        self.print_result(False)

    # Configure a loopback address as secondary DNS.
    print('\n\nTEST CASE TITLE : Test to Configure a loopback address as secondary DNS')
    print('----------------------------------------------------------------------------------')
    output=s1.cmdCLI("nameserver 10.10.10.1 127.0.0.1")
    if 'Unknown command' in output:
        print output
        self.print_result(True)
    else:
        print output
        self.print_result(False)

    # Configure same ip as both primary and secondary DNS.
    print('\n\nTEST CASE TITLE : Test to Configure same ip as both primary and secondary DNS')
    print('----------------------------------------------------------------------------------')
    output=s1.cmdCLI("nameserver 10.10.10.1 10.10.10.1")
    if 'Unknown command' in output:
        print output
        self.print_result(True)
    else:
        print output
        self.print_result(False)

    # Add DNS Server 1 in static mode.
    print('\n\nTEST CASE TITLE : Test to add dns-server-1 10.10.10.1 in static mode')
    print('----------------------------------------------------------------------------------')
    s1.cmdCLI("nameserver 10.10.10.1")
    output = s1.cmdCLI(" ")
    cnt = 15
    while cnt:
      output = s1.cmdCLI("do show interface mgmt")
      output += s1.cmd("echo")
      output += s1.cmd("echo")
      if '10.10.10.1' in output:
        cnt2 = 15
        while cnt2:
          output = s1.cmd("cat /etc/resolv.conf")
          output += s1.cmd("echo")
          if 'nameserver 10.10.10.1' in output:
            print output
            self.print_result(True)
            break
          else:
            cnt2 -= 1
            sleep(1)
        break
      else:
        sleep(1)
        cnt -= 1
    if not cnt or not cnt2:
      print output
      self.print_result(False)

    # Add another primary DNS server.
    print('\n\nTEST CASE TITLE : Test to add primary DNS server 10.10.10.20 when 10.10.10.1 is already set')
    print('----------------------------------------------------------------------------------')
    s1.cmdCLI("nameserver 10.10.10.20")
    output = s1.cmdCLI(" ")
    cnt = 15
    while cnt:
      output = s1.cmdCLI("do show interface mgmt")
      output += s1.cmd("echo")
      output += s1.cmd("echo")
      if '10.10.10.20' in output:
        cnt2 = 15
        while cnt2:
          output = s1.cmd("cat /etc/resolv.conf")
          output += s1.cmd("echo")
          if 'nameserver 10.10.10.20' in output and 'nameserver 10.10.10.1' not in output:
            print output
            self.print_result(True)
            break
          else:
            cnt2 -= 1
            sleep(1)
        break
      else:
        sleep(1)
        cnt -= 1
    if not cnt or not cnt2:
      print output
      self.print_result(False)

    # Remove primary DNS server.
    print('\n\nTEST CASE TITLE : Test to remove primary DNS server when 10.10.10.20 is set')
    print('----------------------------------------------------------------------------------')
    s1.cmdCLI("no nameserver 10.10.10.20")
    cnt = 15
    while cnt:
      output = s1.cmdCLI("do show interface mgmt")
      output += s1.cmd("echo")
      output += s1.cmd("echo")
      if 'Primary Nameserver            : 10.10.10.20' not in output:
        cnt2 = 15
        while cnt2:
          output = s1.cmd("cat /etc/resolv.conf")
          output += s1.cmd("echo")
          if 'nameserver 10.10.10.20' not in output:
            print output
            self.print_result(True)
            break
          else:
            cnt2 -= 1
            sleep(1)
        break
      else:
        sleep(1)
        cnt -= 1
    if not cnt or not cnt2:
      print output
      self.print_result(False)

    # Add Secondary DNS Server in static mode.
    print('\n\nTEST CASE TITLE : Test to add secondary DNS server 10.10.10.5 in static mode')
    print('----------------------------------------------------------------------------------')
    s1.cmdCLI("nameserver 10.10.10.4 10.10.10.5")
    cnt = 15
    while cnt:
      output = s1.cmdCLI("do show interface mgmt")
      output += s1.cmd("echo")
      output += s1.cmd("echo")
      if re.findall("Primary Nameserver\s+: 10.10.10.4",output) and \
           re.findall("Secondary Nameserver\s+: 10.10.10.5",output):
        cnt2 = 15
        while cnt2:
          output = s1.cmd("cat /etc/resolv.conf")
          output += s1.cmd("echo")
          if 'nameserver 10.10.10.5' in output and 'nameserver 10.10.10.4' in output:
            print output
            self.print_result(True)
            break
          else:
            cnt2 -= 1
            sleep(1)
        break
      else:
        sleep(1)
        cnt -= 1
    if not cnt or not cnt2:
      print output
      self.print_result(False)

    # Add another secondary DNS server.
    print('\n\nTEST CASE TITLE : Test to add secondary DNS server 10.10.10.20 when 10.10.10.5 is already set')
    print('----------------------------------------------------------------------------------')
    s1.cmdCLI("nameserver 10.10.10.4 10.10.10.20")
    output_show = s1.cmdCLI("do show interface mgmt")
    output += s1.cmdCLI(" ")
    cnt = 15
    while cnt:
      output = s1.cmdCLI("do show interface mgmt")
      output += s1.cmd("echo")
      output += s1.cmd("echo")
      if re.findall("Primary Nameserver\s+: 10.10.10.4",output) and \
        re.findall("Secondary Nameserver\s+: 10.10.10.20",output):
        cnt2 = 15
        while cnt2:
          output = s1.cmd("cat /etc/resolv.conf")
          output += s1.cmd("echo")
          if 'nameserver 10.10.10.4' in output and 'nameserver 10.10.10.5' not in output and \
             'nameserver 10.10.10.20' in output:
            print output
            self.print_result(True)
            break
          else:
            cnt2 -= 1
            sleep(1)
        break
      else:
        sleep(1)
        cnt -= 1
    if not cnt or not cnt2:
      print output
      self.print_result(False)

    # Remove Secondary DNS server.
    print('\n\nTEST CASE TITLE : Test to remove secondary DNS server when 10.10.10.20 is already set')
    print('----------------------------------------------------------------------------------')
    s1.cmdCLI("no nameserver  10.10.10.4 10.10.10.20")
    cnt = 15
    while cnt:
      output = s1.cmdCLI("do show interface mgmt")
      output += s1.cmd("echo")
      output += s1.cmd("echo")
      if '10.10.10.20' not in output:
        cnt2 = 15
        while cnt2:
          output = s1.cmd("cat /etc/resolv.conf")
          output += s1.cmd("echo")
          if 'nameserver 10.10.10.20' not in output:
            print output
            self.print_result(True)
            break
          else:
            cnt2 -= 1
            sleep(1)
        break
      else:
        sleep(1)
        cnt -= 1
    if not cnt or not cnt2:
      print output
      self.print_result(False)

    # Change mode from static to dhcp.
    print('\n\nTEST CASE TITLE : Test to change mode to DHCP from static')
    print('----------------------------------------------------------------------------------')
    s1.cmdCLI("ip dhcp")
    output = s1.cmdCLI(" ")
    cnt = 15
    while cnt:
      output = s1.cmdCLI("do show interface mgmt")
      output += s1.cmd("echo")
      output += s1.cmd("echo")
      if 'dhcp' in output:
        break
      else:
        sleep(1)
        cnt -= 1
    if not cnt or not cnt2:
      print output
      self.print_result(False)

    # Populate values as though populated from DHCP.
    time.sleep(5)
    s1.cmd("ifconfig eth0 172.17.0.100 netmask 255.255.255.0")
    s1.cmd("route add default gw 172.17.0.1 eth0")
    s1.cmd("echo nameserver 1.1.1.1  > /etc/resolv.conf")
    s1.cmd("echo nameserver 2.2.2.2 >> /etc/resolv.conf")

    output = s1.cmd("ifconfig")
    print output
    output = s1.cmd("ip route show")
    print output
    output = s1.cmd("cat /etc/resolv.conf")
    print output

    # Test if IP got from DHCP is set.
    print('\n\nTEST CASE TITLE : Test to check IP address from DHCP is set')
    print('----------------------------------------------------------------------------------')
    output = ''
    out = s1.cmd("ifconfig eth0")
    hostIpAddress = out.split("\n")[1].split()[1][5:]
    print "IP:" + hostIpAddress
    cnt = 15
    while cnt:
      output = s1.cmdCLI("do show interface mgmt")
      output += s1.cmd("echo")
      output += s1.cmd("echo")
      if hostIpAddress in output:
        break
      else:
        sleep(1)
        cnt -= 1
    if not cnt or not cnt2:
      print output
      self.print_result(False)

    # Test if Default gateway got from DHCP is set.
    print('\n\nTEST CASE TITLE : Test to check default gateway address from DHCP is set')
    print('----------------------------------------------------------------------------------')
    out = s1.cmd("ip route show")
    def_gw = out.split("\n")[0].split()[2][0:]
    print "def_gw" + def_gw
    cnt = 15
    while cnt:
      output = s1.cmdCLI("do show interface mgmt")
      output += s1.cmd("echo")
      output += s1.cmd("echo")
      if def_gw in output:
        break
      else:
        sleep(1)
        cnt -= 1
    if not cnt or not cnt2:
      print output
      self.print_result(False)

    # Test if DNS server got from DHCP is set.
    print('\n\nTEST CASE TITLE : Test if DNS server got from DHCP is set')
    print('----------------------------------------------------------------------------------')
    output = s1.cmd("cat /etc/resolv.conf")
    start = output.find("nameserver")
    if start >= 0:
      end = output[start:].find('\n')
      end = end + start
      dhcp_dns_1 = output[start:end]

      start = output[end:].find('nameserver')
      if start >= 0:
        start = start + end + 11
        end = output[start:].find('\n')
        end = end + start
        dhcp_dns_2 = output[start:end]
        if dhcp_dns_1 not in output or dhcp_dns_2  not in output:
          print output
          self.print_result(False)
        else:
          print output
          self.print_result(True)
      else:
        print output
        self.print_result(True)
    else:
      print output
      self.print_result(True)

  # Extra cleanup if test fails in middle.
  def mgmt_intf_cleanup(self):
    s1 = self.net.switches[ 0 ]

    output = s1.cmd("ip netns exec swns ip addr show dev 1")
    if 'inet' in output:
      s1.cmd("ip netns exec swns ip address flush dev 1")

class Test_mgmt_intf:
  # Create the Mininet topology based on mininet.
  test = mgmtIntfTests()

  def setup(self):
    pass

  def teardown(self):
    pass

  def setup_class(cls):
    pass

  def teardown_class(cls):
    # Stop the Docker containers, and
    # mininet topology.
    Test_mgmt_intf.test.net.stop()

  def setup_method(self, method):
    pass

  def teardown_method(self, method):
    self.test.mgmt_intf_cleanup()

  def __del__(self):
    del self.test

  # mgmt intf tests.
  def test_mgmt_intf_config_commands(self):
    self.test.mgmt_intf_config_commands()
