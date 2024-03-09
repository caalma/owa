# owa - Organizador de Aplicaciones Web

**Versión: 0.1**

Organizador y lanzador de aplicaciones web.
De simple configuración y personalización.


## Requisitos

+ Python 3
+ Navegador web que admita apertura de páginas como aplicación. Actualmente esta característica está presente en: Chromium, Chrome, Brave.


## Cómo instalar

### en Linux

Ubicarse en una carpeta estable, donde pueda permanecer el software.

```
git clone https://github.com/caalma/owa.git
cd owa
./instalar-linux.sh
```


## Modo de uso

Admite varias opciones de acción:

+ Abrir url o id en perfil de usuario activo. Apertura normal: `owa <id o url>`
+ Abrir url o id en perfil de incognito: `owa p <id o url>`
+ Abrir url o id en perfil de incognito + tor (disponible en Brave): `owa t <id o url>`
+ Editar configuración: `owa ec`
+ Editar urls: `owa eu`
+ Agregar identificadores de url: `owa a <id> <url>`
+ Listar identificadores y url disponibles, con o sin filtrado: `owa l <id o parte-de-id>`
+ Mostrar ayuda: `owa h`
