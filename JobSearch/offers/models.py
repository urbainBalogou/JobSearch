from datetime import date


from django.db import models
from django.urls import reverse


class Categorie(models.Model):
    libelle =  models.CharField(max_length=128)
    image = models.ImageField(blank=True,null=True, upload_to="images/")

    def get_absolute_url(self):
        return reverse('offres', kwargs={"id": self.id})

    def __str__(self):
        return self.libelle

class Recruteur(models.Model):
    nom_entreprise_ou_recruteur = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50, null=True, blank=True)
    date_naissance = models.DateField()
    domaine_ou_services = models.TextField(null=True,blank=True)
    situation_geographique = models.CharField(max_length=128)
    coordonne_localisation = models.CharField(blank=True, null=True,max_length=128)

    def __str__(self):
        return f"{self.nom_entreprise_ou_recruteur}"

class Offre(models.Model):
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    recruteur =  models.ForeignKey(Recruteur, on_delete=models.CASCADE)
    nom = models.CharField(max_length=128)
    description = models.TextField()
    renumeration_min = models.PositiveIntegerField()
    renumeration_max = models.PositiveIntegerField()
    type_de_contrat = models.CharField(max_length=10, choices=[("FREELANCE","Freelance"),("STAGE","Stage"),("CDD","CDD"),("CDI","CDI")])
    niveau_requis = models.CharField(max_length=128)

    def __str__(self):
        return self.nom

class Candidat(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField()
    date_naissance = models.DateField()
    niveau_d_etude = models.CharField(max_length=30)
    specialite = models.CharField(max_length=30)
    cv_ou_attestation = models.FileField(upload_to="dossier/",blank=True,null=True)

    def __str__(self):
        return f"{self.nom}, {self.specialite}"

class PostOffre(models.Model):
    candidat = models.ForeignKey(Candidat,on_delete=models.CASCADE)
    offre = models.ForeignKey(Offre,on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    deja_poste = models.BooleanField(default = False)
    status = models.CharField(max_length=10,default = "En cours", choices=[('EN_COURS', 'En cours'), ('ACCEPTE', 'Accepté'), ('REFUSE', 'Refusé')])


    def __str__(self):
        return f"{self.candidat.nom},{self.offre.nom}"













