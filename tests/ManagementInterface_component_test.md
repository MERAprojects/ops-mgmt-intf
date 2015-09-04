
<!--  See the https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet for additional information about markdown text.
Here are a few suggestions in regards to style and grammar:
* Use active voice. With active voice, the subject is the doer of the action. Tell the reader what
to do by using the imperative mood, for example, Press Enter to view the next screen. See https://en.wikipedia.org/wiki/Active_voice for more information about the active voice. 
* Use present tense. See https://en.wikipedia.org/wiki/Present_tense for more information about using the present tense. 
* The subject is the test case. Explain the actions as if the "test case" is doing them. For example, "Test case configures the IPv4 address on one of the switch interfaces". Avoid the use of first (I) or second person. Explain the instructions in context of the test case doing them. 
* See https://en.wikipedia.org/wiki/Wikipedia%3aManual_of_Style for an online style guide.
 --> 
Management Interface Component Test Cases
=======

<!--Provide the name of the grouping of commands, for example, LLDP commands-->

 - Test cases to verify Management interface configuration in IPV4 DHCP mode
 - Test case to verify Management interface configuration in Static IPV4 mode 
 - Test cases to verify Management interface configuration in IPV6 DHCP mode
 - Test case to verify Management interface configuration in Static IPV6 mode

##  Test cases to verify Management interface configuration in IPV4 DHCP mode ##

### Objective ###
 Test cases to configure,reconfigure and unconfigure the management interface and to verify the expected behavior of management interface with DHCP IPV4 addressing mode.
   
### Requirements ###
The requirements for this test case are:

 - IPV4 DHCP Server
 
### Setup ###
#### Topology Diagram ####
<pre>





                                                           +-------------------+
              +------------------+                         | Linux workstation |
              |                  |eth0                eth0 |+-----------------+|
              |  AS5712 switch   |&lt;----+         +--------&gt;||DHCP IPV4 Server ||
              |                  |     |         |         |+-----------------+|
              +------------------+     |         |         +-------------------+
                                       |         |
                                       v         v
                                 +---------------------+
                                 | port 1      port 2  |
                                 |                     |
                                 |      Switch         |
                                 |                     |
                                 +---------------------+</pre>
#### Test Setup ####
### Test case 1.01 : Verify DHCP client is started on the management interface  ###
#### Description ####
Test to verify whether dhcp client has started on Management interface by using the following systemctl command "systemctl status dhclient@eth0.service" after booting the switch.

### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if dhcpclient service status is in running state.
#### Test Fail Criteria ####
Testcase result is fail if dhcpclient service status is not in running state.

### Test case 1.02 - Verify management interface is updated from image.manifest file ###
#### Description ####
Test to verify management interface name is updated from image.manifest file during bootup".
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if 'name=eth0' is present in mgmt_intf column.
#### Test Fail Criteria ####
Testcase result is fail if 'name=eth0' is missing in mgmt_intf column.
 
### Test case 1.03 - Verify user is able to enter the management interface context ###
#### Description ####
Test whether user is able to enter the management interface context.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user is able to enter management interface context.
#### Test Fail Criteria ####
Testcase result is fail if user is not able to enter management interface context.

### Test case 1.04 - Verify management interface is updated in DHCP mode ###
#### Description ####
Test to verify management interface is updated in DHCP mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if IPV4 address is present in 'show interface mgmt' output and dhcclient@eth0.service status is in running state.
#### Test Fail Criteria ####
Testcase result is fail if IPV4 address is not present in 'show interface mgmt' output or
dhcclient@eth0.service status is not in running state.
 

### Test case 1.05 - Verify default gateway is configurable in DHCP mode ###
#### Description ####
Test whether user is able to configure default gateway in DHCP mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user is not able to configure default gateway in DHCP mode.
#### Test Fail Criteria ####
Testcase result is fail if user is able to configure.

### Test case 1.06 - Verify primary DNS is configurable in DHCP mode ###
#### Description ####
Test whether user is able to configure primary DNS in DHCP mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user is not able to configure primary DNS in DHCP mode.
#### Test Fail Criteria ####
Testcase result is fail if user is able to configure.

