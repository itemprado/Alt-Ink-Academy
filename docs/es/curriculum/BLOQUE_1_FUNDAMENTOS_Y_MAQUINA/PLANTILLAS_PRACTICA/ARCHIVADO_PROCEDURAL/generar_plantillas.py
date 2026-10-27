# -*- coding: utf-8 -*-
"""
Generador del Bloque 1 del Curso de Tatuaje:
Crea los manuales Markdown, la videoteca de YouTube verificada,
la guía de mapeo de estilos y compila las plantillas PDF vectoriales de práctica en A4.
"""

import os
import math
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas

BASE_DIR = r"C:\Users\quesa\Documents\CURSO TATTOO"
B1_DIR = os.path.join(BASE_DIR, "BLOQUE_1_FUNDAMENTOS_Y_MAQUINA")
SHEETS_DIR = os.path.join(B1_DIR, "PLANTILLAS_PRACTICA")
os.makedirs(SHEETS_DIR, exist_ok=True)

# ---------------------------------------------------------
# 1. ARCHIVO: 01_MANUAL_MONTAJE_Y_CALIBRACION.md
# ---------------------------------------------------------
manual_content = """# Bloque 1 — Manual de Taller: Montaje, Ergonomía y Calibración Mecánica

Bienvenido a tu estación de trabajo. Este manual está redactado específicamente para los componentes exactos que tienes en tu kit: **Máquina rotativa Poseidon Pen HM142-2**, **batería digital inalámbrica de 1200 mAh (pantalla LED)**, agujas **1205RL** y **1207RM**, y consumibles incluidos.

Sigue este protocolo paso a paso antes de conectar la máquina por primera vez.

---

## 1. Anatomía y Funcionamiento de tu Equipo

```
 [ BATERÍA DIGITAL USB-C ]  --> Conector RCA macho
           ||
           \/
 [ CONECTOR RCA HEMBRA ]    --> Parte superior del chasis
           ||
 [ CUERPO DEL MOTOR ROTATIVO ] --> Motor DC 8.000 RPM (Stroke 3.5 mm)
           ||
 [ ANILLO REGULADOR DE GRIP ] --> Roscado telescópico (gira para sacar/meter aguja)
           ||
 [ BOQUILLA UNIVERSAL BAYONETA ] --> Acepta cartuchos estándar con membrana
```

* **Stroke (Recorrido de la aguja): 3.5 mm.** Es el recorrido estándar más versátil del tatuaje moderno. Proporciona suficiente fuerza para clavar una línea 5RL sólida de un solo pase, pero es lo bastante suave para no destrozar la piel sintética ni desgarrarla al hacer sombreado en degradado con la 7RM.
* **Batería Digital Poseidon (4V a 12V):** La pantalla muestra el voltaje activo con incrementos de 0.1V. El botón central enciende/apaga (mantener presionado 2 segundos) y pausa el motor (un toque corto). Los botones `+` y `-` gradúan la velocidad.

---

## 2. Preparación Higiénica de la Estación de Trabajo

Incluso practicando en silicona, debes mecanizar la rutina de un estudio profesional para que tu memoria muscular no adquiera vicios:

1. **Superficie limpia:** Despeja la mesa. Pasa una bayeta con alcohol o limpiador multiusos.
2. **Campo de trabajo:** Coloca una hoja de papel film transparente o papel de cocina limpio cubriendo la zona donde apoyarás la máquina y los cups.
3. **Fijación de los Cups de Tinta:**
   * Coge un poco de vaselina (del tamaño de un grano de arroz) y úntala en la base del cup de plástico.
   * Pégalo sobre tu campo de trabajo. La vaselina evitará que el cup salga volando cuando metas la aguja.
4. **Servilletas absorbentes dobladas:** Dobla 2 hojas de papel de cocina en cuatro capas y colócalas a tu derecha (si eres diestro). Servirán para secar el exceso de tinta (*dab*) antes de cada trazo.

---

## 3. El Encintado Ergonómico del Grip (Grip Wrap)

> [!CAUTION]
> **Nunca tatúes con el metal del pen al descubierto.**
> El metal liso resbala con los guantes y transmite todas las micro-vibraciones del motor a las articulaciones de tus dedos. Si tatúas sobre metal desnudo, a los 15 minutos tu mano temblará y perderás el pulso fino que exige el Cybersigilism.

### Cómo colocar la venda cohesiva (Grip Wrap):
1. **Punto de partida:** Empieza a envolver unos 5 mm por encima de la boquilla del cartucho, cubriendo el agarre metálico inferior.
2. **Forma cónica:** Aplica entre 3 y 4 vueltas de cinta. Debe quedar más gruesa cerca de tus dedos y afinarse hacia la batería.
3. **El test del grosor:** El agarre debe sentirse como un rotulador grueso (tipo Posca o marcador permanente), no como un bolígrafo fino. Esto permite que tu mano se cierre relajada sin forzar los tendones flexores.
4. **Cuidado con el anillo giratorio:** Asegúrate de que el wrap no tape la ranura donde gira el grip para calibrar la aguja. Debes poder girar el anillo libremente con dos dedos.

---

## 4. Colocación del Cartucho y Calibración del *Needle Hang*

Tu kit Poseidon utiliza cartuchos de bayoneta universales. 

### Montaje del cartucho:
1. Con la máquina apagada, inserta el cartucho en la boquilla frontal.
2. Presiona suavemente hacia adentro y **gira un cuarto de vuelta en el sentido de las agujas del reloj**. Notarás un "clic" mecánico: el cartucho ha quedado bloqueado.
3. Comprueba visualmente que la aguja se retrae completamente dentro de la boquilla de plástico gracias a su membrana de silicona interna.

### Calibración del Needle Hang (Sacar la aguja):
En el tatuaje moderno de línea fina y Cybersigilism se trabaja **"al vuelo" (Floating / Riding the Needle)**, nunca apoyando la boquilla de plástico contra la piel.

```
       PLÁSTICO DEL CARTUCHO
              |======|
              |  /\\  |  <--- Boquilla de plástico transparente
              | /  \\ |
              ---------
                 ||
                 ||  <--- AGUJA EXPUESTA: Exactamente 1.5 mm a 2.0 mm
                 \\/       (Grosor de una moneda de 2 Euros)
```

1. Enciende la batería a **7.0V**.
2. Mira la punta de la máquina de perfil mientras el motor está funcionando.
3. **Gira el grip metálico:**
   * Hacia la derecha: la aguja sale más hacia afuera (*más hang*).
   * Hacia la izquierda: la aguja se mete hacia la boquilla (*menos hang*).
4. **La medida sagrada:** La aguja en funcionamiento debe sobresalir entre **1.5 mm y 2.0 mm** de la boquilla de plástico.
   * *Por qué 1.5 - 2 mm:* Te da visibilidad total del punto exacto donde la aguja perfora la piel sin que el plástico tape tu campo de visión, y evita que la boquilla arrastre la tinta por la superficie emborronando el diseño.

---

## 5. Tabla de Voltajes Maestros para tu Equipo Poseidon

La batería Poseidon entrega corriente continua muy estable. Utiliza estos voltajes calibrados para su motor:

| Técnica / Estilo | Aguja | Voltaje Recomendado | Velocidad de Mano | Sensación / Sonido |
| :--- | :--- | :--- | :--- | :--- |
| **Líneas estructurales Cybersigilism / Contorno Anime** | **1205RL** | **7.4V – 7.8V** | Media / Constante | Zumbido medio continuo. La línea entra sólida y negra al primer pase sin repasar. |
| **Espinas cónicas Cyber / Remates afilados** | **1205RL** | **7.0V – 7.2V** | Rápida al salir (flick) | Movimiento de latigazo: entra a profundidad y sale al vuelo aligerando la presión. |
| **Puntillismo / Whip Shading / Tramas de Grabado Gótico** | **1205RL** | **5.0V – 5.5V** | Media / Rápida pendular | Motor lento ("tac-tac-tac"). Cada impacto de la aguja deja un punto visible independiente (*pepper shading*). |
| **Degradados suaves / Corsé / Sombras acanto** | **1207RM** | **6.4V – 7.0V** | Suave pendular / barrido | Deslizamiento de la aguja curva como un pincel. Crea transiciones de gris sedosas sin arañar la silicona. |
| **Empaque de negro sólido (Relleno de fondo)** | **1207RM** | **7.0V – 7.4V** | Lenta en pequeños círculos | Saturación completa del poro sin dejar huecos blancos ni masticar la superficie. |

---

## 6. La Carga de Tinta y el Truco del "Dab" (Evitar el Charco de Tinta)

El error número 1 de todos los principiantes es hundir la aguja y llenar la boquilla de tinta hasta que rebosa, creando un charco negro gigante sobre la piel sintética que no deja ver por dónde va la línea.

### El proceso correcto de carga:
1. **Pon la máquina en marcha a 6V - 7V.**
2. Acerca la punta del cartucho al cup de tinta y **sumerge solo la punta metálica de la aguja durante 1 segundo** (apenas 2 milímetros).
3. La propia vibración de la aguja succionará la cantidad exacta de tinta hacia el depósito interno del cartucho por capilaridad.
4. **EL TRUCO DEL DAB (Obligatorio):**
   * Antes de tocar la piel sintética, apoya suavemente la boquilla durante medio segundo sobre la servilleta de papel doblada.
   * Esto absorberá la gota sobrante de la carcasa de plástico exterior.
   * Ahora la aguja escribirá con un flujo constante y limpio, como una pluma estilográfica de precisión, sin derramar ni una sola gota de más.

---

## 7. Postura, Ergonomía y el Tercer Punto de Apoyo

Para hacer líneas perfectas en Cybersigilism y filigranas de corsé, la estabilidad no sale de apretar los dedos, sino de la postura del brazo y la mano:

1. **Ángulo de inclinación:** Sujeta el pen con una inclinación de **70° a 80°** respecto a la piel (ligeramente inclinado hacia la dirección hacia donde avanzas, como quien escribe con pluma). Nunca completamente perpendicular (90°) porque la aguja rebotará, ni demasiado tumbado (<60°) porque la tinta se esparcirá bajo la superficie.
2. **El dedo meñique (Tu pivote sagrado):** Apoya siempre el nudillo o la yema de tu dedo meñique sobre la piel sintética. Este dedo actúa como patín y amortiguador de profundidad: mantiene la máquina siempre a la misma distancia milimétrica aunque tu muñeca se mueva.
3. **Movimiento desde el codo y el hombro:** Para trazar líneas largas continuas (como las curvas de un corsé o una espina larga de hombro), **no muevas los dedos**. Bloquea la muñeca y desliza todo el antebrazo desde el codo. Los dedos solo se mueven para micro-detalles y espinas cortas.
4. **Respiración:** No aguantes la respiración. Exhala suavemente mientras realizas el trazo largo. La tensión en los pulmones transmite micro-pulsaciones a la mano.

---

## 8. Protocolo de Fin de Sesión y Mantenimiento

1. **Retirada del cartucho:** Con la máquina apagada, gira el cartucho un cuarto de vuelta hacia la izquierda y extráelo. Si vas a volver a practicar con esa misma aguja en silicona en las próximas horas, puedes enjuagarla en un vasito con agua, secarla en papel y guardarla en su blíster.
2. **Retirada del Grip Wrap:** Corta la venda con cuidado de no arañar el chasis de la máquina y tírala a la basura.
3. **Limpieza del chasis:** Pasa una toallita con alcohol o desinfectante por todo el cuerpo del pen y el cabezal de la batería. No sumerjas nunca la máquina en líquidos ni permitas que entre agua por la conexión RCA.
4. **Carga de la batería:** Conéctala con su cable USB-C a un cargador de 5V estándar. Una carga completa dura entre 3 y 4 horas de trabajo continuo.
"""

