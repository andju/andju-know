---
published: true
---
# Tips and tricks

## Literal value variables for database references
When you are adding a database reference (e.g. for the database OtherDB in the same solution) to your project, its database variable becomes `$(OtherDB)`. You can use it like `SELECT * FROM [$(OtherDB)].[dbo].[tblA]`.

If you want to use the reference without the special characters (`SELECT * FROM [OtherDB].[dbo].[tblA]`), open the `<Projectname>.sqlproj` file in a text editor and search for `<DatabaseSqlCmdVariable>OtherDB</DatabaseSqlCmdVariable>` and replace it by `<DatabaseVariableLiteralValue>OtherDB</DatabaseVariableLiteralValue>`.