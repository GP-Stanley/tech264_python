# Research: Version Control System
source: https://www.atlassian.com/git/tutorials/comparing-workflows

**What is the difference between Git and Git Bash?**

**Git**

- **What It Is**: Git is a version control system. It helps you track changes to your files and collaborate with others.
- **How It Works**: You use Git commands to save versions of your project, switch between versions, and share your work with others.

**Git Bash**

- **What It Is**: Git Bash is a tool for Windows that provides a command-line interface to use Git.
- [**How It Works**: It gives you a Unix-like terminal on Windows, so you can run Git commands just like you would on a Linux or macOS system](https://www.atlassian.com/git/tutorials/git-bash).
  - It runs an interpreter that is using parts that originated from Linux. That is why git bash understands a lot of Linux commands.
  - The “shell” that runs behind the scenes is the thing that interprets the commands.

In short, **Git** is the software that does the version control, and **Git Bash** is a way to use Git on Windows through a command-line interface.

**What is a Version Control System** (VCS)

- A Version Control System (VCS) is a software tool that tracks and manages changes to files and directories over time.

**When to use one**

- When you need to track and manage changes to files or sets of files over time, especially when working on large, complicated projects with multiple contributors.
- Developing software collaboratively.
- Maintain back-up of work.

**Benefits**

- **Collaboration**: allows multiple people to work on the same project at the same time, and see who is working on what. This can make collaboration more efficient and seamless.
- **Avoiding conflicts**: tracks every change made to the code and can help prevent developers from accidentally overwriting each other's work.
- **Managing source code**: helps keep track of all the versions of a project and can help protect the source code from human error.
- **Restoring previous versions**: can help you go back to earlier versions of the code if you need to find the root cause of a bug (re-verting changes).
  - It is much easier to go back when you are making small, incremental changes.
- **Access to the latest version**: gives everyone on the team access to the latest version of the project, so they can work on the same thing.,
- **Keep history of changes made**.
- **Experimenting**: without messing up other files because they are “separate”. You can work on them independently.
- **Compare changes**: between different versions of the files.

**Types of version control**

Centralised VCS

- **Single Storage**: All versions of your files are kept on one main server.
- **Easy Management**: It’s straightforward to keep track of changes.
- **Risky**: If the main server crashes, no one can access or work on the files.

Distributed VCS

- **Local Copies**: Every developer has their own complete copy of the project.
- **Work Offline**: Developers can keep working even if there’s no internet connection.

**What is manual version control (VMC)**

- Manual version control is a method of tracking document versions using manual methods like naming conventions, spreadsheets, and date stamps.

**How did early version control systems work?**

The early systems were centralised, relied on file locking to avoid conflicts, had limited support from branching and offline work.

Collaborations more difficult compared to modern git.

- **Early Days**: Programmers manually tracked changes to each file and created backups.
  - Tools like SCCS and RCS were used, but only one person could work on a file at a time.
- **Centralised Systems**: These systems used a single, shared repository on a server or a developer’s local machine.
  - This allowed multiple people to work on different files but still had limitations.
- **Network-Based Systems**: In the mid-90s, version control became network-based, allowing better collaboration over the internet.

**Centralised VCS vs Distributed VCS like Git**

**Local Version Control with Git**

- Local version control with Git means that all the changes you make to your project are tracked and stored on your own computer.

Here’s a simple breakdown:

1. **Local Repository**: When you use Git, you create a local repository on your machine. This repository keeps track of all the changes you make to your files.
2. **Commits**: You can save snapshots of your project at different points in time by making commits. Each commit records the state of your project at that moment.
3. **History**: Git allows you to view the entire history of your project, including all the changes made, who made them, and when.
4. **Branches**: You can create branches to work on different features or fixes without affecting the main project. Once you’re done, you can merge these branches back into the main project.

The key advantage of local version control is that you don’t need an internet connection to work on your project or to view its history. [Everything is stored locally, making it fast and efficient](https://about.gitlab.com/topics/version-control/what-is-git-version-control/).


**What is stored in each version of a file that changes?**

In Git, each version of a file that changes is stored as a **commit** (like a save point in a video game**)**.
- When you make a commit, you’re saving the current state of your project.
    - A folder on your machine where Git is recording the changes to the files in that folder.
    - Git repository: a folder where git is tracking changes, storing your history, and allows collaboration.
    - It will save the whole file again for a file that is changed.

**Does Git need to be used as a distributed VCS?**

- No, Git doesn’t have to be used as a distributed version control system (DVCS), but that’s one of its main strengths.

Distributed Mode

- **Multiple Copies**: Every developer has a full copy of the repository on their local machine.
- **Offline Work**: You can commit changes, view history, and create branches without needing an internet connection.
- **Collaboration**: Changes can be shared between repositories, making it easier to collaborate with others.

Centralised Mode

- **Single Repository**: You can use Git in a way that mimics a centralized system by having a single main repository that everyone pushes their changes to.
- **Central Control**: This setup can be simpler for small teams or projects where centralized control is preferred.


While Git is designed to be distributed, you can still use it in a centralised manner if that suits your workflow better. The flexibility of Git allows you to choose the approach that works best for your team.

**What does Git store in a 'commit'?**

Saving a version of the file on your local computer. Here’s what is typically stored in each commit:

1. **Snapshot of Changes**: Git stores a snapshot of the entire project directory, but it only saves the differences (deltas) between the current version and the previous version for each file.
2. **Details** (metadata): Information about the changes, like:
    - Unique ID: A special code that identifies this version.
    - Author Info: Who made the changes.
    - Date and Time: When the changes were made.
    - Message: A short note explaining what was changed.
3. **Link to Previous Version**: A reference to the version before this one.

This setup helps you keep track of all changes, go back to earlier versions if needed, and work with others without messing up each other’s changes.

**The three states in Git**

In Git, files can be in one of three states:

- **Modified**: You’ve made changes to the file, but haven’t saved them in Git yet. Any change will mean that that new file will be classed as modified. Untracked.
- **Staged**: You’ve marked the modified file to be included in the next commit. You are saying that you want this file(s) to be in the next commit. Tracked. Added to the index.
- **Committed**: The changes are saved in the local Git database.
- [These states help you keep track of what changes are being worked on, what changes are ready to be saved, and what changes have already been saved](https://serengetitech.com/tech/three-states-of-git-and-three-sections-of-a-git-project/).


**Where does Git store its information?**

Git stores its information in a hidden directory called “.git”, located at the root of your project.

Here’s a breakdown of what it contains:

- **Object Store**: This is where Git keeps all the data for your project, including the content of your files, commit history, and other metadata. It’s like a database that holds everything Git needs to reconstruct any version of your project.
- **Index**: Also known as the staging area, this is where Git keeps track of changes that are ready to be committed.
- [**Configuration Files**: These files store settings and preferences for your repository, such as user information and repository-specific configurations](https://dev.to/developernationsurvey/git-internals-how-does-git-store-your-data-1gd7).

This setup allows Git to efficiently manage and track changes, making it easy to collaborate with others and maintain a detailed history of your project.

If you delete the .git folder, it is no longer tracked and all of the versions and changes are gone as well. You will only have the most recent versions of those files.

**Common workflow of Git commands (LOCAL)**

1. **Start a Project**: git init: Begin using Git in your project folder. Init = ititialised.
2. **Copy a Project**: git clone &lt;repository_url&gt;: Download a project from the internet to your computer.
3. **Check Changes**: git status: See what files have changed.
4. **Prepare Changes**:
    1. git add &lt;file&gt;: Mark a file to be saved.
    2. git add .: Mark all changed files to be saved.
5. **Save Changes**: git commit -m "message": Save your changes with a note about what you did.
6. **See History**: git log: Look at all the past changes.
7. **Create a New Version**:
    1. git branch &lt;branch_name&gt;: Make a new version of your project.
    2. git checkout -b &lt;branch_name&gt;: Make and switch to a new version.
8. **Switch Versions**: git checkout &lt;branch_name&gt;: Change to a different version of your project.
9. **Combine Versions**: git merge &lt;branch_name&gt;: Combine changes from one version into another.
10. **Fix Conflicts**: When there are conflicts, Git will show you where they are. You need to fix them and save again.


You have a remote repository and you’re going beyond having your local VCS:

1. **Share Changes**: git push origin &lt;branch_name&gt;: Upload your changes to the internet. Uploads changes to a remote repository 🡪 extending it to other places.
2. **Get Updates**: git pull: Download and combine changes from the internet. Fetch and merge changes from a remote repository 🡪 extending it to other places.


**1\. Check You Have Git on Your Machine**

Open Git Bash and type:

git --version

If Git is installed, you’ll see the version number. If not, you’ll need to install Git.

**2\. Create Your First Git Repo Named** tech264-test-git

1. **Open Git Bash**.
2. **Navigate to Your Desired Directory**:
3. cd path/to/your/directory
4. **Initialize the Repository**:
5. git init tech264-test-git
6. **Navigate to the New Repository**:
7. cd tech264-test-git

**3\. Create a** README.md **with Something in It**

1. **Create the File**:
2. echo "This is my first Git repository." > README.md
3. **Stage the File**:
4. git add README.md

**4\. Do Your First Git Commit**

1. **Commit the Changes**:
2. git commit -m "Initial commit with README.md"

**5\. Make Changes to the File and Do Another Commit**

1. **Edit the** README.md **File**:
2. echo "Adding more content to my README file." >> README.md
3. **Stage the Changes**:
4. git add README.md
5. **Commit the Changes**:
6. git commit -m "Updated README.md with additional content"

**6\. Check Differences Between the Commits**

1. **View the Differences**:
2. git diff HEAD~1 HEAD

**7\. Use** git checkout **to:**

**a. Checkout a Previous Commit, Then Get Back to the Latest Commit**

1. **List Commits**:
2. git log --oneline
3. **Checkout a Previous Commit** (replace commit_id with the actual ID from the log):
4. git checkout commit_id
5. **Return to the Latest Commit**:
6. git checkout main

**b. Restore a Specific File to Its State in a Previous Commit**

1. **Restore the File** (replace commit_id with the actual ID from the log):
2. git checkout commit_id -- README.md

By following these steps, you’ll complete your tasks and gain a solid understanding of basic Git operations. Let me know if you need any more details or run into any issues!

















