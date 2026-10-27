# -*- coding: utf-8 -*-
"""
Generador del Bloque 2 del Curso de Tatuaje:
Crea los manuales Markdown de caligrafía de línea, videoteca de YouTube de empalmes y Cybersigilism,
y compila las plantillas PDF vectoriales de precisión A4 (03 y 04).
"""

import os
import math
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas

BASE_DIR = r"C:\Users\quesa\Documents\CURSO TATTOO"
B2_DIR = os.path.join(BASE_DIR, "BLOQUE_2_LINEA_PROFUNDIDAD_Y_CYBER")
SHEETS_DIR = os.path.join(B2_DIR, "PLANTILLAS_PRACTICA")
os.makedirs(SHEETS_DIR, exist_ok=True)

# ---------------------------------------------------------
# 1. ARCHIVO: 01_MANUAL_CALIGRAFIA_Y_ESPINAS_CYBER.md
# ---------------------------------------------------------
manual_content = """# Bloque 2 — Manual de Caligrafía: Control Milimétrico de Profundidad, Empalmes y Espinas Cybersigilism

En este bloque pasamos de la configuración mecánica básica al dominio artesanal del trazo. El Cybersigilism y la filigrana barroca no perdonan: una línea vacilante, un empalme con "bulto" o una espina con la punta mocha arruinan la armonía visual de la pieza.

Aquí aprenderás a sincronizar la mano con el motor rotativo Poseidon, diagnosticar tu profundidad leyendo el reverso de la silicona y ejecutar la técnica del **latigazo cónico ("tapered flick")** que define a las espinas cyber.

---

## 1. La Física del Trazo: Hand Speed vs Frecuencia de Picada

Tu máquina Poseidon a **7.5V** mueve el motor rotativo a unas **8.000 RPM**, lo que equivale a unos **133 impactos de aguja por segundo**.
Tu cartucho **1205RL** tiene 5 agujas de 0.35 mm agrupadas en un círculo compacto de aproximadamente 0.7 mm de diámetro.

```
 [ IMPACTO 1 ] -> [ IMPACTO 2 ] -> [ IMPACTO 3 ] -> [ IMPACTO 4 ]
    ( • • • • • • • • • • • • • • • • • • • • • • • • • • • • )
          <--- SOLAPAMIENTO DEL 70% ENTRE PICADAS --->
                  = LÍNEA SÓLIDA NEGRA PERFECTA
```

### Los 4 Estados del Trazo (Diagnóstico Inmediato):

1. **El Trazo "Costura de Máquina de Coser" (Grave):**
   * *Síntoma:* La línea no es negra continua, sino que se ven puntitos individuales separados o un contorno dentado.
   * *Causa:* Estás moviendo la mano demasiado rápido para el voltaje actual, o el voltaje está demasiado bajo (<6.8V).
   * *Solución:* Reduce la velocidad de avance de tu mano a la mitad, o sube el voltaje a **7.6V – 7.8V**.
2. **El Trazo "Quemado / Mastigado" (Grave):**
   * *Síntoma:* La aguja rasga la piel sintética, suelta virutas de silicona y la línea queda con bordes deshilachados.
   * *Causa:* Mano paralizada o extremadamente lenta con voltaje alto (>8V). La aguja perfora 10 veces en el mismo milímetro y destruye el soporte.
   * *Solución:* Mantén la mano siempre en movimiento continuo mientras la aguja esté dentro de la piel.
3. **El Trazo "Fantasma" (Superficial):**
   * *Síntoma:* Mientras tatúas parece negro, pero al pasar la servilleta con vaselina desaparece el 70% de la tinta.
   * *Causa:* La aguja apenas entra a 0.5 mm; la tinta se queda en la capa superior sin anclarse.
   * *Solución:* Saca medio milímetro más de aguja girando el grip hacia afuera (*needle hang*) y asegura el apoyo firme del dedo meñique.
4. **El Trazo "Perfecto" (Grado Profesional):**
   * *Síntoma:* Color negro azabache uniforme al primer pase, bordes rectos como un corte con bisturí y brillo limpio sin rebaba de plástico.

---

## 2. El Test del Reverso de la Piel Sintética (Control de Profundidad)

No te fíes solo de cómo se ve la silicona por delante. El verdadero indicador de si estás listo para piel humana está en la parte trasera de tu lámina de práctica:

```
  VISTA DE PERFIL DE LA PIEL SINTÉTICA (Grosor: 2.0 mm - 3.0 mm)
 -----------------------------------------------------------------
   [ Capa 1: Epidermis simulada ]   (0.5 mm - La tinta aquí se borra)
 -----------------------------------------------------------------
   [ Capa 2: Dermis simulada ]      (1.5 mm - ZONA EXACTA DE ANCLAJE)
 -----------------------------------------------------------------
   [ Capa 3: Reverso / Hipodermis ] (Si la aguja llega aquí = BLOWOUT)
 =================================================================
```

### Cómo hacer la auditoría del reverso:
1. Traza 5 líneas horizontales en tu plantilla.
2. Limpia la superficie con una gota de vaselina y una servilleta de papel.
3. **Dale la vuelta a la piel sintética:**
   * **Reverso intacto sin marcas ni tinta:** Vas demasiado superficial (<1 mm). Tienes que entrar con un poco más de convicción.
   * **Reverso con tinta negra visible o relieve al pasar el dedo:** Has perforado la piel por completo (>2.5 mm). En piel humana habrías alcanzado el tejido celular subcutáneo graso, provocando un derrame de tinta irreversible (*blowout* verdoso).
   * **Reverso con una ligera sombra gris traslúcida (sin relieve al tacto):** **¡PROFUNDIDAD PERFECTA!** Has penetrado exactamente entre 1.5 mm y 1.8 mm, la profundidad exacta de la dermis humana.

---

## 3. El Estiramiento a 3 Puntos (The 3-Point Stretch)

En piel sintética apoyada sobre la mesa suele haber fricción y holgura. Si no estiras, la aguja empuja el material elástico hacia abajo antes de perforar, deformando las líneas rectas.

* **Punto 1 y 2 (Mano no dominante):** Coloca el dedo pulgar y el dedo índice formando una "L" o una "V" abierta sobre la piel, separándolos suavemente unos 5 a 8 centímetros para poner la superficie en tensión como el parche de un tambor.
* **Punto 3 (Mano que tatúa):** El nudillo o lateral de tu dedo meñique se apoya con firmeza entre los dos dedos anteriores, creando un triángulo de soporte rígido.
* Con este trípode, tu máquina Poseidon puede deslizarse con precisión milimétrica sin que la piel se arrugue ni vibre.

---

## 4. Técnica de Empalme Invisible (Tapered Overlap)

Nadie puede trazar una línea de 20 cm de un solo tirón sin respirar o sin que la muñeca llegue a su límite anatómico de giro. La diferencia entre un principiante y un maestro es **cómo unen dos tramos de línea**.

```
 TRAMO 1:                   ...======-------______ (Levantando suavemente al vuelo)
                                  \                  /
                                   \   ZONA DE      /
                                    \  SOLAPAMIENTO/
                                     \ (10 - 15 mm)/
 TRAMO 2:             ______-------======... (Entrando suavemente en ángulo agudo de 30°)
```

### Reglas de oro del empalme invisible:
1. **Nunca frenes en seco:** Si paras la máquina con la aguja clavada a profundidad total, dejarás un punto negro gordo (*dot of death*) imposible de disimular.
2. **El "Fade Out" de salida:** Cuando estés llegando al límite cómodo de tu alcance de mano (unos 4-6 cm de trazo), comienza a aligerar la presión sobre la piel durante el último centímetro, sacando la aguja gradualmente al vuelo. El trazo se afilará en gris suave.
3. **El "Fade In" de entrada:** Para continuar la línea, apoya el meñique, arranca el movimiento de la mano en el aire con la máquina inclinada a 70° y **entra en la piel sobre la zona gris desvanecida**, hundiendo la aguja gradualmente hasta recuperar la profundidad completa.
4. El resultado visual es una línea monolítica donde nadie puede distinguir dónde se levantó la aguja.

---

## 5. La Espina Cybersigilism: El Latigazo Cónico (Tapered Flick)

El Cybersigilism no está compuesto por líneas rectas aburridas; está formado por **espinas orgánicas dinámicas**, como garras, raíces afiladas, exoesqueletos de insecto o agujas de hueso (observa la referencia `01_Cybersigilism_Biomecanico_Brazo.jpeg`).

```
 BASE GRUESA                   CUERPO EN TENSIÓN                PUNTA AFILADA (0 mm)
     |==============               =============                     --------->
     |                 \         /                                 /
     |                   \_____/                                  /  (Flick al vuelo)
```

### El movimiento en 3 tiempos:
1. **Tiempo 1 — El Anclaje (Base):** Clava la aguja **1205RL** con decisión en la base de la espina a **7.4V**, con una ligera pausa de 0.2 segundos para saturar el negro inicial.
2. **Tiempo 2 — La Conducción (Cuerpo):** Tira de la línea siguiendo la curvatura del diseño. Mantén la velocidad constante durante el primer 70% del recorrido.
3. **Tiempo 3 — El Latigazo (Punta - Flick):** En el 30% final, acelera el movimiento de la muñeca y **despega la máquina de la piel hacia arriba** en un arco parabólico rápido.
   * La aguja va perdiendo contacto progresivamente con el soporte hasta que la punta se desvanece en una micro-línea más fina que el diámetro propio de la aguja.
   * Si la punta te queda redonda o roma, significa que levantaste la aguja verticalmente de golpe en lugar de lanzarla hacia adelante en ángulo rasante.

---

## 6. Las Ramificaciones Biomecánicas (Nudos y Tendones)

En tus referencias `01` y `08`, varias espinas nacen de un mismo punto o se cruzan formando "nudos de articulación":
* **Orden de trazado:** Traza primero la **espina principal (la más larga y gruesa)**.
* Luego, traza las espinas secundarias **naciendo desde adentro del cuerpo de la primera**. Nunca dejes un hueco en blanco entre la espina madre y la hija; deben fundirse orgánicamente.
* Para crear volumen óseo, añade una micro-sombra en el ángulo de intersección usando la técnica de puntillismo (*stippling*) a **5.2V**.

---

> [!TIP]
> **Plan de entrenamiento del Bloque 2:**
> 1. Mira la videoteca del Bloque 2 para observar el movimiento de latigazo en video real.
> 2. Imprime la **Plantilla 03** y practica el test de reverso y los empalmes en 3 tramos.
> 3. Imprime la **Plantilla 04** y ejecuta el proyecto guiado: **"El Sigilo del Hombro"**.
"""

