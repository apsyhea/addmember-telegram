import subprocess

group_source = input('Enter chat ID or link source: ')
group_target = input('Enter chat ID or link target: ')

subprocess.run(["python", "init_session.py", group_source, group_target])
subprocess.run(["python", "get_members.py", group_source, group_target])
subprocess.run(["python", "add_members.py", group_source, group_target])