### Test case 1.07 - Verify secondary DNS is configurable in DHCP mode ###
#### Description ####
Test whether user is able to configure secondary DNS in DHCP mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user is not able to configure secondary DNS in DHCP mode.
#### Test Fail Criteria ####
Testcase result is fail if user is able to configure.

##  Test case to verify management interface configuration in static IPV4 mode ##

### Objective ###
 Test cases to configure, reconfigure and unconfigure the management interface and to verify the expected behavior of management interface in static IPV4 mode.
   
### Requirements ###
No Requirements.
 
### Setup ###
#### Topology Diagram ####
<pre>





                                                           +-------------------+
              +------------------+                         |                   |
              |                  |eth0                eth0 |                   |
              |  AS5712 switch   |&lt;----+         +--------&gt;| Linux Workstation |
              |                  |     |         |         |                   |
              +------------------+     |         |         +-------------------+
                                       |         |
                                       v         v
                                 +---------------------+
                                 | port 1      port 2  |
                                 |                     |
                                 |      Switch         |
                                 |                     |
                                 +---------------------+</pre>
#### Test Setup ####
### Test case 2.01 - Verify static IPV4 address is configured on management interface  ###
#### Description ####
Test whether user is able to configure static IPV4 address on management interface from management interface context.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if configured IPV4 address is present in show interface mgmt & ifconfig output.
#### Test Fail Criteria ####
Testcase result is fail if configured IPV4 address is not present in show interface mgmt or ifconfig output.

### Test case 2.02 - Verify reconfiguring static IPV4 address on management interface ###
#### Description ####
Test to verify reconfiguration of static IPV4 address on management interface from management interface context.
### Test Result Criteria ###
<!--    Explain the criteria that clearly identifies under whch conditions would the test be considered as pass or fail. Also if the test case can exit with any other result, explain that result and similarly the relevant criteria. -->
#### Test Pass Criteria ####
Testcase result is success if configured IPV4 address is present in show interface mgmt & ifconfig output.
#### Test Fail Criteria ####
Testcase result is fail if configured IPV4 address is not present in show interface mgmt or ifconfig output.

### Test case 2.03 - Verify default gateway is configured in static mode ###
#### Description ####
Test whether user is able to configure static IPV4 on management interface from management interface context.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if configured default gateway is present in show interface mgmt & ip route show output.
#### Test Fail Criteria ####
Testcase result is fail if configured default gateway is not present in show interface mgmt or ip route show output.

### Test case 2.04 - Verify default gateway is removed in static mode ###
#### Description ####
Test whether user is able to remove default gateway in state mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if configured default gateway is not present in show interface mgmt & ip route show output.
#### Test Fail Criteria ####
Testcase result is fail if configured default gateway is present in show interface mgmt or ip route show output.

### Test case 2.05 - Verify primary DNS is configured in static mode ###
#### Description ####
Test whether user is able to configure primary DNS in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if configured primary DNS is present in show interface mgmt output & /etc/resolv.conf file.
#### Test Fail Criteria ####
Testcase result is fail if configured primary DNS is not present in show interface mgmt output or /etc/resolv.conf file.

### Test case 2.06 - Verify reconfiguration of primary DNS in static mode ###
#### Description ####
Test whether user is able to reconfigure the primary DNS in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if configured primary DNS is present in show interface mgmt output & /etc/resolv.conf file.
#### Test Fail Criteria ####
Testcase result is fail if configured primary DNS is not present in show interface mgmt output or /etc/resolv.conf file.

### Test case 2.07 - Verify primary DNS is removed in static mode ###
#### Description ####
Test whether user is able to remove primary DNS in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if configured primary DNS is not present in show interface mgmt output & /etc/resolv.conf file.
#### Test Fail Criteria ####
Testcase result is fail if configured primary DNS is present in show interface mgmt output or /etc/resolv.conf file.

### Test case 2.08 - Verify secondary DNS is configured in static mode ###
#### Description ####
Test whether user is able to configure secondary DNS in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if configured secondary DNS is present in show interface mgmt output & /etc/resolv.conf file.
#### Test Fail Criteria ####
Testcase result is fail if configured secondary DNS is not present in show interface mgmt output or /etc/resolv.conf file.

