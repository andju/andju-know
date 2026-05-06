---
published: true
---
# Changes since a git commit
If you need to (re-)deploy all changes since a specific git commit (e.g. in case of a sandbox refresh), you can get a list of files changed with the following command:

```shell
git  --no-pager diff --name-status $commit_hash HEAD -- force-app/main/default/
```

To copy the added and modified files into a separate folder, using Git Bash:

```shell
git  --diff-filter=AM --name-only $commit_hash HEAD -- force-app/main/default/ | xargs -I {} cp --parents -f {} /c/new/project/path
```

> [!tip] Copy path's to Git Bash
> If you drag-and-drop a folder from the Windows Explorer into Git Bash, you get the correct (Unix-style) folder name.

Alternatively, the CLI plugin [SFDX-Git-Delta](https://github.com/scolladon/sfdx-git-delta "https://github.com/scolladon/sfdx-git-delta") will generate a ready-to-deploy package.xml (and destructiveChanges.xml) file:

```shell
sf sgd source delta --to "HEAD" --from "$commit_hash" --output-dir "."
```
