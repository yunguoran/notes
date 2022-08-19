# SSH

## Elementary Knowledge

  TODO

## GitLab and SSH keys

### Prerequisites

To view the version of SSH installed on your system, run `ssh -V`.

### Generate an SSH key pair

Type `ssh-keygen -t` followed by the key type and an optional comment. This comment is included in the `.pub` file that's created. You may want to use an email address for the comment.

For example, for ED25519:

```shell
ssh-keygen -t ed25519 -C "<comment>"
```

For 2048-bit RSA:

```shell
ssh-keygen -t rsa -b 2048 -C "<comment>"
```

### Add an SSH key to your GitLab account

To use SSH with GitLab, copy your public key to your GitLab account.

macOS:

```shell
tr -d '\n' < ~/.ssh/id_ed25519.pub | pbcopy
```

Linux (requires the xclip package):

```shell
xclip -sel clip < ~/.ssh/id_ed25519.pub
```

Git Bash on Windows:

```shell
cat ~/.ssh/id_ed25519.pub | clip
```
