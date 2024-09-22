# Process killer script
A script that automatically shuts down a specified process (e.g. Discord).

## Running
**1. Make sure to have at least Python version 3.6 or higher**

This is required to actually run the script. 

**2. Set up venv**

Just do `python -m venv venv`

**3. Install dependencies**

This is `pip install -U -r requirements.txt`. Make sure to have **pip** installed first. 

**4. Setup configuration**

Open the `config.ini` file and set the `enabled` variable to `true`/`false` if you want to **enable**/**disable** the script. Set the variable `program_name` to program you want to shut down automatically.

## Turning the script into a background process
This is completely optional. You can choose to skip this step.
### On Windows
**1. Open File Explorer:** Open the current folder in File Explorer.

**2. Create a shortcut:** Right click on the `proc_killer.bat` file and click on **Create shortcut**

**3. Make a startup program:** Right click the created shortcut and click on **Cut**. Go to the Windows Start Menu and type `Run` then press Enter. Type `shell:startup` in the Run window and press Enter. The startup folder will open. You can right click in the blank space of the folder and click on Paste (or you can use the `Ctrl-V` keyboard combination). 

### On Linux
**1. Open the terminal:** Use the `Ctrl-Alt-T` keyboard combination or search for it. 

**2. Make the script executable:** Navigate to the `proc_killer.sh` script and run `chmod +x proc_killer.sh`

**2. Edit the crontab file:** Type `crontab -e` in the terminal.

**3. Edit crontab:** Add `@reboot /path/to/your/proc_killer.sh` at the end of the file. **NOTE**: Don't forget to change `/path/to/your/` with the actual *absolute* file path to `proc_killer.sh`. After that, save and exit the editor.