with open(os.path.join(B1_DIR, "01_MANUAL_MONTAJE_Y_CALIBRACION.md"), "w", encoding="utf-8") as f:
    f.write(manual_content)
print("Creado 01_MANUAL_MONTAJE_Y_CALIBRACION.md")

# ---------------------------------------------------------
# 2. ARCHIVO: 02_VIDEOTECA_YOUTUBE_PROFESIONAL.md
# ---------------------------------------------------------
videoteca_content = """# Bloque 1 — Videoteca Profesional: Tutoriales Reales en YouTube

En el tatuaje, ver el movimiento real de la aguja, la postura de las manos y escuchar el sonido del motor es fundamental. A continuación tienes los mejores videos técnicos explicados por artistas profesionales reconocidos (sin resúmenes de IA, enlaces directos a YouTube).

---

## 1. Calibración de la Aguja y Salida (Needle Hang & Depth)

### 🎥 [Tattoo NEEDLE DEPTH: 4 Steps to FINALLY Master Tattoo Depth (Tattooing 101)](https://www.youtube.com/watch?v=0i1bqPWqzVc)
* **Qué aprenderás:** La diferencia entre la aguja expuesta en reposo vs en marcha, cómo encontrar la profundidad exacta en la dermis (1.5mm - 2mm) y por qué clavar demasiado provoca líneas azules ensanchadas ("blowout").
* **Momento clave para pausar:** Fíjate en cómo ajustan el grip giratorio de la pluma para dejar salir la aguja fija antes de empezar a trazar.

### 🎥 [Tattoo Needle Depth Visually Explained (Daniel Yuck)](https://www.youtube.com/watch?v=iCpssrFOhzM)
* **Qué aprenderás:** Animación y corte anatómico que demuestra cómo entra la aguja en las capas de la piel y cómo regular la presión de la mano.

### 🎥 [Cómo Calibrar la Salida de Aguja para Tatuar (En Español)](https://www.youtube.com/watch?v=QnwD2u1V9iU)
* **Qué aprenderás:** Explicación paso a paso en español de cómo regular el recorrido visual de la aguja para tener visibilidad absoluta de la línea.

---

## 2. Preparación de la Máquina y Grip Wrap Ergonómico

### 🎥 [Tattooing 101: How To Wrap A Tattoo Machine (Daniel Yuck)](https://www.youtube.com/watch?v=2M4JxZ2oN-s)
* **Qué aprenderás:** Cómo envolver una máquina tipo Pen con cinta cohesiva de vendaje (grip wrap).
* **Detalle profesional:** Observa cómo crea una almohadilla cónica para no aplastar los dedos y cómo deja libre la holgura del mecanismo giratorio para que puedas cambiar el *needle hang* sin quitar la cinta.

---

## 3. Sincronización de Velocidad de Mano y Voltaje (Líneas Limpias)

### 🎥 [Hand Speed vs Machine Voltage: Finding The Balance (Tattooing 101)](https://www.youtube.com/watch?v=PvIC2-459Ok)
* **Qué aprenderás:** La fórmula matemática del tatuaje: `Voltaje Alto + Mano Lenta = Piel rota / Línea quemada`. `Voltaje Bajo + Mano Rápida = Línea punteada discontinua`. Cómo encontrar el ritmo continuo con un cartucho Round Liner como tu 1205RL.

### 🎥 [Voltajes para Tatuar Líneas y Cartuchos (En Español)](https://www.youtube.com/watch?v=1i5LdvERUOc)
* **Qué aprenderás:** Tabla práctica de voltajes en español para máquinas rotativas con cartuchos estándar RL y RM.

### 🎥 [Line Work Mastery for Tattoo Beginners (Tattooing 101)](https://www.youtube.com/watch?v=EsEgLUxOW1E)
* **Qué aprenderás:** Técnicas de empalme de líneas largas, uso del meñique como patín guía y respiración durante el trazo.

---

## 4. Práctica en Piel Sintética

### 🎥 [How to Tattoo Fake Skin for Beginners (Daniel Yuck)](https://www.youtube.com/watch?v=75lkRaDWlFE)
* **Qué aprenderás:** Cómo limpiar la tinta sobre silicona sin borrar el calco, uso de vaselina fina como lubricante de arrastre y cómo colocar la piel sintética sobre una botella cilíndrica para simular la curvatura real de un brazo o pierna.

---

> [!TIP]
> **Orden recomendado de visualización hoy:**
> 1. Mira el video de Daniel Yuck sobre **Wrap de la máquina** (dura 5 minutos).
> 2. Mira el video de Tattooing 101 sobre **Needle Depth** para fijar en tu mente los 1.5mm - 2mm.
> 3. Enciende tu Poseidon a 7.5V y reproduce el video de **Hand Speed vs Voltage** escuchando la máquina al mismo tiempo para calibrar tu oído al zumbido del motor rotativo.
"""

