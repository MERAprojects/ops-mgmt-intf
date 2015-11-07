#High level design of OPS-MGMT-INTF

The primary goal of the management module is to facilitate the management of device. It provides the following:

	•	Device access and configuration
	•	Event collection for monitoring, analysis, and correlation
	•	Device and user authentication, authorization, and accounting
	•	Device time synchronization
	•	Device image downloading

The device is configured or monitored through the management interface. All management traffic like `ssh` to the device, `tftp`, etc goes through the management interface.

##Reponsibilities

The management interface module is responsible for:

- Configuring the mode in which the management interface should operate.

- Populating the `ovsdb` with DHCP client populated values (IP, subnet, default gateway and nameserver) when the mode is `dhcp`.

-  Providing support for configuration of the IP, default gateway and nameserver when the mode is `static`.
- Start the DHCP client when the mode is configured as `DHCP`.

- Update the DHCP populated values in ovsdb when DHCP server provides new values.

- Stop the DHCP client when the mode is configured as `static`.

- Configuring system hostname through `CLI` or `DHCP`.


## Design choices

The design decisions made for management interface modules are:

- Same mode is used for both IPv4 and IPv6 configuration.
- No configurations are allowed in DHCP mode other than mode change.
- User cannot modify the physical interface that is marked as management interface.


Relationships to external OpenSwitch entities
---------------------------------------------
The following diagram provides a detailed description of relationships and interactions of management interface modules with other modules in the switch.
```ditaa
	+---------------+              +---------------+        +------------------------+
	|               |              |               |        |  Modules that require  |
	|   CLI         |              |    REST       |        |  Mgmt Intf attrbutes   |
	|               |              |               |        |                        |
	+--------+------+              +------+--------+        +----------+-------------+
	         |                            |                            |
	         |                            |                            |
	         |                            |                            |
	    +--------------------------------------------------------------v---------------------+
	    |  +----------------------------------------+                          OVSDB         |
	    |  |                             System     |                                        |
	    |  | mgmt_intf_col                          |                                        |
	    |  | mgmt_intf_status_col                   |                                        |
	    |  | hostname                               |                                        |
	    |  +----------------------------------------+                                        |
	    +------------------------------------------------------------------------------------+
	                          |
	                          |
	                          |
	                          |
	        +-----------------+--------------------+
	        |                                      |
	        |  Management Interface                |        +------------------+
	        |                                      +--------+                  |
	        |                  Daemon              |        |   Dhclient       |
	        |                                      |        |                  |
	        +--------------------------------------+        +------------------+
```


OVSDB-Schema
------------
The management interface related columns on openSwitch table are the **mgmt\_intf** column and the **mgmt\_intf\_status** column. The **mgmt\_intf** column has the configuration information and the **mgmt\_intf\_status** has the status information of the attributes configured.
```ditaa
	+------------------------------------------------------------------------------------+
	|  +----------------------------------------+                          OVSDB         |
	|  |                             System     |                                        |
	|  | mgmt_intf_col                          |                                        |
	|  | mgmt_intf_status_col                   |                                        |
	|  | hostname                               |                                        |
	|  +----------------------------------------+                                        |
	+------------------------------------------------------------------------------------+
```

The keys and values supported by the management interface columns are:

|    Key  |    Value       |
| --------|----------------|
| name      | string       |
| mode      | string       |
| ip      | IPv4 address   |
| subnet_mask    | Integer with range 1 to 31   |
| ipv6    | IPv6 address   |
| default_gateway      | IPv4 address   |
| default_gateway_v6    | IPv6 address   |
| dns_server_1      | IPv4 address   |
| dns_server_2    | IPv4 address   |
| ipv6_linklocal| IPv6 address   |
| link_state      | string       |
| hostname      | string       |
| dhcp_hostname      | string       |

##Internal structure

The various functionality of sub modules are :

####CLI####
The CLI module is used for configuring the various management interface mode and attributes and system hostname. The CLI provides basic sanity check of the parameters entered like checking the validity of the IP entered, checking the mode before any parameter configuration, checking if hostname provided is alpha-numeric etc. The **mgmt\_intf** column and **hostname** column are updated by the CLI.

The CLI displays the interface parameters configured using the **mgmt\_intf\_status** column. If the configuration fails at the daemon then those configurations are present in the **mgmt\_intf** column and not in the **mgmt\_intf\_status** column.

####REST####
The REST module works similar to CLI. The operations allowed on the **System** table are GET and PUT.

####Management Interface Daemon####
The management interface daemon is responsible for retrieving the configurations from CLI and configuring them on the physical interface marked as management interface. In DHCP mode, the management interface reads the DHCP client populated values and updates the **mgmt\_intf\_status** column.

The other responsibilites of the management interface daemon include:
- The management interface also maintains the state of the physical port configured as management interface.
- When the hostname is configured through management interfaces like CLI or DHCP, the management interface daemon configures the new hostname in the system. If none of these are available, system hostname defaults to **switch**

In `static` mode, the user configures the IP, default gateway, and nameservers addresses through CLI/REST. The management interface daemon configures these values in the pysical interface marked as management interface and updates the **mgmt\_intf\_status** column.

In `DHCP` mode, the management interface daemon listens on the netlink socket. Any change in the IP or link state is notified to the management interface daemon by the netlink module. On reception of notification, the management interface daemon reads the IP, default gateway, nameservers addresses populated by DHCP client, and updates the **mgmt\_intf\_status** column.

####DHCP client####
The `dhclient` is used as a DHCP client. The management interface starts or stops the DHCP client based on the mode. Separate DHCP client instances are spawned for Ipv4 and Ipv6. Since the same mode parameter is used to control both IPv4 and IPv6, both the instances are started and stopped at the same time.

##References

* [Management Interface Command Reference](/documents/user/mgmt_intf_cli)
