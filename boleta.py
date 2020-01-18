from conexion import Conexion

class Boleta:

    def __init__(self):
        self.conexion=Conexion()

# listara las boletas que sean de la fecha ingresada
    def listarVentas(self,fechaFactura):
        query=f'select * from registro_ventas.factura where fecha_factura="{fechaFactura}"'
       
        resultado=self.conexion.ejecutar_query(query)
        filas = resultado.fetchall()
        print(filas)

