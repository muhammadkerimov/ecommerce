from django.db import models

# Create your models here.

ADMIN_LEVELS =(
("Moderator","level0"),
("Admin Level 1","level1"),
("Admin Level 2","level2"),
("Admin Level 3","level3"),
("Admin General","level4"),
("Owner","level5"),
)

class adminaccs(models.Model):
    admin_name = models.CharField(max_length = 255)
    admin_surname = models.CharField(max_length = 255)
    admin_id = models.CharField(max_length = 255)
    admin_password = models.CharField(max_length = 255)
    admin_level = models.CharField(choices=ADMIN_LEVELS,max_length=40)
    admin_login_last = models.DateTimeField()
    