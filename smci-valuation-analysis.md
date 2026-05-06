# Análisis de Valoración SMCI (Super Micro Computer)
**Fecha:** 6 de mayo, 2026
**Precio de cierre:** $27.92 USD
**Analista:** Modelo independiente (sin uso de price targets publicados por sell-side)

---

## 1. Aclaración estructural previa

SMCI NO es una semiconductora; es un **integrador de sistemas de servidores AI** (rack-scale OEM). Los chips los diseña NVIDIA / AMD / Broadcom; SMCI ensambla. Por lo tanto, comparar su valoración directamente contra NVDA, AVGO o AMD es engañoso — sus márgenes brutos son estructuralmente diferentes (70%+ vs ~10%). Los **comparables correctos son Dell y HPE** (también OEMs de servidores AI). En el resto del análisis se tratará a NVDA/AVGO/AMD como benchmark de mercado/sentimiento, no como múltiplos aplicables.

---

## 2. Snapshot comparativo (May 2026)

| Compañía | Market Cap | Precio | P/E TTM | P/E Fwd | Rev TTM | EV/Sales | YTD 2026 |
|----------|-----------:|-------:|--------:|--------:|--------:|---------:|---------:|
| NVDA  | $4.78 T   | $196.85 | 40.5x  | ~32x   | $215.9 B | ~22x   | +flat/+ |
| AVGO  | $1.99 T   | -      | 80.8x  | 38.0x  | ~$60 B   | ~33x   | +      |
| AMD   | $579 B    | $341.54 | 127.9x | 54.0x  | ~$32 B   | ~18x   | +      |
| **DELL** | **$130 B** | **$208** | 20.9x | 15.2x  | $113.5 B | ~1.28x | **+67%** |
| **HPE**  | ~$30 B    | ~$23   | ~14x   | ~12x   | ~$32 B   | ~1.4x  | +20%   |
| **SMCI** | **$19.9 B** | **$27.92** | ~12x | ~11x | ~$33 B (TTM) | **0.69x** | **-7%** |

**Observación clave:** SMCI cotiza al múltiplo más bajo del grupo OEM en EV/Sales y P/E forward, pero también tiene el peor desempeño YTD. El mercado le está aplicando un descuento de riesgo significativo, no un descuento de valor irracional.

---

## 3. Datos fundamentales SMCI (Q3 FY26, trimestre cerrado 31-mar-2026)

### Income Statement
- **Revenue Q3:** $10.24 B (vs estimado $12.33 B → miss de -17%)
- **Revenue YoY:** +123%
- **Non-GAAP EPS:** $0.84 (beat de +35% sobre $0.62 esperado)
- **Non-GAAP Gross Margin:** 10.1% (recuperación desde 6.4% en Q2 FY26)
- **Guidance FY26 completo:** $38.9 B – $40.4 B (punto medio $39.65 B)
- **Guidance Q4 FY26:** Revenue $11.0–12.5 B; EPS $0.65–$0.79

### Balance Sheet (al 31-mar-2026)
- Cash & equivalents: $1.29 B
- Bank debt + convertibles: $8.80 B
- **Net debt: $7.50 B** (vs $787 M trimestre anterior — deterioro masivo)
- Inventario: $11.1 B (vs $10.6 B Q2)
- Cash conversion cycle: **106 días** (vs 54 días en Q2 — deterioro de 96%)
- Días de inventario: 106 (vs 63)
- DSO: 85 días (vs 49)

### Capital Structure
- Diluted shares (non-GAAP): 709 M Q3 → guía 712 M Q4
- Diluted shares (GAAP): 692 M Q3 → guía 695 M Q4

### Riesgos cualitativos
- **Concentración:** ~58% del revenue en top-3 clientes (CoreWeave, xAI, Tesla)
- **Pérdida de exclusividad:** Tesla y xAI ahora también compran a Dell
- **Reportes adversos:** BlueFin reportó posible pérdida de contrato Oracle (mayo 2026); Hindenburg legacy aún pesa
- **Competencia:** Dell tiene backlog AI de $43 B; HPE creció networking +152% post-Juniper

---

## 4. Modelo propio de valoración (3 métodos)

### Método A — EV/Sales relativo a peers OEM
EV actual SMCI: 712 M × $27.92 + $7.5 B net debt = **$27.39 B**
Forward sales (mid FY26): **$39.65 B**
EV/Sales actual: **0.69x**

