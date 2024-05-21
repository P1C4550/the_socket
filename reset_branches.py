import subprocess

def reset_all_branches():
    # Fetch all branches from the remote repository
    subprocess.run(["git", "fetch", "--all"], check=True)

    # Get the list of all remote branches
    remote_branches = subprocess.run(["git", "branch", "-r"], capture_output=True, text=True, check=True)
    remote_branches = remote_branches.stdout.splitlines()

    # Loop through each remote branch and reset the corresponding local branch
    for branch in remote_branches:
        # Extract the branch name from the remote branch
        branch_name = branch.split("/", 1)[-1].strip()
        # Checkout and reset the local branch to match the remote branch
        subprocess.run(["git", "checkout", branch_name], check=True)
        subprocess.run(["git", "reset", "--hard", branch.strip()], check=True)

if __name__ == "__main__":
    reset_all_branches()
