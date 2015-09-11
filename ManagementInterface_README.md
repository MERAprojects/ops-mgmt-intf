OPS-MGMT-INTF
=======

What is ops-mgmt-intf?
----------------
The primary goal of the management module is to facilitate the management of device. It provides the following:

	•	Device access and configuration
	
	•	Event collection for monitoring, analysis, and correlation
	
	•	Device and user authentication, authorization, and accounting
	
	•	Device time synchronization
	
	•	Download image to device
	

The device is configured or monitored through the management interface. All management traffic like ssh to the device, tftp, etc goes through the management interface.  
 

What is the structure of the repository?
----------------------------------------
* src/ops-mgmt-intf/ contains the management interface daemon code.
* src/ops-mgmt-intf/test/ contains all the component tests of ops-mgmt-intf based on [ops-test-framework](http://git.openswitch.net/openswitch/ops-test-framework)

* src/ops-mgmt-intf/doc/ contains the document related to the management interface module.

What is the license?
--------------------
NA

What other documents are available?
-----------------------------------
For the high level design of ops-mgmt-intf, refer to [DESIGN.md-TBL](DESIGN.md)
For answers to common questions, read [FAQ.md - TBL](FAQ.md)
For the current list of contributors and maintainers, refer to [AUTHORS.md - TBL](AUTHORS.md)

For general information about OpenSwitch project refer to http://www.openswitch.net