| Escenario | Múltiplo aplicado | EV implícito | Equity | Precio |
|-----------|-----------------:|-------------:|-------:|-------:|
| Bear (descuento extremo, pérdida share) | 0.55x | $21.8 B | $14.3 B | **$20.1** |
| Base (50% del múltiplo de Dell, justifica el riesgo) | 0.85x | $33.7 B | $26.2 B | **$36.8** |
| Bull (paridad con Dell) | 1.20x | $47.6 B | $40.1 B | **$56.3** |

### Método B — P/E forward
Estimación FY26 EPS (suma Q1–Q4):
- Q1 FY26: ~$0.30 (estimado conservador)
- Q2 FY26: $0.69 (reportado)
- Q3 FY26: $0.84 (reportado)
- Q4 FY26: $0.72 (mid de guía)
- **EPS FY26 ≈ $2.55**

FY27 — proyección propia:
- Revenue +25% (deceleración por madurez del ciclo y Dell ganando share): $49.6 B
- Operating margin recuperándose a 6.5% (con ramp de DCBBS y mix mejor): $3.22 B EBIT
- Tax 17%, intereses ~$0.45 B: Net income $2.30 B
- **EPS FY27 ≈ $3.20**

| Escenario | P/E aplicado | EPS base | Precio |
|-----------|-------------:|---------:|-------:|
| Bear (premio de riesgo de 60% vs Dell) | 7x | $2.55 | **$17.9** |
| Base (descuento ~30% vs Dell forward 15x) | 11x | $2.85 (blend FY26/FY27) | **$31.4** |
| Bull (paridad Dell forward 15x) | 15x | $3.20 | **$48.0** |

### Método C — DCF simplificado
Supuestos:
- Revenue: FY26 $39.6 B → CAGR 18% a FY30 ($76 B) → terminal +4%
- Operating margin: 5% FY26 → 8% terminal (con DCBBS y escala)
- WACC: 12% (beta alta, governance risk)
- Working capital: drag de ~$2 B en FY26-FY27 luego normaliza
- Net debt: $7.5 B; shares: 712 M

FCF descontado:
| Año | FCF | PV @ 12% |
|-----|-----|---------:|
| FY27 | $1.8 B | $1.61 B |
| FY28 | $2.8 B | $2.23 B |
| FY29 | $3.6 B | $2.56 B |
| FY30 | $4.2 B | $2.67 B |
| Terminal | $4.2B × 1.04/(0.12-0.04) = $54.6 B | $34.7 B |

**EV total = $43.8 B; Equity = $36.3 B; Precio = $51.0**

Sensibilidad:
- WACC 14%: precio cae a ~$36
- Margen terminal solo 6%: precio cae a ~$32
- Caso muy adverso (WACC 14% + margen 6%): ~$22

---

## 5. Síntesis: Fair Value actual

Promedio ponderado (40% Método A, 30% Método B, 30% Método C):

| Escenario | Probabilidad asignada | Precio |
|-----------|----------------------:|-------:|
| Bear      | 25%                   | $19–22 |
| Base      | 50%                   | $33–37 |
| Bull      | 25%                   | $50–55 |

**Fair Value ponderado actual ≈ $34 USD** (rango $30–38)

> **Conclusión sobre el precio actual ($27.92):** SMCI cotiza ~17–22% por debajo de mi fair value central. Hay margen de seguridad real, pero el descuento existe por razones legítimas (working capital, governance, concentración). No es un "deep value sin razón" — es un "value con riesgos identificables".

---

## 6. Probabilidad de "catch up" con peers

| Comparable | Probabilidad de cerrar gap | Lógica |
|------------|--------------------------:|--------|
| NVDA / AVGO / AMD | **~0%** | Modelos de negocio incomparables (chip designers vs assemblers). Nunca llegará a esos múltiplos. |
| Dell (gap ~50% en EV/Sales) | **35–45%** en 12 meses | Posible si: márgenes >12% sostenidos, WC normaliza, sin nuevos episodios de governance |
| HPE | **50%** | HPE no es un objetivo aspiracional; es paridad razonable |
| Su propio máximo 52w ($62.36) | **<15%** en 12 meses | Requeriría re-rating completo + crecimiento sorpresa + perdón total del mercado |

**Veredicto:** El "catch up" relevante es contra Dell, no contra el sector semis. La compañía puede volver a $40–50 si ejecuta dos trimestres limpios consecutivos. Volver a >$60 requiere un evento extraordinario (gran contrato anunciado, resolución legal definitiva, etc.).

---

