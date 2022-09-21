# Trabajo de Fin de Máster
# Máster en Big Data y Ciencia de Datos

El presente repositorio contiene el código de los scripts utilizados para la prueba de concepto realizada para el trabajo de fin de Máster, para lo cual se utilizó la herramienta SIEM "ELK Stack", que es el conjunto de tres proyectos open source: Elasticsearch, Logstash y Kibana.

En la implementación se utiliza la situación de análisis de logs, los cuales son generados de los tipos información (info), ya que son los logs que más se utilizan en un servidor o aplicación. Estos logs son el input de Logstash, los cuales son procesados mediante el uso de filtros para posteriormente ser enviados a la base de datos de Elasticsearch, los cuales llegan ser el output por parte de Logstash.

Elasticsearch al estar guardando la información de los logs, pueden ser manipulados para su análisis, esto se realiza con un script utilizando el lenguaje de programación Python, el cual otorga una gran facilidad en cuanto al manejo y análisis de datos grandes, terminado el estudio de los datos extraídos de Elasticsearch estos son guardados en una nueva base de datos de esta misma herramienta.

La información guardada en Elasticsearch puede ser visualizada a través de Kibana, dicha herramienta otorga una interfaz amigable para los usuarios.

**Comandos para la ejecución de los scripts**
- Script: generate_logs.py
  ``` 
  python3 generate_logs.py
  ``` 
  
- Script: data_analysis.py
  ``` 
  python3 data_analysis.py
  ``` 

