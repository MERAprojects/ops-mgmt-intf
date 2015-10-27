High level design of OPS-MGMT-INTF
============================

The primary goal of the management module is to facilitate the management of device. It provides the following:

	•	Device access and configuration
	
	•	Event collection for monitoring, analysis, and correlation
	
	•	Device and user authentication, authorization, and accounting
	
	•	Device time synchronization
	
	•	Download image to device
	

The device is configured or monitored through the management interface. All management traffic like ssh to the device, tftp, etc goes through the management interface.  
 

Reponsibilities
---------------
The management interface module is responsible for

- Configuring the mode in which the management interface should operate.
 
- Populating the ovsdb with DHCP client populated values (IP, subnet, default gateway and nameserver) when the mode is dhcp.

-  Providing support for configuration of the IP, default gateway and nameserver when the mode is static.
- Start the DHCP client when the mode is configured as DHCP.

- Update the DHCP populated values in ovsdb when DHCP server provides new values.

- Stop the DHCP client when the mode is configured as static.


Design choices
--------------
The design decisions made for management interface modules are:

- Same mode will be used for both IPv4 and IPv6 configuration.
- No configurations will be allowed in DHCP mode other than mode change.
- User cannot modify the physical interface that is marked as management interface.


Relationships to external OpenSwitch entities
---------------------------------------------
The following diagram provides detailed description of relationships and interactions of management interface modules with other modules in the switch.
	                                                                                          
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
	    |  |                             openvswitch|                                        |
	    |  | mgmt_intf_col                          |                                        |
	    |  | mgmt_intf_col                          |                                        |
	    |  |                                        |                                        |
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



OVSDB-Schema
------------
The management interface related columns on openSwitch table are mgmt\_intf column and mgmt\_intf\_status column. The "mgmt\_intf" column has the configuration information and the "mgmt\_intf\_status" has the status information of the attributes configured.

	+------------------------------------------------------------------------------------+
	|  +----------------------------------------+                          OVSDB         |
	|  |                             openvswitch|                                        |
	|  | mgmt_intf_col                          |                                        |
	|  | mgmt_intf_col                          |                                        |
	|  |                                        |                                        |
	|  +----------------------------------------+                                        |
	+------------------------------------------------------------------------------------+


Internal structure
------------------
The various functionality of sub modules are :

####CLI####
The CLI module is used for configuring the various management interface mode and attributes. The CLI provides basic sanity check of the parameters entered like checking the validity of the IP entered, checking the mode before any parameter configuration etc.
The "mgmt\_intf" column will be updated by the CLI. 

The CLI displays the interface parameters configured using "mgmt\_intf\_status" column. If the configuration fails at the daemon then those configurations will be present in "mgmt\_intf" column and not in "mgmt\_intf\_status" column.  

####REST####
REST module works similar to CLI.

####Management Interface Daemon####
The management interface daemon is responsible for retrieving the configurations from CLI and configuring them on the physical interface marked as management interface. In DHCP mode the management interface reads the DHCP client populated values and updated the "mgmt\_intf\_status" column.  

####DHCP client####
The dhclient is used as DHCP client. The management interface starts or stops the DHCP client based on the mode. Separate DHCP client instance is spawned for Ipv4 and Ipv6. Since same mode parameter is used to control both IPv4 and IPv6, both the instances are started and stopped at the same time.
  
References
----------
* [Management Interface Command Reference - TBL](http://www.openswitch.net/docs/redest1)


