# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['AllocationArgs', 'Allocation']

@pulumi.input_type
class AllocationArgs:
    def __init__(__self__, *,
                 fqdn: pulumi.Input[str],
                 allocated_ipv4_addr: Optional[pulumi.Input[str]] = None,
                 allocated_ipv6_addr: Optional[pulumi.Input[str]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 dns_view: Optional[pulumi.Input[str]] = None,
                 enable_dns: Optional[pulumi.Input[bool]] = None,
                 ext_attrs: Optional[pulumi.Input[str]] = None,
                 internal_id: Optional[pulumi.Input[str]] = None,
                 ipv4_addr: Optional[pulumi.Input[str]] = None,
                 ipv4_cidr: Optional[pulumi.Input[str]] = None,
                 ipv6_addr: Optional[pulumi.Input[str]] = None,
                 ipv6_cidr: Optional[pulumi.Input[str]] = None,
                 network_view: Optional[pulumi.Input[str]] = None,
                 ttl: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a Allocation resource.
        :param pulumi.Input[str] fqdn: The host name for Host Record in FQDN format.
        :param pulumi.Input[str] allocated_ipv4_addr: Value which comes from 'ipv4_addr' (if specified) or from auto-allocation function (using 'ipv4_cidr').
        :param pulumi.Input[str] allocated_ipv6_addr: Value which comes from 'ipv6_addr' (if specified) or from auto-allocation function (using 'ipv6_cidr').
        :param pulumi.Input[str] comment: A description of IP address allocation.
        :param pulumi.Input[str] dns_view: DNS view under which the zone has been created.
        :param pulumi.Input[bool] enable_dns: flag that defines if the host record is to be used for DNS purposes.
        :param pulumi.Input[str] ext_attrs: The extensible attributes for IP address allocation, as a map in JSON format
        :param pulumi.Input[str] internal_id: Internal ID of an object at NIOS side, used by Infoblox Terraform plugin to search for a NIOS's object which corresponds
               to the Terraform resource.
        :param pulumi.Input[str] ipv4_addr: IPv4 address of cloud instance.Set a valid IP address for static allocation and leave empty if dynamically allocated.
        :param pulumi.Input[str] ipv4_cidr: The IPv4 cidr from which an IPv4 address will be allocated.
        :param pulumi.Input[str] ipv6_addr: IPv6 address of cloud instance.Set a valid IP address for static allocation and leave empty if dynamically allocated.
        :param pulumi.Input[str] ipv6_cidr: The IPv6 cidr from which an IPv6 address will be allocated.
        :param pulumi.Input[str] network_view: network view name on NIOS server.
        :param pulumi.Input[int] ttl: TTL attribute value for the record.
        """
        pulumi.set(__self__, "fqdn", fqdn)
        if allocated_ipv4_addr is not None:
            pulumi.set(__self__, "allocated_ipv4_addr", allocated_ipv4_addr)
        if allocated_ipv6_addr is not None:
            pulumi.set(__self__, "allocated_ipv6_addr", allocated_ipv6_addr)
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if dns_view is not None:
            pulumi.set(__self__, "dns_view", dns_view)
        if enable_dns is not None:
            pulumi.set(__self__, "enable_dns", enable_dns)
        if ext_attrs is not None:
            pulumi.set(__self__, "ext_attrs", ext_attrs)
        if internal_id is not None:
            pulumi.set(__self__, "internal_id", internal_id)
        if ipv4_addr is not None:
            pulumi.set(__self__, "ipv4_addr", ipv4_addr)
        if ipv4_cidr is not None:
            pulumi.set(__self__, "ipv4_cidr", ipv4_cidr)
        if ipv6_addr is not None:
            pulumi.set(__self__, "ipv6_addr", ipv6_addr)
        if ipv6_cidr is not None:
            pulumi.set(__self__, "ipv6_cidr", ipv6_cidr)
        if network_view is not None:
            pulumi.set(__self__, "network_view", network_view)
        if ttl is not None:
            pulumi.set(__self__, "ttl", ttl)

    @property
    @pulumi.getter
    def fqdn(self) -> pulumi.Input[str]:
        """
        The host name for Host Record in FQDN format.
        """
        return pulumi.get(self, "fqdn")

    @fqdn.setter
    def fqdn(self, value: pulumi.Input[str]):
        pulumi.set(self, "fqdn", value)

    @property
    @pulumi.getter(name="allocatedIpv4Addr")
    def allocated_ipv4_addr(self) -> Optional[pulumi.Input[str]]:
        """
        Value which comes from 'ipv4_addr' (if specified) or from auto-allocation function (using 'ipv4_cidr').
        """
        return pulumi.get(self, "allocated_ipv4_addr")

    @allocated_ipv4_addr.setter
    def allocated_ipv4_addr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "allocated_ipv4_addr", value)

    @property
    @pulumi.getter(name="allocatedIpv6Addr")
    def allocated_ipv6_addr(self) -> Optional[pulumi.Input[str]]:
        """
        Value which comes from 'ipv6_addr' (if specified) or from auto-allocation function (using 'ipv6_cidr').
        """
        return pulumi.get(self, "allocated_ipv6_addr")

    @allocated_ipv6_addr.setter
    def allocated_ipv6_addr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "allocated_ipv6_addr", value)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        """
        A description of IP address allocation.
        """
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter(name="dnsView")
    def dns_view(self) -> Optional[pulumi.Input[str]]:
        """
        DNS view under which the zone has been created.
        """
        return pulumi.get(self, "dns_view")

    @dns_view.setter
    def dns_view(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dns_view", value)

    @property
    @pulumi.getter(name="enableDns")
    def enable_dns(self) -> Optional[pulumi.Input[bool]]:
        """
        flag that defines if the host record is to be used for DNS purposes.
        """
        return pulumi.get(self, "enable_dns")

    @enable_dns.setter
    def enable_dns(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_dns", value)

    @property
    @pulumi.getter(name="extAttrs")
    def ext_attrs(self) -> Optional[pulumi.Input[str]]:
        """
        The extensible attributes for IP address allocation, as a map in JSON format
        """
        return pulumi.get(self, "ext_attrs")

    @ext_attrs.setter
    def ext_attrs(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ext_attrs", value)

    @property
    @pulumi.getter(name="internalId")
    def internal_id(self) -> Optional[pulumi.Input[str]]:
        """
        Internal ID of an object at NIOS side, used by Infoblox Terraform plugin to search for a NIOS's object which corresponds
        to the Terraform resource.
        """
        return pulumi.get(self, "internal_id")

    @internal_id.setter
    def internal_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "internal_id", value)

    @property
    @pulumi.getter(name="ipv4Addr")
    def ipv4_addr(self) -> Optional[pulumi.Input[str]]:
        """
        IPv4 address of cloud instance.Set a valid IP address for static allocation and leave empty if dynamically allocated.
        """
        return pulumi.get(self, "ipv4_addr")

    @ipv4_addr.setter
    def ipv4_addr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv4_addr", value)

    @property
    @pulumi.getter(name="ipv4Cidr")
    def ipv4_cidr(self) -> Optional[pulumi.Input[str]]:
        """
        The IPv4 cidr from which an IPv4 address will be allocated.
        """
        return pulumi.get(self, "ipv4_cidr")

    @ipv4_cidr.setter
    def ipv4_cidr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv4_cidr", value)

    @property
    @pulumi.getter(name="ipv6Addr")
    def ipv6_addr(self) -> Optional[pulumi.Input[str]]:
        """
        IPv6 address of cloud instance.Set a valid IP address for static allocation and leave empty if dynamically allocated.
        """
        return pulumi.get(self, "ipv6_addr")

    @ipv6_addr.setter
    def ipv6_addr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv6_addr", value)

    @property
    @pulumi.getter(name="ipv6Cidr")
    def ipv6_cidr(self) -> Optional[pulumi.Input[str]]:
        """
        The IPv6 cidr from which an IPv6 address will be allocated.
        """
        return pulumi.get(self, "ipv6_cidr")

    @ipv6_cidr.setter
    def ipv6_cidr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv6_cidr", value)

    @property
    @pulumi.getter(name="networkView")
    def network_view(self) -> Optional[pulumi.Input[str]]:
        """
        network view name on NIOS server.
        """
        return pulumi.get(self, "network_view")

    @network_view.setter
    def network_view(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_view", value)

    @property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[int]]:
        """
        TTL attribute value for the record.
        """
        return pulumi.get(self, "ttl")

    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ttl", value)


@pulumi.input_type
class _AllocationState:
    def __init__(__self__, *,
                 allocated_ipv4_addr: Optional[pulumi.Input[str]] = None,
                 allocated_ipv6_addr: Optional[pulumi.Input[str]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 dns_view: Optional[pulumi.Input[str]] = None,
                 enable_dns: Optional[pulumi.Input[bool]] = None,
                 ext_attrs: Optional[pulumi.Input[str]] = None,
                 fqdn: Optional[pulumi.Input[str]] = None,
                 internal_id: Optional[pulumi.Input[str]] = None,
                 ipv4_addr: Optional[pulumi.Input[str]] = None,
                 ipv4_cidr: Optional[pulumi.Input[str]] = None,
                 ipv6_addr: Optional[pulumi.Input[str]] = None,
                 ipv6_cidr: Optional[pulumi.Input[str]] = None,
                 network_view: Optional[pulumi.Input[str]] = None,
                 ref: Optional[pulumi.Input[str]] = None,
                 ttl: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering Allocation resources.
        :param pulumi.Input[str] allocated_ipv4_addr: Value which comes from 'ipv4_addr' (if specified) or from auto-allocation function (using 'ipv4_cidr').
        :param pulumi.Input[str] allocated_ipv6_addr: Value which comes from 'ipv6_addr' (if specified) or from auto-allocation function (using 'ipv6_cidr').
        :param pulumi.Input[str] comment: A description of IP address allocation.
        :param pulumi.Input[str] dns_view: DNS view under which the zone has been created.
        :param pulumi.Input[bool] enable_dns: flag that defines if the host record is to be used for DNS purposes.
        :param pulumi.Input[str] ext_attrs: The extensible attributes for IP address allocation, as a map in JSON format
        :param pulumi.Input[str] fqdn: The host name for Host Record in FQDN format.
        :param pulumi.Input[str] internal_id: Internal ID of an object at NIOS side, used by Infoblox Terraform plugin to search for a NIOS's object which corresponds
               to the Terraform resource.
        :param pulumi.Input[str] ipv4_addr: IPv4 address of cloud instance.Set a valid IP address for static allocation and leave empty if dynamically allocated.
        :param pulumi.Input[str] ipv4_cidr: The IPv4 cidr from which an IPv4 address will be allocated.
        :param pulumi.Input[str] ipv6_addr: IPv6 address of cloud instance.Set a valid IP address for static allocation and leave empty if dynamically allocated.
        :param pulumi.Input[str] ipv6_cidr: The IPv6 cidr from which an IPv6 address will be allocated.
        :param pulumi.Input[str] network_view: network view name on NIOS server.
        :param pulumi.Input[str] ref: NIOS object's reference, not to be set by a user.
        :param pulumi.Input[int] ttl: TTL attribute value for the record.
        """
        if allocated_ipv4_addr is not None:
            pulumi.set(__self__, "allocated_ipv4_addr", allocated_ipv4_addr)
        if allocated_ipv6_addr is not None:
            pulumi.set(__self__, "allocated_ipv6_addr", allocated_ipv6_addr)
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if dns_view is not None:
            pulumi.set(__self__, "dns_view", dns_view)
        if enable_dns is not None:
            pulumi.set(__self__, "enable_dns", enable_dns)
        if ext_attrs is not None:
            pulumi.set(__self__, "ext_attrs", ext_attrs)
        if fqdn is not None:
            pulumi.set(__self__, "fqdn", fqdn)
        if internal_id is not None:
            pulumi.set(__self__, "internal_id", internal_id)
        if ipv4_addr is not None:
            pulumi.set(__self__, "ipv4_addr", ipv4_addr)
        if ipv4_cidr is not None:
            pulumi.set(__self__, "ipv4_cidr", ipv4_cidr)
        if ipv6_addr is not None:
            pulumi.set(__self__, "ipv6_addr", ipv6_addr)
        if ipv6_cidr is not None:
            pulumi.set(__self__, "ipv6_cidr", ipv6_cidr)
        if network_view is not None:
            pulumi.set(__self__, "network_view", network_view)
        if ref is not None:
            pulumi.set(__self__, "ref", ref)
        if ttl is not None:
            pulumi.set(__self__, "ttl", ttl)

    @property
    @pulumi.getter(name="allocatedIpv4Addr")
    def allocated_ipv4_addr(self) -> Optional[pulumi.Input[str]]:
        """
        Value which comes from 'ipv4_addr' (if specified) or from auto-allocation function (using 'ipv4_cidr').
        """
        return pulumi.get(self, "allocated_ipv4_addr")

    @allocated_ipv4_addr.setter
    def allocated_ipv4_addr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "allocated_ipv4_addr", value)

    @property
    @pulumi.getter(name="allocatedIpv6Addr")
    def allocated_ipv6_addr(self) -> Optional[pulumi.Input[str]]:
        """
        Value which comes from 'ipv6_addr' (if specified) or from auto-allocation function (using 'ipv6_cidr').
        """
        return pulumi.get(self, "allocated_ipv6_addr")

    @allocated_ipv6_addr.setter
    def allocated_ipv6_addr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "allocated_ipv6_addr", value)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        """
        A description of IP address allocation.
        """
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter(name="dnsView")
    def dns_view(self) -> Optional[pulumi.Input[str]]:
        """
        DNS view under which the zone has been created.
        """
        return pulumi.get(self, "dns_view")

    @dns_view.setter
    def dns_view(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dns_view", value)

    @property
    @pulumi.getter(name="enableDns")
    def enable_dns(self) -> Optional[pulumi.Input[bool]]:
        """
        flag that defines if the host record is to be used for DNS purposes.
        """
        return pulumi.get(self, "enable_dns")

    @enable_dns.setter
    def enable_dns(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_dns", value)

    @property
    @pulumi.getter(name="extAttrs")
    def ext_attrs(self) -> Optional[pulumi.Input[str]]:
        """
        The extensible attributes for IP address allocation, as a map in JSON format
        """
        return pulumi.get(self, "ext_attrs")

    @ext_attrs.setter
    def ext_attrs(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ext_attrs", value)

    @property
    @pulumi.getter
    def fqdn(self) -> Optional[pulumi.Input[str]]:
        """
        The host name for Host Record in FQDN format.
        """
        return pulumi.get(self, "fqdn")

    @fqdn.setter
    def fqdn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fqdn", value)

    @property
    @pulumi.getter(name="internalId")
    def internal_id(self) -> Optional[pulumi.Input[str]]:
        """
        Internal ID of an object at NIOS side, used by Infoblox Terraform plugin to search for a NIOS's object which corresponds
        to the Terraform resource.
        """
        return pulumi.get(self, "internal_id")

    @internal_id.setter
    def internal_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "internal_id", value)

    @property
    @pulumi.getter(name="ipv4Addr")
    def ipv4_addr(self) -> Optional[pulumi.Input[str]]:
        """
        IPv4 address of cloud instance.Set a valid IP address for static allocation and leave empty if dynamically allocated.
        """
        return pulumi.get(self, "ipv4_addr")

    @ipv4_addr.setter
    def ipv4_addr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv4_addr", value)

    @property
    @pulumi.getter(name="ipv4Cidr")
    def ipv4_cidr(self) -> Optional[pulumi.Input[str]]:
        """
        The IPv4 cidr from which an IPv4 address will be allocated.
        """
        return pulumi.get(self, "ipv4_cidr")

    @ipv4_cidr.setter
    def ipv4_cidr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv4_cidr", value)

    @property
    @pulumi.getter(name="ipv6Addr")
    def ipv6_addr(self) -> Optional[pulumi.Input[str]]:
        """
        IPv6 address of cloud instance.Set a valid IP address for static allocation and leave empty if dynamically allocated.
        """
        return pulumi.get(self, "ipv6_addr")

    @ipv6_addr.setter
    def ipv6_addr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv6_addr", value)

    @property
    @pulumi.getter(name="ipv6Cidr")
    def ipv6_cidr(self) -> Optional[pulumi.Input[str]]:
        """
        The IPv6 cidr from which an IPv6 address will be allocated.
        """
        return pulumi.get(self, "ipv6_cidr")

    @ipv6_cidr.setter
    def ipv6_cidr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv6_cidr", value)

    @property
    @pulumi.getter(name="networkView")
    def network_view(self) -> Optional[pulumi.Input[str]]:
        """
        network view name on NIOS server.
        """
        return pulumi.get(self, "network_view")

    @network_view.setter
    def network_view(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_view", value)

    @property
    @pulumi.getter
    def ref(self) -> Optional[pulumi.Input[str]]:
        """
        NIOS object's reference, not to be set by a user.
        """
        return pulumi.get(self, "ref")

    @ref.setter
    def ref(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ref", value)

    @property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[int]]:
        """
        TTL attribute value for the record.
        """
        return pulumi.get(self, "ttl")

    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ttl", value)


class Allocation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allocated_ipv4_addr: Optional[pulumi.Input[str]] = None,
                 allocated_ipv6_addr: Optional[pulumi.Input[str]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 dns_view: Optional[pulumi.Input[str]] = None,
                 enable_dns: Optional[pulumi.Input[bool]] = None,
                 ext_attrs: Optional[pulumi.Input[str]] = None,
                 fqdn: Optional[pulumi.Input[str]] = None,
                 internal_id: Optional[pulumi.Input[str]] = None,
                 ipv4_addr: Optional[pulumi.Input[str]] = None,
                 ipv4_cidr: Optional[pulumi.Input[str]] = None,
                 ipv6_addr: Optional[pulumi.Input[str]] = None,
                 ipv6_cidr: Optional[pulumi.Input[str]] = None,
                 network_view: Optional[pulumi.Input[str]] = None,
                 ttl: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Create a Allocation resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] allocated_ipv4_addr: Value which comes from 'ipv4_addr' (if specified) or from auto-allocation function (using 'ipv4_cidr').
        :param pulumi.Input[str] allocated_ipv6_addr: Value which comes from 'ipv6_addr' (if specified) or from auto-allocation function (using 'ipv6_cidr').
        :param pulumi.Input[str] comment: A description of IP address allocation.
        :param pulumi.Input[str] dns_view: DNS view under which the zone has been created.
        :param pulumi.Input[bool] enable_dns: flag that defines if the host record is to be used for DNS purposes.
        :param pulumi.Input[str] ext_attrs: The extensible attributes for IP address allocation, as a map in JSON format
        :param pulumi.Input[str] fqdn: The host name for Host Record in FQDN format.
        :param pulumi.Input[str] internal_id: Internal ID of an object at NIOS side, used by Infoblox Terraform plugin to search for a NIOS's object which corresponds
               to the Terraform resource.
        :param pulumi.Input[str] ipv4_addr: IPv4 address of cloud instance.Set a valid IP address for static allocation and leave empty if dynamically allocated.
        :param pulumi.Input[str] ipv4_cidr: The IPv4 cidr from which an IPv4 address will be allocated.
        :param pulumi.Input[str] ipv6_addr: IPv6 address of cloud instance.Set a valid IP address for static allocation and leave empty if dynamically allocated.
        :param pulumi.Input[str] ipv6_cidr: The IPv6 cidr from which an IPv6 address will be allocated.
        :param pulumi.Input[str] network_view: network view name on NIOS server.
        :param pulumi.Input[int] ttl: TTL attribute value for the record.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AllocationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Allocation resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param AllocationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AllocationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allocated_ipv4_addr: Optional[pulumi.Input[str]] = None,
                 allocated_ipv6_addr: Optional[pulumi.Input[str]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 dns_view: Optional[pulumi.Input[str]] = None,
                 enable_dns: Optional[pulumi.Input[bool]] = None,
                 ext_attrs: Optional[pulumi.Input[str]] = None,
                 fqdn: Optional[pulumi.Input[str]] = None,
                 internal_id: Optional[pulumi.Input[str]] = None,
                 ipv4_addr: Optional[pulumi.Input[str]] = None,
                 ipv4_cidr: Optional[pulumi.Input[str]] = None,
                 ipv6_addr: Optional[pulumi.Input[str]] = None,
                 ipv6_cidr: Optional[pulumi.Input[str]] = None,
                 network_view: Optional[pulumi.Input[str]] = None,
                 ttl: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AllocationArgs.__new__(AllocationArgs)

            __props__.__dict__["allocated_ipv4_addr"] = allocated_ipv4_addr
            __props__.__dict__["allocated_ipv6_addr"] = allocated_ipv6_addr
            __props__.__dict__["comment"] = comment
            __props__.__dict__["dns_view"] = dns_view
            __props__.__dict__["enable_dns"] = enable_dns
            __props__.__dict__["ext_attrs"] = ext_attrs
            if fqdn is None and not opts.urn:
                raise TypeError("Missing required property 'fqdn'")
            __props__.__dict__["fqdn"] = fqdn
            __props__.__dict__["internal_id"] = internal_id
            __props__.__dict__["ipv4_addr"] = ipv4_addr
            __props__.__dict__["ipv4_cidr"] = ipv4_cidr
            __props__.__dict__["ipv6_addr"] = ipv6_addr
            __props__.__dict__["ipv6_cidr"] = ipv6_cidr
            __props__.__dict__["network_view"] = network_view
            __props__.__dict__["ttl"] = ttl
            __props__.__dict__["ref"] = None
        super(Allocation, __self__).__init__(
            'infoblox:ip/allocation:Allocation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            allocated_ipv4_addr: Optional[pulumi.Input[str]] = None,
            allocated_ipv6_addr: Optional[pulumi.Input[str]] = None,
            comment: Optional[pulumi.Input[str]] = None,
            dns_view: Optional[pulumi.Input[str]] = None,
            enable_dns: Optional[pulumi.Input[bool]] = None,
            ext_attrs: Optional[pulumi.Input[str]] = None,
            fqdn: Optional[pulumi.Input[str]] = None,
            internal_id: Optional[pulumi.Input[str]] = None,
            ipv4_addr: Optional[pulumi.Input[str]] = None,
            ipv4_cidr: Optional[pulumi.Input[str]] = None,
            ipv6_addr: Optional[pulumi.Input[str]] = None,
            ipv6_cidr: Optional[pulumi.Input[str]] = None,
            network_view: Optional[pulumi.Input[str]] = None,
            ref: Optional[pulumi.Input[str]] = None,
            ttl: Optional[pulumi.Input[int]] = None) -> 'Allocation':
        """
        Get an existing Allocation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] allocated_ipv4_addr: Value which comes from 'ipv4_addr' (if specified) or from auto-allocation function (using 'ipv4_cidr').
        :param pulumi.Input[str] allocated_ipv6_addr: Value which comes from 'ipv6_addr' (if specified) or from auto-allocation function (using 'ipv6_cidr').
        :param pulumi.Input[str] comment: A description of IP address allocation.
        :param pulumi.Input[str] dns_view: DNS view under which the zone has been created.
        :param pulumi.Input[bool] enable_dns: flag that defines if the host record is to be used for DNS purposes.
        :param pulumi.Input[str] ext_attrs: The extensible attributes for IP address allocation, as a map in JSON format
        :param pulumi.Input[str] fqdn: The host name for Host Record in FQDN format.
        :param pulumi.Input[str] internal_id: Internal ID of an object at NIOS side, used by Infoblox Terraform plugin to search for a NIOS's object which corresponds
               to the Terraform resource.
        :param pulumi.Input[str] ipv4_addr: IPv4 address of cloud instance.Set a valid IP address for static allocation and leave empty if dynamically allocated.
        :param pulumi.Input[str] ipv4_cidr: The IPv4 cidr from which an IPv4 address will be allocated.
        :param pulumi.Input[str] ipv6_addr: IPv6 address of cloud instance.Set a valid IP address for static allocation and leave empty if dynamically allocated.
        :param pulumi.Input[str] ipv6_cidr: The IPv6 cidr from which an IPv6 address will be allocated.
        :param pulumi.Input[str] network_view: network view name on NIOS server.
        :param pulumi.Input[str] ref: NIOS object's reference, not to be set by a user.
        :param pulumi.Input[int] ttl: TTL attribute value for the record.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AllocationState.__new__(_AllocationState)

        __props__.__dict__["allocated_ipv4_addr"] = allocated_ipv4_addr
        __props__.__dict__["allocated_ipv6_addr"] = allocated_ipv6_addr
        __props__.__dict__["comment"] = comment
        __props__.__dict__["dns_view"] = dns_view
        __props__.__dict__["enable_dns"] = enable_dns
        __props__.__dict__["ext_attrs"] = ext_attrs
        __props__.__dict__["fqdn"] = fqdn
        __props__.__dict__["internal_id"] = internal_id
        __props__.__dict__["ipv4_addr"] = ipv4_addr
        __props__.__dict__["ipv4_cidr"] = ipv4_cidr
        __props__.__dict__["ipv6_addr"] = ipv6_addr
        __props__.__dict__["ipv6_cidr"] = ipv6_cidr
        __props__.__dict__["network_view"] = network_view
        __props__.__dict__["ref"] = ref
        __props__.__dict__["ttl"] = ttl
        return Allocation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allocatedIpv4Addr")
    def allocated_ipv4_addr(self) -> pulumi.Output[str]:
        """
        Value which comes from 'ipv4_addr' (if specified) or from auto-allocation function (using 'ipv4_cidr').
        """
        return pulumi.get(self, "allocated_ipv4_addr")

    @property
    @pulumi.getter(name="allocatedIpv6Addr")
    def allocated_ipv6_addr(self) -> pulumi.Output[str]:
        """
        Value which comes from 'ipv6_addr' (if specified) or from auto-allocation function (using 'ipv6_cidr').
        """
        return pulumi.get(self, "allocated_ipv6_addr")

    @property
    @pulumi.getter
    def comment(self) -> pulumi.Output[Optional[str]]:
        """
        A description of IP address allocation.
        """
        return pulumi.get(self, "comment")

    @property
    @pulumi.getter(name="dnsView")
    def dns_view(self) -> pulumi.Output[Optional[str]]:
        """
        DNS view under which the zone has been created.
        """
        return pulumi.get(self, "dns_view")

    @property
    @pulumi.getter(name="enableDns")
    def enable_dns(self) -> pulumi.Output[Optional[bool]]:
        """
        flag that defines if the host record is to be used for DNS purposes.
        """
        return pulumi.get(self, "enable_dns")

    @property
    @pulumi.getter(name="extAttrs")
    def ext_attrs(self) -> pulumi.Output[Optional[str]]:
        """
        The extensible attributes for IP address allocation, as a map in JSON format
        """
        return pulumi.get(self, "ext_attrs")

    @property
    @pulumi.getter
    def fqdn(self) -> pulumi.Output[str]:
        """
        The host name for Host Record in FQDN format.
        """
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter(name="internalId")
    def internal_id(self) -> pulumi.Output[str]:
        """
        Internal ID of an object at NIOS side, used by Infoblox Terraform plugin to search for a NIOS's object which corresponds
        to the Terraform resource.
        """
        return pulumi.get(self, "internal_id")

    @property
    @pulumi.getter(name="ipv4Addr")
    def ipv4_addr(self) -> pulumi.Output[Optional[str]]:
        """
        IPv4 address of cloud instance.Set a valid IP address for static allocation and leave empty if dynamically allocated.
        """
        return pulumi.get(self, "ipv4_addr")

    @property
    @pulumi.getter(name="ipv4Cidr")
    def ipv4_cidr(self) -> pulumi.Output[Optional[str]]:
        """
        The IPv4 cidr from which an IPv4 address will be allocated.
        """
        return pulumi.get(self, "ipv4_cidr")

    @property
    @pulumi.getter(name="ipv6Addr")
    def ipv6_addr(self) -> pulumi.Output[Optional[str]]:
        """
        IPv6 address of cloud instance.Set a valid IP address for static allocation and leave empty if dynamically allocated.
        """
        return pulumi.get(self, "ipv6_addr")

    @property
    @pulumi.getter(name="ipv6Cidr")
    def ipv6_cidr(self) -> pulumi.Output[Optional[str]]:
        """
        The IPv6 cidr from which an IPv6 address will be allocated.
        """
        return pulumi.get(self, "ipv6_cidr")

    @property
    @pulumi.getter(name="networkView")
    def network_view(self) -> pulumi.Output[Optional[str]]:
        """
        network view name on NIOS server.
        """
        return pulumi.get(self, "network_view")

    @property
    @pulumi.getter
    def ref(self) -> pulumi.Output[str]:
        """
        NIOS object's reference, not to be set by a user.
        """
        return pulumi.get(self, "ref")

    @property
    @pulumi.getter
    def ttl(self) -> pulumi.Output[Optional[int]]:
        """
        TTL attribute value for the record.
        """
        return pulumi.get(self, "ttl")

