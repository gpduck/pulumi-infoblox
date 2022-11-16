# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['AssociationArgs', 'Association']

@pulumi.input_type
class AssociationArgs:
    def __init__(__self__, *,
                 duid: Optional[pulumi.Input[str]] = None,
                 enable_dhcp: Optional[pulumi.Input[bool]] = None,
                 internal_id: Optional[pulumi.Input[str]] = None,
                 mac_addr: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Association resource.
        :param pulumi.Input[str] duid: DHCP unique identifier for IPv6.
        :param pulumi.Input[bool] enable_dhcp: The flag which defines if the host record is to be used for IPAM purposes.
        :param pulumi.Input[str] internal_id: This value must point to the ID of the appropriate allocation resource. Required on resource creation.
        :param pulumi.Input[str] mac_addr: MAC address of a cloud instance.
        """
        if duid is not None:
            pulumi.set(__self__, "duid", duid)
        if enable_dhcp is not None:
            pulumi.set(__self__, "enable_dhcp", enable_dhcp)
        if internal_id is not None:
            pulumi.set(__self__, "internal_id", internal_id)
        if mac_addr is not None:
            pulumi.set(__self__, "mac_addr", mac_addr)

    @property
    @pulumi.getter
    def duid(self) -> Optional[pulumi.Input[str]]:
        """
        DHCP unique identifier for IPv6.
        """
        return pulumi.get(self, "duid")

    @duid.setter
    def duid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "duid", value)

    @property
    @pulumi.getter(name="enableDhcp")
    def enable_dhcp(self) -> Optional[pulumi.Input[bool]]:
        """
        The flag which defines if the host record is to be used for IPAM purposes.
        """
        return pulumi.get(self, "enable_dhcp")

    @enable_dhcp.setter
    def enable_dhcp(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_dhcp", value)

    @property
    @pulumi.getter(name="internalId")
    def internal_id(self) -> Optional[pulumi.Input[str]]:
        """
        This value must point to the ID of the appropriate allocation resource. Required on resource creation.
        """
        return pulumi.get(self, "internal_id")

    @internal_id.setter
    def internal_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "internal_id", value)

    @property
    @pulumi.getter(name="macAddr")
    def mac_addr(self) -> Optional[pulumi.Input[str]]:
        """
        MAC address of a cloud instance.
        """
        return pulumi.get(self, "mac_addr")

    @mac_addr.setter
    def mac_addr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mac_addr", value)


@pulumi.input_type
class _AssociationState:
    def __init__(__self__, *,
                 duid: Optional[pulumi.Input[str]] = None,
                 enable_dhcp: Optional[pulumi.Input[bool]] = None,
                 internal_id: Optional[pulumi.Input[str]] = None,
                 mac_addr: Optional[pulumi.Input[str]] = None,
                 ref: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Association resources.
        :param pulumi.Input[str] duid: DHCP unique identifier for IPv6.
        :param pulumi.Input[bool] enable_dhcp: The flag which defines if the host record is to be used for IPAM purposes.
        :param pulumi.Input[str] internal_id: This value must point to the ID of the appropriate allocation resource. Required on resource creation.
        :param pulumi.Input[str] mac_addr: MAC address of a cloud instance.
        :param pulumi.Input[str] ref: NIOS object's reference, not to be set by a user.
        """
        if duid is not None:
            pulumi.set(__self__, "duid", duid)
        if enable_dhcp is not None:
            pulumi.set(__self__, "enable_dhcp", enable_dhcp)
        if internal_id is not None:
            pulumi.set(__self__, "internal_id", internal_id)
        if mac_addr is not None:
            pulumi.set(__self__, "mac_addr", mac_addr)
        if ref is not None:
            pulumi.set(__self__, "ref", ref)

    @property
    @pulumi.getter
    def duid(self) -> Optional[pulumi.Input[str]]:
        """
        DHCP unique identifier for IPv6.
        """
        return pulumi.get(self, "duid")

    @duid.setter
    def duid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "duid", value)

    @property
    @pulumi.getter(name="enableDhcp")
    def enable_dhcp(self) -> Optional[pulumi.Input[bool]]:
        """
        The flag which defines if the host record is to be used for IPAM purposes.
        """
        return pulumi.get(self, "enable_dhcp")

    @enable_dhcp.setter
    def enable_dhcp(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_dhcp", value)

    @property
    @pulumi.getter(name="internalId")
    def internal_id(self) -> Optional[pulumi.Input[str]]:
        """
        This value must point to the ID of the appropriate allocation resource. Required on resource creation.
        """
        return pulumi.get(self, "internal_id")

    @internal_id.setter
    def internal_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "internal_id", value)

    @property
    @pulumi.getter(name="macAddr")
    def mac_addr(self) -> Optional[pulumi.Input[str]]:
        """
        MAC address of a cloud instance.
        """
        return pulumi.get(self, "mac_addr")

    @mac_addr.setter
    def mac_addr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mac_addr", value)

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


