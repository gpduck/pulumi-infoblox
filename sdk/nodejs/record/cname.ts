// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

export class CName extends pulumi.CustomResource {
    /**
     * Get an existing CName resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CNameState, opts?: pulumi.CustomResourceOptions): CName {
        return new CName(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'infoblox:record/cName:CName';

    /**
     * Returns true if the given object is an instance of CName.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is CName {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === CName.__pulumiType;
    }

    /**
     * The alias name in FQDN format.
     */
    public readonly alias!: pulumi.Output<string>;
    /**
     * The Canonical name in FQDN format.
     */
    public readonly canonical!: pulumi.Output<string>;
    /**
     * A description about CNAME record.
     */
    public readonly comment!: pulumi.Output<string | undefined>;
    /**
     * Dns View under which the zone has been created.
     */
    public readonly dnsView!: pulumi.Output<string | undefined>;
    /**
     * The Extensible attributes of CNAME record, as a map in JSON format
     */
    public readonly extAttrs!: pulumi.Output<string | undefined>;
    /**
     * TTL attribute value for the record.
     */
    public readonly ttl!: pulumi.Output<number | undefined>;

    /**
     * Create a CName resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CNameArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: CNameArgs | CNameState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as CNameState | undefined;
            resourceInputs["alias"] = state ? state.alias : undefined;
            resourceInputs["canonical"] = state ? state.canonical : undefined;
            resourceInputs["comment"] = state ? state.comment : undefined;
            resourceInputs["dnsView"] = state ? state.dnsView : undefined;
            resourceInputs["extAttrs"] = state ? state.extAttrs : undefined;
            resourceInputs["ttl"] = state ? state.ttl : undefined;
        } else {
            const args = argsOrState as CNameArgs | undefined;
            if ((!args || args.alias === undefined) && !opts.urn) {
                throw new Error("Missing required property 'alias'");
            }
            if ((!args || args.canonical === undefined) && !opts.urn) {
                throw new Error("Missing required property 'canonical'");
            }
            resourceInputs["alias"] = args ? args.alias : undefined;
            resourceInputs["canonical"] = args ? args.canonical : undefined;
            resourceInputs["comment"] = args ? args.comment : undefined;
            resourceInputs["dnsView"] = args ? args.dnsView : undefined;
            resourceInputs["extAttrs"] = args ? args.extAttrs : undefined;
            resourceInputs["ttl"] = args ? args.ttl : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(CName.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering CName resources.
 */
export interface CNameState {
    /**
     * The alias name in FQDN format.
     */
    alias?: pulumi.Input<string>;
    /**
     * The Canonical name in FQDN format.
     */
    canonical?: pulumi.Input<string>;
    /**
     * A description about CNAME record.
     */
    comment?: pulumi.Input<string>;
    /**
     * Dns View under which the zone has been created.
     */
    dnsView?: pulumi.Input<string>;
    /**
     * The Extensible attributes of CNAME record, as a map in JSON format
     */
    extAttrs?: pulumi.Input<string>;
    /**
     * TTL attribute value for the record.
     */
    ttl?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a CName resource.
 */
export interface CNameArgs {
    /**
     * The alias name in FQDN format.
     */
    alias: pulumi.Input<string>;
    /**
     * The Canonical name in FQDN format.
     */
    canonical: pulumi.Input<string>;
    /**
     * A description about CNAME record.
     */
    comment?: pulumi.Input<string>;
    /**
     * Dns View under which the zone has been created.
     */
    dnsView?: pulumi.Input<string>;
    /**
     * The Extensible attributes of CNAME record, as a map in JSON format
     */
    extAttrs?: pulumi.Input<string>;
    /**
     * TTL attribute value for the record.
     */
    ttl?: pulumi.Input<number>;
}
