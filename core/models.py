from django.db import models


class Job(models.Model):
    """
    Job Posting Model
    """

    title = models.TextField(
        max_length=255,
        blank=False,
        verbose_name="Job Title",
        help_text="Job Post Title",
    )

    def __str__(self):
        return str(self.title)
