** 👋 Hola me llamo Santiago Goldstein **
** Y esta es mi pagina web Tienda Libre**


Tienda libre es conjunto de aplicaciones web, donde su funcion principal es poder crearnos una cuenta, iniciar sesion, poner a la venta productos y comprarlos.

Lo primero y principal que se hizo, es crear el entorno virtual y allí instalar las librerias pertinentes, luego, la estructura con python y django, donde se crearon 2 apps para poder llevar a cabo el proyecto de la página.

Se descargo una plantilla de bootstrap y se acoplo al proyecto django, luego se modificó para que sea original a los principios de la página.

Se creo el CRUD de productos, donde permite que los usuarios puedan agregar, quitar, editar y consultar los productos.

Se creo el login, register y logout con sus respectivas paginas html, ademas se dieron permisos exclusivos para los usuarios que inicien sesion en la pagina, luego se dio un permiso especial para los usuarios que decidan vender, (Hay un apartado en la pagina para pedir dicho permiso).

Se creo la ultima app llamada venta, para registrar los productos vendidos de los vendedores y demás datos.

Una vez terminada la logica de la página, se le dedico varios dias a la mejora de flujo y diseño, dandole un toque mas profesional.

Se hizo un catalogo destacado en la pagina principal, teniendo la opcion de "ver más" sobre aquellos productos.


**usuarios en la base de datos**

Usuario administrador: Tiene la capacidad de poder ver y editar todo tipo de datos de la base de datos.

Usuario vendedor: Puede crear y editar categoria de productos y productos, pero no tiene acceso a la administración.

Usuario normal: Solo puede ver los productos listados y si lo desea puede comprarlos.

**Cualquier usuario normal puede pedir acceso para vender, siempre y cuando sea supervisado por el admin**

Se creron paginas con error 404, cuando un usuario intenta acceder a sectores privados, para asi mejorar la seguridad de la pagina y respetar los rangos. De todas maneras los usuarios normales no tienen la posibilidad de acceder visualmente a dichos sectores.

Cuando un usuario no inicia sesion, solo podrá ver un sector de la página, (Inicio, Sobre Mi, Contacto y Login).

En el apartado de Login el usuario no solo podrá iniciar sesion, sino que si se olvido la contraseña, puede recuperarla. Ademas se incorporó la opcion de crear una cuenta si el usuario no dispone de una.

El admin puede elegir las fotos de los avatares, que en un principio estan configurados por orden de jerarquia.


**Errores que presenta la página que no se pudieron solucionar**

Al iniciar sesion en la url del navegador aparece un /login seguido del :8000, esto causa que al tocar en (ver más) del catalogo salte un error. Se soluciona eliminando el /login para dejar limpio el localhost, de esta forma se podra utilizar la pagina web sin inconvenientes.

**Link a video mostrando el funcionamiento de la página**
https://drive.google.com/file/d/1XaiHe6PVqzwU2ebRKrx9HYf0Yx7saQ6y/view?usp=sharing



