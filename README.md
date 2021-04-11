# ec2-metadata-json

This is a utility to query the meta data of an instance within aws and provide a json formatted output.

# Assumptions

In case we are looking for a utility to be used with in instance for programatic use cases I would use the ec2-metadata utility that is available [here](https://github.com/adamchainz/ec2-metadata) 

Very simple to use and also supports cache if required. In most recent days this utility has been very handy.

```
>>> from ec2_metadata import ec2_metadata
>>> print(ec2_metadata.region)
us-east-1
>>> print(ec2_metadata.instance_id)
i-123456
```

If its one off activity I would prefer a simple curl command to get the data of a given key.

For ex: 
1. SSH to an instance
2. Command to retrieve the ami-id 
```
curl http://169.254.169.254/latest/meta-data/ami-id
```
In case you need a json output and use it for some comparison or debugging you can use this utility.

```
$ python --version
Python 2.7.17

$ python ec2-metadata-json.py

{
    "ami": "/dev/sda1",
    "ami-id": "ami-XXXXXXXX",
    "ami-launch-index": 0,
    "ami-manifest-path": "(unknown)",
    "availability-zone": "eu-west-1a",
    "availability-zone-id": "euw1-az2",
    "device-number": 0,
    "domain": "amazonaws.com",
    "ec2-instance": {
        "AccessKeyId": "XXXXXXXXXXXXXX",
        "Code": "Success",
        "Expiration": "2021-04-11T14:16:57Z",
        "LastUpdated": "2021-04-11T08:11:11Z",
        "SecretAccessKey": "XXXXXXXXXXXXXXXX",
        "Token": "XXXXXXXXXXXXXX",
        "Type": "AWS-HMAC"
    },
    "ephemeral0": "sdb",
    "ephemeral1": "sdc",
    "history": [],
    "hostname": "ip-XXXXXXXXXX.eu-west-1.compute.internal",
    "info": {
        "AccountId": "XXXXXXXXXXX",
        "Code": "Success",
        "LastUpdated": "2021-04-11T08:11:32Z"
    },
    "instance-action": "none",
    "instance-id": "i-XXXXXXXXXX",
    "instance-life-cycle": "on-demand",
    "instance-type": "t2.small",
    "interface-id": "eni-XXXXXXXX",
    "local-hostname": "ip-XXXXXXXXXX.eu-west-1.compute.internal",
    "local-ipv4": "XXXXXXXXXX",
    "local-ipv4s": "XXXXXXXXXX",
    "mac": "06:2e:1d:c9:ac:ff",
    "owner-id": XXXXXXXXXX,
    "partition": "aws",
    "product-codes": "dc3kgx9eyqg3we2d6fa4ndr8",
    "profile": "default-hvm",
    "region": "eu-west-1",
    "reservation-id": "r-XXXXXXXXXX",
    "root": "/dev/sda1",
    "scheduled": [],
    "security-group-ids": "sg-XXXXXXXXXX\nsg-XXXXXXXXXX",
    "security-groups": "XXXXXXXXXX",
    "subnet-id": "subnet-XXXXXXXXXX",
    "subnet-ipv4-cidr-block": "XXXXXXXXXX",
    "vhostmd": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>",
    "vpc-id": "vpc-XXXXXXXXXX",
    "vpc-ipv4-cidr-block": "XXXXXXXXXX/20",
    "vpc-ipv4-cidr-blocks": "XXXXXXXXXX/20"
}
The value of the choosen key info/AccountId is XXXXXXXXXXX

```
