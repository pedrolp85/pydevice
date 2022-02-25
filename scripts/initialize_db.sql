#!/bin/bash

mysql -u root -ppassword << QUERY_INPUT

SHOW DATABASES;
USE py_device;

CREATE TABLE manufacturer (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(10) NOT NULL,
    enterprise_name varchar(25) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE l3interface (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(20) NOT NULL,
    ip_address varchar(20) NOT NULL,
    PRIMARY KEY (id)
);


CREATE TABLE device (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(20) NOT NULL,
    model varchar(20) NOT NULL,
    manufacturer_id int ,
    mgmt_interface_id int,
    PRIMARY KEY (id),
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturer(id),
    FOREIGN KEY (mgmt_interface_id) REFERENCES l3interface(id)
);


INSERT INTO manufacturer (name, enterprise_name) VALUES
    ('paloalto','PALO ALTO NETWORKS INC.'),
    ('cisco', 'CISCO SYSTEMS INC.')
    ;

INSERT INTO l3interface (name, ip_address ) VALUES
    ('mgmt0','172.16.0.22'),
    ('FastEthernet0','172.16.0.23') 
    ;

INSERT INTO device (name, model, manufacturer_id, mgmt_interface_id) VALUES
    ('FW_INT1','VM100',1, 1),
    ('BranchCSR1000v','iosxe',2, 2) 
    ;



SELECT *
FROM device
INNER JOIN manufacturer
ON device.manufacturer_id = manufacturer.id
INNER JOIN l3interface
ON device.mgmt_interface_id = l3interface.id

QUERY_INPUT