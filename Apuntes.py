 #git add x (se usa para a�adir x al git, si x es un . se añade todo lo que no este metido)
#git commit -m "x" (se usa para a�adir el commit)
# git checkout x (se usa para devolver x al estado previamente guardado, si x es el codigo de un commit vuelve a ese estado, elemenando archivos)
# git config --global (con esto se agregan distintas configuraciones al perfil, si pone global es para tu usuario)
    #@ git config -- global alias.x "" (esto vale para grabar un alias a un codigo y con solo poner el alias se ejecute un codigo entero)
# .gitignore (un archivo con este nombre vale para que los elementos escritos en el sean ignorados) **/.vs (este es el formato para carpeta .vs)
# git diff (te informa de los cambios en los ficheros ya guardados respecto a los actuales. Ignora aquellos de los que no haya guardados)
    # git diff x (si x es una branch, te vale para ver la diferencia para posibles merge)
# --x  cuando se ponen dos guiones es un parametro, los que tienen solo uno -m son abreviaturas en este caso realmente es --message
#git log muestra los cambios, deflog muestra todo
#@git brach x (genera una nueva rama que se llame x desde el commit en el que estes)
    #@   git switch x (cambia a una rama ya creada)  
    # git branch -d x (Elimina la rama con el nombre x)
#@ dit stash (es como un commit local para seguir con trabajo a medias)
#@ git stash pop (es para volver al git stash que guardaste)
    # git stash drop (para cancelar un stash guardado)
#@ git push -u origin main (push sube lo local a la nube, desde origin, nombre local del repositorio por defecto, a main, nombre por defecto a la rama nube por defecto)
    #Despues con git push es suficiente.   
    # git fetch (te permite descarga remoto para poder comprobarlo pero sin afectar al local)
     # git pull (vale para descargar la parte remoto a la local, nomalmente requiere un merge)
     # con git pull en muchas ocasiones hace un merge que habre Editor Vim, si quieres esquibir pulsa i, despues tanto si escribes como si no dale a ESC 
     # Una vez dado ESC dale a :q para salir,:wq para guardar lo escrito y :q! para cancelar el merge



print ("Apuntes")