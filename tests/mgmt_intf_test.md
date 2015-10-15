#Management interface component test cases

The following test cases verify management interface configurations in :
- [IPv4 DHCP mode](#verifying-management-interface-configuration-test-cases-in-ipv4-dhcp-mode)
- [Static IPv4 mode](#verifying-management-interface-configuration-test-cases-in-static-ipv4-mode)
- [IPv6 DHCP mode](#verifying-management-interface-configuration-test-cases-in-ipv6-dhcp-mode)
- [Static IPv6 mode](#verifying-management-interface-configuration-test-cases-in-static-ipv6-mode)
- [System Hostname](#verifying-system-hostname-configuration-testcases)

## Verifying management interface configuration test cases in IPv4 DHCP mode ##
### Objectives ###
These test cases are used for:
- Configuring, reconfiguring, and unconfiguring the management interface.
- Verifying the expected behavior of the management interface with the DHCP IPv4 addressing mode.

### Requirements ###
The requirements for this test case are:
 - IPv4 DHCP Server

### Setup ###
- #### Topology diagram ####
                                                           +-------------------+
              +------------------+                         | Linux workstation |
              |                  |eth0                eth0 |+-----------------+|
              |  AS5712 switch   |-----+         +-------- ||DHCP IPv4 Server ||
              |                  |     |         |         |+-----------------+|
              +------------------+     |         |         +-------------------+
                                       |         |
                                       v         v
                                 +---------------------+
                                 | port 1      port 2  |
                                 |                     |
                                 |      Switch         |
                                 +---------------------+

### Test case: Verifying the DHCP client has started  ###
#### Description ####
After booting the switch, verify that the DHCP client has started on the management interface by using the system ctl command: `systemctl status dhclient@eth0.service`.
#### Test result criteria ####
##### Pass criteria #####
The test is successful if the `dhcpclient` service is in a running state.
##### Fail criteria ######
The test is failed if the `dhcpclient` service is not in a running state.


### Test case: Verifying that the management interface is updated from the `image.manifest` file ###
#### Description ####
Verify that the management interface name is updated from the `image.manifest` file during boot.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if `name=eth0` is present in the **mgmt_intf** column.
##### Fail criteria ####
The test is failed if `name=eth0` is missing from the **mgmt_intf** column.


### Test case: Verifying that the user is able to enter the management interface context ###
#### Description ####
Verify that the user is able to enter the management interface context.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the user is in management context.
##### Fail criteria ####
The test is failed if the user is not in management context.


### Test case: Verifying management interface attributes in DHCP mode ###
#### Description ####
Verify that the management interface attributes are configured in DHCP mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the following criteria are met:
   - The **IPv4 address/subnet-mask**, **Default gateway IPv4**, **Primary Nameserver**, and  **Secondary Nameserver** addresses are present in the `show interface mgmt` output .
   - The `dhcp client` service is running.

##### Fail criteria ####
   The test fails if:
   - The **IPv4 address/subnet-mask**, **Default gateway IPv4**, **Primary Nameserver**, **Secondary Nameserver** addresses are missing in the `show interface mgmt` output.
   - The `dhcp client` is not running.


### Test case: Verifying that the default gateway is configurable in DHCP mode ###
#### Description ####
Configure the IPv4 default gateway in DHCP mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the IPv4 default gateway is not configured.
##### Fail criteria ####
The test is failed if the IPv4 default gateway is configured.


### Test case: Verifying that the primary DNS is configurable in DHCP mode ###
#### Description ####
Configure the IPv4 primary DNS in DHCP mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the IPv4 primary DNS is not configured.
##### Fail criteria ####
The test is failed if the IPv4 primary DNS is configured.


### Test case: Verifying that the secondary DNS is configurable in DHCP mode ###
#### Description ####
Configure the IPv4 secondary DNS in DHCP mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the IPv4 secondary DNS is not configured.
##### Fail criteria ####
The test is failed if the IPv4 secondary DNS is configured.


##  Verifying Management interface configuration test cases in Static IPv4 mode ##

### Objectives ###
These cases test are used for:
- Configuring, reconfiguring, and unconfiguring the management interface.
- Verifying the expected behavior of the management interface with the static IPv4 addressing mode.

### Requirements ###
No requirements.
### Setup ###
- #### Topology diagram ####
              +------------------+                         +-------------------+
              |                  |eth0                eth0 |                   |
              |  AS5712 switch   |----+          +-------- | Linux Workstation |
              |                  |     |         |         |                   |
              +------------------+     |         |         +-------------------+
                                       |         |
                                       v         v
                                 +---------------------+
                                 | port 1      port 2  |
                                 |                     |
                                 |      Switch         |
                                 +---------------------+

### Test case: Verifying that the static IPv4 address is configured on the management interface ###
#### Description ####
Configure the static IPv4 address on the management interface using the management interface context.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the **IPv4 address/subnet-mask** address is present in the `show interface mgmt` output and the `ifconfig` ouptut.
##### Fail criteria ####
The test fails if the **IPv4 address/subnet-mask** address is missing from the `show interface mgmt` output and the `ifconfig` ouptut.

### Test case: Verifying that the static IPv4 address is reconfigured on the management interface ###
#### Description ####
Reconfigure the static IPv4 address on the management interface using the management interface context.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the new **IPv4 address/subnet-mask** address is present in the `show interface mgmt` output and `ifconfig` ouptut.
##### Fail criteria ####
The test fails if the new **IPv4 address/subnet-mask** address is missing in the `show interface mgmt` output and `ifconfig` ouptut.


### Test case: Verifying that the default gateway is configured in static mode ###
#### Description ####
Configure the static default IPv4 gateway in the management interface using the management interface context.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the **Default gateway IPv4** address is present in the `show interface mgmt` output and in the `ip route show` output.
##### Fail criteria ####
The test fails if the **Default gateway IPv4** address is missing in the `show interface mgmt` or the `ip route show` ouput.


### Test case: Verifying that the default gateway is removed in static mode ###
#### Description ####
Remove IPv4 default gateway in static mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the **Default gateway IPv4** address is missing in the `show interface mgmt ` or the `ip route show` output.
##### Fail criteria ####
The test fails if the **Default gateway IPv4** address is missing in the `show interface mgmt` or the `ip route show` output.


### Test case: Verifying that the primary DNS is configured in static mode ###
#### Description ####
Configure the IPv4 primary DNS in static mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the **Primary Nameserver** address is present in the `show interface mgmt` output and `/etc/resolv.conf` file.
##### Fail criteria ####
The test fails if the **Primary Nameserver** address is missing in the `show interface mgmt` output or `/etc/resolv.conf` file.


### Test case: Verifying that the primary DNS is reconfigured in static mode ###
#### Description ####
Reconfigure IPv4 primary DNS in static mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the new **Primary Nameserver** address is present in the `show interface mgmt` output and `/etc/resolv.conf` file.
##### Fail criteria ####
The test fails if the new **Primary Nameserver** address is missing in the `show interface mgmt` output or `/etc/resolv.conf` file.


### Test case: Verifying that the primary DNS is removed in static mode ###
#### Description ####
Remove IPv4 primary DNS in static mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the **Primary Nameserver** address is missing in the `show interface mgmt` output and `/etc/resolv.conf` file.
##### Fail criteria ####
The test fails if the **Primary Nameserver** address is present in the `show interface mgmt` output or `/etc/resolv.conf` file.


### Test case: Verifying that the secondary DNS is configured in static mode ###
#### Description ####
Configure IPv4 secondary DNS in static mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the **Primary Nameserver**, **Secondary Nameserver** address is present in the `show interface mgmt` output and `/etc/resolv.conf` file.
##### Fail criteria ####
The test fails if the **Primary Nameserver**, **Secondary Nameserver** address is missing in the `show interface mgmt` output or `/etc/resolv.conf` file.


### Test case: Verifying that the secondary DNS is reconfigured in static mode ###
#### Description ####
Reconfigure IPv4 secondary DNS in static mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the **Primary Nameserver**, new **Secondary Nameserver** address is missing in the `show interface mgmt` output and `/etc/resolv.conf` file.
##### Fail criteria ####
The test fails if the **Primary Nameserver**, new **Secondary Nameserver** address is present in the `show interface mgmt` output or `/etc/resolv.conf` file.



### Test case: Verifying that the secondary DNS is removed in static mode ###
#### Description ####
Remove IPv4 secondary DNS in static mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the **Primary Nameserver** and **Secondary Nameserver** address is missing in the `show interface mgmt` output and `/etc/resolv.conf` file.
##### Fail criteria ####
The test fails if the **Primary Nameserver** and **Secondary Nameserver** address is present in the `show interface mgmt` output or `/etc/resolv.conf` file.



### Test case: Verifying that the invalid IPv4 address is configurable in static mode ###
#### Description ####
Configure static invalid IPv4 address on the management interface using the management interface context.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the invalid IPv4 address is not configured.
##### Fail criteria ####
The test fails if the invalid IPv4 address is configured.


### Test case: Verifying that the multicast IPv4 address is configurable in static mode ###
#### Description ####
Configure static multicast IPv4 address on the management interface using the management interface context.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the multicast IPv4 address is not configured.
##### Fail criteria ####
The test fails if the multicast IPv4 address is configured.


### Test case: Verifying that the broadcast IPv4 address is configurable in static mode ###
#### Description ####
Configure static broadcast IPv4 address on the management interface using the management interface context.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the broadcast IPv4 address is not configured.
##### Fail criteria ####
The test fails if the broadcast IPv4 address is configured.


### Test case: Verifying that the loopback IPv4 address is configurable in static mode ###
#### Description ####
Configure static loopback IPv4 address on the management interface using the management interface context.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the loopback IPv4 address is not configured.
##### Fail criteria ####
The test fails if the loopback IPv4 address is configured.


### Test case: Verifying that the invalid IPv4 default gateway address is configurable in static mode ###
#### Description ####
Configure invalid default IPv4 gateway on the management interface using the management interface context.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the invalid IPv4 default gateway address is not configured.
##### Fail criteria ####
The test fails if the invalid IPv4 default gateway address is configured.


### Test case: Verifying that the multicast IPv4 default gateway address is configurable in static mode ###
#### Description ####
Configure multicast IPv4 default gateway on the management interface using the management interface context.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the multicast IPv4 default gateway address is not configured.
##### Fail criteria ####
The test fails if the multicast IPv4 default gateway address is configured.


### Test case: Verifying that the broadcast IPv4 default gateway address is configurable in static mode ###
#### Description ####
Configure broadcast IPv4 default gateway on the management interface using the management interface context.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the broadcast IPv4 default gateway address is not configured.
##### Fail criteria ####
The test fails if the broadcast IPv4 default gateway address is configured.


### Test case: Verifying that the loopback IPv4 default gateway address is configurable in static mode ###
#### Description ####
Configure loopback IPv4 default gateway on the management interface using the management interface context.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the loopback IPv4 default gateway address is not configured.
##### Fail criteria ####
The test fails if the loopback IPv4 default gateway address is configured.


### Test case: Verifying that the invalid IPv4 primary DNS address is configurable in static mode ###
#### Description ####
Configure invalid IPv4 primary DNS address in static mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the invalid IPv4 primary DNS address is not configured.
##### Fail criteria ####
The test fails if the invalid IPv4 primary DNS address is configured.


### Test case: Verifying that the multicast IPv4 primary DNS address is configurable in static mode ###
#### Description ####
Configure multicast IPv4 primary DNS address in static mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the multicast IPv4 primary DNS address is not configured.
##### Fail criteria ####
The test fails if the multicast IPv4 primary DNS address is configured.


### Test case: Verifying that the broadcast IPv4 primary DNS address is configurable in static mode ###
#### Description ####
Configure broadcast IPv4 primary DNS address in static mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the broadcast IPv4 primary DNS address is not configured.
##### Fail criteria ####
The test fails if the broadcast IPv4 primary DNS address is configured.


### Test case: Verifying that the loopback IPv4 primary DNS address is configurable in static mode ###
#### Description ####
Configure loopback IPv4 primary DNS address in static mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the loopback IPv4 primary DNS address is not configured.
##### Fail criteria ####
The test fails if the loopback IPv4 primary DNS address is configured.



### Test case: Verifying that the invalid IPv4 secondary DNS address is configurable in static mode ###
#### Description ####
Configure invalid IPv4 secondary DNS address in static mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the invalid IPv4 secondary DNS address is not configured.
##### Fail criteria ####
The test fails if the invalid IPv4 secondary DNS address is configured.


### Test case: Verifying that the management interface mode is changeable ###
#### Description ####
Verify that the management interface is changed from static mode to DHCP mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the `Address Mode=DHCP` is present in the `show interface mgmt` output.
##### Fail criteria ####
The test fails if the `Address Mode=DHCP` is missing in the `show interface mgmt` output.


### Test case: Verifying that the management interface is got IPv4 if DHCP mode is set ###
#### Description ####
Verify that the management interface is got IPv4 address after populated static ip in DHCP mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the new `IPv4 address/subnet-mask` address is present in the `show interface mgmt` output and `ifconfig` ouptut.
##### Fail criteria ####
The test fails if the new `IPv4 address/subnet-mask` address is missing in the `show interface mgmt` output and `ifconfig` ouptut.


### Test case: Verifying that the management interface is got default gateway IPv4 address if DHCP mode set ###
#### Description ####
Verify that the management interface got default gateway IPv4 address after populate static ip in DHCP mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the `Default gateway IPv4` address is missing in the `show interface mgmt` or `ip route show` output.
##### Fail criteria ####
The test fails if the `Default gateway IPv4` address is present in the `show interface mgmt` output and `ip route show` output.



### Test case: Verifying that the management interface is got DNS IPv4 address if DHCP set ###
#### Description ####
Verify that the management interface is got primary & secondary DNS IPv4 address after populate static ip in DHCP mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the `Primary Nameserver`,`Secondary Nameserver` address is present in the `show interface mgmt` output and `/etc/resolv.conf` file.
##### Fail criteria ####
The test fails if the `Primary Nameserver`,`Secondary Nameserver` address is missing in the `show interface mgmt` output or `/etc/resolv.conf` file.


### Test case: Verifying that the static IPv4 address is removed and mode is changed to DHCP ###
#### Description ####
Verify that the configured static IPv4 address is removed and mode is changed to DHCP.
#### Test result criteria ###
##### Pass criteria ####
The test case result is successful if new `IPv4 address/subnet-mask`,`IPv6 address/prefix` address and `Address Mode=DHCP` is present in a `show interface mgmt` ouput.
##### Fail criteria ####
The test fails if new `IPv4 address/subnet-mask`,`IPv6 address/prefix` address or `Address Mode=DHCP` is missing in a `show interface mgmt` ouput.


### Test case: Verifying that the static IPv4 address is removed if IPv6 address is configured and mode is in static ###
#### Description ####
Verify that the static IPv4 address is removed if IPv6 address is configured and it's mode is in static.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if `IPv4 address/subnet-mask` address is removed and `IPv6 address/prefix` address is present in a `show interface mgmt` ouput.
##### Fail criteria ####
The test fails if `IPv4 address/subnet-mask` address is present in a `show interface mgmt` ouput.


### Test case: Verifying that the static IPv4 address is removable if default gateway IPv4 address is configured ###
#### Description ####
Verify that the static IPv4 address is removable if default gateway IPv4 address is configured.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the `IPv4 address/subnet-mask` address is present in the `show interface mgmt` output and `ifconfig` ouptut.
##### Fail criteria ####
The test fails if the `IPv4 address/subnet-mask` address is missing in the `show interface mgmt` output or `ifconfig` ouptut.


### Test case: Verifying that the static IPv4 address is removable if IPv4 nameserver address is configured ###
#### Description ####
Verify that the static IPv4 address is removable if IPv4 nameserver address is configured.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the `IPv4 address/subnet-mask` address is present in the `show interface mgmt` output and `ifconfig` ouptut.
##### Fail criteria ####
The test fails if the `IPv4 address/subnet-mask` address is missing in the `show interface mgmt` output or `ifconfig` ouptut.


### Test case: Verifying that the static IPv4 address is removable if IPv4 & IPv6 nameserver address is configured ###
#### Description ####
Verify that the static IPv4 address is removable if IPv4 and IPv6 nameserver address is configured.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the `IPv4 address/subnet-mask` address is present in the `show interface mgmt` output and `ifconfig` ouptut.
##### Fail criteria ####
The test fails if the `IPv4 address/subnet-mask` address is missing in the `show interface mgmt` output or `ifconfig` ouptut.



## Verifying management interface configuration test cases in IPv6 DHCP mode ##
### Objectives ###
These cases test:
- Configuring, reconfiguring, and unconfiguring the management interface.
- Verifying the expected behavior of the management interface with the DHCP IPv6 addressing mode.

### Requirements ###
The requirements for this test case are:

 -  IPv6 DHCP server.

### Setup ###
  - #### Topology diagram ####
                                                           +-------------------+
              +------------------+                         | Linux workstation |
              |                  |eth0                eth0 |+-----------------+|
              |  AS5712 switch   |-----+         +---------||DHCP IPv6 Server ||
              |                  |     |         |         |+-----------------+|
              +------------------+     |         |         +-------------------+
                                       |         |
                                       v         v
                                 +---------------------+
                                 | port 1      port 2  |
                                 |                     |
                                 |      Switch         |
                                 +---------------------+

### Test case: Verifying that the default gateway is configurable in DHCP mode ###
#### Description ####
Configure the IPv6 default gateway in DHCP mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the IPv6 default gateway is not configured.
##### Fail criteria ####
The test fails if the IPv6 default gateway is configured.

### Test case: Verifying that the primary DNS is configurable in DHCP mode ###
#### Description ####
Configure the IPv6 primary DNS in DHCP mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the IPv6 primary is not configured.
##### Fail criteria ####
The test fails if the IPv6 primary is configured.


### Test case: Verifying that the secondary DNS is configurable in DHCP mode ###
#### Description ####
Configure the IPv6 secondary DNS in DHCP mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the IPv6 secondary is not configured.
##### Fail criteria ####
The test fails if the IPv6 secondary is configured.



## Verifying management interface configuration test cases in Static IPv6 mode ##
### Objectives ###
These cases test:
- Configuring, reconfiguring, and unconfiguring the management interface.
- Verifying the expected behavior of the management interface in static IPv6 mode.

### Requirements ###
No requirements.

### Setup ###
- #### Topology diagram ####
                                                           +-------------------+
              +------------------+                         |                   |
              |                  |eth0                eth0 |                   |
              |  AS5712 switch   |-----+         +---------| Linux Workstation |
              |                  |     |         |         |                   |
              +------------------+     |         |         +-------------------+
                                       |         |
                                       v         v
                                 +---------------------+
                                 | port 1      port 2  |
                                 |                     |
                                 |      Switch         |
                                 +---------------------+

### Test case: Verifying that the static IPv6 address is configured on the management interface ##
#### Description ####
Configure the static IPv6 address on the management interface in the management interface context.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the `IPv6 address/prefix` address is present in the `show interface mgmt` output and `ip -6 addr show dev eth0` output.
##### Fail criteria ####
The test fails if the `IPv6 address/prefix` address is missing in the `show interface mgmt` output or `ip -6 addr show dev eth0` output.


### Test case: Verifying that the static IPv6 address is reconfigured on management interface ###
#### Description ####
Reconfigure the static IPv6 address on the management interface in the management interface context.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the  new`IPv6 address/prefix` address is present in the `show interface mgmt` output and `ip -6 addr show dev eth0` output.
##### Fail criteria ####
The test fails if the new `IPv6 address/prefix` address is missing in the `show interface mgmt` output or `ip -6 addr show dev eth0` output.


### Test case: Verifying that the invalid IPv6 address is configurable in static mode ###
#### Description ####
Configure static invalid IPv6 address on the management interface in the management interface context.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the invalid IPv6 address is not configured.
##### Fail criteria ####
The test fails if the invalid IPv6 address is configured.


### Test case: Verifying that the multicast IPv6 address is configurable in static mode ###
#### Description ####
Configure static multicast IPv6 address on the management interface in the management interface context.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the multicast IPv6 address is not configured.
##### Fail criteria ####
The test fails if the multicast IPv6 address is configured.


### Test case: Verifying that the link-local IPv6 address is configurable in static mode ###
#### Description ####
Configure static link-local IPv6 address on the management interface in the management interface context.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the link-local IPv6 address is not configured.
##### Fail criteria ####
The test fails if the link-local IPv6 address is configured.


### Test case: Verifying that the loopback IPv6 address is configurable in static mode ###
#### Description ####
Configure a static loopback IPv6 address on the management interface in the management interface context.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the loopback IPv6 address is not configured.
##### Fail criteria ####
The test fails if the loopback IPv6 address is configured.


### Test case: Verifying that the default gateway is configured in static mode ###
#### Description ####
Configure a static default IPv6 gateway on the management interface in the management interface context.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the `Default gateway IPv6` address is present in the `show running-config` output.
##### Fail criteria ####
The test fails if the `Default gateway IPv6` address is missing in the `show running-config` output.


### Test case: Verifying that the invalid IPv6 default gateway address is configurable in static mode ###
#### Description ####
Configure an invalid default IPv6 gateway on the management interface in the management interface context.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the invalid IPv6 default gateway address is not configured.
##### Fail criteria ####
The test fails if the invalid IPv6 default gateway address is configured.


### Test case: Verifying that the multicast IPv6 default gateway address is configurable in static mode ###
#### Description ####
Configure a multicast default IPv6 gateway on the management interface in the management interface context.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the multicast IPv6 default gateway address is not configured.
##### Fail criteria ####
The test fails if the multicast IPv6 default gateway address is configured.


### Test case: Verifying that the link-local default gateway IPv6 address is configurable in static mode ###
#### Description ####
Configure a link-local IPv6 default gateway on the management interface in the management interface context.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the link-local IPv6 default gateway address is not configured.
##### Fail criteria ####
The test fails if the link-local IPv6 default gateway address is configured.


### Test case: Verifying that the loopback IPv6 default gateway address is configurable in static mode ###
#### Description ####
Configure a loopback IPv6 default gateway on the management interface in the management interface context.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the loopback IPv6 default gateway address is not configured.
##### Fail criteria ####
The test fails if the loopback IPv6 default gateway address is configured.


### Test case: Verifying that the default gateway is removable in static mode ###
#### Description ####
Remove the IPv6 default gateway in state mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the `Default gateway IPv6` address is missing in the `show running-config` output.
##### Fail criteria ####
The test fails if the `Default gateway IPv6` address is present in the `show running-config` output.


### Test case: Verifying that the invalid IPv6 primary DNS address is configurable in static mode ###
#### Description ####
Configure an invalid IPv6 primary DNS in static mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the invalid IPv6 primary DNS address is not configured.
##### Fail criteria ####
The test fails if the invalid IPv6 primary DNS address is configured.


### Test case: Verifying that the multicast IPv6 primary DNS address is configurable in static mode ###
#### Description ####
Configure a multicast IPv6 primary DNS in static mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the multicast IPv6 primary DNS address is not configured.
##### Fail criteria ####
The test fails if the multicast IPv6 primary DNS address is configured.


### Test case: Verifying that the link-local IPv6 primary DNS address configurable in static mode ###
#### Description ####
Configure a link-local IPv6 primary DNS in static mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the link-local IPv6 primary DNS address is not configured.
##### Fail criteria ####
The test fails if the link-local IPv6 primary DNS address is configured.


### Test case: Verifying that the loopback IPv6 primary address is configurable in static mode ###
#### Description ####
Configure a loopback IPv6 primary DNS in static mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the loopback IPv6 primary DNS address is not configured.
##### Fail criteria ####
The test fails if the loopback IPv6 primary DNS address is configured.


### Test case: Verifying that the invalid IPv6 secondary DNS address is configurable in static mode ###
#### Description ####
Configure an invalid IPv6 secondary DNS in static mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the invalid IPv6 secondary DNS address is not configured.
##### Fail criteria ####
The test fails if the invalid IPv6 secondary DNS address is configured.


### Test case: Verifying that the multicast IPv6 secondary DNS address is configurable in static mode ###
#### Description ####
Configure a multicast IPv6 secondary DNS in static mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the multicast IPv6 secondary DNS address is not configured.
##### Fail criteria ####
The test fails if the multicast IPv6 secondary DNS address is configured.


### Test case: Verifying that the link-local IPv6 secondry DNS address is configurable in static mode ###
#### Description ####
Configure a link-local IPv6 secondary DNS in static mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the link-local IPv6 secondary DNS address is not configured.
##### Fail criteria ####
The test fails if the link-local IPv6 secondary DNS address is configured.


### Test case: Verifying that the loopback IPv6 secondary address is configurable in static mode ###
#### Description ####
Configure a loopback IPv6 secondary DNS in static mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the loopback IPv6 secondary DNS address is not configured.
##### Fail criteria ####
The test fails if the loopback IPv6 secondary DNS address is configured.


### Test case: Verifying that the same IPv6 address of primary and secondary DNS is configurable in static mode ###
#### Description ####
Configure the same IPv6 primary and secondary DNS address in static mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the same IPv6 primary and secondary DNS is not configured.
##### Fail criteria ####
The test fails if the same IPv6 primary and secondary DNS is configured.


### Test case: Verifying that the primary DNS address is configured in static mode ###
#### Description ####
Configure an IPv6 primary DNS in static mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the `Primary Nameserver` address is present in the `show interface mgmt` output and `/etc/resolv.conf` file.
##### Fail criteria ####
The test fails if the `Primary Nameserver` address is missing in the `show interface mgmt` output or `/etc/resolv.conf` file.


### Test case: Verifying that the primary DNS address is reconfigured in static mode ###
#### Description ####
Reconfigure an IPv6 primary DNS in static mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the new `Primary Nameserver` address is present in the `show interface mgmt` output and `/etc/resolv.conf` file.
##### Fail criteria ####
The test fails if the new `Primary Nameserver` address is missing in the `show interface mgmt` output or `/etc/resolv.conf` file.


### Test case: Verifying that the primary DNS address is removed in static mode ###
#### Description ####
Remove an IPv6 primary DNS in static mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the `Primary Nameserver` address is missing in the `show interface mgmt` output and `/etc/resolv.conf` file.
##### Fail criteria ####
The test fails if the `Primary Nameserver` address is present in the `show interface mgmt` output or `/etc/resolv.conf` file.


### Test case: Verifying that the secondary DNS address is configured in static mode ###
#### Description ####
Configure an IPv6 secondary DNS in static mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the `Primary Nameserver` and `Secondary Nameserver` address is present in the `show interface mgmt` output and `/etc/resolv.conf` file.
##### Fail criteria ####
The test fails if the `Primary Nameserver`and `Secondary Nameserver` address is missing in the `show interface mgmt` output or `/etc/resolv.conf` file.



### Test case: Verifying that the secondary DNS address is reconfigured in static mode ###
#### Description ####
Reconfigure an IPv6 secondary DNS in static mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the `Primary Nameserver` and new `Secondary Nameserver` address is present in the `show interface mgmt` output and `/etc/resolv.conf` file.
##### Fail criteria ####
The test fails if the `Primary Nameserver`and new `Secondary Nameserver` address is missing in the `show interface mgmt` output or `/etc/resolv.conf` file.


### Test case: Verifying that the secondary DNS address is removed in static mode ###
#### Description ####
Remove an IPv6 secondary DNS in static mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the `Secondary Nameserver` address is missing in the `show interface mgmt` output and `/etc/resolv.conf` file.
##### Fail criteria ####
The test fails if the `Secondary Nameserver` address is present in the `show interface mgmt` output or `/etc/resolv.conf` file.


### Test case: Verifying that the management interface mode is changeable ###
#### Description ####
Verify that the management interface is changed from static mode to DHCP mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the `Address Mode=DHCP` is present in the `show interface mgmt` output.
##### Fail criteria ####
The test fails if the `Address Mode=DHCP` is missing in the `show interface mgmt` output.


### Test case: Verifying that the management interface is got IPv6 if DHCP mode set ###
#### Description ####
Verify that the management interface got IPv6 address after populated static IPv6 in DHCP mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the new `IPv6 address/prefix` address is present in the `show interface mgmt` output.
##### Fail criteria ####
The test fails if the new `IPv6 address/prefix` address is missing in the `show interface mgmt` output.


### Test case: Verifying that the management interface is got default gateway IPv6 address in DHCP mode ###
#### Description ####
Verify that the management interface got default gateway IPv6 address after populate static ip in DHCP mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the `Default gateway IPv6` address is missing in the `show interface mgmt` or `ip route show` output.
##### Fail criteria ####
The test fails if the `Default gateway IPv6` address is present in the `show interface mgmt` output and `ip route show` output.


### Test case: Verifying that the static IPv6 address is removed and mode is changed to DHCP ###
#### Description ####
Verify that the configured static IPv6 address is removed and the mode is changed to DHCP.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if new `IPv4 address/subnet-mask`,`IPv6 address/prefix` address and `Address Mode=DHCP` is present in a `show interface mgmt` ouput.
##### Fail criteria ####
The test fails if new `IPv4 address/subnet-mask`,`IPv6 address/prefix` address or `Address Mode=DHCP` is missing in a `show interface mgmt` ouput.


### Test case: Verifying that the static IPv6 address is removed if IPv4 address is configured and mode is in static ###
#### Description ####
Verify that the static IPv6 address is removed if an IPv4 address is configured and the mode is in static.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if `IPv6 address/prefix` address is removed and `IPv4 address/subnet-mask` address is present in a `show interface mgmt` ouput.
##### Fail criteria ####
The test fails if `IPv6 address/prefix` address is present in a `show interface mgmt` ouput.


### Test case: Verifying that the static IPv6 address is removable if default gateway IPv6 address is configured ###
#### Description ####
Verify that the static IPv6 address is removable if a default gateway IPv6 address is configured.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the  new`IPv6 address/prefix` address is present in the `show interface mgmt` output and `ip -6 addr show dev eth0` output.
##### Fail criteria ####
The test fails if the new `IPv6 address/prefix` address is missing in the `show interface mgmt` output or `ip -6 addr show dev eth0` output.


### Test case: Verifying that the static IPv6 address is removable if IPv6 nameserver address is configured###
#### Description ####
Verify that the static IPv6 address is removable if the IPv6 nameserver address is configured.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the  new`IPv6 address/prefix` address is present in the `show interface mgmt` output and `ip -6 addr show dev eth0` output.
##### Fail criteria ####
The test fails if the new `IPv6 address/prefix` address is missing in the `show interface mgmt` output or `ip -6 addr show dev eth0` output.


### Test case: Verifying that the static IPv6 address is removable if IPv4 & IPv6 nameserver address is configured ###
#### Description ####
Verify that the static IPv6 address is removable if the IPv4 and IPv6 nameserver address is configured.
#### Test result criteria ###
##### Pass Criteria ####
The test is successful if the  new`IPv6 address/prefix` address is present in the `show interface mgmt` output and `ip -6 addr show dev eth0` output.
##### Fail criteria ####
The test fails if the new `IPv6 address/prefix` address is missing in the `show interface mgmt` output or `ip -6 addr show dev eth0` output.

## Verifying system hostname configuration testcases  ##

### Objectives ###
   These cases test the following:
   - Configuring, reconfiguring and unconfiguring the system hostname.
   - Verifying the expected behavior of the system hostname.

### Requirements ###
The requirements for this test case are:

 -  DHCP server.

### Setup ###
- #### Topology diagram ####

                                                +-------------------+
              +------------------+              | Linux workstation |
              |                  |eth0     eth1 |+-----------------+|
              |  AS5712 switch   |--------------||   DHCP Server   ||
              |                  |              |+-----------------+|
              +------------------+              +-------------------+


### Test case: Verifying that the system hostname is configured using CLI  ###
#### Description ####
Test to verify whether hthe ostname of the system changes to the value configured using CLI command "hostname new-name" in config mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the configured value is present in `uname -n` output.
##### Fail criteria ####
The test fails if the configured hostname is not present in `uname -n` output.

### Test case: Verifying that the system hostname is unconfigured using CLI  ###
#### Description ####
Test to verify whether the hostname of the system changes to the default value **switch** when unconfigured using the CLI command `no hostname` in config mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the default hostname **switch** is present in `uname -n` output.
##### Fail criteria ####
The test fails if the default value **switch** is not present in `uname -n` output.

### Test case: Verifying that the system hostname defaults to switch ###
#### Description ####
Test to verify whether the system hostname defaults to **switch** when nothing is configured through the CLI in config mode.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the default hostname **switch** is present in `uname -n` output.
##### Fail criteria ####
The test fails if the default value **switch** is not present in `uname -n` output.

### Test case: Verifying that the system hostname is configured via DHCP Server  ###
#### Description ####
Test to verify whether the hostname of the system changes to the value configured by DHCP server via **dhclient** using option12 `option host-name`.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if the configured value is present in `uname -n` output.
##### Fail criteria ####
The test fails if  the configured hostname is not present in `uname -n` output.

### Test case: Verifying that the system hostname is unconfigured via DHCP Server  ###
#### Description ####
Test to verify whether the system hostname defaults to **switch** when option12 `option host-name` is not configured by DHCP server.
#### Test result criteria ###
##### Pass criteria ####
The test is successful if default hostname **switch** is present in `uname -n` output.
##### Fail criteria ####
The test fails if the default value **switch** is not present in `uname -n` output.
