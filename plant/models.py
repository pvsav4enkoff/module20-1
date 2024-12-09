from django.db import models

# Create your models here.
# Бригада
class Brigade(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    leader = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='brigade_leader')
    class Meta:
        verbose_name = "Бригада"
        verbose_name_plural = "Бригады"
    def __str__(self):
        return self.name
# Сотрудник
class Employee(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=50)
    boss = models.BooleanField(default=False)
    activ = models.BooleanField(default=True)
    brigade = models.ForeignKey(Brigade, on_delete=models.CASCADE, related_name='brigade_employees')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

class Position(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"
class LocationZone(models.Model):
    zone_location = models.CharField(max_length=25)
    class Meta:
        verbose_name = "Локализация"
        verbose_name_plural = "Локализации"
    def __str__(self):
        return self.zone_location
class Segment(models.Model):
    name = models.CharField(max_length=125)
    class Meta:
        verbose_name = "Сегмент"
        verbose_name_plural = "Сегменты"
    def __str__(self):
        return self.name
# Оборудование
class Equipment(models.Model):
    # name = models.CharField(max_length=255)
    name = models.ForeignKey(Segment, on_delete=models.CASCADE, related_name='equipment_name')
    description = models.TextField(default=None)
    location = models.ForeignKey(LocationZone, on_delete=models.CASCADE, related_name='equipment_location')
    class Meta:
        verbose_name = "Оборудование"
        verbose_name_plural = "Объетк ремонта."
    @property
    def full_info(self):
        return f"{self.name} - {self.location}"
    # def __str__(self):
    #     return self.name
# Ремонт
class Repair(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='repairs')
    brigade = models.ForeignKey(Brigade, on_delete=models.CASCADE, related_name='brigade_repairs')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=25)
    class Meta:
        verbose_name = "Ремонт"
        verbose_name_plural = "Ремонты"
    @property
    def full_info(self):
        return f"{self.equipment.name} - {self.brigade}"
    # def __str__(self):
    #     return self.status
# Задача
class Task(models.Model):
    segment = models.ForeignKey(Segment, on_delete=models.CASCADE, related_name='tasks', null=True)
    repair = models.ForeignKey(Repair, on_delete=models.CASCADE, related_name='repair_tasks')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee_tasks')
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=25)
    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
    @property
    def full_info(self):
        return f"{self.segment} - {self.employee.name} - {self.status}"
    # def __str__(self):
    #     return self.name