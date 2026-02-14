---
published: true
---
# Dependency management

> If I have been able to see further, it was only because I stood on the shoulders of giants.

The power of modern programming languages stems from the possibility to re-use functionality provided by other programmers. With Python they can be installed in form of packages. The more of these packages your project depends on, the more important dependency management becomes.

While there are many different tools (uv, poetry, etc.), I haven't found one that fulfills my requirements:
1. Be able to update the dependencies in my dev environment to their latest versions
2. Pin a dependency to a specific version (if needed)
3. A distribution file (sdist or wheel) should be locked to the dependency versions used at build time

For my personal projects I am using the following setup, based on [pip-tools](https://pypi.org/project/pip-tools/) .

## Preparation

In the project folder, create:
1. A virtual environment (`venv`).
2. A `requirements.in` file with the project dependencies (in the format of a `requirements.txt` file). Do not specify dependency versions in this file, unless you need a specific one.

```
pandas==3.0.0
jupyter
```

3. Feel free to add additional .in files (e.g. `dev-requirements.in` for development-only dependencies).

```
build
pytest
```

4. A `pyproject.toml` file with the following content (you will want to add additional information, like project name and version):

```toml
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"

[project]
dynamic = ["dependencies"]
  
[tool.setuptools.dynamic]
dependencies = { file = ["requirements.txt"] }
```

## Generic

The solution is based on centrally defined PowerShell that can be called for any project. The project-specific settings are defined in an `.env` file in the root folder.

Create a `.env` file in the project folder with the following content:
	1. `VENV_DIR_NAME`: The name of the virtual environment folder (created in step 1 of the Preparation).
	2. `REQUIREMENTS_FILES`: The (comma-separated) names of the .in files (created in step 2 of the Preparation).

```env
VENV_DIR_NAME=venv
REQUIREMENTS_FILES=requirements.in,dev-requirements.in
```

> [!warning] .env syntax restrictions
> For the PowerShell scripts to work, do not add comments (`#`) after the lines specified, or use double quotation marks (`"`) to enclose their string values (use single ones - `'` - instead).

### Update and install dependencies
Save the following PowerShell script as `UpdateDependencies.ps1` in a central location:

```powershell
param(
    [switch]$InstallOnly
)
if (!(Test-Path -Path .env -PathType Leaf)) {
    Write-Host ".env file not found.";
    exit 1;
}
# Get the variables from .env.
$EnvVar = Get-Content .env -Raw | %{$_ -replace '\\', '\\'} | ConvertFrom-StringData;
$InFiles = $EnvVar.REQUIREMENTS_FILES  -split ',';
# Activate the venv.
& ".\$($EnvVar.VENV_DIR_NAME)\Scripts\Activate.ps1";
# Upgrade pip.
python -m pip install --upgrade pip==25.3;
# Upgrade pip-tools.
pip install -U --require-virtualenv pip-tools;
if (!$InstallOnly) {
    # Call pip-compile -U for all *.in files.
    $InFiles | ForEach-Object { pip-compile -U $_ };
}
# Call pip-sync with all .txt versions of the *.in files.
pip-sync @($InFiles | ForEach-Object { $_.replace('.in', '.txt') });
deactivate;
```

The call of `pip-compile` will create (resp. update) .txt versions of all specified .in files. These contain the exact versions of all dependencies - and are therefore used for the build. `pip-sync` installs the dependency versions into the `venv` (resp. removes dependencies that are no longer needed).

To update the dependencies of a project, call the script from the project's root folder.

If you want to install the dependencies from existing .txt files without updating them (e.g. when moving to a new Computer), run the following command:

```shell
.\UpdateDependencies.ps1 -InstallOnly
```

### Build
To build an sdist package run the following PowerShell script:

```shell
venv\scripts\Activate.ps1;
python -m build -s;
deactivate;
```

### Local deployment

You can deploy your package into a local folder to test or run it. To do so, add the `LOCAL_DEPLOYMENT_TARGET` into the `.env` file. In this folder, a `venv` with the package will be created.

```env
LOCAL_DEPLOYMENT_TARGET='C:\Program Files\my-python-program'
```

Save the following PowerShell script as `BuildAndDeployLocal.ps1` in a central location:

```powershell
param(
    [switch]$DeployOnly
)
if (!$DeployOnly) {
	# Build the project.
	venv\scripts\Activate.ps1;
	python -m build -s;
	deactivate;
}
# Get the variables from .env.
$EnvVar = Get-Content .env -Raw | %{$_ -replace '\\', '\\'} | %{$_ -replace "'", ""} | ConvertFrom-StringData;
if (!(Test-Path -Path .env -PathType Leaf)) {
    Write-Host ".env file not found.";
    exit 1;
}
$Target = "$($EnvVar.LOCAL_DEPLOYMENT_TARGET)\venv";
# Get path to python directory, used to create the project's venv.
$PythonPath = Get-Content 'venv\\pyvenv.cfg' | %{$_ -replace '\\', '\\\\'} | %{ConvertFrom-StringData $_} | %{$_.home};
# Get latest distribution file.
$DistFile = Get-ChildItem -Path dist | Sort-Object Name -Descending | Select-Object -First 1 | %{$_.FullName};
Write-Host ('Deploying ', $DistFile.split('\\')[-1]);
# Delete old venv in deploy target.
Remove-Item $Target -Recurse -erroraction silentlycontinue;
# Create venv in deploy target.
Set-Location $PythonPath[0];
.\python.exe -m venv $Target --upgrade-deps;
# Install distribution file.
Set-Location $EnvVar.LOCAL_DEPLOYMENT_TARGET;
venv\scripts\Activate.ps1;
pip install --require-virtualenv $DistFile;
deactivate;
```

To update the dependencies of a project, call the script from the project's root folder.

If you want to deploy an already built distribution file, run the following command:

```shell
.\BuildAndDeployLocal.ps1 -DeployOnly
```

### Integration in PyCharm
The scripts can be added in PyCharm as [run/debug configurations﻿](https://www.jetbrains.com/help/pycharm/run-debug-configuration.html) or [external tools](https://www.jetbrains.com/help/pycharm/configuring-third-party-tools.html). To add e.g. `UpdateDependencies.ps1` as external tool, create a tool with the following settings:

- Program: `powershell.exe`
- Arguments: `"& 'C:\path to script\UpdateDependencies.ps1'"`
- Working directory: `$ProjectFileDir$`

## Visual Studio Code
The functionality for building and locally deploying projects are defined as user tasks while the project-specific properties are defined as workspace settings.
### settings.json
Open `.vscode\settings.json` via: `Ctrl + Shift + P` > Preferences: Open Workspace Settings (JSON). Add the following entries:
- `local_deployment_target`
- `requirements_files`
- `venv_dir_name`

```json
{
    "venv_dir_name": "venv",
    "requirements_files": "requirements.in,dev-requirements.in",
    "local_deployment_target": "C:\\Program Files\\my-python-program",
}
```

### tasks.json
Select: `Ctrl + Shift + P` > Tasks: Open User Tasks. Add the following tasks:

```json
{
    "tasks": [
        {
            "label": "Build",
            "type": "shell",
            "command": [
                "venv\\scripts\\Activate.ps1;",
                "python -m build -s;",
                "deactivate"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "problemMatcher": [],
            "detail": "create dist file for package version"
        },
        {
            "label": "Local deploy",
            "type": "shell",
            "command": [
                // Get path to python directory, used to create the project's venv.
                "$PythonPath = Get-Content 'venv\\pyvenv.cfg' | %{$_ -replace '\\\\', '\\\\\\\\'} | %{ConvertFrom-StringData $_} | %{$_.home};",
                // Get latest distribution file.
                "$DistFile = Get-ChildItem -Path 'dist' | Sort-Object Name -Descending | Select-Object -First 1 | %{$_.FullName};",
                "Write-Host ('Deploying ', $DistFile.split('\\')[-1]);",
                // Delete old venv in deploy target.
                "Remove-Item '${config:local_deployment_target}\\venv' -Recurse -erroraction silentlycontinue;",
                // Create venv in deploy target.
                "Set-Location $PythonPath[0];",
                ".\\python.exe -m venv '${config:local_deployment_target}\\venv' --upgrade-deps;",
                // Install distribution file.
                "Set-Location '${config:local_deployment_target}';",
                "venv\\scripts\\Activate.ps1;",
                "pip install --require-virtualenv $DistFile;",
                "deactivate"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "problemMatcher": [],
            "detail": "re-create venv in deploy target & install latest dist file"
        },
        {
            "label": "Build & Local deploy",
            "dependsOrder": "sequence",
            "command": [
                "Build",
                "Deploy",
                "Deploy (additional files)"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "problemMatcher": []
        },
    ]
}
```

The individual tasks can be called by: `Ctrl + Shift + P` > Tasks: Run Task.

## Why not use uv?

With the popular pakcage manager [uv](https://docs.astral.sh/uv/) it is currently not possible to (easily) lock the build dependencies (see [GitHub issue](https://github.com/astral-sh/uv/issues/5190)).