### Test case 2.09 - Verify reconfiguration of secondary DNS in static mode ###
#### Description ####
Test whether user is able to reconfigure the secondary DNS in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if configured secondary DNS is present in show interface mgmt output & /etc/resolv.conf file.
#### Test Fail Criteria ####
Testcase result is fail if configured secondary DNS is not present in show interface mgmt output or /etc/resolv.conf file.


### Test case 2.10 - Verify secondary DNS is removed in static mode ###
#### Description ####
Test whether user is able to remove secondary DNS in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if configured secondary DNS is not present in show interface mgmt  output & /etc/resolv.conf file.
#### Test Fail Criteria ####
Testcase result is fail if configured secondary DNS is present in show interface mgmt output or /etc/resolv.conf file.

### Test case 2.11 - Verify invalid IPV4 address is not configured on mgmt_intf in static mode ###
#### Description ####
Test whether the user is able to configure invalid IPV4 address on mgmt_intf in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user not able to configure invalid IPV4 address on mgmt_intf in static mode.
#### Test Fail Criteria ####
Testcase result is fail if user able to configure.

### Test case 2.12 - Verify multicast IPV4 address is not configurable on mgmt_intf in static mode ###
#### Description ####
Test whether the user is able to configure multicast IPV4 address on mgmt_intf in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user not able to configure Multicast IPV4 address on mgmt_intf in static mode.
#### Test Fail Criteria ####
Testcase result is fail if user able to configure.

### Test case 2.13 - Verify broadcast IPV4 address is not configurable on mgmt_intf in static mode ###
#### Description ####
Test whether the user is able to configure broadcast IPV4 address on mgmt_intf in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user not able to configure broadcast IPV4 address on mgmt_intf in static mode.
#### Test Fail Criteria ####
Testcase result is fail if user able to configure.

### Test case 2.14 - Verify loopback IPV4  address is not configurable on mgmt_intf in static mode ###
 
#### Description ####
Test whether the user is able to configure loopback IPV4 address on mgmt_intf in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user not able to configure loopback IPV4  address on mgmt_intf in static mode.
#### Test Fail Criteria ####
Testcase result is fail if user able to configure.

### Test case 2.15 - Verify Invalid default gateway IPV4  address is not configurable in static mode ###
#### Description ####
Test whether the user is able to configure invalid default gateway IPV4 address on mgmt_intf in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user not able to configure invalid default gateway IPV4 address on mgmt_intf in static mode.
#### Test Fail Criteria ####
Testcase result is fail if user able to configure.



### Test case 2.16 - Verify multicast default  gateway IPV4 address is not configurable in static mode ###
#### Description ####
Test whether the user is able to configure multicast default gateway IPV4 address on mgmt_intf in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user not able to configure multicast default gateway IPV4 address on mgmt_intf in static mode.
#### Test Fail Criteria ####
Testcase result is fail if user able to configure.

### Test case 2.17 - Verify broadcast default  gateway IPV4 address is configurable in static mode ###
#### Description ####
Test whether the user is able to configure broadcast default gateway IPV4 address on mgmt_intf in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user not able to configure broadcast default gateway IPV4 address on mgmt_intf in static mode.
#### Test Fail Criteria ####
Testcase result is fail if user able to configure.


### Test case 2.18 - Verify loopback default  gateway IPV4 address is not configurable in static mode ###
#### Description ####
Test whether the user is able to configure loopback default gateway IPV4 address on mgmt_intf in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user not able to configure loopback default gateway IPV4 address on mgmt_intf in static mode.
#### Test Fail Criteria ####
Testcase result is fail if user able to configure.


### Test case 2.19 - Verify invalid primary IPV4 address is not configurable in static mode ###
#### Description ####
Test whether the user is able to configure invalid primary IPV4 address on mgmt_intf in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user not able to configure invalid primary IPV4 address on mgmt_intf in static mode.
#### Test Fail Criteria ####
Testcase result is fail if user able to configure.


### Test case 2.20- Verify multicast primary IPV4 address is not configurable in static mode ###
#### Description ####
Test whether the user is able to configure multicast primary IPV4 address on mgmt_intf in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user not able to configure multicast primary IPV4 address on mgmt_intf in static mode.
#### Test Fail Criteria ####
Testcase result is fail if user able to configure.


