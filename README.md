# File Organizer

I made this files organizer to make my life easier when I'm dealing with a bunch of messy files.

## Installation Instructions

To set up and use the organizer, follow these steps:

1. Clone this repository to your local machine:

```
git clone https://github.com/oebelus/files_manager.git
```

2. Navigate to the project directory:

```
cd files_manager
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

Now you're ready to organize your files! You can run:

```
manager organize  # For organizing files manually
manager manage    # For grouping and moving files based on keywords
```

## Features

### Organize

The `organize` command is for grouping files by keywords and moving them into a new folder. For example, you can take all files named `SCREENSHOTS*` by entering `SCREENSHOTS` and move them into a new folder.

How to use?

```
manager organize
```

Follow the prompts:

- Enter your files directory (e.g., . for the current directory).
- Enter the directory where you want to create the folder.
- Enter a name for your folder.
- Specify the number of keywords to be used for filtering files. The files will be organized into the folder based on these common keywords.
- You will be then prompted to enter the keywords one by one.

### Manage:

The `manage` command helps you sort your files into specific directories, giving you control over how and where to move your files.

How to use?

```
manager manage
```

You can enter 'h' to get the commands' list:

```
--- Enter your command: h
> Enter a number to access the directory
> Enter (r) to read the file
> Enter (.) to save the file here
> Enter (..) to navigate to the parent directory
> Enter (+) to create a directory
> Enter (d) to delete the file
> Enter (D) to delete a directory
> Enter (n) to show the name of the file
> Enter (re) to rename the file
> Enter (dirs) to display directories
> Enter (redir) to rename a directory
> Enter (mv) to move a directory
> Enter (-) to move to the next file
> Enter (q) to exit
```

And the folders are displayed like this:

```
(1)> Articles
(2)> Biology
(3)> Computer Science
(4)> Languages
(5)> Mathematics
(6)> Pictures
(7)> Physics
```