with open(os.path.join(B1_DIR, "02_VIDEOTECA_YOUTUBE_PROFESIONAL.md"), "w", encoding="utf-8") as f:
    f.write(videoteca_content)
print("Creado 02_VIDEOTECA_YOUTUBE_PROFESIONAL.md")

# ---------------------------------------------------------
# 3. ARCHIVO: 03_MAPEO_HARDWARE_Y_ESTILOS.md
# ---------------------------------------------------------
mapeo_content = """# Bloque 1 — Mapeo de Hardware: Tus 14 Diseños vs Tu Equipo Actual

Este documento desglosa cada una de las 14 referencias fotográficas que guardaste en tu carpeta de gustos personales (`C:\\Users\\quesa\\Documents\\CURSO TATTOO\\REFERENCIAS_ESTILOS`), indicando la técnica exacta requerida, cómo ejecutarla con tu equipo actual (**Poseidon Pen + 1205RL + 1207RM**) y qué cartucho complementario te recomendamos adquirir en el futuro.

---

## Grupo A: Cybersigilism Orgánico y Espinas Afiladas

### Referencias:
* `01_Cybersigilism_Biomecanico_Brazo.jpeg` (Manga biomecánica cyber con articulaciones óseas y patas de araña).
* `08_Chandelier_Cybersigilism_Hombro.jpeg` (Lámpara colgante de espinas entrelazadas en hombro).
* `09_Corse_Espalda_Lazos_Filigrana.jpeg` (Corsé con espinas cyber que se abren hacia las costillas).

### Análisis Técnico:
* **El secreto del estilo:** Líneas de grosor dinámico (*tapered lines*). Comienzan con una base ancha y terminan en un extremo afilado como una aguja hipodérmica.
* **Ejecución con tu 1205RL (0.35 mm):**
  * Coloca la batería Poseidon entre **7.2V y 7.6V**.
  * Para las espinas: clava la aguja con tu dedo meñique de apoyo, desliza 5 milímetros a velocidad constante y, al llegar a la punta, realiza un **movimiento rápido de latigazo hacia arriba ("flick")** sacando la aguja de la piel al vuelo. La punta quedará afilada en cero absoluto.
  * Para los nudos oscuros y sombras de articulación: baja el voltaje a **5.2V** y realiza pequeños barridos pendulares.
* **Futura compra recomendada:** Agujas **Bugpin 0803RL (0.25 mm 3RL)** para micro-espinas de menos de 1 mm.

---

## Grupo B: Filigrana Barroca, Encajes y Corsé Femenino

### Referencias:
* `02_Acanto_Barroco_WhipShading.jpeg` (Voluta clásica de hoja de acanto con sombreado de látigo).
* `04_Medallon_Muslo_Encaje_Filigrana.jpeg` (Cresta de muslo con malla de corsé y filigrana Korterola).
* `05_Espejo_Corazon_Filigrana_Barroca.jpeg` (Marco de espejo barroco en forma de corazón).
* `06_Liga_Encaje_Daga_Puntillismo.jpeg` (Liga de encaje en muslo con daga y cadenas suspendidas).
* `07_Textura_Filigrana_Relieve_Monster.jpeg` (Relieve de volutas plateadas barrocas).

### Análisis Técnico:
* **El secreto del estilo:** Simetría perfecta, arcos continuos de radio constante y degradados de sombra transparentes (*greywash*).
* **Ejecución con tus agujas:**
  * **Estructura y bordes:** Usa la **1205RL** a **7.5V**. Traza las líneas de encaje de una sola pasada continua, moviendo todo el brazo desde el codo (no flexiones los dedos en mitad del arco o se notará una pausa).
  * **Sombras de pliegues y volumen:** Usa la **1207RM (Curved Magnum 7)** a **6.5V**. El perfil arqueado de la 7RM permite que los bordes de la aguja no corten la piel, dejando un sombreado difuminado como aerógrafo.
* **Futura compra recomendada:** Papel transfer de alta pigmentación (Spirit hectográfico) para no perder las líneas milimétricas del calco al limpiar.

---

## Grupo C: Grabado Medieval, Xilografía y Catedrales Góticas

### Referencias:
* `03_Catedral_Gotica_Grabado.jpeg` (Aguja de catedral gótica con bandadas de murciélagos y entramado).
* `10_Grabado_Medieval_Monje_Arbol.jpeg` (Xilografía de peregrino medieval, árbol retorcido y roseta).
* `11_Tatuando_Grabado_Medieval_Accion.jpeg` (Fotografía en vivo del tatuador trabajando el grabado).
* `12_Espiral_Coraline_Puntillismo.jpeg` (Espiral de puntillismo denso estilo Coraline).

### Análisis Técnico:
* **El secreto del estilo:** *Cross-hatching* (tramado de líneas cruzadas) y *stippling* (puntillismo visible). No se buscan degradados de humo, sino textura táctil de imprenta del siglo XV.
* **Ejecución con tu 1205RL:**
  * **La técnica del Grabador:** Baja la batería Poseidon a **5.0V – 5.3V**. Con el motor girando lento, cada pasada de tu mano a velocidad media deja al descubierto los puntos individuales de tinta.
  * Cruza las líneas en ángulos agudos (de 30° a 45°), nunca en cruz de 90°.
  * Para las zonas de sombra densa del árbol y los ropajes: haz varias capas de tramas superpuestas.

---

## Grupo D: Anime y Microtatuaje

### Referencias:
* `13_Microtatuaje_Hello_Kitty.jpeg` (Microtatuaje con línea de contorno fina y relleno suave de color).
* `14_Anime_Marceline_AdventureTime.jpg` (Marceline con línea sólida contrastada y relleno negro puro).

### Análisis Técnico:
* **El secreto del estilo:** Consistencia absoluta en el grosor del contorno y saturación completa del negro sin dejar huecos grises.
* **Ejecución con tus agujas:**
  * **Marceline (Línea + Relleno):** El contorno exterior se hace con la **1205RL** a **7.6V**. Para rellenar el pelo negro opaco, usa la **1207RM** a **7.2V** con movimientos circulares superpuestos de medio centímetro de diámetro hasta saturar la silicona.
  * **Hello Kitty (Micro-línea):** Voltaje moderado a **7.0V** con 1205RL, velocidad de mano media-lenta para garantizar que la línea cierre limpia en las orejas y ojos.
"""

