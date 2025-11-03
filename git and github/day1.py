# Git and Github

# Git is a VCS that keeps the track of our project code
# Github is an online platform to store our project code

# Steps to follow 
# 1. Initialize the git => git init ( only one time for a project )
# U - Untracked
# A - Added
# M - Modified
# 2. Connect system folder with github repository => git remote add origin {ssh_key} ( only one time for a project )
# 3. Add files to github => git add {file_name}. To add all files, we use => git add .
# 4. Commit the files > git commit -m "Message"
# 5. Push the git to github => git push -u origin {branch_name} // git push origin {branch_name}
# -u => Upstream. Upstream saves the branch 
# At the first push , it is recommended to use => git push -u origin {branch_name}

# To pull the code from github => git pull origin {branch_name}
# This change is made from the github

# To create a new branch => git branch {branch_name}
# To view all the branches => git branch // git branch -a
# To switch between the branches => git switch {branch_name}

# This change is done in Ujjwal branch

# You should create a PR (Pull Request)
# PR is a request to the owner of the repo of the github stating that to merge your code into the repo
# Tour step is to create a PR and the rest of the work is done by your senior 

# To merge the two branches => git merge {branch_name} 
# To merge, we should be in a branch to be merged.
