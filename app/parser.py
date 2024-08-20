import argparse

def main():
    parser = argparse.ArgumentParser(prog="dutify", description="A simple CLI task manager")
    parser.add_argument('-h', '--help', help="Show this help message.")
    parser.add_argument('-a', '--add', help="Add a new task.")
    parser.add_argument('-l', '--list', help="List all tasks.")
    parser.add_argument('-d', '--done', help="Mark a task as done.")
    parser.add_argument('-r', '--remove', help="Remove a task.")
    parser.add_argument('-c', '--clear', help="Remove all tasks.")
    args = parser.parse_args()
main()