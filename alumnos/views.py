from django.shortcuts import render
from .models import Alumno,Genero
# Create your views here.



def index(request):
    alumnos= Alumno.objects.all()
    context={"alumnos": alumnos}
    return render(request, 'alumnos/index.html', context)

def crud(request):
    alumnos= Alumno.objects.all()
    context={"alumnos": alumnos}
    return render(request, 'alumnos/alumnos_list.html', context)

def alumnosAdd(request):
    if request.method is not "POST":
        generos=Genero.objects.all()
        context={'generos':generos}
        return render(request, 'alumnos/alumnos_add.html', context)
    else:
        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["paterno"]
        aMaterno=request.POST["materno"]
        fechaNac=request.POST["fechaNac"]
        genero=request.POST["genero"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        activo="1"

        objGenero=Genero.objects.get(id_genero=genero)
        obj=Alumno.objects.create(
            rut=rut,
            nombre=nombre,
            apellido_paterno=aPaterno,
            apellido_materno=aMaterno,
            fecha_nacimiento=fechaNac,
            id_genero=objGenero,
            telefono=telefono,
            email=email,
            direccion=direccion,
            activo=1
        )
        obj.save() 
        context={'mensaje':"Ok, datos grabados..."}
    return render(request, 'alumnos/alumnos_add.html', context)
