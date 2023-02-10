import os

#Check platform name (UNIX/Linux = posix, Windows = nt):
print(os.name)

#Print the current working directory
print(os.getcwd())

#List files in specific directory
fList = os.listdir("/home")
for f in fList:
    print(f)

#Remove a file (delete)
os.remove("file.txt")

#Check the platform line terminator (Windows = „\r\n‟ , Linux = „\n‟ , Mac = „\r‟ )
os.linesep

#Get the effective UID for current user
os.geteuid()

#Check if file and check if directory
os.path.isfile("/tmp")
os.path.isdir("/tmp")

#Run a shell command
os.system("ping -c 2 127.0.0.1")

#Execute a command & return a file object
files = os.popen("ls -l /tmp")
for i in files:
    print(i)

#Mask example
mask = os.umask(0o022)

#Path example
path = os.path.basename('C:/xyz/Documents/')

# Executing a shell command
os.system()

# Get the status of a file
os.stat()

# Get the users environment
os.environ()

# Move focus to a different directory
os.chdir()

# Returns the current working directory
os.getcwd()

# Return the real group id of the current process
os.getgid()

# Return the current process‟s user id
os.getuid()

# Returns the real process ID of the current process
os.getpid()

# Return the name of the user logged
os.getlogin()

# Check read permissions
os.access()

# Change the mode of path to the numeric mode
os.chmod()

# Change the owner and group id
os.chown()

# Set the current numeric umask
os.umask(mask)

# Get the size of a file
os.getsize()

# Last time a given directory was modified
os.path.getmtime()

# Last time a given directory was accessed
os.path.getatime()

# Get the users environment
os.environ()

# Return information about the current OS
os.uname()

# Change the root directory of the current process to path
os.chroot(path)

# List of the entries in the directory given by path
os.listdir(path)

# Show queue averaged over the last 1, 5, and 15 minutes
os.getloadavg()

# Check if a path exists
os.path.exists()

# Print out all directories, sub-directories and files
os.walk()

# Create a directory named path with numeric mode mode
os.mkdir(path)

# Recursive directory creation function
os.makedirs(path)

# Remove (delete) the file path
os.remove(path)

# Remove directories recursively
os.removedirs(path)

# Rename the file or directory src to dst
src = 'namefile1.py'
dst = 'namefile2.py'
os.rename(src, dst)

# Remove (delete) the directory path
os.rmdir(path)