#!/usr/bin/env python3
"""Generate PDF report from SMCI valuation analysis."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether
)

OUT = "/home/user/lectures/smci-valuation-analysis.pdf"

doc = SimpleDocTemplate(
    OUT, pagesize=letter,
    leftMargin=0.7*inch, rightMargin=0.7*inch,
    topMargin=0.7*inch, bottomMargin=0.7*inch,
    title="SMCI Valuation Analysis - May 2026",
    author="Independent valuation memo",
)

styles = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=styles['Heading1'], fontSize=18,
                   textColor=colors.HexColor('#0b3d91'), spaceAfter=10, spaceBefore=6)
H2 = ParagraphStyle('H2', parent=styles['Heading2'], fontSize=13,
                   textColor=colors.HexColor('#0b3d91'), spaceAfter=6, spaceBefore=12)
H3 = ParagraphStyle('H3', parent=styles['Heading3'], fontSize=11,
                   textColor=colors.HexColor('#333333'), spaceAfter=4, spaceBefore=8)
BODY = ParagraphStyle('Body', parent=styles['BodyText'], fontSize=9.5,
                     leading=13, alignment=TA_JUSTIFY, spaceAfter=4)
SMALL = ParagraphStyle('Small', parent=styles['BodyText'], fontSize=8,
                      leading=10, textColor=colors.HexColor('#555555'))
QUOTE = ParagraphStyle('Quote', parent=BODY, leftIndent=14, rightIndent=14,
                      textColor=colors.HexColor('#222222'),
                      backColor=colors.HexColor('#f3f6fb'),
                      borderColor=colors.HexColor('#0b3d91'),
                      borderWidth=0, borderPadding=8, spaceAfter=6)
META = ParagraphStyle('Meta', parent=styles['BodyText'], fontSize=9,
                     textColor=colors.HexColor('#555555'))

def p(t, s=BODY): return Paragraph(t, s)

def tbl(data, col_widths, header=True, highlight_rows=None):
    style = [
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 8.5),
        ('GRID', (0,0), (-1,-1), 0.3, colors.HexColor('#aaaaaa')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]
    if header:
        style += [
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0b3d91')),
            ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ]
    if highlight_rows:
        for r in highlight_rows:
            style.append(('BACKGROUND', (0,r), (-1,r), colors.HexColor('#fff4cc')))
            style.append(('FONTNAME', (0,r), (-1,r), 'Helvetica-Bold'))
    t = Table(data, colWidths=col_widths, hAlign='LEFT')
    t.setStyle(TableStyle(style))
    return t

story = []

# --- Title ---
story.append(p("Análisis de Valoración SMCI (Super Micro Computer)", H1))
story.append(p("<b>Fecha:</b> 6 de mayo, 2026 &nbsp;&nbsp; <b>Precio cierre:</b> $27.92 USD &nbsp;&nbsp; "
               "<b>Analista:</b> Modelo independiente (sin price targets de sell-side)", META))
story.append(Spacer(1, 8))

# --- 1. Aclaración estructural ---
story.append(p("1. Aclaración estructural previa", H2))
story.append(p(
    "SMCI <b>NO</b> es semiconductora; es un <b>integrador de sistemas de servidores AI</b> (rack-scale OEM). "
    "Los chips los diseña NVIDIA / AMD / Broadcom; SMCI ensambla. Por lo tanto, comparar su valoración "
    "directamente contra NVDA, AVGO o AMD es engañoso — sus márgenes brutos son estructuralmente diferentes "
    "(70%+ vs ~10%). Los <b>comparables correctos son Dell y HPE</b> (también OEMs de servidores AI). "
    "En el resto del análisis se trata a NVDA/AVGO/AMD como benchmark de mercado/sentimiento, no como "
    "múltiplos aplicables."))

# --- 2. Snapshot comparativo ---
story.append(p("2. Snapshot comparativo (May 2026)", H2))
peer_data = [
    ["Compañía", "Market Cap", "Precio", "P/E TTM", "P/E Fwd", "Rev TTM", "EV/Sales", "YTD 2026"],
    ["NVDA",  "$4.78 T",  "$196.85", "40.5x",  "~32x",  "$215.9 B", "~22x",  "≈ flat"],
    ["AVGO",  "$1.99 T",  "—",       "80.8x",  "38.0x", "~$60 B",   "~33x",  "+"],
    ["AMD",   "$579 B",   "$341.54", "127.9x", "54.0x", "~$32 B",   "~18x",  "+"],
    ["DELL",  "$130 B",   "$208",    "20.9x",  "15.2x", "$113.5 B", "~1.28x","+67%"],
    ["HPE",   "~$30 B",   "~$23",    "~14x",   "~12x",  "~$32 B",   "~1.4x", "+20%"],
    ["SMCI",  "$19.9 B",  "$27.92",  "~12x",   "~11x",  "~$33 B",   "0.69x", "−7%"],
]
story.append(tbl(peer_data,
    [0.75*inch, 0.85*inch, 0.7*inch, 0.65*inch, 0.65*inch, 0.85*inch, 0.8*inch, 0.85*inch],
    highlight_rows=[4,5,6]))
story.append(Spacer(1, 4))
story.append(p(
    "<b>Observación clave:</b> SMCI cotiza al múltiplo más bajo del grupo OEM en EV/Sales y P/E forward, "
    "pero también tiene el peor desempeño YTD. El mercado le está aplicando un descuento de riesgo "
    "significativo, no un descuento de valor irracional."))

# --- 3. Datos fundamentales SMCI ---
story.append(p("3. Datos fundamentales SMCI (Q3 FY26, cerrado 31-mar-2026)", H2))

story.append(p("Income Statement", H3))
fund_is = [
    ["Métrica", "Valor"],
    ["Revenue Q3", "$10.24 B (vs estimado $12.33 B → miss −17%)"],
    ["Revenue YoY", "+123%"],
    ["Non-GAAP EPS", "$0.84 (beat +35%)"],
    ["Non-GAAP Gross Margin", "10.1% (recuperación desde 6.4% en Q2)"],
    ["Guía FY26 completa", "$38.9 – $40.4 B (mid $39.65 B)"],
    ["Guía Q4 FY26", "Rev $11.0–12.5 B; EPS $0.65–$0.79"],
]
story.append(tbl(fund_is, [2.0*inch, 4.5*inch]))

story.append(Spacer(1, 6))
story.append(p("Balance Sheet (al 31-mar-2026)", H3))
fund_bs = [
    ["Métrica", "Valor"],
    ["Cash & equivalents", "$1.29 B"],
    ["Bank debt + convertibles", "$8.80 B"],
    ["Net debt", "$7.50 B (vs $787 M trimestre anterior — deterioro masivo)"],
    ["Inventario", "$11.1 B (vs $10.6 B Q2)"],
    ["Cash conversion cycle", "106 días (vs 54 — deterioro de 96%)"],
    ["Días de inventario", "106 (vs 63)"],
    ["DSO", "85 días (vs 49)"],
    ["Diluted shares (non-GAAP)", "709 M Q3 → guía 712 M Q4"],
]
story.append(tbl(fund_bs, [2.0*inch, 4.5*inch]))

story.append(Spacer(1, 6))
story.append(p("Riesgos cualitativos", H3))
risks = [
    "<b>Concentración:</b> ~58% del revenue en top-3 clientes (CoreWeave, xAI, Tesla).",
    "<b>Pérdida de exclusividad:</b> Tesla y xAI ahora también compran a Dell.",
    "<b>Reportes adversos:</b> BlueFin reportó posible pérdida de contrato Oracle (mayo 2026); Hindenburg legacy aún pesa.",
    "<b>Competencia:</b> Dell tiene backlog AI de $43 B; HPE creció networking +152% post-Juniper.",
]
for r in risks:
    story.append(p("• " + r))

story.append(PageBreak())

# --- 4. Modelo propio ---
story.append(p("4. Modelo propio de valoración (3 métodos)", H2))

story.append(p("Método A — EV/Sales relativo a peers OEM", H3))
story.append(p("EV actual SMCI: 712 M × $27.92 + $7.5 B net debt = <b>$27.39 B</b>. "
               "Forward sales (mid FY26): <b>$39.65 B</b>. EV/Sales actual: <b>0.69x</b>."))
mA = [
    ["Escenario", "Múltiplo", "EV implícito", "Equity", "Precio"],
    ["Bear (descuento extremo, pérdida share)", "0.55x", "$21.8 B", "$14.3 B", "$20.1"],
    ["Base (50% del múltiplo de Dell)", "0.85x", "$33.7 B", "$26.2 B", "$36.8"],
    ["Bull (paridad con Dell)", "1.20x", "$47.6 B", "$40.1 B", "$56.3"],
]
story.append(tbl(mA, [2.6*inch, 0.7*inch, 1.0*inch, 0.9*inch, 0.7*inch]))

story.append(Spacer(1, 6))
story.append(p("Método B — P/E forward", H3))
story.append(p("EPS FY26 ≈ <b>$2.55</b> (Q1 ~$0.30 + Q2 $0.69 + Q3 $0.84 + Q4 ~$0.72). "
               "EPS FY27 estimado ≈ <b>$3.20</b> (revenue +25% a $49.6 B; op margin 6.5%; net income $2.30 B)."))
mB = [
    ["Escenario", "P/E", "EPS base", "Precio"],
    ["Bear (premio de riesgo de 60% vs Dell)", "7x",  "$2.55", "$17.9"],
    ["Base (descuento ~30% vs Dell forward)",  "11x", "$2.85 (blend)", "$31.4"],
    ["Bull (paridad Dell forward 15x)",        "15x", "$3.20", "$48.0"],
]
story.append(tbl(mB, [2.8*inch, 0.6*inch, 1.3*inch, 0.7*inch]))

story.append(Spacer(1, 6))
story.append(p("Método C — DCF simplificado", H3))
story.append(p(
    "Supuestos: Revenue FY26 $39.6 B → CAGR 18% a FY30 ($76 B); margen op 5% FY26 → 8% terminal; "
    "WACC 12%; terminal growth 4%; net debt $7.5 B; shares 712 M."))
mC = [
    ["Año", "FCF", "PV @ 12%"],
    ["FY27", "$1.8 B", "$1.61 B"],
    ["FY28", "$2.8 B", "$2.23 B"],
    ["FY29", "$3.6 B", "$2.56 B"],
    ["FY30", "$4.2 B", "$2.67 B"],
    ["Terminal", "$54.6 B (4% gr.)", "$34.7 B"],
]
story.append(tbl(mC, [1.5*inch, 1.8*inch, 1.2*inch]))
story.append(Spacer(1, 4))
story.append(p("<b>EV total = $43.8 B → Equity = $36.3 B → Precio = $51.0</b>"))
story.append(p("<i>Sensibilidad:</i> WACC 14% → ~$36; margen terminal 6% → ~$32; ambos adversos → ~$22.", SMALL))

# --- 5. Síntesis fair value ---
story.append(p("5. Síntesis: Fair Value actual", H2))
synth = [
    ["Escenario", "Probabilidad", "Precio"],
    ["Bear", "25%", "$19 – $22"],
    ["Base", "50%", "$33 – $37"],
    ["Bull", "25%", "$50 – $55"],
]
story.append(tbl(synth, [1.5*inch, 1.5*inch, 1.5*inch], highlight_rows=[2]))
story.append(Spacer(1, 6))
story.append(p("<b>Fair Value ponderado actual ≈ $34 USD</b> (rango $30–38).", QUOTE))
story.append(p(
    "<b>Sobre el precio actual ($27.92):</b> SMCI cotiza ~17–22% por debajo de mi fair value central. "
    "Hay margen de seguridad real, pero el descuento existe por razones legítimas (working capital, "
    "governance, concentración). No es un \"deep value sin razón\" — es un \"value con riesgos identificables\"."))

story.append(PageBreak())

# --- 6. Catch up ---
story.append(p("6. Probabilidad de \"catch up\" con peers", H2))
catch = [
    ["Comparable", "Probabilidad", "Lógica"],
    ["NVDA / AVGO / AMD", "~0%", "Modelos de negocio incomparables (chip designers vs assemblers). Nunca llegará a esos múltiplos."],
    ["Dell (gap ~50% en EV/Sales)", "35–45% (12m)", "Posible si márgenes >12% sostenidos, WC normaliza, sin nuevos episodios de governance."],
    ["HPE", "~50%", "HPE no es objetivo aspiracional; es paridad razonable."],
    ["Su 52w high ($62.36)", "<15% (12m)", "Requeriría re-rating completo + crecimiento sorpresa + perdón total del mercado."],
]
story.append(tbl(catch, [1.7*inch, 1.1*inch, 3.7*inch]))
story.append(Spacer(1, 6))
story.append(p(
    "<b>Veredicto:</b> El \"catch up\" relevante es contra Dell, no contra el sector semis. La compañía "
    "puede volver a $40–50 si ejecuta dos trimestres limpios consecutivos. Volver a >$60 requiere un "
    "evento extraordinario (gran contrato anunciado, resolución legal definitiva, etc.)."))

# --- 7. Targets ---
story.append(p("7. Price Targets (modelo propio, sin sell-side)", H2))

story.append(p("Target a 6 meses (Nov 2026)", H3))
story.append(p(
    "<b>Catalizadores:</b> earnings Q4 FY26 (ago 2026), Q1 FY27 (nov 2026), ramp completo del rack GB300, "
    "posible refinanciamiento del convertible."))
story.append(p("<b>Rango realista: $28 – $38 &nbsp;&nbsp; Target central 6m: $32 (+14.6%)</b>", QUOTE))
story.append(p("Asume: Q4 cumple guía, GM no cae debajo de 9% non-GAAP, sin crisis de liquidez por WC."))

story.append(p("Target a 12 meses (May 2027)", H3))
story.append(p(
    "<b>Catalizadores:</b> resultados completos FY26, 2 trimestres más de FY27, transición Blackwell Ultra → Rubin, "
    "posibles acuerdos soberanos/AI nacionales, resolución del overhang regulatorio."))
story.append(p("<b>Rango realista: $30 – $48 &nbsp;&nbsp; Target central 12m: $38 (+36.1%)</b>", QUOTE))
story.append(p("Asume: revenue FY27 $48–50 B, GM non-GAAP estable >11%, WC normalizado (CCC <70 días), sin eventos negativos."))

scen = [
    ["Caso", "Probabilidad", "Rango 12m", "Condición"],
    ["Bull", "~25%", "$50 – $55", "GM 13%, WC en orden, gana 1 hyperscaler nuevo, refinancia con éxito."],
    ["Base", "~50%", "$33 – $42", "Ejecuta guía, GM estable >11%, sin sorpresas negativas."],
    ["Bear", "~25%", "$18 – $22", "Pérdida Oracle confirmada, miss Q4, presión de refi, share loss continúa."],
]
story.append(tbl(scen, [0.8*inch, 1.0*inch, 1.0*inch, 3.7*inch], highlight_rows=[2]))

# --- 8. Resumen ---
story.append(p("8. Resumen ejecutivo / decisión", H2))
exec_t = [
    ["Métrica", "Valor"],
    ["Precio actual", "$27.92"],
    ["Fair value central (hoy)", "~$34"],
    ["Margen vs fair value", "+22%"],
    ["Target 6 meses", "$32 (+15%)"],
    ["Target 12 meses", "$38 (+36%)"],
    ["Caso bull 12m", "$50–55"],
    ["Caso bear 12m", "$18–22"],
    ["Risk/Reward 12m", "~1.6 a 1 (favorable, no extremo)"],
]
story.append(tbl(exec_t, [2.4*inch, 4.0*inch], highlight_rows=[2,4,5]))

story.append(Spacer(1, 6))
story.append(p(
    "<b>Tesis en una frase:</b> SMCI está descontada vs su fair value, pero los descuentos están "
    "justificados por riesgos reales (working capital, gobernanza, concentración de clientes). El "
    "\"catch up\" con Dell es plausible (35–45% prob.) pero el \"catch up\" con NVDA/AVGO es "
    "estructuralmente imposible. Posición de tamaño moderado con stop psicológico en ~$22 tiene "
    "risk/reward aceptable; el \"home run\" requiere ejecución que la compañía aún no ha demostrado "
    "en dos trimestres seguidos.", QUOTE))

# --- Sources ---
story.append(p("Fuentes", H2))
sources = [
    "Yahoo Finance — SMCI Quote: finance.yahoo.com/quote/SMCI/",
    "CNBC — Super Micro Q3 2026 earnings report (5-may-2026)",
    "Motley Fool — SMCI Q3 2026 earnings transcript",
    "StockTitan — SMCI 8-K Q3 FY26 financial results",
    "Foreign Policy Journal — SMCI close $27.92 (6-may-2026)",
    "24/7 Wall St — Dell vs Super Micro vs HPE April 2026",
    "StockAnalysis — DELL Statistics & Valuation",
    "Capital.com — NVIDIA Market Cap May 2026",
    "GuruFocus — AVGO Forward PE (May 2026)",
    "GuruFocus — AMD Forward PE (May 2026)",
    "Hindenburg Research — SMCI report (legacy)",
]
for s in sources:
    story.append(p("• " + s, SMALL))

story.append(Spacer(1, 8))
story.append(p(
    "<i>Disclaimer: Análisis hecho con fines educativos/ilustrativos. No es recomendación de inversión. "
    "Incluye supuestos del autor que pueden no materializarse. La data subyacente fue obtenida de "
    "fuentes públicas a la fecha del reporte.</i>", SMALL))

doc.build(story)
print(f"PDF generado: {OUT}")