### Test case 2.21- Verify broadcast primary IPV4 address is not configurable in static mode ###
#### Description ####
Test whether the user is able to configure broadcast primary IPV4 address on mgmt_intf in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user not able to configure broadcast primary IPV4 address on mgmt_intf in static mode.
#### Test Fail Criteria ####
Testcase result is fail if user able to configure.


### Test case 2.22- Verify loopback primary IPV4 address is configurable in static mode ###
#### Description ####
Test whether the user is able to configure loopback primary IPV4 address on mgmt_intf in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user not able to configure loopback primary IPV4 address on mgmt_intf in static mode.
#### Test Fail Criteria ####
Testcase result is fail if user able to configure.


### Test case 2.23 - Verify invalid secondary IPV4 address is not configurable in static mode ###
#### Description ####
Test whether the user is able to configure invalid secondary IPV4 address on mgmt_intf in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user not able to configure invalid secondary IPV4 address on mgmt_intf in static mode.
#### Test Fail Criteria ####
Testcase result is fail if user able to configure.

### Test case 2.24 - Verify management interface mode is changeable ###
#### Description ####
Test whether the management interface is changed from static mode to DHCP mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if DHCP is present in show interface mgmt output.
#### Test Fail Criteria ####
Testcase result is fail if DHCP is not present in show interface mgmt output.

### Test case 2.25 - Verify management interface got IPV4 if DHCP mode is set ###
#### Description ####
Test whether the management interface got IPV4 address after populated static ip in DHCP mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if IPV4 address is present in show interface mgmt & ifconfig output.
#### Test Fail Criteria ####
Testcase result is fail if IPV4 address is not present in show interface mgmt or ifconfig output.

### Test case 2.26 - Verify management interface got default gateway IPV4 address if DHCP set ###
#### Description ####
Test whether the management interface got default gateway IPV4 address after populate static ip in DHCP mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if default gateway IPV4 address is present in show interface mgmt & ip route show output.
#### Test Fail Criteria ####
Testcase result is fail if default gateway IPV4 address is not present in show interface mgmt or ip route show output.


### Test case 2.27 - Verify management interface got DNS IPV4 address if DHCP set ###
#### Description ####
Test whether the management interface got primary & secondary DNS IPV4 address after populate static ip in DHCP mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if DNS IPV4 address is present in show interface mgmt output & /etc/resolv.conf file.
#### Test Fail Criteria ####
Testcase result is fail if DNS IPV4 address is not present in show interface mgmt output or /etc/resolv.conf file.


##  Test cases to verify management interface configuration in IPV6 DHCP mode ##

### Objective ###
Test cases to configure,reconfigure and unconfigure the management interface and to verify the expected behavior of management interface with DHCP IPV6 addressing mode. 

   
### Requirements ###
The requirements for this test case are:

 -  IPV6 DHCP Server
 
### Setup ###
#### Topology Diagram ####
<pre>





                                                           +-------------------+
              +------------------+                         | Linux workstation |
              |                  |eth0                eth0 |+-----------------+|
              |  AS5712 switch   |&lt;----+         +--------&gt;||DHCP IPV6 Server ||
              |                  |     |         |         |+-----------------+|
              +------------------+     |         |         +-------------------+
                                       |         |
                                       v         v
                                 +---------------------+
                                 | port 1      port 2  |
                                 |                     |
                                 |      Switch         |
                                 |                     |
                                 +---------------------+</pre>
#### Test Setup ####
### Test case 3.01 - Verify default gateway is configurable in DHCP mode ###
#### Description ####
Test whether the user is able to configure default gateway in DHCP mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user not able to configure default gateway in DHCP mode.
#### Test Fail Criteria ####
Testcase result is fail if user able to configure.

### Test case 3.02 - Verify primary DNS is configurable in DHCP mode ###
#### Description ####
Test whether the user is able to configure primary DNS in DHCP mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user not able to configure primary DNS in DHCP mode.
#### Test Fail Criteria ####
Testcase result is fail if user able to configure.

