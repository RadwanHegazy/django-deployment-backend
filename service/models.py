from django.db import models
from users.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from random import randint
import docker, threading



class Service (models.Model) :
    user = models.ForeignKey(User, related_name='user_serivce', on_delete=models.CASCADE)
    image = models.CharField(max_length=225)
    port = models.IntegerField(unique=True, null=True, blank=True)
    is_online = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.image + " | " + self.user.email 
    

def run_docker(service_id) : 
    serivce = Service.objects.get(id=service_id)
    client = docker.from_env()
    port = serivce.port
    client.containers.run(serivce.image, "python manage.py runserver 0.0.0.0:8000", ports={f"8000":port})
    serivce.is_online = True
    serivce.save()


@receiver(post_save, sender=Service)
def choose_port_for_service(created, instance:Service, **kwargs) : 
    if not created :
        return
    
    # confirm that we generated a uniqe port
    while True :
        port = '1'
        for i in range(1, randint(2,5)) :
            port += str(randint(0,9))

        if Service.objects.filter(port=int(port)).exists() == False:
            break

    thread = threading.Thread(target=run_docker, args=(instance.id,))
    thread.start()


    instance.port = int(port)
    instance.save()