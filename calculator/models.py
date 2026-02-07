from django.db import models
class Course(models.Model):
    GRADE_CHOICES = [
        ('10', 'A (10)'),
        ('9', 'A- (9)'),
        ('8', 'B (8)'),
        ('7', 'B- (7)'),
        ('6', 'C (6)'),
        ('5', 'C- (5)'),
        ('4', 'D (4)'),
        ('2', 'E (2)'),
        ('0', 'NC (0)'),
    ]
    name = models.CharField(max_length=100)
    credits = models.IntegerField()
    grade_point = models.CharField(max_length=2, choices=GRADE_CHOICES)
    def __str__(self):
        return f"{self.name} ({self.get_grade_point_display()})"