### Test case 3.03 - Verify secondary DNS is configurable in DHCP mode ###
#### Description ####
Test whether the user is able to configure secondary DNS in DHCP mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user not able to configure secondary DNS in DHCP mode.
#### Test Fail Criteria ####
Testcase result is fail if user able to configure.


##  Test case to verify management interface configuration in static IPV6 mode ##

### Objective ###
 Test cases to configure, reconfigure and unconfigure the management interface and to verify the expected behavior of management interface in static IPV6 mode.
   
### Requirements ###
No Requirements.
 
### Setup ###
#### Topology Diagram ####
<pre>





                                                           +-------------------+
              +------------------+                         |                   |
              |                  |eth0                eth0 |                   |
              |  AS5712 switch   |&lt;----+         +--------&gt;| Linux Workstation |
              |                  |     |         |         |                   |
              +------------------+     |         |         +-------------------+
                                       |         |
                                       v         v
                                 +---------------------+
                                 | port 1      port 2  |
                                 |                     |
                                 |      Switch         |
                                 |                     |
                                 +---------------------+</pre>
#### Test Setup ####
### Test case 4.01 - Verify static IPV6 address is configured on management interface  ###
#### Description ####
Test whether the user is able to configure static IPV6 address on management interface from management interface context.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if configured IPV6 address is present in show interface mgmt & ip -6 addr show dev eth0 output.
#### Test Fail Criteria ####
Testcase result is fail if configured IPV6 address is not present in show interface mgmt or ip -6 addr show dev eth0 output.

### Test case 4.02 - Verify reconfiguring static IPV6 address on management interface ###
#### Description ####
 Test to verify re-configuring static IPV6 address on management interface from management interface context.
### Test Result Criteria ###
<!--    Explain the criteria that clearly identifies under which conditions would the test be considered as pass or fail. Also if the test case can exit with any other result, explain that result and similarly the relevant criteria. -->
#### Test Pass Criteria ####
Testcase result is success if configured IPV6 address is present in show interface mgmt & ip -6 addr show dev eth0 output.
#### Test Fail Criteria ####
Testcase result is fail if configured IPV6 address is not present in show interface mgmt or ip -6 addr show dev eth0 output.

### Test case 4.03 - Verify invalid IPV6 address is not configurable on mgmt_intf in static mode ###
#### Description ####
Test whether the user is able to configure invalid IPV6 address on mgmt_intf in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user not able to configure invalid IPV6 address on mgmt_intf in static mode.
#### Test Fail Criteria ####
Testcase result is fail if user able to configure.


### Test case 4.04 - Verify multicast IPV6 address is not configurable on mgmt_intf in static mode ###
#### Description ####
Test whether the user is able to configure multicast IPV6 address on mgmt_intf in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user not able to configure multicast IPV6 address on mgmt_intf in static mode.
#### Test Fail Criteria ####
Testcase result is fail if user able to configure.

### Test case 4.05 - Verify link-local IPV6 address is not configurable on mgmt_intf in static mode ###
#### Description ####
Test whether the user is able to configure link-local IPV6 address on mgmt_intf in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user not able to configure link-local IPV6 address on mgmt_intf in static mode.
#### Test Fail Criteria ####
Testcase result is fail if user able to configure.

### Test case 4.06 - Verify loopback IPV6 address is not configurable on mgmt_intf in static mode ###
#### Description ####
Test whether the user is able to configure loopback IPV6 address on mgmt_intf in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user not able to configure loopback IPV6 address on mgmt_intf in static mode.
#### Test Fail Criteria ####
Testcase result is fail if user able to configure.


### Test case 4.07 - Verify default gateway is configured in static mode ###
#### Description ####
Test whether the user is able to configure static IPV6 default gateway address on management interface from management interface context.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if configured default gateway is present in show running-config.
#### Test Fail Criteria ####
Testcase result is fail if configured default gateway is not present in show running-config.


### Test case 4.08 - Verify invalid default gateway IPV6  address is not configurable on mgmt_intf in static mode ###
#### Description ####
Test whether the user is able to invalid default gateway IPV6 address on mgmt_intf in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user not able to invalid default gateway IPV6 on mgmt_intf in static mode.
#### Test Fail Criteria ####
Testcase result is fail if user able to configure.


