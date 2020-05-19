# nameComparison

Prerequisites:

Steps: 
1. Get Chocolately
  a. Run Powershell as Admin
  b. Run command: 
  Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
  
  c. Type choco into Powershell and you shouldn't see any errors
2. Getting Python
  a. in Powershell as Admin run: 
    choco install python
  b. once finished type: python --version
      you should see a version nunber and no errors
      
3. Download Github Desktop (google search and download, create an account so I can add you to repo)

4. Visual Studio Code (google search and download from Microsoft)

5. pip stuff:
  a. run in powershell as admin the following commands: 
    pip install --upgrade pip 
    pip install fuzzywuzzy

Cloning the repo:
In the topright corner of this page, click clone or Download
copy the url
open Github Desktop
File>Clone Repo>URL tab, paste url

You should see this repo on your local machine in your Github folder (usually in \Documents by default).


Steps to run analysis:

Open Visual Studio code
File>Open Folder> {Select the repo you just cloned}

  Setup the "test" file
  
  Open test file, paste in the data in the same format as shown [{...}], must have opening and closing brackets, use excel to set this part up, and save over "test"
  
  Once you have the data in the same format, open nameComparison.py and then click the Green play button in top right to run the python script. Your output will be in the terminal window that shows up (you might have to hit enter to get the python to actually exectue.
