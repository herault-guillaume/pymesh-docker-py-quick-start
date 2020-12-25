import docker

# connect to docker
client = docker.from_env()

# start a detached container
pymesh = client.containers.run(image = 'pymesh/pymesh',
                                remove = True,
                                detach = True,
                                tty = True,
                                command='/bin/bash')

cmds = ';'.join(["import pymesh","import numpy","print(dir(pymesh))"])

res = pymesh.exec_run(cmd = 'python -c "{cmds}"'.format(cmds=cmds))
print(res.output.decode("utf-8"))

pymesh.stop()
