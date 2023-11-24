# Optimizing Interview Scheduling for HR Professionals

Managing interview schedules can be a challenging task for HR personnel. Coordinating between candidates and interviewers while considering everyone's availability and preferences often leads to complexities.

To streamline the interview scheduling process, a comprehensive solution is required. Leveraging technology and efficient tools, such as Django and Django REST framework, alongside Redis for caching, becomes crucial. Dedicated scheduling software and strategic utilization of these frameworks allow for enhanced scheduling capabilities and improved management of interview schedules.

## Mind Map

![Mind Map](Interview_Creation.png)

## Installation
1. Clone repository
2. Create Virtualenv & activate
    
        virtualenv venv
        source venv/bin/activate
    
3. Install the packages

        pip install -r requirement.txt
    
## Getting started

1. start the Django application 
    
        cd interview_scheduler
        python3 manage.py runserver
    
2. Start the redis server on port 6376(refer settings.py)
   
        redis-server --port 6376

3. 



    
      
