from django.db import models


class Post(models.Model):
    url = models.URLField(
        verbose_name="Посилання на пост",
        null=False,
        blank=True
    )

    def __str__(self):
        return self.url


class TeamMember(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="І'мя",
        blank=True,
        null=False
    )
    role = models.CharField(
        max_length=60,
        verbose_name="Роль, що виконує у команді",
        blank=True,
        null=False
    )
    description = models.TextField(verbose_name="Опис", blank=True)
    photo = models.ImageField(
        upload_to="team_members/",
        blank=True,
        null=False
    )

    def __str__(self):
        return self.name


class Report(models.Model):
    name = models.CharField(
        max_length=120,
        verbose_name="Назва звіту",
        blank=True
    )
    url = models.URLField(
        verbose_name="Посилання на звіт",
        blank=True
    )

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Назва",
        null=False,
        blank=True
    )
    description = models.TextField(
        verbose_name="Опис",
        null=False,
        blank=True
    )
    photos = models.ManyToManyField(Post, blank=False)

    def __str__(self):
        return self.name


class Shelter(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Назва",
        blank=True,
        null=False,
    )
    description = models.TextField(
        verbose_name="Опис",
        blank=True,
        null=False
    )
    phone_number = models.CharField(
        max_length=13,
        verbose_name="Контактний номер",
        blank=True,
        null=False
    )
    url = models.URLField(
        verbose_name="Контактне посилання",
        blank=True,
        null=False
    )
    photo = models.ImageField(
        upload_to="shelters/",
        blank=True,
        null=False
    )

    def __str__(self):
        return self.name


class Response(models.Model):
    first_name = models.CharField(
        max_length=40,
        verbose_name="Ім'я",
        null=False
    )
    last_name = models.CharField(
        max_length=40,
        verbose_name="Прізвище",
        null=False
    )
    phone_number = models.CharField(
        max_length=40,
        verbose_name="Номер телефону",
        null=False
    )
    email = models.EmailField(
        verbose_name="Пошта",
        null=False
    )
    help_desc = models.TextField(verbose_name="Чим може допомогти")

    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.help_desc[:50]}"
