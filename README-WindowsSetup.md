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
    - Expect to see a "Containers" page once Docker Desktop opens successfully. May need to restart.

## Installing Python + Prerequisites ##
- Open Ubuntu through the start menu + run `python3 --version`
     - Expected Output: `Python #.##.##`
- Run `sudo apt install python3-pip` to install `pip`
- Run `sudo apt install python3-venv` to install `venv`
- Optional but highly recommended: Create a project folder for this demo and cd into it
    - Example: `mkdir hackathondemo; cd hackathondemo`
- Run `python3 -m venv venv` to create a virtual environment
- Run `source venv/bin/activate` to activate the virtual environment.
    - Expected Result: `(venv)` should appear before the command prompt
        - Example: `(venv) username@devicename:`
     
## Ollama Setup ##
- Clone the Ollama repository
    - `git clone https://github.com/ollama/ollama.git`
- Pull the Ollama Docker Image
    - `docker pull ollama/ollama`
- Run the Docker container (command below uses CPU - recommended)
    - `docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama`
- Run the model
    - `docker exec -it ollama ollama run llama3.2:1b`

      
