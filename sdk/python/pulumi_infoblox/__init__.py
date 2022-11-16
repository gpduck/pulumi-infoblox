# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .provider import *

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_infoblox.config as __config
    config = __config
    import pulumi_infoblox.ip as __ip
    ip = __ip
    import pulumi_infoblox.ipv4 as __ipv4
    ipv4 = __ipv4
    import pulumi_infoblox.record as __record
    record = __record
else:
    config = _utilities.lazy_import('pulumi_infoblox.config')
    ip = _utilities.lazy_import('pulumi_infoblox.ip')
    ipv4 = _utilities.lazy_import('pulumi_infoblox.ipv4')
    record = _utilities.lazy_import('pulumi_infoblox.record')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "infoblox",
  "mod": "ip/allocation",
  "fqn": "pulumi_infoblox.ip",
  "classes": {
   "infoblox:ip/allocation:Allocation": "Allocation"
  }
 },
 {
  "pkg": "infoblox",
  "mod": "ip/association",
  "fqn": "pulumi_infoblox.ip",
  "classes": {
   "infoblox:ip/association:Association": "Association"
  }
 },
 {
  "pkg": "infoblox",
  "mod": "ipv4/allocation",
  "fqn": "pulumi_infoblox.ipv4",
  "classes": {
   "infoblox:ipv4/allocation:Allocation": "Allocation"
  }
 },
 {
  "pkg": "infoblox",
  "mod": "ipv4/association",
  "fqn": "pulumi_infoblox.ipv4",
  "classes": {
   "infoblox:ipv4/association:Association": "Association"
  }
 },
 {
  "pkg": "infoblox",
  "mod": "ipv4/network",
  "fqn": "pulumi_infoblox.ipv4",
  "classes": {
   "infoblox:ipv4/network:Network": "Network"
  }
 },
 {
  "pkg": "infoblox",
  "mod": "ipv4/networkContainer",
  "fqn": "pulumi_infoblox.ipv4",
  "classes": {
   "infoblox:ipv4/networkContainer:NetworkContainer": "NetworkContainer"
  }
 },
 {
  "pkg": "infoblox",
  "mod": "record/a",
  "fqn": "pulumi_infoblox.record",
  "classes": {
   "infoblox:record/a:A": "A"
  }
 },
 {
  "pkg": "infoblox",
  "mod": "record/aAAA",
  "fqn": "pulumi_infoblox.record",
  "classes": {
   "infoblox:record/aAAA:AAAA": "AAAA"
  }
 },
 {
  "pkg": "infoblox",
  "mod": "record/cName",
  "fqn": "pulumi_infoblox.record",
  "classes": {
   "infoblox:record/cName:CName": "CName"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "infoblox",
  "token": "pulumi:providers:infoblox",
  "fqn": "pulumi_infoblox",
  "class": "Provider"
 }
]
"""
)
