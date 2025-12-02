---
published: true
---
# Tips and tricks
Apex code snippets that provide helpful functionality.

## Picklist entry: Label to API name
Get the API name of a picklist entry by querying its label. If you are using the [Translation Workbench](https://help.salesforce.com/s/articleView?id=platform.workbench.htm&language=en_US&type=5) to set the label, keep in mind that it will depend on the users language settings.

```java
public static String picklistValue(String objectName, String fieldName, String label) {
    // Get the object's schema and field
    Schema.SObjectType sObjectType = Schema.getGlobalDescribe().get(objectName);
    Schema.DescribeSObjectResult describeRes = sObjectType.getDescribe();
    Schema.SObjectField sObjectField = describeRes.fields.getMap().get(fieldName);
    
    // Get picklist values for the field
    Schema.DescribeFieldResult fieldDescribe = sObjectField.getDescribe();
    List<Schema.PicklistEntry> picklistValues = fieldDescribe.getPicklistValues();

    // Iterate through picklist values and match the label
    for (Schema.PicklistEntry entry : picklistValues) {
        if (entry.getLabel() == label) {
            return entry.getValue();
        }
    }
    
    return null;
}
```

To get the ID of the entry "Automotive" in `Account.Industry` run:

```java
String industryId = picklistValue('Account', 'Industry', 'Automotive');
```

For more options (including a Flow-only implementations), check [medium.com](https://medium.com/metadata-wizard/how-to-get-picklist-labels-in-salesforce-flow-f0b79fed6266).

## Record Type ID
To obtain the ID of a record type (by its developer name) without using a SOQL query (governor limits!), you can use the following command ([source](https://trailhead.salesforce.com/trailblazer-community/feed/0D54V00007T4EIeSAN)):

```java
Id prospectRt = SObjectType.Account.getRecordTypeInfosByDeveloperName().get('End_Customer').getRecordTypeId();
```

If you are trying to query a record type that does not exist (on the specified object) you will receive the error: `static can only be used on fields of a top level type`.

## Test setup: Create records and setup entries
When trying to create records (e.g. Accounts, Opportunities) and "setup entries" (e.g. Users, Custom Settings) in the `@testSetup` method, you will encounter the `MIXED_DML_OPERATION` error. The reason is, that it is not allowed to alter records of these two types in the same transaction. More details can be found on [developer.salesforce.com](https://developer.salesforce.com/docs/atlas.en-us.198.0.apexcode.meta/apexcode/apex_dml_non_mix_sobjects.htm).

To fix this, use the following code ([source](https://salesforce.stackexchange.com/a/211718)):

```java
@testSetup
static void setupTestData() {
    System.runAs(new User(Id = UserInfo.getUserId())) {
        // Create your setup entries here.
    }
    // Create your records here.
}
```
