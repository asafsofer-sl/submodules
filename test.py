import gen_plot
from clearml import Task


task = Task.init(project_name='runai/devops', task_name='Asaf plotly')
task.set_base_docker("python:3.12-bullseye")
task.execute_remotely(queue_name="exampleQueue")

gen_plot.print_plotly()
