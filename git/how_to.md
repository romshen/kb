# How to:

1. rename current branch: `git branch -m new-name`.
2. add a file to the last commit if it wasn't pushed:
```shell
git add file-path
git commit --amend --no-edit
```
If it was pushed to your remote branch,
then - after amending your commit locally (as described above):
```shell
git push (-f | --force) <remote> <branch> 
```