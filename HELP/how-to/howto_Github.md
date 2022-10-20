# how-to :: GitHub Smartly
---
## Overview
GitHub is a code hosting platform used in numerous collaborative (or personal) projects.

### Estimated Time Cost: 1.5 hrs

### Prerequisites:

- Git must be installed onto your machine.
- Know to open and navigate your file system in the terminal
- Have an already made github account and added an ssh key for your machine (see Resources)

### The Basics
0. Create a repo on [github.com](https://github.com/) by clicking new repo and configure to needs.
1. Copy the SSH link from your repo by clicking on the green "Code" button.
2. Navigate to desired directory for cloning your repo.
3. Type `git clone {SSH link} {Optionally, Name of Local Clone}` and Enter.
4. Navigate into the local clone.
5. Type `git pull` ALWAYS before you make changes to your repo.
6. Add/modify/remove code in the local clone.
7. Type `git pull` again just to be safe.
8. Type `git add/rm {list all modified files}`
9. Type `git commit -m "{Commit Message}"` to commit changes.
10. Type `git push` to push changes to the online repo. 

### Repos with > 1 Contributers (Assume Repo Exists)
0. Do steps 1-5 from *The Basics*
1. Type `git branch {Name of Branch}`
2. Type `git checkout {Name of Branch}`
3. Do steps 6-10 from *The Basics*

### Resources
* [All about SSH Keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/about-ssh)
* [Set up Git](https://docs.github.com/en/get-started/quickstart/set-up-git)

---

Accurate as of (last update): 2022-10-20

#### Contributors:  
Fang Chen, pd 02 (Team Bottlers)
Jeff Chen, pd 02 (Team Bottlers)
Yusha Aziz, pd 02 (Team Bottlers)