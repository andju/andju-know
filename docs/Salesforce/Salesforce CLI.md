---
published: true
---
# Command Line Interface (CLI)
## package.xml file
Generate the package.xml file for a specific Org:

- [Visual Studio Code extension](https://marketplace.visualstudio.com/items?itemName=VignaeshRamA.sfdx-package-xml-generator)
- [Salesforce package.xml Builder](https://packagebuilder.herokuapp.com/)
- Salesforce CLI command ([asagarwal.com](https://www.asagarwal.com/generate-package-xml-for-your-salesforce-org-with-a-single-command/)): `sf project generate manifest --from-org <salesforce-org-alias>`

Generic package.xml files:

- [asagarwal](https://github.com/asagarwal/salesforce-package-xml/blob/main/package-all-metadata-v53.xml)
- [iamsonal](https://gist.github.com/iamsonal/1f4a97d9bdec14248613e8675ccf5981)
- [Jayakrishna Ganjikunta](https://jayakrishnasfdc.wordpress.com/2020/12/25/salesforce-metadata-xml-file-retrieve-deploy-components/)
- [Salesforce Diaries](https://salesforcediaries.com/2019/09/09/xml-package-to-retrieve-metadata-from-org/)


> [!caution] Extensive package.xml files
> The number of files in the retrieve-result is limited to 10 000.

## Profiles
If a package.xml file includes only the type Profiles, it won't download the complete profile files: Sections like `pageAccesses`, `fieldPermissions` and `tabVisibilities` will be missing. In order for these to be included, additional metadata needs to be downloaded.

The following package.xml file will download the most important profile information ([source](https://github.com/asagarwal/salesforce-package-xml/blob/main/package-all-metadata-v53.xml)):
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
        <members>*</members>
        <name>CustomField</name>
    </types>
    <types>
        <members>*</members>
        <name>CustomMetadata</name>
    </types>
	<types>
		<members>*</members>
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
    <version>64.0</version>
</Package>
```