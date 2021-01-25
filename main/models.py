from django.db import models


class Customer(models.Model):
    STATUS_CHOICES = (
        ('S', 'Standard'),
        ('P', 'Premium'),
    )

    name = models.CharField(max_length=512)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)

    def __str__(self):
        return f'{self.name} ({self.get_status_display()})'


class UpgradeRequest(models.Model):
    STATUS_CHOICES = (
        ('N', 'New'),
        ('A', 'Accepted'),
        ('R', 'Rejected'),
    )

    description = models.TextField()
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    note_by_approver = models.TextField()

    @property
    def approval_blocked_by(self):
        if self.customer.status == 'P':
            return 'Customer is already upgraded'

        return None

    def __str__(self):
        return f'{self.get_status_display()} - {self.customer.name}'


class Contract(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    text = models.TextField()
