from django.db import models

# Create your models here.
class Font(models.Model):
    name = models.CharField(max_length=100,unique=True)
    path = models.CharField(max_length=500,unique=True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        for t in Font.objects.all():
            if t.name == self.name:
                if t.path != self.path:
                    t.path = self.path
                    super(Font,t).save(*args,**kwargs)
                    print("Path for Font",self.__str__(),"was updated.")
                    return
                else:
                    print(self.__str__(),"had already been saved.")
                    return
        super(Font,self).save(*args,**kwargs)
        print(self.__str__(),"was sucessfully added to the DB.")