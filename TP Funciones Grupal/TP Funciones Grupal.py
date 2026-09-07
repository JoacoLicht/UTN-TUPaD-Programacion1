#Integrantes: Mateo Godoy, Alejo Barroso, Joaquin Lichtenberg, Bautista Cano 
# ==============================================================================
# TRABAJO PRÁCTICO: DISEÑO, IMPLEMENTACIÓN Y ARQUITECTURA MODULAR DE FUNCIONES
# ==============================================================================


# ------------------------------------------------------------------------------
# Ejercicio 1: Funciones puras con parámetros opcionales y keyword arguments
# ------------------------------------------------------------------------------
def calcular_factura_final(
    monto_base: float,
    impuesto: float = 21.0,
    descuento: float = 0.0,
    envio_prioritario: float | None = None,
) -> float:
    # 1. Calcular el monto con descuento
    monto_descontado = monto_base * (1 - descuento / 100)

    # 2. Aplicar el impuesto sobre el monto descontado
    subtotal = monto_descontado * (1 + impuesto / 100)

    # 3. Sumar envío prioritario si no es None
    if envio_prioritario is not None:
        subtotal += envio_prioritario

    # 4. Retornar el valor redondeado a 2 decimales
    return round(subtotal, 2)


# ------------------------------------------------------------------------------
# Ejercicio 2: Métodos Estáticos (@staticmethod) como Librería de Utilidades
# ------------------------------------------------------------------------------
class ValidadorFinanciero:

    @staticmethod
    def es_cuit_valido(cuit: str) -> bool:
        return cuit.isdigit() and len(cuit) == 11

    @staticmethod
    def convertir_moneda(
        monto: float, tasa_cambio: float, comision: float = 0.02
    ) -> float:
        monto_convertido = monto * tasa_cambio
        monto_final = monto_convertido * (1 - comision)
        return monto_final


# ------------------------------------------------------------------------------
# Ejercicio 3: Interacción Inter-Clase, Métodos de Instancia y Delegación
# ------------------------------------------------------------------------------
class Notificador:

    def enviar_recibo(self, cliente: str, total: float) -> None:
        print(f"--- RECIBO DE COMPRA ---")
        print(f"Cliente: {cliente}")
        print(f"Total abonado: ${total:.2f}")
        print("------------------------")


class ProcesadorPagos:

    def __init__(self, notificador: Notificador | None = None):
        if notificador is None:
            self.notificador = Notificador()
        else:
            self.notificador = notificador

    def procesar_transaccion(
        self, cliente: str, items: list[dict], descuento_cupon: float = 0.0
    ) -> float:
        total_acumulado = 0.0
        for item in items:
            total_acumulado += item["precio"]

        monto_final = total_acumulado * (1 - descuento_cupon / 100)
        self.notificador.enviar_recibo(cliente, monto_final)
        return monto_final


# ------------------------------------------------------------------------------
# Ejercicio 4: Manejo de Aridad Variable (*args y **kwargs)
# ------------------------------------------------------------------------------
def generar_auditoria_sistema(modulo: str, *mensajes: str, **metadatos) -> str:
    lineas = []
    lineas.append(f"MÓDULO: {modulo.upper()}")

    lineas.append("MENSAJES:")
    for i, mensaje in enumerate(mensajes, start=1):
        lineas.append(f"  [{i}] {mensaje}")

    lineas.append("METADATOS:")
    for clave, valor in metadatos.items():
        lineas.append(f"  {clave.upper()}: {valor}")

    return "\n".join(lineas)


# ------------------------------------------------------------------------------
# Ejercicio 5: Sistema Integrador (POO, Estáticos, Métodos y Kwargs)
# ------------------------------------------------------------------------------
class CalculadoraFitness:

    @staticmethod
    def calcular_imc(peso_kg: float, altura_m: float) -> float:
        return peso_kg / (altura_m**2)

    @staticmethod
    def clasificar_nivel(imc: float) -> str:
        if imc < 18.5:
            return "Bajo peso"
        elif imc < 25.0:
            return "Normal"
        else:
            return "Sobrepeso"


class Atleta:

    def __init__(self, nombre: str, peso: float, altura: float):
        self.nombre = nombre
        self.peso = peso
        self.altura = altura

    def obtener_reporte(
        self, incluir_recomendacion: bool = False, **metricas_extra
    ) -> str:
        imc = CalculadoraFitness.calcular_imc(self.peso, self.altura)
        clasificacion = CalculadoraFitness.clasificar_nivel(imc)

        lineas = [
            f"REPORTE DE ATLETA: {self.nombre}",
            f"IMC: {imc:.2f} ({clasificacion})",
        ]

        if metricas_extra:
            lineas.append("Métricas Adicionales:")
            for clave, valor in metricas_extra.items():
                lineas.append(
                    f"  - {clave.replace('_', ' ').capitalize()}: {valor}"
                )

        if incluir_recomendacion:
            if clasificacion == "Bajo peso":
                rec = "Aumentar ingesta calórica y entrenamiento de fuerza."
            elif clasificacion == "Normal":
                rec = "Mantener dieta balanceada y rutina actual."
            else:
                rec = "Ajustar déficit calórico e incrementar ejercicio aeróbico."
            lineas.append(f"Recomendación: {rec}")

        return "\n".join(lineas)


# ==============================================================================
# EJECUCIÓN DE PRUEBAS OBLIGATORIAS
# ==============================================================================
if __name__ == "__main__":
    print("=== PRUEBAS EJERCICIO 1 ===")
    print(calcular_factura_final(1000.0))  # Esperado: 1210.0
    print(
        calcular_factura_final(1000.0, descuento=10.0)
    )  # Esperado: 1089.0
    print(
        calcular_factura_final(
            1000.0, impuesto=10.0, descuento=5.0, envio_prioritario=150.0
        )
    )  # Esperado: 1195.0

    print("\n=== PRUEBAS EJERCICIO 2 ===")
    print(ValidadorFinanciero.es_cuit_valido("20384920194"))  # Esperado: True
    print(ValidadorFinanciero.es_cuit_valido("20-38492019-4"))  # Esperado: False
    print(
        ValidadorFinanciero.convertir_moneda(100.0, 1000.0, comision=0.05)
    )  # Esperado: 95000.0

    print("\n=== PRUEBAS EJERCICIO 3 ===")
    carrito = [
        {"nombre": "Teclado", "precio": 50.0},
        {"nombre": "Mouse", "precio": 30.0},
    ]
    procesador = ProcesadorPagos()
    procesador.procesar_transaccion("Ana Gómez", carrito, descuento_cupon=10.0)

    print("\n=== PRUEBAS EJERCICIO 4 ===")
    log = generar_auditoria_sistema(
        "AUTH",
        "Intento fallido",
        "Bloqueo de IP",
        usuario="admin",
        ip="192.168.1.10",
    )
    print(log)

    print("\n=== PRUEBAS EJERCICIO 5 ===")
    atleta = Atleta("Carlos Pérez", peso=75.0, altura=1.75)
    print(
        atleta.obtener_reporte(
            incluir_recomendacion=True,
            grasa_corporal="15%",
            pasos_diarios=10000,
        )
    )