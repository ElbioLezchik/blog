"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from categorias.views import ListadoCategorias, CrearCategoria, EditarCategoria, EliminarCategoria  
from detallesblog.views import MostrarDetallesBlog, EditarDetallesBlog 
from entradas.views import ListadoEntradas, CrearEntrada, EditarEntrada, EliminarEntrada
from usuarios.views import ListadoUsuarios, CrearUsuario 
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    #path('admin/', admin.site.urls),
    #ruta a Categorias
    path('admin/categorias', ListadoCategorias.as_view(template_name = "categorias/index.html"), name = 'listadodecategorias'),
    path('admin/categorias/crear', CrearCategoria.as_view(template_name = "categorias/crear.html"), name= 'crearcategoria'),
    path('admin/categorias/editar/<int:pk>', EditarCategoria.as_view(template_name = "categorias/editar.html"), name= 'editarcategoria'),
    path('admin/categorias/eliminar/<int:pk>', EliminarCategoria.as_view(), name= 'eliminarcategoria'),
    

    #ruta a Detalles del Blog

    path('admin/detallesblog', MostrarDetallesBlog.as_view(template_name = "detallesblog/index.html"), name = 'detallesdelblog'),
    path('admin/detallesblog/editar/<int:pk>', EditarDetallesBlog.as_view(template_name = "detallesblog/editar.html"), name= 'editardetallesblog'),

    #ruta a Entradas del Blog
    path('admin/entradas', ListadoEntradas.as_view(template_name = "entradas/index.html"), name = 'listadodeentradas'),
    path('admin/entradas/crear', CrearEntrada.as_view(template_name = "entradas/crear.html"), name= 'crearentrada'),
    path('admin/entradas/editar/<int:pk>', EditarEntrada.as_view(template_name = "entradas/editar.html"), name= 'editarentrada'),
    path('admin/entradas/eliminar/<int:pk>', EliminarEntrada.as_view(), name= 'eliminarentrada'),
    


    #ruta a Usuarios del Blog
    path('admin/usuarios', ListadoUsuarios.as_view(template_name = "usuarios/index.html"), name = 'listadodeusuarios'),
    path('admin/usuarios/crear', CrearUsuario.as_view(template_name = "usuarios/crear.html"), name= 'crearusuario'),

]
 