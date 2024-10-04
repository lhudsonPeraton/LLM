# Installation + Setup for Windows Computer - TBD#
## Assumptions ##
- Instructions written based on a Windows Computer running Windows 11 with S Mode Disabled

## Installing Docker ##
- Install WSL using the link below:
  - https://learn.microsoft.com/en-us/windows/wsl/install
  - Expected Results:
      - After running `wsl --install`, Output should look like:
        ```
        Installing: Virtual Machine Platform
        Virtual Machine Platform has been installed.
        Installing: Windows Subsystem for Linux
        Windows Subsystem for Linux has been installed.
        Installing: Ubuntu
        Ubuntu has been installed.
        The requested operation is successful. Changes will not be effective until the system is rebooted.
        ```
    - After rebooting the computer, multiple command prompt windows may open for a short time. This is expected.
    - Open the start menu + search for + open Ubuntu
         - Create username + set password
    - To confirm successful installation, open a command prompt window and run `wsl -l -v`
         - Expect to see table with `name | state | version`
- Install Docker for Windows:
    - https://docs.docker.com/desktop/install/windows-install/
    - Follow instructions provided by link above + the installation wizard