### Test case 4.09 - Verify multicast default gateway IPV6 address is not configurable on mgmt_intf in static mode ###
#### Description ####
Test whether the user is able to multicast default gateway IPV6 address on mgmt_intf in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user not able to multicast default gateway IPV6 address on mgmt_intf in static mode.
#### Test Fail Criteria ####
Testcase result is fail if user able to configure.


### Test case 4.10 - Verify link-local default gateway IPV6 address is not configurable on mgmt_intf in static mode ###
#### Description ####
Test whether the user is able to link-local default gateway IPV6 address on mgmt_intf in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user not able to link-local default gateway IPV6 address on mgmt_intf in static mode.
#### Test Fail Criteria ####
Testcase result is fail if user able to configure.


### Test case 4.11 - Verify loopback default gateway IPV6 address is not configurable on mgmt_intf in static mode ###
#### Description ####
Test whether the user is able to loopback default gateway IPV6 address on mgmt_intf in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user not able to loopback default gateway IPV6 address on mgmt_intf in static mode.
#### Test Fail Criteria ####
Testcase result is fail if user able to configure.


### Test case 4.12 - Verify default gateway is removable in static mode ###
#### Description ####
Test whether the user is able to remove default gateway in state mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if configured default gateway is not present in show running-config output.
#### Test Fail Criteria ####
Testcase result is fail if configured default gateway is present in show running-config output.


### Test case 4.13 - Verify invalid IPV6 address is not configurable as primary nameserver in static mode ###
#### Description ####
Test whether the user is able to configure invalid primary nameserver IPV6 address on mgmt_intf in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user not able to configure invalid primary nameserver IPV6 address on mgmt_intf in static mode.
#### Test Fail Criteria ####
Testcase result is fail if user able to configure.


### Test case 4.14  Verify multicast IPV6 address is not configurable as primary nameserver in static mode ###
#### Description ####
Test whether the user is able to configure multicast IPV6 address as primary nameserver on mgmt_intf in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user not able to configure multicast IPV6 address as primary nameserver on mgmt_intf in static mode.
#### Test Fail Criteria ####
Testcase result is fail if user able to configure.


### Test case 4.15 - Verify link-local IPV6 address is not configurable as primary nameserver  in static mode ###
#### Description ####
Test whether the user is able to configure link-local IPV6 address as primary nameserver on mgmt_intf in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user not able to configure link-local IPV6 address as primary nameserver  on mgmt_intf in static mode.
#### Test Fail Criteria ####
Testcase result is fail if user able to configure.


### Test case 4.16- Verify loopback IPV6 address is not configurable as primary nameserver in static mode ###
#### Description ####
Test whether the user is able to configure loopback IPV6 address as primary nameserver on mgmt_intf in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user not able to configure loopback IPV6 address as primary nameserver on mgmt_intf in static mode.
#### Test Fail Criteria ####
Testcase result is fail if user able to configure.


### Test case 4.17 - Verify invalid IPV6 address is not configurable as secondary nameserver in static mode ###
#### Description ####
Test whether the user is able to configure invalid IPV6 address as secondary nameserver on mgmt_intf in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user not able to configure invalid IPV6 address as secondary nameserver on mgmt_intf in static mode.
#### Test Fail Criteria ####
Testcase result is fail if user able to configure.


### Test case 4.18 - Verify multicastIPV6 address is not configurable as secondary nameserver in static mode ###
#### Description ####
Test whether the user is able to configure multicast IPV6 address as secondary nameserver on mgmt_intf in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user not able to configure multicast IPV6 address as secondary nameserver on mgmt_intf in static mode.
#### Test Fail Criteria ####
Testcase result is fail if user able to configure.


### Test case 4.18 - Verify link-local IPV6 address is not configurable as secondary nameserver in static mode ###
#### Description ####
Test whether the user is able to configure link-local IPV6 address as secondary nameserver on mgmt_intf in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user not able to configure link-local IPV6 address as secondary nameserver on mgmt_intf in static mode.
#### Test Fail Criteria ####
Testcase result is fail if user able to configure.