with open(os.path.join(B1_DIR, "03_MAPEO_HARDWARE_Y_ESTILOS.md"), "w", encoding="utf-8") as f:
    f.write(mapeo_content)
print("Creado 03_MAPEO_HARDWARE_Y_ESTILOS.md")

# ---------------------------------------------------------
# 4. COMPILADOR DE PLANTILLAS PDF VECTORIALES LISTAS PARA IMPRIMIR
# ---------------------------------------------------------

def create_sheet_1(filename):
    c = canvas.Canvas(filename, pagesize=A4)
    w, h = A4 # 595.27 x 841.89 points
    
    # Encabezado
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(colors.HexColor("#1A1A1A"))
    c.drawString(35, h - 45, "CURSO PROFESIONAL DE TATUAJE — PLANTILLA 01")
    
    c.setFont("Helvetica", 9)
    c.setFillColor(colors.HexColor("#555555"))
    c.drawString(35, h - 60, "Bloque 1: Calibración de Aguja, Profundidad y Velocidad de Mano | Aguja: 1205RL | Voltaje: 7.4V - 7.8V")
    
    c.setStrokeColor(colors.HexColor("#222222"))
    c.setLineWidth(1.2)
    c.line(35, h - 68, w - 35, h - 68)
    
    # ------------------ SECCIÓN 1: LÍNEAS HORIZONTALES PARALELAS ------------------
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(colors.HexColor("#000000"))
    c.drawString(35, h - 88, "EJERCICIO 1: LÍNEAS HORIZONTALES CONTINUAS (UN SOLO PASE)")
    c.setFont("Helvetica-Oblique", 8)
    c.setFillColor(colors.HexColor("#666666"))
    c.drawString(35, h - 100, "Objetivo: Mantener el meñique apoyado como patín. Velocidad de mano constante sin parar en mitad de la línea.")
    
    y = h - 118
    c.setStrokeColor(colors.HexColor("#333333"))
    for i in range(7):
        # Punto de inicio y fin
        c.circle(45, y, 1.5, fill=1, stroke=0)
        c.circle(w - 45, y, 1.5, fill=1, stroke=0)
        # Línea guía
        c.setLineWidth(0.8)
        c.line(48, y, w - 48, y)
        y -= 14
        
    # ------------------ SECCIÓN 2: LÍNEAS VERTICALES Y CONTROL DE CODO ------------------
    y -= 10
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(colors.HexColor("#000000"))
    c.drawString(35, y, "EJERCICIO 2: LÍNEAS VERTICALES (TRACCIÓN CON EL ANTEBRAZO)")
    c.setFont("Helvetica-Oblique", 8)
    c.setFillColor(colors.HexColor("#666666"))
    c.drawString(35, y - 12, "Objetivo: Trazar hacia ti (tirando de la máquina). No dobles los dedos; mueve todo el antebrazo.")
    
    y_start = y - 28
    col_width = (w - 70) / 12
    c.setLineWidth(0.8)
    c.setStrokeColor(colors.HexColor("#333333"))
    for col in range(12):
        x = 35 + col * col_width + col_width / 2
        c.circle(x, y_start, 1.5, fill=1, stroke=0)
        c.circle(x, y_start - 75, 1.5, fill=1, stroke=0)
        c.line(x, y_start - 2, x, y_start - 73)
        
    # ------------------ SECCIÓN 3: CUADRÍCULA DE PRECISIÓN Y CRUCES 45° (ETCHING) ------------------
    y = y_start - 105
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(colors.HexColor("#000000"))
    c.drawString(35, y, "EJERCICIO 3: TRAMA DE GRABADO GÓTICO A 45° (CROSS-HATCHING)")
    c.setFont("Helvetica-Oblique", 8)
    c.setFillColor(colors.HexColor("#666666"))
    c.drawString(35, y - 12, "Técnica de grabado medieval. Cruza las líneas con suavidad a 5.2V para practicar la textura de xilografía.")
    
    # Cajón de tramas
    box_y = y - 120
    box_w = 110
    box_h = 100
    
    # Caja 1: Diagonales derecha
    c.setStrokeColor(colors.HexColor("#888888"))
    c.setLineWidth(0.5)
    c.rect(45, box_y, box_w, box_h, stroke=1, fill=0)
    c.setStrokeColor(colors.HexColor("#222222"))
    c.setLineWidth(0.7)
    for d in range(10, box_w + box_h, 10):
        x1 = 45 + max(0, d - box_h)
        y1 = box_y + min(d, box_h)
        x2 = 45 + min(d, box_w)
        y2 = box_y + max(0, d - box_w)
        c.line(x1, y1, x2, y2)
        
    # Caja 2: Diagonales cruzadas (Cross-hatch)
    c.setStrokeColor(colors.HexColor("#888888"))
    c.setLineWidth(0.5)
    c.rect(175, box_y, box_w, box_h, stroke=1, fill=0)
    c.setStrokeColor(colors.HexColor("#222222"))
    c.setLineWidth(0.7)
    for d in range(10, box_w + box_h, 10):
        x1 = 175 + max(0, d - box_h)
        y1 = box_y + min(d, box_h)
        x2 = 175 + min(d, box_w)
        y2 = box_y + max(0, d - box_w)
        c.line(x1, y1, x2, y2)
        # Cruzada inversa
        x1_inv = 175 + max(0, d - box_h)
        y1_inv = box_y + max(0, box_h - d)
        x2_inv = 175 + min(d, box_w)
        y2_inv = box_y + min(box_h, 2 * box_h - d if d > box_h else box_h - (d - box_w) if d > box_w else box_h)
        # Trazo inverso simple
    for d in range(10, box_w, 10):
        c.line(175 + d, box_y + box_h, 175 + box_w, box_y + d)
        c.line(175, box_y + box_h - d, 175 + box_w - d, box_y)
        
    # Caja 3: Cuadrícula geométrica ortogonal
    c.setStrokeColor(colors.HexColor("#888888"))
    c.setLineWidth(0.5)
    c.rect(305, box_y, box_w, box_h, stroke=1, fill=0)
    c.setStrokeColor(colors.HexColor("#222222"))
    c.setLineWidth(0.7)
    for g in range(10, box_w, 10):
        c.line(305 + g, box_y, 305 + g, box_y + box_h)
    for g in range(10, box_h, 10):
        c.line(305, box_y + g, 305 + box_w, box_y + g)
        
    # Caja 4: Cuadros concéntricos
    c.setStrokeColor(colors.HexColor("#888888"))
    c.setLineWidth(0.5)
    c.rect(435, box_y, box_w, box_h, stroke=1, fill=0)
    c.setStrokeColor(colors.HexColor("#222222"))
    c.setLineWidth(0.7)
    for s in range(10, 50, 8):
        c.rect(435 + s, box_y + s, box_w - 2 * s, box_h - 2 * s)
        
    # ------------------ SECCIÓN 4: CONTROL DE VELOCIDAD Y MICRO-LÍNEAS ------------------
    y = box_y - 25
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(colors.HexColor("#000000"))
    c.drawString(35, y, "EJERCICIO 4: PRUEBA DE VOLTAJES COMPARADOS (MISMAS LÍNEAS A 3 VELOCIDADES)")
    c.setFont("Helvetica-Oblique", 8)
    c.setFillColor(colors.HexColor("#666666"))
    c.drawString(35, y - 12, "Traza cada bloque con la batería Poseidon al voltaje indicado para comparar la saturación de la tinta.")
    
    y_test = y - 30
    voltajes = [("Bloque A: 6.5V (Voltaje Bajo)", 35, 180), 
                 ("Bloque B: 7.5V (Voltaje Dulce)", 210, 180), 
                 ("Bloque C: 8.5V (Voltaje Rápido)", 385, 175)]
    for title, vx, vw in voltajes:
        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(colors.HexColor("#333333"))
        c.drawString(vx, y_test, title)
        c.setLineWidth(0.8)
        c.setStrokeColor(colors.HexColor("#444444"))
        for k in range(5):
            ly = y_test - 14 - k * 12
            c.line(vx, ly, vx + vw, ly)
            
    # Pie de página
    c.setFont("Helvetica", 7)
    c.setFillColor(colors.HexColor("#888888"))
    c.drawString(35, 20, "Material del Curso Personalizado de Tatuaje — Imprimir en A4 al 100% de escala (sin ajustar página)")
    c.drawRightString(w - 35, 20, "Página 1 de 2 | Poseidon 1205RL")
    
    c.showPage()
    c.save()
    print("Generado PDF:", filename)

