---
published: true
---
# Container engine on Windows
Some software discussed requires a container engine (and WSL2). I recommend either [Docker](https://docs.docker.com/desktop/setup/install/windows-install/) or [Podman](https://developers.redhat.com/articles/2023/09/27/how-install-and-use-podman-desktop-windows).

Since I am using Podman, all commands my examples will start with `podman`. If you are using Docker, just replace this command with `docker` - the rest should work the same.

## Shrink ext4.vhdx
All volumes not mapped to a host folder are stored in a .vhdx file.

> [!INFO] Location of ext4.vhdx
> With Podman the (default) location is `%USERPROFILE%\.local\share\containers\podman\machine\wsl\wsldist\podman-machine-default\ext4.vhdx`.
> With Docker it is `%LOCALAPPDATA%\Docker\wsl\data\ext4.vhdx`.

Since diskspace is not released when files are deleted from volumes, this file can get very large. You can use `diskpart` (as described on [Stack Overflow](https://stackoverflow.com/a/74870395)) to shrink the file to its actual size:

1. Stop all WSL instances: `wsl --shutdown`
2. Verify all instances are *stopped*: `wsl --list --verbose`
3. Start `diskpart`
	1. Select the .vhdx file with `select vdisk file=""` (for Podman: `DISKPART> select vdisk file="%USERPROFILE%\.local\share\containers\podman\machine\wsl\wsldist\podman-machine-default\ext4.vhdx"`)
	2. Shrink the file: `DISKPART> compact vdisk`
	3. Close the window : `DISKPART> exit`

## ROCm support

The podman-machine-default is created based on a [Fedora](https://de.wikipedia.org/wiki/Fedora_(Linux-Distribution)) image ([source](https://docs.podman.io/en/latest/markdown/podman-machine-init.1.html)). While the [ROCm documentation](https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/wsl/install-radeon.html)  states that only Ubuntu is supported with WSL, there is a [guide](https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/native_linux/install-radeon.html) how to install it on RHEL (which is closely related to Fedora).