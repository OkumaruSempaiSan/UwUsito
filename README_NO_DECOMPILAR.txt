Versión reprogramada por solicitud del usuario.

Cambios aplicados:
- Se desactivó la decompilación por defecto.
- Se desactivó el cache de scripts.
- Se desactivó SaveBytecode.
- Se bloqueó Script, LocalScript y ModuleScript en DecompileIgnore.
- Se agregó una protección directa para que Source de Script, LocalScript y ModuleScript no use LinkedSource, HttpGet, getscriptbytecode ni decompile.

Resultado esperado:
Los Scripts, LocalScripts y ModuleScripts se conservan como instancias, pero su Source se reemplaza por un texto indicando que la decompilación está desactivada.
