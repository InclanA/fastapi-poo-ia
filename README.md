## Estructura de mi proyecto
```
├── managers
│   ├── clienteM.py
│   ├── componentesM.py
│   ├── conexionM.py
│   └── empleadosM.py
├── models
│   └── models.py
├── routes
│   ├── clientesR.py
│   ├── componentesR.py
│   └── empleadosR.py
├── .env
├── .main.py
└── README.md
```

main.py - El inicio de mi api el archivo principal 

routes - define los endpoints para las direscciones para hacer una peticion

managers - es la carpeta  que hace toda la logica pesada para que funvcione bien

models  -  define los modelos de datos con pydantic 


### Componentes Empleados Clientes
GET Obtiene todos los componentes.  
POST Agrega un componente.  
PUT  Actualiza un componente por ID.  
DELETE Elimina un componente por ID.  


Use la IA pa que me ayudara con los errores y para dejar el código mucho mejor de lo que yo lo hago solo.