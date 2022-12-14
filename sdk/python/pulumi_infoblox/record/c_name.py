# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['CNameArgs', 'CName']

@pulumi.input_type
class CNameArgs:
    def __init__(__self__, *,
                 alias: pulumi.Input[str],
                 canonical: pulumi.Input[str],
                 comment: Optional[pulumi.Input[str]] = None,
                 dns_view: Optional[pulumi.Input[str]] = None,
                 ext_attrs: Optional[pulumi.Input[str]] = None,
                 ttl: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a CName resource.
        :param pulumi.Input[str] alias: The alias name in FQDN format.
        :param pulumi.Input[str] canonical: The Canonical name in FQDN format.
        :param pulumi.Input[str] comment: A description about CNAME record.
        :param pulumi.Input[str] dns_view: Dns View under which the zone has been created.
        :param pulumi.Input[str] ext_attrs: The Extensible attributes of CNAME record, as a map in JSON format
        :param pulumi.Input[int] ttl: TTL attribute value for the record.
        """
        pulumi.set(__self__, "alias", alias)
        pulumi.set(__self__, "canonical", canonical)
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if dns_view is not None:
            pulumi.set(__self__, "dns_view", dns_view)
        if ext_attrs is not None:
            pulumi.set(__self__, "ext_attrs", ext_attrs)
        if ttl is not None:
            pulumi.set(__self__, "ttl", ttl)

    @property
    @pulumi.getter
    def alias(self) -> pulumi.Input[str]:
        """
        The alias name in FQDN format.
        """
        return pulumi.get(self, "alias")

    @alias.setter
    def alias(self, value: pulumi.Input[str]):
        pulumi.set(self, "alias", value)

    @property
    @pulumi.getter
    def canonical(self) -> pulumi.Input[str]:
        """
        The Canonical name in FQDN format.
        """
        return pulumi.get(self, "canonical")

    @canonical.setter
    def canonical(self, value: pulumi.Input[str]):
        pulumi.set(self, "canonical", value)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        """
        A description about CNAME record.
        """
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter(name="dnsView")
    def dns_view(self) -> Optional[pulumi.Input[str]]:
        """
        Dns View under which the zone has been created.
        """
        return pulumi.get(self, "dns_view")

    @dns_view.setter
    def dns_view(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dns_view", value)

    @property
    @pulumi.getter(name="extAttrs")
    def ext_attrs(self) -> Optional[pulumi.Input[str]]:
        """
        The Extensible attributes of CNAME record, as a map in JSON format
        """
        return pulumi.get(self, "ext_attrs")

    @ext_attrs.setter
    def ext_attrs(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ext_attrs", value)

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
class _CNameState:
    def __init__(__self__, *,
                 alias: Optional[pulumi.Input[str]] = None,
                 canonical: Optional[pulumi.Input[str]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 dns_view: Optional[pulumi.Input[str]] = None,
                 ext_attrs: Optional[pulumi.Input[str]] = None,
                 ttl: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering CName resources.
        :param pulumi.Input[str] alias: The alias name in FQDN format.
        :param pulumi.Input[str] canonical: The Canonical name in FQDN format.
        :param pulumi.Input[str] comment: A description about CNAME record.
        :param pulumi.Input[str] dns_view: Dns View under which the zone has been created.
        :param pulumi.Input[str] ext_attrs: The Extensible attributes of CNAME record, as a map in JSON format
        :param pulumi.Input[int] ttl: TTL attribute value for the record.
        """
        if alias is not None:
            pulumi.set(__self__, "alias", alias)
        if canonical is not None:
            pulumi.set(__self__, "canonical", canonical)
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if dns_view is not None:
            pulumi.set(__self__, "dns_view", dns_view)
        if ext_attrs is not None:
            pulumi.set(__self__, "ext_attrs", ext_attrs)
        if ttl is not None:
            pulumi.set(__self__, "ttl", ttl)

    @property
    @pulumi.getter
    def alias(self) -> Optional[pulumi.Input[str]]:
        """
        The alias name in FQDN format.
        """
        return pulumi.get(self, "alias")

    @alias.setter
    def alias(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alias", value)

    @property
    @pulumi.getter
    def canonical(self) -> Optional[pulumi.Input[str]]:
        """
        The Canonical name in FQDN format.
        """
        return pulumi.get(self, "canonical")

    @canonical.setter
    def canonical(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "canonical", value)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        """
        A description about CNAME record.
        """
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter(name="dnsView")
    def dns_view(self) -> Optional[pulumi.Input[str]]:
        """
        Dns View under which the zone has been created.
        """
        return pulumi.get(self, "dns_view")

    @dns_view.setter
    def dns_view(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dns_view", value)

    @property
    @pulumi.getter(name="extAttrs")
    def ext_attrs(self) -> Optional[pulumi.Input[str]]:
        """
        The Extensible attributes of CNAME record, as a map in JSON format
        """
        return pulumi.get(self, "ext_attrs")

    @ext_attrs.setter
    def ext_attrs(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ext_attrs", value)

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


class CName(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alias: Optional[pulumi.Input[str]] = None,
                 canonical: Optional[pulumi.Input[str]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 dns_view: Optional[pulumi.Input[str]] = None,
                 ext_attrs: Optional[pulumi.Input[str]] = None,
                 ttl: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Create a CName resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] alias: The alias name in FQDN format.
        :param pulumi.Input[str] canonical: The Canonical name in FQDN format.
        :param pulumi.Input[str] comment: A description about CNAME record.
        :param pulumi.Input[str] dns_view: Dns View under which the zone has been created.
        :param pulumi.Input[str] ext_attrs: The Extensible attributes of CNAME record, as a map in JSON format
        :param pulumi.Input[int] ttl: TTL attribute value for the record.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CNameArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a CName resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param CNameArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CNameArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alias: Optional[pulumi.Input[str]] = None,
                 canonical: Optional[pulumi.Input[str]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 dns_view: Optional[pulumi.Input[str]] = None,
                 ext_attrs: Optional[pulumi.Input[str]] = None,
                 ttl: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CNameArgs.__new__(CNameArgs)

            if alias is None and not opts.urn:
                raise TypeError("Missing required property 'alias'")
            __props__.__dict__["alias"] = alias
            if canonical is None and not opts.urn:
                raise TypeError("Missing required property 'canonical'")
            __props__.__dict__["canonical"] = canonical
            __props__.__dict__["comment"] = comment
            __props__.__dict__["dns_view"] = dns_view
            __props__.__dict__["ext_attrs"] = ext_attrs
            __props__.__dict__["ttl"] = ttl
        super(CName, __self__).__init__(
            'infoblox:record/cName:CName',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            alias: Optional[pulumi.Input[str]] = None,
            canonical: Optional[pulumi.Input[str]] = None,
            comment: Optional[pulumi.Input[str]] = None,
            dns_view: Optional[pulumi.Input[str]] = None,
            ext_attrs: Optional[pulumi.Input[str]] = None,
            ttl: Optional[pulumi.Input[int]] = None) -> 'CName':
        """
        Get an existing CName resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] alias: The alias name in FQDN format.
        :param pulumi.Input[str] canonical: The Canonical name in FQDN format.
        :param pulumi.Input[str] comment: A description about CNAME record.
        :param pulumi.Input[str] dns_view: Dns View under which the zone has been created.
        :param pulumi.Input[str] ext_attrs: The Extensible attributes of CNAME record, as a map in JSON format
        :param pulumi.Input[int] ttl: TTL attribute value for the record.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CNameState.__new__(_CNameState)

        __props__.__dict__["alias"] = alias
        __props__.__dict__["canonical"] = canonical
        __props__.__dict__["comment"] = comment
        __props__.__dict__["dns_view"] = dns_view
        __props__.__dict__["ext_attrs"] = ext_attrs
        __props__.__dict__["ttl"] = ttl
        return CName(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def alias(self) -> pulumi.Output[str]:
        """
        The alias name in FQDN format.
        """
        return pulumi.get(self, "alias")

    @property
    @pulumi.getter
    def canonical(self) -> pulumi.Output[str]:
        """
        The Canonical name in FQDN format.
        """
        return pulumi.get(self, "canonical")

    @property
    @pulumi.getter
    def comment(self) -> pulumi.Output[Optional[str]]:
        """
        A description about CNAME record.
        """
        return pulumi.get(self, "comment")

    @property
    @pulumi.getter(name="dnsView")
    def dns_view(self) -> pulumi.Output[Optional[str]]:
        """
        Dns View under which the zone has been created.
        """
        return pulumi.get(self, "dns_view")

    @property
    @pulumi.getter(name="extAttrs")
    def ext_attrs(self) -> pulumi.Output[Optional[str]]:
        """
        The Extensible attributes of CNAME record, as a map in JSON format
        """
        return pulumi.get(self, "ext_attrs")

    @property
    @pulumi.getter
    def ttl(self) -> pulumi.Output[Optional[int]]:
        """
        TTL attribute value for the record.
        """
        return pulumi.get(self, "ttl")

