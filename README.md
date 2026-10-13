# Strix

A lightweight custom shell built with Python, exploring command execution, shell internals, and Unix-like command-line interaction.

## Overview

**Strix** is a small, custom-built shell written in Python. It explores how command-line interpreters work, from reading user input to executing commands and handling basic shell interactions.

The project is primarily a learning experience focused on understanding the fundamentals behind a shell rather than building a full replacement for Bash or Zsh.

## Features

- **Interactive Command Line** — Accept and process user commands.
- **Command Execution** — Execute system commands and interact with the operating system.
- **Shell Internals** — Explore input parsing, command handling, and process execution.
- **Lightweight Design** — Built with Python and minimal dependencies.
- **Unix-Like Experience** — Inspired by the behavior and workflow of traditional Unix shells.

## Getting Started

### Prerequisites

- Python 3.10 or later
- A Unix-like operating system, preferably Linux

### Installation

Clone the repository:

```bash
git clone https://github.com/Strangerfuture/strix.git
cd strix
```

Run the shell:

```bash
python app/main.py
```


## Usage

Start Strix and enter commands in its interactive prompt.

```text
strix> ls
strix> pwd
strix> whoami
```

Available commands and their behavior depend on the current implementation.

## Project Goals

- Understand how shells process user input.
- Learn how commands are executed through Python.
- Explore process management and operating-system interfaces.
- Experiment with command parsing and shell behavior.
- Build a functional shell incrementally while strengthening Python fundamentals.

## Roadmap

- [x] Interactive command prompt
- [x] External command execution
- [x] Built-in commands such as `cd` and `exit`
- [x] Command-line argument parsing
- [ ] Environment variable support
- [ ] Input and output redirection
- [ ] Pipes between commands
- [ ] Command history
- [ ] Improved error handling

## Philosophy

Strix is an experiment in understanding the tools we use every day. Rather than treating the shell as a black box, this project explores the mechanisms behind command execution and the interface between users and the operating system.

Small, simple, and built to learn.