with open(os.path.join(B2_DIR, "01_MANUAL_CALIGRAFIA_Y_ESPINAS_CYBER.md"), "w", encoding="utf-8") as f:
    f.write(manual_content)
print("Creado 01_MANUAL_CALIGRAFIA_Y_ESPINAS_CYBER.md")

# ---------------------------------------------------------
# 2. ARCHIVO: 02_VIDEOTECA_YOUTUBE_PRACTICA_LINEA.md
# ---------------------------------------------------------
videoteca_content = """# Bloque 2 — Videoteca: Empalmes Invisibles y Técnica Cybersigilism

En este bloque nos centramos en la destreza manual fina. Estos videos seleccionados muestran exactamente cómo solapar trazos y cómo dibujar y tatuar formas de neo-tribal y cybersigilism con fluidez.

---

## 1. Técnica de Empalme Invisible y Solapamiento de Líneas

### 🎥 [Tattooing 101: How To Connect Tattoo Lines (Daniel Yuck)](https://www.youtube.com/watch?v=kccPi8BOhHQ)
* **Qué observar:** Daniel Yuck muestra cómo desvanecer la línea al salir (*taper out*) y cómo reanudar entrando suavemente dentro del trazo anterior (*taper in*) para que la unión sea 100% indetectable.
* **Detalle clave:** Fíjate en cómo utiliza el dedo meñique para frenar la inercia de la mano al conectar las líneas.

### 🎥 [How To Join Tattoo Lines Without Bumps (Tattooing 101)](https://www.youtube.com/watch?v=IawDTs7K9KM)
* **Qué observar:** Los errores más comunes de los principiantes (dejar gotas negras en los empalmes o crear desviaciones de ángulo) y cómo evitarlos con la técnica del ángulo rasante de 30°.

### 🎥 [Back To Basics: Line Work Tutorial & Hand Mechanics (Tattooing 101)](https://www.youtube.com/watch?v=K71ejXCZtLQ)
* **Qué observar:** Demostración en vivo de tracción de líneas largas empalmadas sobre piel sintética, control del ritmo respiratorio y estabilidad del codo.

---

## 2. Cybersigilism y Neo-Tribal: Fluidez de Espinas y Latigazo

### 🎥 [How to Design & Flow: Cybersigilism Neo-Tribal Ornamental Tattoo (@va2xan)](https://www.youtube.com/watch?v=4tVbN-hmYKA)
* **Qué observar:** Cómo estructurar las curvas biomecánicas, el balance de peso visual entre espinas principales y ramas secundarias, y cómo colocar los sigilos siguiendo la musculatura del cuerpo (hombro, antebrazo y espalda).

### 🎥 [Cómo Diseñar Neotribales / Digital y Tradicional (Alexgaelbs - En Español)](https://www.youtube.com/watch?v=guqyMN4mhjE)
* **Qué observar:** Desglose en español de la geometría de las espinas, el grosor cónico dinámico y la transición entre formas curvas y vértices punzantes.

### 🎥 [Neo Tribal Tattoo RealTime Tutorial: Lining & Tapering (Leoskulltattoos)](https://www.youtube.com/watch?v=l8RJ1l5cP9E)
* **Qué observar:** Sesión real de tatuaje en tiempo real. Presta especial atención al movimiento de "latigazo al vuelo" de la mano al terminar cada punta de espina.

---

> [!IMPORTANT]
> **Ejercicio recomendado antes de encender la máquina:**
> Coge un bolígrafo o rotulador de punta fina sobre un folio en blanco. Practica el movimiento de "flick" (latigazo) haciendo 50 espinas rápidas. Tu mano debe despegar del papel como un avión despegando de una pista, nunca frenando en seco. Cuando tu mano domine ese gesto en papel, trasládalo al pen Poseidon sobre la silicona.
"""

