---
published: true
---
# Standard tasks
Snippets that will execute and monitor standard (recurring) tasks.

## Run Apex Tests
CLI command to run the test classes `Class1_Test` and `Class2_Test` (including code coverage):

```shell
sf apex run test --class-names Class1_Test --class-names Class2_Test --code-coverage
```

SOQL query (on [ApexTestRunResult](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_apextestrunresult.htm)) to monitor the progress (use Id returned in previous step):

```sql
SELECT Id, ClassesEnqueued, ClassesCompleted, MethodsCompleted, MethodsFailed, EndTime, Status FROM ApexTestRunResult WHERE AsyncApexJobId = ''
```

## Run Batch Apex
Anonymous Apex to run the (batchable) class `BatchableApexClass` with a batch size of 200:

```java
Id batchJobId = Database.executeBatch(new BatchableApexClass(), 200);
System.debug(batchJobId);
```

SOQL query (on [AsyncApexJob](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_asyncapexjob.htm)) to monitor the progress (use Id returned in previous step):

```sql
SELECT Status, TotalJobItems, JobItemsProcessed, NumberOfErrors, ExtendedStatus FROM AsyncApexJob WHERE Id = ''
```
