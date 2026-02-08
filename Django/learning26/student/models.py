from django.db import models
# Create your models here.

class Student(models.Model):
    studentName = models.CharField(max_length=100)
    studentAge = models.IntegerField()
    studentCity = models.CharField(max_length=50)
    studentEmail = models.EmailField(max_length=254)

    class Meta:
        db_table = "student"

    def __str__(self):
        return self.studentName


class product(models.Model):
    productName=models.CharField(max_length=50)
    productPrice=models.IntegerField()
    productDescription=models.TextField()
    productStock=models.IntegerField()
    productColor=models.CharField(null=True)
    proudctStatus=models.BooleanField(default=True)

    class Meta:
        db_table = "product"

    def __str__(self):
        return self.productName
   
    
class movie(models.Model):
    Name=models.CharField( max_length=50)
    # showTime=models.CharField(max_length=20)
    showTime=models.TimeField(auto_now=False, auto_now_add=False)
    ticketPrice=models.PositiveIntegerField()
    MovieStory=models.TextField()

    class Meta:
        db_table='Movies'
    def __str__(self):
        return self.Name

class studentprofile(models.Model):
    hobbies=(("reading","reading"),("writing","writing"),("coding","coding"))
    studentId=models.OneToOneField(Student,on_delete=models.CASCADE)
    studenthobbie=models.CharField(max_length=50,choices=hobbies)
    studentAddress=models.CharField(max_length=100)
    studentPhone=models.CharField(max_length=10)
    studentGender=models.CharField(max_length=10)
    studentDOB=models.DateField()
    
    class Meta:
        db_table = "studentprofile"

    def __str__(self):
        return self.studentId.studentName

class review(models.Model):
    movieid=models.ForeignKey(movie,on_delete=models.CASCADE) #one to many(movie)
    rating=models.IntegerField()
    review=models.TextField()
    
    class Meta:
        db_table='review'
    def __str__(self):
        return self.movieid.Name

class productpirce(models.Model):
    productid=models.OneToOneField(product,on_delete=models.CASCADE)# one to one(product)
    productprice=models.IntegerField()
    productdiscount=models.IntegerField()
    productfinalprice=models.IntegerField(editable=False)
    
    def productfinalprice(self):
        discount=self.productprice*self.productdiscount/100
        return self.productprice-discount
    class meta:
        db_table='productpirce'
    def __str__(self):
        return self.productid.productName


class category(models.Model):
    categoryName=models.CharField(max_length=50)
    categoryDescription=models.TextField()
    
    class Meta:
        db_table='category'

    def __str__(self):
        return self.categoryName

class service(models.Model):
    categoryid=models.ForeignKey(category,on_delete=models.CASCADE)#one to many(category)
    serviceName=models.CharField(max_length=50)
    serviceDescription=models.TextField()
    servicePrice=models.IntegerField()
    serviceStatus=models.BooleanField(default=True)
    
    
    class Meta:
        db_table='service'
    def __str__(self):
        return self.serviceName