with open(os.path.join(B2_DIR, "02_VIDEOTECA_YOUTUBE_PRACTICA_LINEA.md"), "w", encoding="utf-8") as f:
    f.write(videoteca_content)
print("Creado 02_VIDEOTECA_YOUTUBE_PRACTICA_LINEA.md")

# ---------------------------------------------------------
# 3. PLANTILLA 03: CONTROL DE PROFUNDIDAD Y EMPALMES INVISIBLES
# ---------------------------------------------------------
def create_sheet_3(filename):
    c = canvas.Canvas(filename, pagesize=A4)
    w, h = A4 # 595.27 x 841.89
    
    # Encabezado
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(colors.HexColor("#111111"))
    c.drawString(35, h - 45, "CURSO PROFESIONAL DE TATUAJE — PLANTILLA 03")
    
    c.setFont("Helvetica", 9)
    c.setFillColor(colors.HexColor("#555555"))
    c.drawString(35, h - 60, "Bloque 2: Caligrafía de Línea, Empalmes Invisibles y Test de Profundidad | Aguja: 1205RL | Voltaje: 7.5V")
    
    c.setStrokeColor(colors.HexColor("#222222"))
    c.setLineWidth(1.2)
    c.line(35, h - 68, w - 35, h - 68)
    
    # ------------------ SECCIÓN 1: EL TEST DEL REVERSO (3 PROFUNDIDADES) ------------------
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(colors.HexColor("#000000"))
    c.drawString(35, h - 88, "EJERCICIO 1: TEST DE CALIBRACIÓN DE PROFUNDIDAD (AUDITORÍA DEL REVERSO)")
    c.setFont("Helvetica-Oblique", 8)
    c.setFillColor(colors.HexColor("#666666"))
    c.drawString(35, h - 100, "Traza cada par de líneas a la profundidad indicada. Al terminar, gira la silicona y comprueba la marca trasera.")
    
    y = h - 120
    profundidades = [
        ("Nivel A: Superficial (<1 mm - Presión de pluma muy suave)", "#777777", 0.6),
        ("Nivel B: Dermis Óptima (1.5 mm - Profundidad real de tatuaje)", "#222222", 1.0),
        ("Nivel C: Profunda (>2.2 mm - Peligro de perforación y blowout)", "#000000", 1.5)
    ]
    for label, stroke_col, lw in profundidades:
        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(colors.HexColor(stroke_col))
        c.drawString(45, y, label)
        c.setStrokeColor(colors.HexColor(stroke_col))
        c.setLineWidth(lw)
        c.line(45, y - 10, w - 45, y - 10)
        c.line(45, y - 18, w - 45, y - 18)
        y -= 32
        
    # ------------------ SECCIÓN 2: EMPALMES INVISIBLES EN 3 TRAMOS ------------------
    y -= 5
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(colors.HexColor("#000000"))
    c.drawString(35, y, "EJERCICIO 2: TÉCNICA DE EMPALME INVISIBLE (LÍNEAS SEGMENTADAS DE 15 CM)")
    c.setFont("Helvetica-Oblique", 8)
    c.setFillColor(colors.HexColor("#666666"))
    c.drawString(35, y - 12, "Cada línea está dividida en 3 tramos de 5 cm. Aligera en el rombo gris y reanuda entrando suavemente en ángulo.")
    
    y_lines = y - 32
    c.setLineWidth(0.8)
    for row in range(5):
        ly = y_lines - row * 24
        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(colors.HexColor("#444444"))
        c.drawString(35, ly - 3, f"L{row+1}:")
        
        # Tramo 1 (45 a 195)
        c.setStrokeColor(colors.HexColor("#222222"))
        c.line(55, ly, 200, ly)
        # Rombo de empalme 1
        c.setFillColor(colors.HexColor("#BBBBBB"))
        pr1 = c.beginPath()
        pr1.moveTo(200, ly - 3)
        pr1.lineTo(215, ly)
        pr1.lineTo(200, ly + 3)
        pr1.lineTo(185, ly)
        pr1.close()
        c.drawPath(pr1, fill=1, stroke=0)
        
        # Tramo 2 (205 a 360)
        c.setStrokeColor(colors.HexColor("#222222"))
        c.line(205, ly, 370, ly)
        # Rombo de empalme 2
        c.setFillColor(colors.HexColor("#BBBBBB"))
        pr2 = c.beginPath()
        pr2.moveTo(370, ly - 3)
        pr2.lineTo(385, ly)
        pr2.lineTo(370, ly + 3)
        pr2.lineTo(355, ly)
        pr2.close()
        c.drawPath(pr2, fill=1, stroke=0)
        
        # Tramo 3 (375 a 540)
        c.setStrokeColor(colors.HexColor("#222222"))
        c.line(375, ly, w - 45, ly)
        
    # ------------------ SECCIÓN 3: ONDAS DE PRESIÓN MODULADA (ANCHO VARIABLE) ------------------
    y = y_lines - 130
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(colors.HexColor("#000000"))
    c.drawString(35, y, "EJERCICIO 3: ONDAS DE PRESIÓN DINÁMICA (CONTROL DE ESPESOR POR INCLINACIÓN)")
    c.setFont("Helvetica-Oblique", 8)
    c.setFillColor(colors.HexColor("#666666"))
    c.drawString(35, y - 12, "Modula suavemente la velocidad de la mano y la inclinación del pen para ensanchar y afilar el trazo orgánico.")
    
    y_mod = y - 28
    for row in range(3):
        my = y_mod - row * 38
        p = c.beginPath()
        p.moveTo(45, my)
        for segment in range(4):
            sx = 45 + segment * 125
            # Curva superior e inferior que simula línea modulada
            p.curveTo(sx + 30, my + 15, sx + 60, my + 15, sx + 62, my)
            p.curveTo(sx + 65, my - 15, sx + 95, my - 15, sx + 125, my)
        c.setStrokeColor(colors.HexColor("#222222"))
        c.setLineWidth(1.2)
        c.drawPath(p, stroke=1, fill=0)
        
    # ------------------ SECCIÓN 4: UNIONES EN 'Y' BIOMECÁNICAS Y VÉRTICES CYBER ------------------
    y = y_mod - 125
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(colors.HexColor("#000000"))
    c.drawString(35, y, "EJERCICIO 4: CRUCES EN 'Y' BIOMECÁNICOS Y VÉRTICES AGUDOS")
    c.setFont("Helvetica-Oblique", 8)
    c.setFillColor(colors.HexColor("#666666"))
    c.drawString(35, y - 12, "Las ramas secundarias nacen desde el interior de la línea principal sin dejar huecos en blanco.")
    
    y_joint = y - 30
    # 5 nudos biomecánicos
    for k in range(5):
        jx = 65 + k * 105
        # Línea vertebral
        c.setStrokeColor(colors.HexColor("#1A1A1A"))
        c.setLineWidth(1.4)
        c.line(jx, y_joint + 35, jx, y_joint - 35)
        # Ramas laterales en Y
        c.setLineWidth(1.0)
        p = c.beginPath()
        p.moveTo(jx, y_joint + 10)
        p.curveTo(jx + 25, y_joint + 15, jx + 35, y_joint + 30, jx + 40, y_joint + 35)
        c.drawPath(p, stroke=1, fill=0)
        
        p = c.beginPath()
        p.moveTo(jx, y_joint + 10)
        p.curveTo(jx - 25, y_joint + 15, jx - 35, y_joint + 30, jx - 40, y_joint + 35)
        c.drawPath(p, stroke=1, fill=0)
        
        p = c.beginPath()
        p.moveTo(jx, y_joint - 10)
        p.curveTo(jx + 25, y_joint - 15, jx + 35, y_joint - 30, jx + 40, y_joint - 35)
        c.drawPath(p, stroke=1, fill=0)
        
        p = c.beginPath()
        p.moveTo(jx, y_joint - 10)
        p.curveTo(jx - 25, y_joint - 15, jx - 35, y_joint - 30, jx - 40, y_joint - 35)
        c.drawPath(p, stroke=1, fill=0)
        
    # Pie de página
    c.setFont("Helvetica", 7)
    c.setFillColor(colors.HexColor("#888888"))
    c.drawString(35, 20, "Material del Curso Personalizado de Tatuaje — Bloque 2 | Imprimir en A4 al 100% de escala")
    c.drawRightString(w - 35, 20, "Página 1 de 2 | Poseidon HM142-2 (1205RL)")
    
    c.showPage()
    c.save()
    print("Generado PDF:", filename)