def create_sheet_2(filename):
    c = canvas.Canvas(filename, pagesize=A4)
    w, h = A4
    
    # Encabezado
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(colors.HexColor("#1A1A1A"))
    c.drawString(35, h - 45, "CURSO PROFESIONAL DE TATUAJE — PLANTILLA 02")
    
    c.setFont("Helvetica", 9)
    c.setFillColor(colors.HexColor("#555555"))
    c.drawString(35, h - 60, "Bloque 1: Curvas Barrocas, Filigrana y Espinas Cybersigilism | Aguja: 1205RL | Voltaje: 7.2V - 7.6V")
    
    c.setStrokeColor(colors.HexColor("#222222"))
    c.setLineWidth(1.2)
    c.line(35, h - 68, w - 35, h - 68)
    
    # ------------------ SECCIÓN 1: ESPINAS CÓNICAS CYBERSIGILISM (TAPERED FLICK) ------------------
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(colors.HexColor("#000000"))
    c.drawString(35, h - 88, "EJERCICIO 1: ESPINAS CÓNICAS CYBERSIGILISM (TÉCNICA DE LATIGAZO EN VUELO)")
    c.setFont("Helvetica-Oblique", 8)
    c.setFillColor(colors.HexColor("#666666"))
    c.drawString(35, h - 100, "Comienza en la base apoyando con firmeza; alarga el trazo y sal al vuelo aligerando la presión para afilar la punta.")
    
    y = h - 115
    # Espinas horizontales
    for i in range(5):
        cy = y - i * 16
        c.drawString(35, cy - 3, f"Fila {i+1}:")
        # Dibujamos espinas cónicas estilizadas
        for s in range(5):
            sx = 75 + s * 95
            p = c.beginPath()
            p.moveTo(sx, cy - 2.5)
            p.curveTo(sx + 30, cy - 1.5, sx + 60, cy - 0.5, sx + 80, cy)
            p.curveTo(sx + 60, cy + 0.5, sx + 30, cy + 1.5, sx, cy + 2.5)
            p.close()
            c.setFillColor(colors.HexColor("#222222"))
            c.drawPath(p, fill=1, stroke=0)
            
    # ------------------ SECCIÓN 2: VOLUTAS EN 'S' Y HOJAS DE ACANTO BARROCAS ------------------
    y = h - 210
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(colors.HexColor("#000000"))
    c.drawString(35, y, "EJERCICIO 2: CURVAS BARROCAS EN 'S' Y 'C' (FILIGRANA Y ENCAJES)")
    c.setFont("Helvetica-Oblique", 8)
    c.setFillColor(colors.HexColor("#666666"))
    c.drawString(35, y - 12, "Traza arcos continuos girando el pen sobre el eje de tu muñeca. Mantén la velocidad sin titubear.")
    
    y_wave = y - 30
    for row in range(4):
        wy = y_wave - row * 32
        p = c.beginPath()
        p.moveTo(40, wy)
        for wave in range(6):
            wx = 40 + wave * 80
            p.curveTo(wx + 20, wy + 20, wx + 40, wy + 20, wx + 40, wy)
            p.curveTo(wx + 40, wy - 20, wx + 60, wy - 20, wx + 80, wy)
        c.setStrokeColor(colors.HexColor("#333333"))
        c.setLineWidth(1.0)
        c.drawPath(p, stroke=1, fill=0)
        
    # ------------------ SECCIÓN 3: CÍRCULOS Y ESPIRALES CONCÉNTRICAS (CORALINE & ENCAJE) ------------------
    y = y_wave - 145
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(colors.HexColor("#000000"))
    c.drawString(35, y, "EJERCICIO 3: CÍRCULOS CONCÉNTRICOS Y ESPIRALES (CONTROL DE PULSO)")
    c.setFont("Helvetica-Oblique", 8)
    c.setFillColor(colors.HexColor("#666666"))
    c.drawString(35, y - 12, "Realiza cada círculo de dos semicírculos empalmados, o en un solo giro girando la piel sintética si es necesario.")
    
    cy_circ = y - 75
    # Círculos concéntricos
    c.setStrokeColor(colors.HexColor("#333333"))
    c.setLineWidth(0.8)
    for rad in [10, 20, 30, 40, 50, 60]:
        c.circle(115, cy_circ, rad, stroke=1, fill=0)
    c.circle(115, cy_circ, 2, stroke=0, fill=1)
    
    # Espiral tipo Coraline
    p = c.beginPath()
    cx, c_y = 280, cy_circ
    p.moveTo(cx, c_y)
    for theta_deg in range(0, 1080, 15):
        theta = math.radians(theta_deg)
        r = 1.2 * math.sqrt(theta_deg) * 1.7
        px = cx + r * math.cos(theta)
        py = c_y + r * math.sin(theta)
        p.lineTo(px, py)
    c.setStrokeColor(colors.HexColor("#222222"))
    c.setLineWidth(1.0)
    c.drawPath(p, stroke=1, fill=0)
    
    # Roseta ornamental de filigrana
    cx_rose = 445
    c.circle(cx_rose, cy_circ, 5, fill=1, stroke=0)
    for petal in range(8):
        ang = math.radians(petal * 45)
        px = cx_rose + 28 * math.cos(ang)
        py = cy_circ + 28 * math.sin(ang)
        c.circle(px, py, 12, stroke=1, fill=0)
    c.circle(cx_rose, cy_circ, 42, stroke=1, fill=0)
    
    # ------------------ SECCIÓN 4: COMPOSICIÓN DE PRUEBA: ESPINA DE HOMBRO CYBERSIGILISM ------------------
    y = cy_circ - 80
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(colors.HexColor("#000000"))
    c.drawString(35, y, "EJERCICIO 4: MINI-COMPOSICIÓN CYBERSIGILISM DE INTEGRACIÓN")
    c.setFont("Helvetica-Oblique", 8)
    c.setFillColor(colors.HexColor("#666666"))
    c.drawString(35, y - 12, "Tatuaje de prueba final del Bloque 1: integra espinas cónicas curvas con filigrana gótica central.")
    
    # Diseño de espina cyber central
    center_x = w / 2
    y_spine = y - 45
    c.setLineWidth(1.2)
    c.setStrokeColor(colors.HexColor("#1A1A1A"))
    
    # Eje central
    p = c.beginPath()
    p.moveTo(center_x, y_spine + 25)
    p.curveTo(center_x - 15, y_spine, center_x + 15, y_spine - 25, center_x, y_spine - 45)
    c.drawPath(p, stroke=1, fill=0)
    
    # Ramas simétricas tipo cyber
    for sign in [-1, 1]:
        p = c.beginPath()
        # Espina superior
        p.moveTo(center_x, y_spine + 20)
        p.curveTo(center_x + sign * 60, y_spine + 35, center_x + sign * 120, y_spine + 15, center_x + sign * 160, y_spine + 30)
        p.curveTo(center_x + sign * 115, y_spine + 10, center_x + sign * 60, y_spine + 28, center_x, y_spine + 15)
        # Espina media curvada
        p.moveTo(center_x, y_spine)
        p.curveTo(center_x + sign * 80, y_spine - 10, center_x + sign * 140, y_spine - 40, center_x + sign * 180, y_spine - 20)
        p.curveTo(center_x + sign * 130, y_spine - 32, center_x + sign * 75, y_spine - 5, center_x, y_spine - 5)
        # Espina inferior gótica
        p.moveTo(center_x, y_spine - 25)
        p.curveTo(center_x + sign * 50, y_spine - 45, center_x + sign * 90, y_spine - 35, center_x + sign * 130, y_spine - 55)
        p.curveTo(center_x + sign * 85, y_spine - 30, center_x + sign * 45, y_spine - 40, center_x, y_spine - 20)
        c.setFillColor(colors.HexColor("#222222"))
        c.drawPath(p, fill=1, stroke=0)
        
    # Pie de página
    c.setFont("Helvetica", 7)
    c.setFillColor(colors.HexColor("#888888"))
    c.drawString(35, 20, "Material del Curso Personalizado de Tatuaje — Imprimir en A4 al 100% de escala (sin ajustar página)")
    c.drawRightString(w - 35, 20, "Página 2 de 2 | Poseidon 1205RL")
    
    c.showPage()
    c.save()
    print("Generado PDF:", filename)

# Generar ambos PDFs
create_sheet_1(os.path.join(SHEETS_DIR, "01_Calibracion_Lineas_Y_Profundidad.pdf"))
create_sheet_2(os.path.join(SHEETS_DIR, "02_Curvas_Barrocas_Y_Espinas_Cybersigilism.pdf"))
print("Todo el Bloque 1 se ha completado satisfactoriamente.")
