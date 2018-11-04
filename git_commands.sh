# Git is the industry-standard version control system for web developers
# Use Git commands to help keep track of changes made to a project:

git init #creates a new Git repository
git status #inspects the contents of the working directory and staging area
git add #adds files from the working directory to the staging area
git diff #shows the difference between the working directory and the staging area
git commit -m "comment" #permanently stores file changes from the staging area in the repository
git log #shows a list of all previous commits

git show HEAD #
git checkout HEAD <filename> #Discards changes in the working directory.
git add <filename_1> <filename_2> #
git reset HEAD <filename> #Unstages file changes in the staging area.
git reset <commit_SHA> #Resets to a previous commit in your commit history.

git branch # Lists all a Git project's branches.
git branch <new_branch> # Creates a new branch "git branch fencing"
git checkout <branch_name> # Used to switch from one branch to another. "git checkout fencing"
git merge <branch_name> # Used to join file changes from one branch to another. Switch back to master then "git merge fencing"
git branch -d <branch_name> # Deletes the branch specified. "git branch -d fencing"

git clone <remote_location> <clone_name> # Creates a local copy of a remote. "git clone science-quizzes/ my-quizzes"
git remote -v # Lists a Git project's remotes.
git fetch # Fetches work from the remote into the local copy.
git merge origin/master # Merges origin/master into your local branch.
git push origin <your_branch_name> # Pushes a local branch to the origin remote. "git push origin bio-questions"

"The workflow for Git collaborations typically follows this order:

1. Fetch and merge changes from the remote
2. Create a branch to work on a new project feature
3. Develop the feature on your branch and commit your work
4. Fetch and merge from the remote again (in case new commits were made while you were working)
5. Push your branch up to the remote for review

Steps 1 and 4 are a safeguard against merge conflicts, which occur when two branches contain file changes that cannot be merged with the git merge command. 
Step 5 involves git push, a command you will learn in the next exercise."


"adding code to github

https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/ 

Create a new repository on GitHub. To avoid errors, do not initialize the new repository with README, license, or gitignore files. You can add these files after your project has been pushed to GitHub.
Open Git Bash.

Change the current working directory to your local project.

Initialize the local directory as a Git repository."

git init

"Add the files in your new local repository. This stages them for the first commit."

git add .
# Adds the files in the local repository and stages them for commit. To unstage a file, use 'git reset HEAD YOUR-FILE'.
"Commit the files that you''ve staged in your local repository."

git commit -m "First commit"
# Commits the tracked changes and prepares them to be pushed to a remote repository. To remove this commit and modify the file, use 'git reset --soft HEAD~1' and commit and add the file again.
"Copy remote repository URL fieldAt the top of your GitHub repository''s Quick Setup page, click  to copy the remote repository URL.

In the Command prompt, add the URL for the remote repository where your local repository will be pushed."

git remote add origin <remote repository URL>
# Sets the new remote
git remote -v
# Verifies the new remote URL
"Push the changes in your local repository to GitHub."

git push origin master
# Pushes the changes in your local repository up to the remote repository you specified as the origin