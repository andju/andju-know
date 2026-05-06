---
published: true
---
# package.xml file
The individual type-entries are described at [developer.salesforce.com](https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_types_list.htm).

Tools that will help you generate the package.xml file for a specific Org:

- [Visual Studio Code extension](https://marketplace.visualstudio.com/items?itemName=VignaeshRamA.sfdx-package-xml-generator)
- [Salesforce package.xml Builder](https://packagebuilder.herokuapp.com/)
- Salesforce CLI command ([asagarwal.com](https://www.asagarwal.com/generate-package-xml-for-your-salesforce-org-with-a-single-command/)): `sf project generate manifest --from-org $salesforce_org_alias`

Examples of generic package.xml files:

- [asagarwal](https://github.com/asagarwal/salesforce-package-xml/blob/main/package-all-metadata-v53.xml)
- [iamsonal](https://gist.github.com/iamsonal/1f4a97d9bdec14248613e8675ccf5981)
- [Jayakrishna Ganjikunta](https://jayakrishnasfdc.wordpress.com/2020/12/25/salesforce-metadata-xml-file-retrieve-deploy-components/)
- [Salesforce Diaries](https://salesforcediaries.com/2019/09/09/xml-package-to-retrieve-metadata-from-org/)

> [!caution] Large package.xml files
> The Metadata API [limits](https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_metadata.htm) the retrieve-result to 10 000 files and 600 MB (or 39 MB if downloaded as zip-file).