### Test case 4.19 - Verify loopback IPV6 address is not configurable as secondary nameserver in static mode ###
#### Description ####
Test whether the user is able to configure loopback IPV6 address as secondary nameserver on mgmt_intf in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user not able to configure loopback IPV6 address as secondary nameserver on mgmt_intf in static mode.
#### Test Fail Criteria ####
Testcase result is fail if user able to configure.

### Test case 4.20 - Verify same IPV6 address of primary and secondary DNS is not configurable in static mode ###
#### Description ####
Test whether the user is able to configure same IPV6 address of primary and secondary DNS in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if user not able to configure same IPV6 address of primary and secondary DNS.
#### Test Fail Criteria ####
Testcase result is fail if user able to configure.


### Test case 4.21 - Verify IPV6 address is configured as  primary DNS in static mode ###
#### Description ####
Test whether the user is able to configure IPV6 address primary DNS in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if configured IPV6 address primary DNS is present in show interface mgmt output & /etc/resolv.conf file.
#### Test Fail Criteria ####
Testcase result is fail if configured IPV6 address primary DNS is not present in show interface mgmt output or /etc/resolv.conf file.


### Test case 4.22 - Verify reconfiguring IPV6 address as primary DNS in static mode ###
#### Description ####
Test whether the user is able to reconfiguration of IPV6 address primary DNS in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if configured IPV6 address as primary DNS is present in show interface mgmt output & /etc/resolv.conf file.
#### Test Fail Criteria ####
Testcase result is fail if configured ipv6 address as Primary DNS is not present in show interface mgmt output or /etc/resolv.conf file.

### Test case 4.23 - Verify IPV6 address as  primary DNS is removed in static mode ###
#### Description ####
Test whether the user is able to remove IPV6 address as primary DNS in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if configured IPV6 address as primary DNS is not present in show interface mgmt output & /etc/resolv.conf file.
#### Test Fail Criteria ####
Testcase result is fail if configured IPV6 address as primary DNS is present in show interface mgmt output or /etc/resolv.conf file.

### Test case 4.24 - Verify IPV6 address as secondary DNS is configured in static mode ###
#### Description ####
Test whether the user is able to configure IPv6 address as secondary DNS in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if configured IPV6 address as secondary DNS is present in show interface mgmt output & /etc/resolv.conf file.
#### Test Fail Criteria ####
Testcase result is fail if configured IPV6 address as secondary DNS is not present in show interface mgmt output or /etc/resolv.conf file.

### Test case 4.25 - Verify reconfiguring IPV6 address as secondary DNS in static mode ###
#### Description ####
Test whether the user is able to reconfiguration of IPV6 secondary DNS in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if configured IPV6 secondary DNS is present in show interface mgmt output & /etc/resolv.conf file.
#### Test Fail Criteria ####
Testcase result is fail if configured IPV6 secondary DNS is not present in show interface mgmt output or /etc/resolv.conf file.


### Test case 4.26 - Verify  secondary DNS address is removed in static mode ###
#### Description ####
Test whether the user is able to remove secondary DNS IPV6 address in static mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if configured IPV6 secondary DNS is not present in show interface mgmt  output & /etc/resolv.conf file.
#### Test Fail Criteria ####
Testcase result is fail if configured IPV6 secondary DNS is present in show interface mgmt output or /etc/resolv.conf file.

### Test case 4.27 - Verify management interface mode is changeable ###
#### Description ####
Test whether the management interface has changed from static mode to DHCP mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if DHCP is present in show interface mgmt output.
#### Test Fail Criteria ####
Testcase result is fail if DHCP is not present in show interface mgmt output.

### Test case 4.28 - Verify management interface got IPV6 if DHCP set ###
#### Description ####
Test whether the management interface got IPV6 address in dhcp mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if IPV6 address is present in show interface mgmt output.
#### Test Fail Criteria ####
Testcase result is fail if IPV6 address is not present in show interface mgmt output.

### Test case 4.29 - Verify management interface got default gateway IPV6 address in DHCP mode ###
#### Description ####
Test whether the management interface got default gateway in DHCP mode.
### Test Result Criteria ###
#### Test Pass Criteria ####
Testcase result is success if default gateway IPV6 is present in show interface mgmt output.
#### Test Fail Criteria ####
Testcase result is fail if default gateway IPV6 is not present in show interface mgmt output.

