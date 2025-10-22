from collections import defaultdict, deque

tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)]

def task_manager(tasks):
    servers = defaultdict(deque)
    
    for task_id, server_name, high_priority in tasks:
        if high_priority:
            servers[server_name].appendleft(task_id)
        else:
            servers[server_name].append(task_id)
            
    return servers

print(task_manager(tasks))


