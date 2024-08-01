```markdown
# Git Commands Documentation

## Configuration and Setup

1. **Check Existing Credential Helpers**
   ```bash
   git config --global --get-all credential.helper
   ```
   - Lists all credential helpers configured in Git.

2. **Add Remote Repository**
   ```bash
   git remote add origin https://github.com/anindyadc/python-script-helper.git
   ```
   - Sets the URL for the remote repository named `origin`.

3. **Install Git Credential Manager**
   ```bash
   brew install --cask git-credential-manager
   ```
   - Installs the Git Credential Manager using Homebrew.

## Working with Branches

4. **Push Changes to Remote `master`**
   ```bash
   git push -u origin master
   ```
   - Pushes the local `master` branch to the remote `origin`.

5. **Push Changes to Remote `main`**
   ```bash
   git push -u origin main
   ```
   - Pushes the local `main` branch to the remote `origin`.

6. **Switch to `main` Branch**
   ```bash
   git checkout main
   ```
   - Switches to the `main` branch.

7. **Fetch Remote Changes**
   ```bash
   git fetch origin
   ```
   - Fetches changes from the remote repository.

8. **Create Local `main` Branch Tracking Remote `main`**
   ```bash
   git checkout -b main origin/main
   ```
   - Creates a local branch `main` that tracks the remote `main` branch.

9. **Merge `master` into `main`**
   ```bash
   git merge master
   ```
   - Merges changes from `master` into `main`.

10. **Merge `master` into `main` Allowing Unrelated Histories**
    ```bash
    git merge master --allow-unrelated-histories
    ```
    - Merges `master` into `main` even though the branches have unrelated histories.

11. **Commit the Merge**
    ```bash
    git commit
    ```
    - Commits the merge changes.

12. **Push Merged Changes to Remote `main`**
    ```bash
    git push origin main
    ```
    - Pushes the updated `main` branch to the remote repository.

13. **Delete Local `master` Branch**
    ```bash
    git branch -d master
    ```
    - Deletes the local `master` branch.

14. **Delete Remote `master` Branch**
    ```bash
    git push origin --delete master
    ```
    - Deletes the remote `master` branch.

## Additional Commands

15. **Check Status**
    ```bash
    git status
    ```
    - Displays the status of the working directory and staging area.

16. **List Files**
    ```bash
    ls -l
    ```
    - Lists files in the current directory with detailed information.

17. **View Command History**
    ```bash
    history
    ```
    - Displays the command history.

18. **Commit with Message**
    ```bash
    git commit -m "Add ssh-select project to the repository"
    ```
    - Commits changes with a message.

```
