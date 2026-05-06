---
published: true
---
# Metadata dependencies
In some cases the content of the retrieved files depends on, which other metadata types were retrieved.

## Profiles
If a package.xml file includes only the type Profiles, it won't download the complete profile files: Sections like `pageAccesses`, `fieldPermissions` and `tabVisibilities` will be missing. In order for these to be included, additional metadata needs to be downloaded.

The following package.xml file will download the most important profile information (based on [asagarwal](https://github.com/asagarwal/salesforce-package-xml/blob/main/package-all-metadata-v53.xml)):

```xml
<?xml version=1.0 encoding=UTF-8 standalone=yes?>
<Package xmlns=http://soap.sforce.com/2006/04/metadata>
    <types>
        <members>*</members>
        <name>ApexClass</name>
    </types>
    <types>
        <members>*</members>
        <name>ApexPage</name>
    </types>
    <types>
        <members>*</members>
        <name>CustomApplication</name>
    </types>
    <types>
	    <!-- Wildcard works, despite documentation. -->
        <members>*</members>
        <name>CustomField</name>
    </types>
    <types>
        <members>*</members>
        <name>CustomMetadata</name>
    </types>
	<types>
		<members>*</members>
		<!-- Standard objects need to be named. -->
		<members>Account</members>
		<members>Asset</members>
		<members>Campaign</members>
		<members>CampaignMember</members>
		<members>Case</members>
		<members>Contact</members>
		<members>Event</members>
		<members>Lead</members>
		<members>Opportunity</members>
		<members>Task</members>
		<name>CustomObject</name>
	</types>
    <types>
        <members>*</members>
        <name>CustomTab</name>
    </types>
    <types>
        <members>*</members>
        <name>DataCategoryGroup</name>
    </types>
    <types>
        <members>*</members>
        <name>ExternalDataSource</name>
    </types>
    <types>
        <members>*</members>
        <name>FlexiPage</name>
    </types>
    <types>
        <members>*</members>
        <name>Flow</name>
    </types>
    <types>
        <members>*</members>
        <name>Layout</name>
    </types>
    <types>
        <members>*</members>
        <name>Profile</name>
    </types>
    <types>
        <members>*</members>
        <name>ProfilePasswordPolicy</name>
    </types>
    <types>
        <members>*</members>
        <name>ProfileSessionSetting</name>
    </types>
    <types>
        <members>*</members>
        <name>RecordType</name>
    </types>
    <version>66.0</version>
</Package>
```

## Lightning Email Templates
If your Lightning Email Templates include pictures stored in "Setup > Feature Settings > Salesforce Files > Salesforce Files", the respective URLs (in `img src`) will be replaced with `{[devName:asset_name]}`. This only works if `ContentAsset` is included in the package.xml file. Otherwise the `img src` will be empty.

```xml
<?xml version=1.0 encoding=UTF-8 standalone=yes?>
<Package xmlns=http://soap.sforce.com/2006/04/metadata>
    <types>
        <members>*</members>
        <name>ContentAsset</name>
    </types>
    <types>
        <members>unfiled$public/Newsletter</members>
        <name>EmailTemplate</name>
    </types>
    <version>66.0</version>
</Package>
```