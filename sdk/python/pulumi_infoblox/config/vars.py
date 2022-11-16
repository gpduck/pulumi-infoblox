# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

import types

__config__ = pulumi.Config('infoblox')


class _ExportableConfig(types.ModuleType):
    @property
    def connect_timeout(self) -> Optional[int]:
        """
        Maximum wait for connection, in seconds. Zero or not specified means wait indefinitely.
        """
        return __config__.get_int('connectTimeout')

    @property
    def password(self) -> Optional[str]:
        """
        Password to authenticate with Infoblox server.
        """
        return __config__.get('password')

    @property
    def pool_connections(self) -> Optional[int]:
        """
        Maximum number of connections to establish to the Infoblox server. Zero means unlimited.
        """
        return __config__.get_int('poolConnections')

    @property
    def port(self) -> Optional[str]:
        """
        Port number used for connection for Infoblox Server.
        """
        return __config__.get('port')

    @property
    def server(self) -> Optional[str]:
        """
        Infoblox server IP address.
        """
        return __config__.get('server')

    @property
    def sslmode(self) -> Optional[bool]:
        """
        If set, Infoblox client will permit unverifiable SSL certificates.
        """
        return __config__.get_bool('sslmode')

    @property
    def username(self) -> Optional[str]:
        """
        User to authenticate with Infoblox server.
        """
        return __config__.get('username')

    @property
    def wapi_version(self) -> Optional[str]:
        """
        WAPI Version of Infoblox server defaults to v2.7.
        """
        return __config__.get('wapiVersion')
