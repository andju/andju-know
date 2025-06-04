---
published: true
---
# Windows

## Access folder in Windows Sandbox
The [Windows Sandbox](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/) feature provides a convenient way of isolating and testing (suspicious) software. To make a host folder available in the sandbox, run a file with the following content and the extension `.wsb`:
```xml
<Configuration>
  <MappedFolders>
    <MappedFolder>
      <HostFolder>C:\temp</HostFolder>
      <ReadOnly>true</ReadOnly>
    </MappedFolder>
  </MappedFolders>
</Configuration>
```