Title: Git Cheat Sheet
Slug: git-cheat-sheet
Status: hidden

## Create and Clone
| Git Command | Action |
|:----:|:------| 
| git init | create new repository |
| git clone _/path/to/repository_ | clone local repository |
| git clone _username@host:/path/to/repository_ | clone remote repository |

## Add and Remove
| Git Command | Action |
|:----:|:------| 
| git add _filename_ | add changes to INDEX |
| git add * | add all changes to INDEX |
| git remove _filename_ | remove / delete |

## Commit and Synchronize
| Git Command | Action |
|:----:|:------| 
| git commit -m "_commit message_" | commit changes |
| git push origin master | | push changes to remote repository |
| git remote add origin _server_ | connect local repository to remote repository |
| git pull | update local repository with the remote changes |

## Branch
| Git Command | Action |
|:----:|:------| 
| git checkout -b _branch_ | create new branch |
| git checkout master | switch to master branch |
| git branch -d _branch_ | delete branch |
| git push origin _branch_ | push branch to remote repository |

## Merge
| Git Command | Action |
|:----:|:------| 
| git merge _branch_ | merge changes from another branch |
| git diff _source-branch_ _target-branch_ | view changes between two branches |

## Tag
| Git Command | Action |
|:----:|:------| 
| git _tag_ _commit-ID_ | create tag |
| git log | get commit IDs |

## Restore
| Git Command | Action |
|:----:|:------| 
| git checkout -- _filename_ | replace working copy with latest from HEAD |

## Sources
* [git cheat sheet](http://rogerdudler.github.io/git-guide/files/git_cheat_sheet.pdf)


## Research
* [git - the simple guide](http://rogerdudler.github.io/git-guide/)
