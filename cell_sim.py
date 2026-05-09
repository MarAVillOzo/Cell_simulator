from vpython import *
import random
import math

# ============================================================
#   SIMULACIÓN CELULAR HUMANA AVANZADA
#   MODELO ENERGÉTICO REALISTA
#   ATP + GTP + SÍNTESIS PROTEICA
# ============================================================

scene = canvas(
    title="Célula Humana - Sistema Energético Molecular",
    width=1650,
    height=950,
    background=vector(0.02,0.02,0.03)
)

scene.forward = vector(-1,-0.25,-1)

# ============================================================
# CONSTANTES
# ============================================================

CELL_RADIUS = 13
NUCLEUS_RADIUS = 3

MRNA_SPEED = 0.018
PROTEIN_SPEED = 0.014
VESICLE_SPEED = 0.012

ATP_SPEED = 0.030
GTP_SPEED = 0.028

BLOOD_SPEED = 0.006

# ============================================================
# COLORES 
# ============================================================

COLORS = {

    "membrane": vector(0,0.8,0.4),
    "nucleus": vector(0.2,0.4,1),
    "nucleolus": vector(0.8,0,1),

    "rer": vector(1,0.5,0),

    "ribosome": vector(1,1,1),

    "golgi": vector(1,0.2,0.2),

    "mitochondria": vector(1,0.7,0),

    "lysosome": vector(0.8,0.8,0),

    "microtubule": vector(0,1,1),

    "mrna": vector(0,1,0.3),

    "protein": vector(0,1,0.8),

    "vesicle": vector(0.259, 0.259, 0.941),

    "secretory": vector(0.5,1,0),

    "blood": vector(1,0,0),

    # NUEVOS
    "ATP": vector(1,0.55,0),       # naranja fluorescente
    "GTP": vector(1,0.1,0.8)         # rosa fluorescente
}

# ============================================================
# CONTADORES
# ============================================================

stats = {

    "genes":0,
    "mrna":0,
    "proteins":0,

    "golgi":0,
    "vesicles":0,
    "secreted":0,

    "ATP_created":0,
    "ATP_used":0,

    "GTP_created":0,
    "GTP_used":0
}

# ============================================================
# MEMBRANA CELULAR
# ============================================================

cell = sphere(
    radius=CELL_RADIUS,
    color=COLORS["membrane"],
    opacity=0.08
)

label(
    pos=vector(0,14,0),
    text="MEMBRANA CELULAR",
    color=COLORS["membrane"],
    box=False,
    height=14
)

# ============================================================
# NÚCLEO
# ============================================================

nucleus = sphere(
    radius=NUCLEUS_RADIUS,
    color=COLORS["nucleus"],
    opacity=0.75
)

label(
    pos=vector(0,4,0),
    text="NÚCLEO",
    color=COLORS["nucleus"],
    box=False,
    height=14
)

# ============================================================
# NUCLÉOLO
# ============================================================

nucleolus = sphere(
    pos=vector(0.7,0.3,0),
    radius=0.8,
    color=COLORS["nucleolus"]
)

label(
    pos=nucleolus.pos + vector(0,1.5,0),
    text="NUCLÉOLO",
    color=COLORS["nucleolus"],
    box=False,
    height=11
)

# ============================================================
# RETÍCULO ENDOPLASMÁTICO RUGOSO
# ============================================================

rer_parts = []

for i in range(18):

    angle = i*(2*pi/18)

    rer = box(
        pos=vector(
            5*cos(angle),
            5*sin(angle),
            random.uniform(-2,2)
        ),
        size=vector(2.5,0.25,1.3),
        color=COLORS["rer"]
    )

    rer_parts.append(rer)

label(
    pos=vector(6,6,0),
    text="RETÍCULO ENDOPLASMÁTICO RUGOSO",
    color=COLORS["rer"],
    box=False,
    height=12
)

# ============================================================
# RIBOSOMAS
# ============================================================

ribosomes = []

for rer in rer_parts:

    for j in range(4):

        r = sphere(
            pos=rer.pos + vector(
                random.uniform(-1,1),
                random.uniform(-0.15,0.15),
                random.uniform(-0.15,0.15)
            ),
            radius=0.13,
            color=COLORS["ribosome"]
        )

        ribosomes.append(r)

label(
    pos=vector(-5,6,0),
    text="RIBOSOMAS",
    color=COLORS["ribosome"],
    box=False,
    height=12
)

# ============================================================
# GOLGI
# ============================================================

golgi = []

for i in range(6):

    g = box(
        pos=vector(8,-2+i*0.7,0),
        size=vector(3,0.35,1.5),
        color=COLORS["golgi"]
    )

    golgi.append(g)

