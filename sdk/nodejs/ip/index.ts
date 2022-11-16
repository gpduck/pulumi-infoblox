// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./allocation";
export * from "./association";

// Import resources to register:
import { Allocation } from "./allocation";
import { Association } from "./association";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "infoblox:ip/allocation:Allocation":
                return new Allocation(name, <any>undefined, { urn })
            case "infoblox:ip/association:Association":
                return new Association(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("infoblox", "ip/allocation", _module)
pulumi.runtime.registerResourceModule("infoblox", "ip/association", _module)