# portal-gp

portal gp es un sitio web que pretende ser una especie de lobby virtual (???) del gp. sirve para que todos los jugadores puedan consultar la base de datos o el registro de los gps, mbds, drgs, faltas y también ver sus puntuaciones y estadísticas. también sirve para gestionar todo el sistema de notas.
 
## quereseres

### importar chat de WhatsApp
#### detección del chat
- [ ] mejorar la detección de mbds
hay que arreglar las regex de get_mbd() en read_wtext.py para que pueda detectar más cadenas de texto raras

#### cargar a la base de datos
- [ ] a ver como coño se hace esto hay qeu cargar los datos a la base de datos y luego linkear las fk...

#### comandos
esto es una feature extra para poner cuando todo esté hecho. consistiría en una especie de sistema de comandos para poder escribir en el chat del grupo y que luego tengan ciertas acciones en el recuento. por ejemplo, un comando para poner un warning a un día que ha pasado algo conflictivo para luego encontrarlo fácil y resolverlo. también se podrían añadir faltas usando comamndos y así. muy fácil de implementar.

### base de datos
- [ ] poder calcular las rachas
- [ ] poder calcular los puestos

### sistema de notas
- [ ] hacerlo...

### la cosa en general
- [ ] coger las listas de tuples y cargarlas a la base de datos...

### interfaz
- [ ] arreglar tablas para poder ser ordenadas por la fecha que no va
- [ ] arreglar lo lento que cargan las tablas.... https://datatables.net/manual/server-side

### validador
- [ ] hacerlo que putisimo coñazo

- [ ] buscar un calendario?????????????

### jugadores