# ---------------------------------------------------------
# 4. PLANTILLA 04: MAESTRÍA EN ESPINAS CYBERSIGILISM Y PROYECTO
# ---------------------------------------------------------
def create_sheet_4(filename):
    c = canvas.Canvas(filename, pagesize=A4)
    w, h = A4
    
    # Encabezado
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(colors.HexColor("#111111"))
    c.drawString(35, h - 45, "CURSO PROFESIONAL DE TATUAJE — PLANTILLA 04")
    
    c.setFont("Helvetica", 9)
    c.setFillColor(colors.HexColor("#555555"))
    c.drawString(35, h - 60, "Bloque 2: Maestría en Espinas Cybersigilism y Proyecto 'Sigilo del Hombro' | Aguja: 1205RL | Voltaje: 7.2V - 7.5V")
    
    c.setStrokeColor(colors.HexColor("#222222"))
    c.setLineWidth(1.2)
    c.line(35, h - 68, w - 35, h - 68)
    
    # ------------------ SECCIÓN 1: ESPINAS EN LAS 8 DIRECCIONES (BRÚJULA CYBER) ------------------
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(colors.HexColor("#000000"))
    c.drawString(35, h - 88, "EJERCICIO 1: RÁFAGA DE ESPINAS EN 8 DIRECCIONES (LATIGAZO MULTI-ANGULAR)")
    c.setFont("Helvetica-Oblique", 8)
    c.setFillColor(colors.HexColor("#666666"))
    c.drawString(35, h - 100, "Aprende a ejecutar el latigazo hacia cualquier dirección sin forzar la postura del hombro ni doblar la muñeca.")
    
    # 3 Estrellas de espinas cónicas
    y_star = h - 170
    centers = [120, 297, 475]
    for cx in centers:
        # Núcleo
        c.setFillColor(colors.HexColor("#111111"))
        c.circle(cx, y_star, 4, fill=1, stroke=0)
        for deg in range(0, 360, 45):
            rad = math.radians(deg)
            # Base a 10 pt del centro, punta a 50 pt
            b_x = cx + 8 * math.cos(rad)
            b_y = y_star + 8 * math.sin(rad)
            tip_x = cx + 48 * math.cos(rad)
            tip_y = y_star + 48 * math.sin(rad)
            
            p_rad = rad + math.pi / 2
            p1_x = b_x + 2.5 * math.cos(p_rad)
            p1_y = b_y + 2.5 * math.sin(p_rad)
            p2_x = b_x - 2.5 * math.cos(p_rad)
            p2_y = b_y - 2.5 * math.sin(p_rad)
            
            p = c.beginPath()
            p.moveTo(p1_x, p1_y)
            p.lineTo(tip_x, tip_y)
            p.lineTo(p2_x, p2_y)
            p.close()
            c.drawPath(p, fill=1, stroke=0)
            
    # ------------------ SECCIÓN 2: ESPINAS CURVAS ORGÁNICAS (RAÍCES Y CUERNOS BIOMECÁNICOS) ------------------
    y = y_star - 80
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(colors.HexColor("#000000"))
    c.drawString(35, y, "EJERCICIO 2: ESPINAS CURVAS ORGÁNICAS ENLAZADAS (ESTILO ARTICULACIÓN)")
    c.setFont("Helvetica-Oblique", 8)
    c.setFillColor(colors.HexColor("#666666"))
    c.drawString(35, y - 12, "Inspirado en la manga de hueso y araña (Ref. 01). Traza el cuerpo curvado y remata en filo de cuchillo.")
    
    y_horns = y - 30
    for col in range(4):
        hx = 65 + col * 135
        # Espina curva izquierda
        p = c.beginPath()
        p.moveTo(hx, y_horns - 15)
        p.curveTo(hx + 10, y_horns + 10, hx + 35, y_horns + 25, hx + 55, y_horns + 30)
        p.curveTo(hx + 30, y_horns + 20, hx + 12, y_horns + 5, hx + 3, y_horns - 15)
        p.close()
        c.setFillColor(colors.HexColor("#222222"))
        c.drawPath(p, fill=1, stroke=0)
        
        # Espina curva contraria entrelazada
        p2 = c.beginPath()
        p2.moveTo(hx + 15, y_horns - 20)
        p2.curveTo(hx + 30, y_horns - 10, hx + 45, y_horns - 25, hx + 65, y_horns - 20)
        p2.curveTo(hx + 42, y_horns - 18, hx + 28, y_horns - 8, hx + 18, y_horns - 20)
        p2.close()
        c.setFillColor(colors.HexColor("#222222"))
        c.drawPath(p2, fill=1, stroke=0)
        
    # ------------------ SECCIÓN 3: PROYECTO REAL BLOQUE 2: 'EL SIGILO DEL HOMBRO' ------------------
    y = y_horns - 75
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(colors.HexColor("#000000"))
    c.drawString(35, y, "EJERCICIO 3 (PROYECTO COMPLETO): 'EL SIGILO DEL HOMBRO' — CYBERSIGILISM ORNAMENTAL")
    c.setFont("Helvetica-Oblique", 8)
    c.setFillColor(colors.HexColor("#666666"))
    c.drawString(35, y - 12, "Tu primer proyecto terminado: tatúa este sigilo completo en tu piel sintética aplicando empalmes y espinas cónicas.")
    
    # Dibujo de gran formato centrado
    center_x = w / 2
    proj_y = y - 130
    
    # Marco guía tenue de la piel
    c.setStrokeColor(colors.HexColor("#E0E0E0"))
    c.setLineWidth(0.5)
    c.rect(center_x - 180, proj_y - 105, 360, 215, stroke=1, fill=0)
    c.setFont("Helvetica", 7)
    c.setFillColor(colors.HexColor("#AAAAAA"))
    c.drawString(center_x - 175, proj_y - 100, "Zona de piel sintética (15 x 10 cm)")
    
    # 1. Columna vertebral central del sigilo
    c.setStrokeColor(colors.HexColor("#1A1A1A"))
    c.setLineWidth(1.6)
    spine = c.beginPath()
    spine.moveTo(center_x, proj_y + 85)
    spine.curveTo(center_x - 8, proj_y + 40, center_x + 8, proj_y - 20, center_x, proj_y - 75)
    c.drawPath(spine, stroke=1, fill=0)
    
    # Nódulo central
    c.setFillColor(colors.HexColor("#1A1A1A"))
    c.circle(center_x, proj_y + 10, 4.5, fill=1, stroke=0)
    c.circle(center_x, proj_y + 55, 3, fill=1, stroke=0)
    c.circle(center_x, proj_y - 35, 3, fill=1, stroke=0)
    
    # 2. Alas simétricas de espinas Cybersigilism
    for side in [-1, 1]:
        # Espina Cresta Superior
        p = c.beginPath()
        p.moveTo(center_x, proj_y + 70)
        p.curveTo(center_x + side * 45, proj_y + 90, center_x + side * 110, proj_y + 80, center_x + side * 155, proj_y + 95)
        p.curveTo(center_x + side * 105, proj_y + 74, center_x + side * 42, proj_y + 80, center_x, proj_y + 65)
        p.close()
        c.setFillColor(colors.HexColor("#222222"))
        c.drawPath(p, fill=1, stroke=0)
        
        # Espina Secundaria hacia arriba
        p = c.beginPath()
        p.moveTo(center_x + side * 50, proj_y + 78)
        p.curveTo(center_x + side * 75, proj_y + 105, center_x + side * 105, proj_y + 115, center_x + side * 125, proj_y + 125)
        p.curveTo(center_x + side * 100, proj_y + 108, center_x + side * 70, proj_y + 98, center_x + side * 48, proj_y + 75)
        p.close()
        c.drawPath(p, fill=1, stroke=0)
        
        # Gran Espina Media (Arco de hombro)
        p = c.beginPath()
        p.moveTo(center_x, proj_y + 15)
        p.curveTo(center_x + side * 60, proj_y + 25, center_x + side * 125, proj_y - 5, center_x + side * 165, proj_y + 15)
        p.curveTo(center_x + side * 120, proj_y - 15, center_x + side * 55, proj_y + 12, center_x, proj_y + 5)
        p.close()
        c.drawPath(p, fill=1, stroke=0)
        
        # Espina Gancho Descendente
        p = c.beginPath()
        p.moveTo(center_x + side * 40, proj_y + 10)
        p.curveTo(center_x + side * 70, proj_y - 20, center_x + side * 110, proj_y - 35, center_x + side * 135, proj_y - 25)
        p.curveTo(center_x + side * 105, proj_y - 30, center_x + side * 68, proj_y - 15, center_x + side * 38, proj_y + 5)
        p.close()
        c.drawPath(p, fill=1, stroke=0)
        
        # Espinas Inferiores de Cierre (Cola biomecánica)
        p = c.beginPath()
        p.moveTo(center_x, proj_y - 30)
        p.curveTo(center_x + side * 35, proj_y - 45, center_x + side * 75, proj_y - 65, center_x + side * 105, proj_y - 55)
        p.curveTo(center_x + side * 70, proj_y - 60, center_x + side * 32, proj_y - 42, center_x, proj_y - 38)
        p.close()
        c.drawPath(p, fill=1, stroke=0)
        
    # Micro-puntos de constelación colgante (estilo chandelier)
    for side in [-1, 1]:
        for dot_idx, (dx, dy) in enumerate([(45, -70), (75, -82), (105, -75), (135, -45)]):
            c.circle(center_x + side * dx, proj_y + dy, 1.8, fill=1, stroke=0)
            
    # Pie de página
    c.setFont("Helvetica", 7)
    c.setFillColor(colors.HexColor("#888888"))
    c.drawString(35, 20, "Material del Curso Personalizado de Tatuaje — Bloque 2 | Imprimir en A4 al 100% de escala")
    c.drawRightString(w - 35, 20, "Página 2 de 2 | Poseidon HM142-2 (1205RL)")
    
    c.showPage()
    c.save()
    print("Generado PDF:", filename)

# Generar ambos PDFs de Bloque 2
create_sheet_3(os.path.join(SHEETS_DIR, "03_Plantilla_Control_Profundidad_Y_Empalmes.pdf"))
create_sheet_4(os.path.join(SHEETS_DIR, "04_Plantilla_Maestria_Espinas_Cybersigilism.pdf"))
print("Todo el Bloque 2 se ha completado satisfactoriamente.")
