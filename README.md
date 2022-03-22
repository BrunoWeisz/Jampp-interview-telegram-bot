# Jampp-interview-telegram-bot

Versión de Python utilizada: 3.6.5

Para iniciar el bot se deben seguir los siguientes pasos:

0) Ejecutar en la raiz del proyecto $pip3 install -r requirements.txt

1) Ir al directorio /scripts 

2) Ejecutar $python3 BankCashFiller.py 
    Esto creara en el directorio /files un archivo 'cajeros-automaticos-cash.csv' a partir del archivo 'cajeros-automaticos.csv', que tendrá un campo dedicado a la cantidad de extracciones restantes de cada cajero automático.

3) Ejecutar $python3 BankSeparator.py
    Esto creará en el mismo directorio /files dos archivos 'cajeros-automaticos-link.csv' y 'cajeros-automaticos-banelco.csv' a partir del archivo 'cajeros-automaticos-cash.csv', separando de esta forma a los cajeros automaticos por red.

4) En el directorio raiz del proyecto, ejecutar $python3 script.py
    Esto comenzara la ejecucion del bot

Info adicional:

    o) El link del bot es t.me/Jampp_Interview_Bruno_ATM_bot
    o) La funcionalidad de compartir la ubicación solo está disponible en dispositivos celulares
       por el momento
    o) Para cumplir con la complejidad de búsqueda, utilicé un KDTree, estructura de datos que
       permite hallar en tiempo logarítmico los puntos más cercanos a determinado punto dado. Esta estructura debe construirse a partir de los datos estáticos cada vez que el sistema se reinicia. 
