from data import db_session
from data.jobs import Jobs
from datetime import datetime

db_session.global_init('db/blogs.sqlite')
session = db_session.create_session()
job = Jobs()
job.team_leader = 'Sanders Teddy'
job.job = 'Development of a management system'
job.work_siz = 25
job.collaborators = '5'
job.start_date = datetime.now()
job.is_finished = False
session.add(job)
session.commit()