label(
    pos=vector(8,3,0),
    text="APARATO DE GOLGI",
    color=COLORS["golgi"],
    box=False,
    height=12
)

# ============================================================
# MITOCONDRIAS
# ============================================================

mitochondria = []

for i in range(8):

    m = ellipsoid(
        pos=vector(
            random.uniform(-8,8),
            random.uniform(-8,8),
            random.uniform(-8,8)
        ),
        length=2,
        height=1,
        width=1,
        color=COLORS["mitochondria"]
    )

    mitochondria.append(m)

label(
    pos=vector(-8,9,0),
    text="MITOCONDRIAS",
    color=COLORS["mitochondria"],
    box=False,
    height=12
)

# ============================================================
# ATP
# ============================================================

label(
    pos=vector(-14,11,0),
    text="ATP (ENERGÍA CELULAR)",
    color=COLORS["ATP"],
    box=False,
    height=11
)

# ============================================================
# GTP
# ============================================================

label(
    pos=vector(-14,9.5,0),
    text="GTP (TRADUCCIÓN RIBOSOMAL)",
    color=COLORS["GTP"],
    box=False,
    height=11
)

# ============================================================
# CITOESQUELETO
# ============================================================

for i in range(16):

    angle = i*(2*pi/16)

    cylinder(
        pos=vector(0,0,0),
        axis=vector(
            CELL_RADIUS*cos(angle),
            CELL_RADIUS*sin(angle),
            random.uniform(-4,4)
        ),
        radius=0.03,
        color=COLORS["microtubule"],
        opacity=0.22
    )

label(
    pos=vector(0,-14,0),
    text="MICROTÚBULOS",
    color=COLORS["microtubule"],
    box=False,
    height=12
)

# ============================================================
# TORRENTE SANGUÍNEO
# ============================================================

bloodstream = cylinder(
    pos=vector(0,16,0),
    axis=vector(0,6,0),
    radius=2,
    color=COLORS["blood"],
    opacity=0.25
)

label(
    pos=vector(0,23,0),
    text="TORRENTE SANGUÍNEO",
    color=COLORS["blood"],
    box=False,
    height=12
)

# ============================================================
# HUD
# ============================================================

hud = label(
    pos=vector(-21,16,0),
    text="",
    box=False,
    line=False,
    height=13,
    color=color.white
)

# ============================================================
# SISTEMAS DINÁMICOS
# ============================================================

mrnas = []
proteins = []
vesicles = []
blood_particles = []

ATP_particles = []
GTP_particles = []

# ============================================================
# MOVIMIENTO SUAVE
# ============================================================

def move_to(obj, target, speed):

    direction = target - obj.pos

    if mag(direction) > speed:

        obj.pos += norm(direction)*speed
        return False

    else:

        obj.pos = target
        return True

# ============================================================
# PRODUCCIÓN ATP
# ============================================================

def create_ATP():

    mito = random.choice(mitochondria)

    target = random.choice(ribosomes)

    atp = sphere(
        pos=mito.pos,
        radius=0.14,
        color=COLORS["ATP"],
        emissive=True,
        make_trail=True,
        retain=25,
        trail_color=COLORS["ATP"]
    )

    ATP_particles.append({
        "obj":atp,
        "target":target
    })

    stats["ATP_created"] += 1

# ============================================================
# PRODUCCIÓN GTP
# ============================================================

def create_GTP():

    mito = random.choice(mitochondria)

    target = random.choice(ribosomes)

    gtp = sphere(
        pos=mito.pos,
        radius=0.14,
        color=COLORS["GTP"],
        emissive=True,
        make_trail=True,
        retain=25,
        trail_color=COLORS["GTP"]
    )

    GTP_particles.append({
        "obj":gtp,
        "target":target
    })

    stats["GTP_created"] += 1

# ============================================================
# MOVIMIENTO ATP
# ============================================================

def update_ATP():

    for a in ATP_particles[:]:

        arrived = move_to(
            a["obj"],
            a["target"].pos,
            ATP_SPEED
        )

        if arrived:

            a["obj"].visible = False
            a["obj"].clear_trail()

            ATP_particles.remove(a)

# ============================================================
# MOVIMIENTO GTP
# ============================================================

def update_GTP():

    for g in GTP_particles[:]:

        arrived = move_to(
            g["obj"],
            g["target"].pos,
            GTP_SPEED
        )

        if arrived:

            g["obj"].visible = False
            g["obj"].clear_trail()

            GTP_particles.remove(g)

# ============================================================
# TRANSCRIPCIÓN
# ============================================================

