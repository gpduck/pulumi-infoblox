// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

export class AAAA extends pulumi.CustomResource {
    /**
     * Get an existing AAAA resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AAAAState, opts?: pulumi.CustomResourceOptions): AAAA {
        return new AAAA(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'infoblox:record/aAAA:AAAA';

    /**
     * Returns true if the given object is an instance of AAAA.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AAAA {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AAAA.__pulumiType;
    }

    /**
     * The network address in cidr format under which record has to be created.
     */
    public readonly cidr!: pulumi.Output<string | undefined>;
    /**
     * A description about AAAA record.
     */
    public readonly comment!: pulumi.Output<string | undefined>;
    /**
     * Dns View under which the zone has been created.
     */
    public readonly dnsView!: pulumi.Output<string | undefined>;
    /**
     * The Extensible attributes of AAAA record to be added/updated, as a map in JSON format
     */
    public readonly extAttrs!: pulumi.Output<string | undefined>;
    /**
     * The name of the AAAA record in FQDN format.
     */
    public readonly fqdn!: pulumi.Output<string>;
    /**
     * IPv6 address for record creation. Set the field with valid IP for static allocation. If to be dynamically allocated set
     * cidr field
     */
    public readonly ipv6Addr!: pulumi.Output<string>;
    /**
     * Network view name of NIOS server.
     */
    public readonly networkView!: pulumi.Output<string>;
    /**
     * TTL attribute value for the record.
     */
    public readonly ttl!: pulumi.Output<number | undefined>;

    /**
     * Create a AAAA resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AAAAArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: AAAAArgs | AAAAState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as AAAAState | undefined;
            resourceInputs["cidr"] = state ? state.cidr : undefined;
            resourceInputs["comment"] = state ? state.comment : undefined;
            resourceInputs["dnsView"] = state ? state.dnsView : undefined;
            resourceInputs["extAttrs"] = state ? state.extAttrs : undefined;
            resourceInputs["fqdn"] = state ? state.fqdn : undefined;
            resourceInputs["ipv6Addr"] = state ? state.ipv6Addr : undefined;
            resourceInputs["networkView"] = state ? state.networkView : undefined;
            resourceInputs["ttl"] = state ? state.ttl : undefined;
        } else {
            const args = argsOrState as AAAAArgs | undefined;
            if ((!args || args.fqdn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'fqdn'");
            }
            resourceInputs["cidr"] = args ? args.cidr : undefined;
            resourceInputs["comment"] = args ? args.comment : undefined;
            resourceInputs["dnsView"] = args ? args.dnsView : undefined;
            resourceInputs["extAttrs"] = args ? args.extAttrs : undefined;
            resourceInputs["fqdn"] = args ? args.fqdn : undefined;
            resourceInputs["ipv6Addr"] = args ? args.ipv6Addr : undefined;
            resourceInputs["networkView"] = args ? args.networkView : undefined;
            resourceInputs["ttl"] = args ? args.ttl : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(AAAA.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering AAAA resources.
 */
export interface AAAAState {
    /**
     * The network address in cidr format under which record has to be created.
     */
    cidr?: pulumi.Input<string>;
    /**
     * A description about AAAA record.
     */
    comment?: pulumi.Input<string>;
    /**
     * Dns View under which the zone has been created.
     */
    dnsView?: pulumi.Input<string>;
    /**
     * The Extensible attributes of AAAA record to be added/updated, as a map in JSON format
     */
    extAttrs?: pulumi.Input<string>;
    /**
     * The name of the AAAA record in FQDN format.
     */
    fqdn?: pulumi.Input<string>;
    /**
     * IPv6 address for record creation. Set the field with valid IP for static allocation. If to be dynamically allocated set
     * cidr field
     */
    ipv6Addr?: pulumi.Input<string>;
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
 * The set of arguments for constructing a AAAA resource.
 */
export interface AAAAArgs {
    /**
     * The network address in cidr format under which record has to be created.
     */
    cidr?: pulumi.Input<string>;
    /**
     * A description about AAAA record.
     */
    comment?: pulumi.Input<string>;
    /**
     * Dns View under which the zone has been created.
     */
    dnsView?: pulumi.Input<string>;
    /**
     * The Extensible attributes of AAAA record to be added/updated, as a map in JSON format
     */
    extAttrs?: pulumi.Input<string>;
    /**
     * The name of the AAAA record in FQDN format.
     */
    fqdn: pulumi.Input<string>;
    /**
     * IPv6 address for record creation. Set the field with valid IP for static allocation. If to be dynamically allocated set
     * cidr field
     */
    ipv6Addr?: pulumi.Input<string>;
    /**
     * Network view name of NIOS server.
     */
    networkView?: pulumi.Input<string>;
    /**
     * TTL attribute value for the record.
     */
    ttl?: pulumi.Input<number>;
}