class Association(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 duid: Optional[pulumi.Input[str]] = None,
                 enable_dhcp: Optional[pulumi.Input[bool]] = None,
                 internal_id: Optional[pulumi.Input[str]] = None,
                 mac_addr: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Association resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] duid: DHCP unique identifier for IPv6.
        :param pulumi.Input[bool] enable_dhcp: The flag which defines if the host record is to be used for IPAM purposes.
        :param pulumi.Input[str] internal_id: This value must point to the ID of the appropriate allocation resource. Required on resource creation.
        :param pulumi.Input[str] mac_addr: MAC address of a cloud instance.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[AssociationArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Association resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param AssociationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AssociationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 duid: Optional[pulumi.Input[str]] = None,
                 enable_dhcp: Optional[pulumi.Input[bool]] = None,
                 internal_id: Optional[pulumi.Input[str]] = None,
                 mac_addr: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AssociationArgs.__new__(AssociationArgs)

            __props__.__dict__["duid"] = duid
            __props__.__dict__["enable_dhcp"] = enable_dhcp
            __props__.__dict__["internal_id"] = internal_id
            __props__.__dict__["mac_addr"] = mac_addr
            __props__.__dict__["ref"] = None
        super(Association, __self__).__init__(
            'infoblox:ip/association:Association',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            duid: Optional[pulumi.Input[str]] = None,
            enable_dhcp: Optional[pulumi.Input[bool]] = None,
            internal_id: Optional[pulumi.Input[str]] = None,
            mac_addr: Optional[pulumi.Input[str]] = None,
            ref: Optional[pulumi.Input[str]] = None) -> 'Association':
        """
        Get an existing Association resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] duid: DHCP unique identifier for IPv6.
        :param pulumi.Input[bool] enable_dhcp: The flag which defines if the host record is to be used for IPAM purposes.
        :param pulumi.Input[str] internal_id: This value must point to the ID of the appropriate allocation resource. Required on resource creation.
        :param pulumi.Input[str] mac_addr: MAC address of a cloud instance.
        :param pulumi.Input[str] ref: NIOS object's reference, not to be set by a user.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AssociationState.__new__(_AssociationState)

        __props__.__dict__["duid"] = duid
        __props__.__dict__["enable_dhcp"] = enable_dhcp
        __props__.__dict__["internal_id"] = internal_id
        __props__.__dict__["mac_addr"] = mac_addr
        __props__.__dict__["ref"] = ref
        return Association(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def duid(self) -> pulumi.Output[Optional[str]]:
        """
        DHCP unique identifier for IPv6.
        """
        return pulumi.get(self, "duid")

    @property
    @pulumi.getter(name="enableDhcp")
    def enable_dhcp(self) -> pulumi.Output[Optional[bool]]:
        """
        The flag which defines if the host record is to be used for IPAM purposes.
        """
        return pulumi.get(self, "enable_dhcp")

    @property
    @pulumi.getter(name="internalId")
    def internal_id(self) -> pulumi.Output[Optional[str]]:
        """
        This value must point to the ID of the appropriate allocation resource. Required on resource creation.
        """
        return pulumi.get(self, "internal_id")

    @property
    @pulumi.getter(name="macAddr")
    def mac_addr(self) -> pulumi.Output[Optional[str]]:
        """
        MAC address of a cloud instance.
        """
        return pulumi.get(self, "mac_addr")

    @property
    @pulumi.getter
    def ref(self) -> pulumi.Output[str]:
        """
        NIOS object's reference, not to be set by a user.
        """
        return pulumi.get(self, "ref")
