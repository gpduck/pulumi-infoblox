// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

export class Allocation extends pulumi.CustomResource {
    /**
     * Get an existing Allocation resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AllocationState, opts?: pulumi.CustomResourceOptions): Allocation {
        return new Allocation(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'infoblox:ipv4/allocation:Allocation';

    /**
     * Returns true if the given object is an instance of Allocation.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Allocation {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Allocation.__pulumiType;
    }

    /**
     * The address in cidr format.
     */
    public readonly cidr!: pulumi.Output<string | undefined>;
    /**
     * A description of IP address allocation.
     */
    public readonly comment!: pulumi.Output<string | undefined>;
    /**
     * Dns View under which the zone has been created.
     */
    public readonly dnsView!: pulumi.Output<string | undefined>;
    /**
     * flag that defines if the host record is to be used for DNS Purposes.
     */
    public readonly enableDns!: pulumi.Output<boolean | undefined>;
    /**
     * The extensible attributes for IP address allocation, as a map in JSON format
     */
    public readonly extAttrs!: pulumi.Output<string | undefined>;
    /**
     * The host name for Host Record in FQDN format.
     */
    public readonly fqdn!: pulumi.Output<string>;
    /**
     * IP address of cloud instance.Set a valid IP for static allocation and leave empty if dynamically allocated.
     */
    public readonly ipAddr!: pulumi.Output<string>;
    /**
     * Network view name of NIOS server.
     */
    public readonly networkView!: pulumi.Output<string | undefined>;
    /**
     * TTL attribute value for the record.
     */
    public readonly ttl!: pulumi.Output<number | undefined>;

    /**
     * Create a Allocation resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AllocationArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: AllocationArgs | AllocationState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as AllocationState | undefined;
            resourceInputs["cidr"] = state ? state.cidr : undefined;
            resourceInputs["comment"] = state ? state.comment : undefined;
            resourceInputs["dnsView"] = state ? state.dnsView : undefined;
            resourceInputs["enableDns"] = state ? state.enableDns : undefined;
            resourceInputs["extAttrs"] = state ? state.extAttrs : undefined;
            resourceInputs["fqdn"] = state ? state.fqdn : undefined;
            resourceInputs["ipAddr"] = state ? state.ipAddr : undefined;
            resourceInputs["networkView"] = state ? state.networkView : undefined;
            resourceInputs["ttl"] = state ? state.ttl : undefined;
        } else {
            const args = argsOrState as AllocationArgs | undefined;
            if ((!args || args.fqdn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'fqdn'");
            }
            resourceInputs["cidr"] = args ? args.cidr : undefined;
            resourceInputs["comment"] = args ? args.comment : undefined;
            resourceInputs["dnsView"] = args ? args.dnsView : undefined;
            resourceInputs["enableDns"] = args ? args.enableDns : undefined;
            resourceInputs["extAttrs"] = args ? args.extAttrs : undefined;
            resourceInputs["fqdn"] = args ? args.fqdn : undefined;
            resourceInputs["ipAddr"] = args ? args.ipAddr : undefined;
            resourceInputs["networkView"] = args ? args.networkView : undefined;
            resourceInputs["ttl"] = args ? args.ttl : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Allocation.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Allocation resources.
 */
export interface AllocationState {
    /**
     * The address in cidr format.
     */
    cidr?: pulumi.Input<string>;
    /**
     * A description of IP address allocation.
     */
    comment?: pulumi.Input<string>;
    /**
     * Dns View under which the zone has been created.
     */
    dnsView?: pulumi.Input<string>;
    /**
     * flag that defines if the host record is to be used for DNS Purposes.
     */
    enableDns?: pulumi.Input<boolean>;
    /**
     * The extensible attributes for IP address allocation, as a map in JSON format
     */
    extAttrs?: pulumi.Input<string>;
    /**
     * The host name for Host Record in FQDN format.
     */
    fqdn?: pulumi.Input<string>;
    /**
     * IP address of cloud instance.Set a valid IP for static allocation and leave empty if dynamically allocated.
     */
    ipAddr?: pulumi.Input<string>;
    /**
     * Network view name of NIOS server.
     */
    networkView?: pulumi.Input<string>;
    /**
     * TTL attribute value for the record.
     */
    ttl?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a Allocation resource.
 */
export interface AllocationArgs {
    /**
     * The address in cidr format.
     */
    cidr?: pulumi.Input<string>;
    /**
     * A description of IP address allocation.
     */
    comment?: pulumi.Input<string>;
    /**
     * Dns View under which the zone has been created.
     */
    dnsView?: pulumi.Input<string>;
    /**
     * flag that defines if the host record is to be used for DNS Purposes.
     */
    enableDns?: pulumi.Input<boolean>;
    /**
     * The extensible attributes for IP address allocation, as a map in JSON format
     */
    extAttrs?: pulumi.Input<string>;
    /**
     * The host name for Host Record in FQDN format.
     */
    fqdn: pulumi.Input<string>;
    /**
     * IP address of cloud instance.Set a valid IP for static allocation and leave empty if dynamically allocated.
     */
    ipAddr?: pulumi.Input<string>;
    /**
     * Network view name of NIOS server.
     */
    networkView?: pulumi.Input<string>;
    /**
     * TTL attribute value for the record.
     */
    ttl?: pulumi.Input<number>;
}