def create_mrna():

    target = random.choice(ribosomes)

    m = sphere(
        pos=nucleus.pos,
        radius=0.18,
        color=COLORS["mrna"],
        emissive=True,
        make_trail=True,
        retain=30,
        trail_color=COLORS["mrna"]
    )

    mrnas.append({
        "obj":m,
        "target":target
    })

    stats["genes"] += 1
    stats["mrna"] += 1

# ============================================================
# TRADUCCIÓN
# ============================================================

def update_mrna():

    for m in mrnas[:]:

        arrived = move_to(
            m["obj"],
            m["target"].pos,
            MRNA_SPEED
        )

        if arrived:

            # necesita ATP y GTP cercanos

            has_ATP = False
            has_GTP = False

            for a in ATP_particles:

                if mag(a["obj"].pos - m["target"].pos) < 1:

                    has_ATP = True
                    break

            for g in GTP_particles:

                if mag(g["obj"].pos - m["target"].pos) < 1:

                    has_GTP = True
                    break

            # SOLO si hay ambos se sintetiza proteína

            if has_ATP and has_GTP:

                p = sphere(
                    pos=m["target"].pos,
                    radius=0.24,
                    color=COLORS["protein"],
                    emissive=True
                )

                proteins.append({
                    "obj":p,
                    "target":random.choice(golgi)
                })

                stats["proteins"] += 1
                stats["ATP_used"] += 1
                stats["GTP_used"] += 1

                m["obj"].visible = False
                m["obj"].clear_trail()

                mrnas.remove(m)

# ============================================================
# GOLGI 2
# ============================================================

def update_proteins():

    for p in proteins[:]:

        arrived = move_to(
            p["obj"],
            p["target"].pos,
            PROTEIN_SPEED
        )

        if arrived:

            membrane_target = norm(vector(
                random.uniform(-1,1),
                random.uniform(-1,1),
                random.uniform(-1,1)
            )) * (CELL_RADIUS+1)

            v = sphere(
                pos=p["obj"].pos,
                radius=0.30,
                color=COLORS["vesicle"],
                emissive=True,
                make_trail=True,
                retain=25,
                trail_color=COLORS["vesicle"]
            )

            vesicles.append({
                "obj":v,
                "target":membrane_target
            })

            stats["golgi"] += 1
            stats["vesicles"] += 1

            p["obj"].visible = False
            proteins.remove(p)

# ============================================================
# EXOCITOSIS
# ============================================================

def update_vesicles():

    for v in vesicles[:]:

        arrived = move_to(
            v["obj"],
            v["target"],
            VESICLE_SPEED
        )

        if arrived:

            blood = sphere(
                pos=v["obj"].pos,
                radius=0.18,
                color=COLORS["blood"],
                emissive=True,
                make_trail=True,
                retain=20,
                trail_color=COLORS["blood"]
            )

            blood_particles.append(blood)

            stats["secreted"] += 1

            v["obj"].visible = False
            v["obj"].clear_trail()

            vesicles.remove(v)

# ============================================================
# TRANSPORTE SANGUÍNEO
# ============================================================

def update_blood():

    for b in blood_particles[:]:

        arrived = move_to(
            b,
            vector(0,22,0),
            BLOOD_SPEED
        )

        if arrived:

            b.visible = False
            b.clear_trail()

            blood_particles.remove(b)

# ============================================================
# HUD
# ============================================================

def update_hud():

    hud.text = (

        "=========== ACTIVIDAD MOLECULAR ===========\n\n"

        f"Genes activados: {stats['genes']}\n"
        f"ARNm sintetizados: {stats['mrna']}\n"
        f"Proteínas sintetizadas: {stats['proteins']}\n\n"

        f"ATP producidos: {stats['ATP_created']}\n"
        f"ATP utilizados: {stats['ATP_used']}\n\n"

        f"GTP producidos: {stats['GTP_created']}\n"
        f"GTP utilizados: {stats['GTP_used']}\n\n"

        f"Procesamiento Golgi: {stats['golgi']}\n"
        f"Vesículas secretoras: {stats['vesicles']}\n"
        f"Moléculas exportadas: {stats['secreted']}\n\n"

        f"ATP activos: {len(ATP_particles)}\n"
        f"GTP activos: {len(GTP_particles)}"
    )

# ============================================================
# LOOP PRINCIPAL
# ============================================================

clock = 0

while True:

    rate(60)

    clock += 1

    # PRODUCCIÓN DE ENERGÍA MITOCONDRIAL

    if clock % 10 == 0:
        create_ATP()

    if clock % 18 == 0:
        create_GTP()

    # TRANSCRIPCIÓN

    if clock % 45 == 0:
        create_mrna()

    # ACTUALIZACIÓN SISTEMAS

    update_ATP()
    update_GTP()

    update_mrna()

    update_proteins()

    update_vesicles()

    update_blood()

    update_hud()

     # 66