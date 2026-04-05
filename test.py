import gen_plot
from allegroai import Task


task = Task.init(project_name='runai/devops', task_name='Assaf plotly')
task.set_base_docker("nvidia/cuda:11.1.1-base-ubuntu20.04")
task.execute_remotely(queue_name="exampleQueue")

gen_plot.print_plotly()