## 7. Price Targets (no analista — modelo propio)

### Target a 6 meses (Nov 2026)
**Catalizadores en ventana:**
- Earnings Q4 FY26 (agosto 2026) — clave para validar guía
- Earnings Q1 FY27 (noviembre 2026)
- Ramp completo del rack GB300
- Posible refinanciación del convertible (presión)

**Rango realista: $28 – $38**
**Target central 6m: $32**  (+14.6% desde $27.92)

Esto asume:
- Q4 cumple guía (no nuevo miss)
- GM no cae debajo de 9% non-GAAP
- No hay crisis de liquidez por el WC

### Target a 12 meses (May 2027)
**Catalizadores:**
- Resultados completos FY26 (resultado anual)
- 2 trimestres más de FY27
- Transición Blackwell Ultra → Rubin (NVIDIA)
- Posibles acuerdos soberanos/AI nacionales
- Resolución (o no) del overhang regulatorio/legal

**Rango realista: $30 – $48**
**Target central 12m: $38**  (+36.1% desde $27.92)

Esto asume:
- Revenue FY27 alcanza $48–50 B
- GM non-GAAP estabilizado >11%
- WC normalizado (CCC vuelve a <70 días)
- Sin nuevos eventos negativos materiales

### Caso bull (12m, prob ~25%): $50–55
- GM a 13%, WC en orden, gana 1 hyperscaler nuevo, refinancia con éxito.

### Caso bear (12m, prob ~25%): $18–22
- Pérdida de Oracle confirmada, miss en Q4 FY26, presión de refinanciamiento, share loss continúa.

---

## 8. Resumen ejecutivo / decisión

| Métrica | Valor |
|---------|------:|
| Precio actual | $27.92 |
| **Fair value central (hoy)** | **~$34** |
| Margen vs fair value | +22% |
| **Target 6 meses** | **$32** (+15%) |
| **Target 12 meses** | **$38** (+36%) |
| Caso bull 12m | $50–55 |
| Caso bear 12m | $18–22 |
| Risk/Reward 12m | ~1.6 a 1 (favorable pero no extremo) |

**Tesis en una frase:** SMCI está descontada vs su fair value, pero los descuentos están justificados por riesgos reales (working capital, gobernanza, concentración de clientes). El "catch up" con Dell es plausible (35–45% prob.) pero el "catch up" con NVDA/AVGO es estructuralmente imposible. Posición de tamaño moderado con stop psicológico en ~$22 tiene risk/reward aceptable; el "home run" requiere ejecución que la compañía aún no ha demostrado en dos trimestres seguidos.

---

## Fuentes
- [Yahoo Finance — SMCI Quote](https://finance.yahoo.com/quote/SMCI/)
- [CNBC — Super Micro Q3 2026 earnings report](https://www.cnbc.com/2026/05/05/super-micro-smci-q3-earnings-report-2026.html)
- [Motley Fool — SMCI Q3 2026 transcript](https://www.fool.com/earnings/call-transcripts/2026/05/05/super-micro-smci-q3-2026-earnings-transcript/)
- [StockTitan — SMCI 8-K Q3 FY26](https://www.stocktitan.net/sec-filings/SMCI/8-k-super-micro-computer-inc-reports-material-event-e70b2f8b3cb7.html)
- [Foreign Policy Journal — SMCI close $27.92](https://www.foreignpolicyjournal.com/2026/05/06/super-micro-nasdaq-smci-stock-closes-at-27-92-ahead-of-q3-earnings-as-legal-headwinds-persist/)
- [24/7 Wall St — Dell vs Super Micro vs HPE April 2026](https://247wallst.com/investing/2026/05/01/dell-super-micro-or-hpe-which-ai-server-stock-crushed-it-in-april/)
- [StockAnalysis — DELL Statistics](https://stockanalysis.com/stocks/dell/statistics/)
- [Capital.com — NVIDIA Market Cap May 2026](https://capital.com/en-int/markets/shares/nvidia-corp-share-price/market-cap)
- [GuruFocus — AVGO Forward PE](https://www.gurufocus.com/term/forward-pe-ratio/AVGO)
- [GuruFocus — AMD Forward PE](https://www.gurufocus.com/term/forward-pe-ratio/AMD)
- [Hindenburg Research — SMCI report (legacy)](https://hindenburgresearch.com/smci/)

> **Disclaimer:** Análisis hecho con fines educativos/ilustrativos. No es recomendación de inversión. Incluye supuestos del autor que pueden no materializarse.
