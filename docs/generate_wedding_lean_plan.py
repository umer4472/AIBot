#!/usr/bin/env python3
"""Generate updated 50-Day Wedding Lean Plan PDF with machine alternatives."""

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

OUTPUT = "/opt/cursor/artifacts/Wedding-Lean-Plan-Machines.pdf"
PAGE_W, PAGE_H = A4
MARGIN = 14 * mm

NAVY = colors.HexColor("#1a2744")
ACCENT = colors.HexColor("#2d6a4f")
LIGHT = colors.HexColor("#f4f7f5")
ROW_ALT = colors.HexColor("#eef3f0")
LINE = colors.HexColor("#c5d0c9")
MUTED = colors.HexColor("#4a5568")


def styles():
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "Title",
            parent=base["Title"],
            fontName="Helvetica-Bold",
            fontSize=20,
            textColor=NAVY,
            spaceAfter=4,
            alignment=TA_CENTER,
            leading=24,
        ),
        "subtitle": ParagraphStyle(
            "Subtitle",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9.5,
            textColor=MUTED,
            spaceAfter=10,
            alignment=TA_CENTER,
            leading=13,
        ),
        "h1": ParagraphStyle(
            "H1",
            parent=base["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=13,
            textColor=NAVY,
            spaceBefore=12,
            spaceAfter=6,
            leading=16,
        ),
        "h2": ParagraphStyle(
            "H2",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=11,
            textColor=ACCENT,
            spaceBefore=10,
            spaceAfter=4,
            leading=14,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9,
            textColor=colors.HexColor("#1f2937"),
            leading=12.5,
            spaceAfter=4,
        ),
        "small": ParagraphStyle(
            "Small",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8,
            textColor=MUTED,
            leading=11,
            spaceAfter=3,
        ),
        "cell": ParagraphStyle(
            "Cell",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8,
            textColor=colors.HexColor("#1f2937"),
            leading=10.5,
        ),
        "cell_b": ParagraphStyle(
            "CellB",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=8,
            textColor=NAVY,
            leading=10.5,
        ),
        "note": ParagraphStyle(
            "Note",
            parent=base["Normal"],
            fontName="Helvetica-Oblique",
            fontSize=8.5,
            textColor=MUTED,
            leading=11.5,
            spaceBefore=4,
            spaceAfter=6,
        ),
        "callout": ParagraphStyle(
            "Callout",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9,
            textColor=NAVY,
            leading=12.5,
            spaceAfter=4,
        ),
    }


def p(text, style):
    return Paragraph(text.replace("\n", "<br/>"), style)


def table(data, col_widths, header=True):
    t = Table(data, colWidths=col_widths, repeatRows=1 if header else 0)
    style_cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("ALIGN", (0, 0), (-1, 0), "LEFT"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("GRID", (0, 0), (-1, -1), 0.4, LINE),
        ("BOX", (0, 0), (-1, -1), 0.8, NAVY),
    ]
    for i in range(1, len(data)):
        if i % 2 == 0:
            style_cmds.append(("BACKGROUND", (0, i), (-1, i), ROW_ALT))
        else:
            style_cmds.append(("BACKGROUND", (0, i), (-1, i), colors.white))
    t.setStyle(TableStyle(style_cmds))
    return t


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, PAGE_H - 6 * mm, PAGE_W, 6 * mm, fill=1, stroke=0)
    canvas.setFillColor(ACCENT)
    canvas.rect(0, 0, PAGE_W, 5 * mm, fill=1, stroke=0)
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica", 7.5)
    canvas.drawString(MARGIN, 1.6 * mm, "50-Day Wedding Lean Plan  ·  Machine gym edition")
    canvas.drawRightString(PAGE_W - MARGIN, 1.6 * mm, f"Page {doc.page}")
    canvas.restoreState()


def build():
    s = styles()
    story = []
    usable = PAGE_W - 2 * MARGIN

    story.append(p("50-Day Wedding Lean Plan", s["title"]))
    story.append(
        p(
            "Male · 27 years · 85 kg · 5′10″ · 1 year of gym training · office job<br/>"
            "<b>Machine gym edition</b> — fully equipped gym: use machines for cleaner angles and form",
            s["subtitle"],
        )
    )
    story.append(
        p(
            "<b>Goal in 50 days:</b> about 79–82 kg, clearly leaner. Fuller shoulders and arms, "
            "flatter stomach, sharper face.",
            s["body"],
        )
    )
    story.append(
        p(
            "<b>How:</b> 3 meals a day (2 is also fine), ~2,300 kcal, 180 g protein, "
            "6 gym days a week, 8,000–10,000 steps a day.",
            s["body"],
        )
    )

    story.append(p("Daily targets", s["h1"]))
    story.append(
        table(
            [
                [p("<b></b>", s["cell_b"]), p("<b>Gym day (Mon–Sat)</b>", s["cell_b"]), p("<b>Rest day (Sunday)</b>", s["cell_b"])],
                [p("<b>Calories</b>", s["cell_b"]), p("2,200–2,300", s["cell"]), p("~2,000", s["cell"])],
                [p("<b>Protein</b>", s["cell_b"]), p("180 g", s["cell"]), p("180 g", s["cell"])],
                [p("<b>Carbs</b>", s["cell_b"]), p("~230 g", s["cell"]), p("~150 g (half rice/roti at dinner)", s["cell"])],
                [p("<b>Fat</b>", s["cell_b"]), p("~60–65 g", s["cell"]), p("~60–65 g", s["cell"])],
                [p("<b>Water</b>", s["cell_b"]), p("3–3.5 litres (1-litre bottle on desk, refill 3×)", s["cell"]), p("Same", s["cell"])],
            ],
            [28 * mm, 70 * mm, 70 * mm],
        )
    )
    story.append(
        p(
            "Meal count does not matter for fat loss. What matters is total calories and protein. "
            "3 meals or 2 meals both work if you hit 180 g protein.",
            s["note"],
        )
    )

    story.append(p("Coffee with milk: rules", s["h1"]))
    story.append(
        p(
            "Up to 2–3 cups a day, each with about 150 ml milk (low-fat or toned). "
            "No sugar — use stevia or sugar-free sweetener. "
            "2 tsp sugar × 3 cups ≈ 100 kcal of nothing every day.<br/>"
            "Each cup with milk ≈ 75 kcal and 5 g protein (already counted below).<br/>"
            "No coffee after 4–5 pm. One cup before an evening workout is OK if sleep stays good.<br/>"
            "Avoid café drinks: lattes with syrup, frappés, mochas (250–450 kcal each).",
            s["body"],
        )
    )

    story.append(p("Option A: 3 meals a day (recommended)", s["h1"]))
    story.append(
        p(
            "Assumes: breakfast at home → office → evening gym → dinner at home. "
            "The banana is a snack, not a meal.",
            s["small"],
        )
    )
    story.append(
        table(
            [
                [p("<b>When</b>", s["cell_b"]), p("<b>What to eat</b>", s["cell_b"]), p("<b>kcal</b>", s["cell_b"]), p("<b>Protein</b>", s["cell_b"])],
                [
                    p("<b>Meal 1: Breakfast</b><br/>home, ~7–8 am", s["cell"]),
                    p(
                        "Omelette: 3 whole eggs + 3 egg whites (1 tsp oil)<br/>"
                        "2 whole-wheat rotis or 80 g oats<br/>Coffee with milk (no sugar)",
                        s["cell"],
                    ),
                    p("~615", s["cell"]),
                    p("~42 g", s["cell"]),
                ],
                [
                    p("<b>Meal 2: Lunch</b><br/>office lunch box, ~1 pm", s["cell"]),
                    p(
                        "180 g cooked chicken breast (tikka / grilled / karahi, little oil)<br/>"
                        "200 g cooked rice or 2 rotis<br/>Salad (cucumber, tomato, onion)<br/>"
                        "200 g plain dahi or 1 protein Greek yogurt (+10 g protein)",
                        s["cell"],
                    ),
                    p("~760", s["cell"]),
                    p("~69 g", s["cell"]),
                ],
                [p("Afternoon", s["cell"]), p("Coffee with milk (no sugar)", s["cell"]), p("~75", s["cell"]), p("~5 g", s["cell"])],
                [p("Before gym", s["cell"]), p("1 banana (at your desk before you leave)", s["cell"]), p("~105", s["cell"]), p("~1 g", s["cell"])],
                [
                    p("<b>Meal 3: Dinner</b><br/>after gym", s["cell"]),
                    p(
                        "180 g cooked chicken / fish / lean beef<br/>"
                        "2 rotis or 150 g rice<br/>Cooked vegetables / sabzi (1 tsp oil)",
                        s["cell"],
                    ),
                    p("~640", s["cell"]),
                    p("~67 g", s["cell"]),
                ],
                [p("<b>Total</b>", s["cell_b"]), p("", s["cell"]), p("<b>~2,200</b>", s["cell_b"]), p("<b>~184 g</b>", s["cell_b"])],
            ],
            [32 * mm, usable - 62 * mm, 15 * mm, 15 * mm],
        )
    )
    story.append(
        p(
            "If hungry or under 2,200 kcal: add 15 almonds (20 g) or 1 tbsp peanut butter (~100–120 kcal). "
            "Swap banana for 2–3 dates before gym if preferred.",
            s["note"],
        )
    )

    story.append(p("Option B: 2 meals a day", s["h1"]))
    story.append(p("For busy days: no breakfast, just coffee in the morning.", s["small"]))
    story.append(
        table(
            [
                [p("<b>When</b>", s["cell_b"]), p("<b>What to eat</b>", s["cell_b"]), p("<b>kcal</b>", s["cell_b"]), p("<b>Protein</b>", s["cell_b"])],
                [p("Morning", s["cell"]), p("Coffee with milk (no sugar)", s["cell"]), p("~75", s["cell"]), p("~5 g", s["cell"])],
                [
                    p("<b>Meal 1: Lunch</b><br/>office, ~1 pm", s["cell"]),
                    p("250 g cooked chicken breast<br/>250 g cooked rice or 3 rotis<br/>Salad + 200 g dahi", s["cell"]),
                    p("~940", s["cell"]),
                    p("~92 g", s["cell"]),
                ],
                [p("Afternoon", s["cell"]), p("Coffee with milk + 1 banana before gym", s["cell"]), p("~180", s["cell"]), p("~6 g", s["cell"])],
                [
                    p("<b>Meal 2: Dinner</b><br/>after gym", s["cell"]),
                    p(
                        "200 g cooked chicken / fish / beef<br/>3 rotis or 200 g rice<br/>Vegetables<br/>"
                        "1 scoop whey in water (after gym or with dinner)",
                        s["cell"],
                    ),
                    p("~910", s["cell"]),
                    p("~101 g", s["cell"]),
                ],
                [p("<b>Total</b>", s["cell_b"]), p("", s["cell"]), p("<b>~2,100</b>", s["cell_b"]), p("<b>~204 g</b>", s["cell_b"])],
            ],
            [32 * mm, usable - 62 * mm, 15 * mm, 15 * mm],
        )
    )
    story.append(
        p(
            "On the 2-meal plan, each meal must have 90+ g protein. "
            "If you can’t eat that much chicken, the whey scoop is the easiest fix.",
            s["note"],
        )
    )

    story.append(PageBreak())
    story.append(p("Your protein dessert: Adonis Protein Cookie Dough (Baklava)", s["h1"]))
    story.append(
        p(
            "1 serving ≈ 140 kcal · 21 g casein protein · low carb. Mix with water and eat like dessert.<br/>"
            "<b>Option A:</b> 1 serving after dinner instead of peanut butter/almonds → ~2,340 kcal, ~205 g protein.<br/>"
            "<b>Option B:</b> instead of the whey scoop at dinner. Same protein, similar calories.<br/>"
            "Sweet craving? Use this instead of mithai, chocolate or biscuits.<br/>"
            "Max 1 serving a day (2 at most on a high-hunger day). Measure the scoop — don’t eat from the jar.",
            s["body"],
        )
    )

    story.append(p("Flavoured protein Greek yogurt", s["h2"]))
    story.append(
        p(
            "Typical cup: ~120–160 kcal · 15–20 g protein. Use instead of dahi at lunch, as an office snack, "
            "or with the banana before gym. 1 cup/day fits as-is. Pick 15 g+ protein and ≤12 g sugar. "
            "Skip “fruit on the bottom” dessert versions.",
            s["body"],
        )
    )

    story.append(p("Dates, nuts and fruit", s["h2"]))
    story.append(
        table(
            [
                [p("<b>Food</b>", s["cell_b"]), p("<b>Daily limit</b>", s["cell_b"]), p("<b>Notes</b>", s["cell_b"])],
                [
                    p("Dates", s["cell"]),
                    p("2–3 normal (~60–70 kcal) or 1–2 Medjool (~65 kcal each)", s["cell"]),
                    p("Best before gym; swap for banana.", s["cell"]),
                ],
                [
                    p("Nuts", s["cell"]),
                    p("20 g/day (~120 kcal): ~15 almonds / 25 pistachios / 5 walnut halves", s["cell"]),
                    p("Instead of peanut butter. Count them — never from the bag.", s["cell"]),
                ],
                [p("Anaar", s["cell"]), p("½–1 cup seeds (~70–145 kcal)", s["cell"]), p("Great with yogurt or fruit salad.", s["cell"])],
                [p("Aaru (peach)", s["cell"]), p("1–2 peaches (~60 kcal each)", s["cell"]), p("Low calorie, filling.", s["cell"])],
                [
                    p("Other fruit", s["cell"]),
                    p("1 piece / 1 cup per serving", s["cell"]),
                    p("Mango, grapes, banana = higher sugar — keep portions small.", s["cell"]),
                ],
            ],
            [28 * mm, 70 * mm, usable - 98 * mm],
        )
    )
    story.append(
        p(
            "Total fruit: 2–3 servings/day. More fruit → less rice/roti. Avoid fruit juice.",
            s["note"],
        )
    )

    story.append(p("Meal idea: boiled chicken + fruit salad (~600 kcal · ~65 g protein)", s["h2"]))
    story.append(
        p(
            "200 g boiled/grilled chicken, shredded + fruit salad (½ cup anaar + 1 peach + 1 apple + cucumber/lettuce). "
            "Dressing: lemon + chaat masala + pepper, or protein Greek yogurt. No rice/roti with this meal. "
            "Avoid mayo, cream, condensed milk or sugar on the chaat.",
            s["body"],
        )
    )

    story.append(p("Rest day (Sunday)", s["h2"]))
    story.append(
        p(
            "Same meals, but no banana and half the rice/roti at dinner (fill up on vegetables). "
            "1 cheat meal per week (e.g. Saturday dinner or Sunday lunch): one normal plate, not a buffet. Still hit protein.",
            s["body"],
        )
    )

    story.append(p("Office lunch box ideas (prep 3 days at a time)", s["h2"]))
    story.append(
        table(
            [
                [p("<b>Box</b>", s["cell_b"]), p("<b>Contents</b>", s["cell_b"])],
                [p("1", s["cell"]), p("Chicken tikka (oven/air-fryer) + rice + salad + dahi", s["cell"])],
                [p("2", s["cell"]), p("Low-oil chicken karahi + 2 rotis + cucumber raita", s["cell"])],
                [p("3", s["cell"]), p("Grilled fish + rice + sabzi", s["cell"])],
                [p("4", s["cell"]), p("Lean beef/qeema (drain fat) + 2 rotis + salad", s["cell"])],
                [p("5", s["cell"]), p("Chicken + daal (1 cup) + smaller rice (daal adds carbs)", s["cell"])],
            ],
            [18 * mm, usable - 18 * mm],
        )
    )
    story.append(
        p(
            "Cook Sunday + Wednesday nights. Fridge up to 3 days. Weigh chicken after cooking.<br/>"
            "<b>Eating out:</b> grilled chicken, tikka, seekh kebab, shawarma plate (no extra sauce), salad, plain rice. "
            "Avoid fried items, naan + creamy curry, biryani (cheat meal), cold drinks, mayo sandwiches.",
            s["body"],
        )
    )

    # —— WORKOUT (machine edition) ——
    story.append(PageBreak())
    story.append(p("Workout plan: 6 days a week (machine gym edition)", s["h1"]))
    story.append(
        p(
            "<b>Machines are preferred</b> for cleaner joint angles, locked path, and stricter form — "
            "ideal while cutting for the wedding. Free-weight options are noted only if useful.<br/>"
            "<b>Warm-up every session (8 min):</b> 5 min bike/treadmill → 2 light sets of the first exercise.<br/>"
            "<b>Rest:</b> 2–3 min on heavy lifts, 60–90 sec on the rest.<br/>"
            "<b>Daily:</b> 8,000–10,000 steps. Walk 10 min after lunch; take the stairs.",
            s["callout"],
        )
    )
    story.append(
        table(
            [
                [p("<b>Day</b>", s["cell_b"]), p("<b>Workout</b>", s["cell_b"]), p("<b>Cardio</b>", s["cell_b"])],
                [p("Monday", s["cell"]), p("Push A (chest)", s["cell"]), p("—", s["cell"])],
                [p("Tuesday", s["cell"]), p("Pull A (back thickness)", s["cell"]), p("25 min incline walk after weights", s["cell"])],
                [p("Wednesday", s["cell"]), p("Legs A (heavy)", s["cell"]), p("—", s["cell"])],
                [p("Thursday", s["cell"]), p("Push B (shoulders)", s["cell"]), p("—", s["cell"])],
                [p("Friday", s["cell"]), p("Pull B (back width + arms)", s["cell"]), p("25 min incline walk after weights", s["cell"])],
                [p("Saturday", s["cell"]), p("Legs B (lighter) + abs", s["cell"]), p("Optional 20 min walk", s["cell"])],
                [p("Sunday", s["cell"]), p("Rest", s["cell"]), p("Steps only", s["cell"])],
            ],
            [28 * mm, 55 * mm, usable - 83 * mm],
        )
    )
    story.append(
        p(
            "Progression: when you hit the top of the rep range on all sets, add one plate/pin next session. "
            "On a diet, holding strength = success. If lifts drop 2 weeks in a row, eat ~200 kcal more or sleep more.",
            s["note"],
        )
    )

    def workout_block(title, rows):
        block = [p(title, s["h2"])]
        data = [[p("<b>Exercise (machine-first)</b>", s["cell_b"]), p("<b>Sets × Reps</b>", s["cell_b"]), p("<b>Form tip</b>", s["cell_b"])]]
        for name, reps, tip in rows:
            data.append([p(name, s["cell"]), p(reps, s["cell"]), p(tip, s["cell"])])
        block.append(table(data, [68 * mm, 28 * mm, usable - 96 * mm]))
        block.append(Spacer(1, 4))
        return KeepTogether(block)

    story.append(
        workout_block(
            "Monday: Push A (chest)",
            [
                ("Chest press machine (flat)", "4 × 6–8", "Seat so handles meet mid-chest; full stretch without shrugging"),
                ("Incline chest press machine", "3 × 8–10", "Seat angle ~30–45°; press up and slightly in"),
                ("Pec deck or cable chest fly", "3 × 10–12", "Slight elbow bend; squeeze at the middle"),
                ("Shoulder press machine", "3 × 8–10", "Don’t lock out hard; stop just before elbows click"),
                ("Lateral raise machine or cable", "3 × 12–15", "Lead with elbows; stop at shoulder height"),
                ("Triceps rope / machine pushdown", "3 × 10–12", "Elbows pinned to sides; spread rope at bottom"),
            ],
        )
    )

    story.append(
        workout_block(
            "Tuesday: Pull A (back thickness)",
            [
                ("Lat pulldown (or assisted pull-up)", "4 × 6–10", "Pull to upper chest; control the stretch up"),
                ("Chest-supported machine row", "3 × 8–10", "Chest glued to pad; squeeze shoulder blades"),
                ("Single-arm cable / machine row", "3 × 10–12", "Elbow close to body; pause at the hip"),
                ("Cable face pulls", "3 × 15", "Pull to forehead; external rotate at the end"),
                ("Preacher curl machine or cable curl", "3 × 10–12", "Full stretch at bottom; no swinging"),
                ("Rope hammer curls (cable)", "2 × 10–12", "Neutral grip; elbows still"),
            ],
        )
    )

    story.append(
        workout_block(
            "Wednesday: Legs A (heavy)",
            [
                ("Leg press or hack squat", "4 × 6–10", "Feet mid-platform; knees track over toes"),
                ("Smith / machine RDL or hip hinge", "3 × 8–10", "Soft knees; push hips back; feel hamstrings"),
                ("Lying or seated leg curl", "3 × 10–12", "Full squeeze at top; slow negative"),
                ("Smith reverse lunge or split-squat", "3 × 10 / leg", "Tall torso; front knee tracks over mid-foot"),
                ("Standing or seated calf machine", "4 × 12–15", "Full stretch at bottom; pause at top"),
                ("Plank", "3 × 45–60 sec", "Ribs down; glutes tight"),
            ],
        )
    )

    story.append(PageBreak())
    story.append(
        workout_block(
            "Thursday: Push B (shoulders)",
            [
                ("Shoulder press machine", "4 × 8–10", "Neutral or slight forward path; don’t flare ribs"),
                ("Chest press machine (lighter)", "3 × 10–12", "Controlled tempo; leave 1–2 reps in reserve"),
                ("Cable lateral raises", "3 × 12–15", "Cable behind body for better side-delt angle"),
                ("Reverse pec deck (rear delts)", "3 × 12–15", "Arms almost straight; squeeze rear delts"),
                ("Assisted dip machine (or close-grip press)", "3 × 8–12", "Lean slightly forward for chest; upright for triceps"),
                ("Cable / machine overhead triceps", "2 × 12", "Elbows high and fixed; full stretch"),
            ],
        )
    )

    story.append(
        workout_block(
            "Friday: Pull B (back width + arms)",
            [
                ("Wide-grip lat pulldown", "4 × 8–10", "Pull elbows down to sides; stretch at top"),
                ("Seated cable / machine row", "3 × 10–12", "Neutral grip; chest up; squeeze mid-back"),
                ("Straight-arm cable pulldown", "3 × 12", "Slight elbow bend; feel lats, not arms"),
                ("Preacher / machine curl (incline angle)", "3 × 10–12", "Long stretch at bottom for peak biceps"),
                ("Preacher curl machine (second angle)", "2 × 12", "Strict — no body swing"),
            ],
        )
    )

    story.append(
        workout_block(
            "Saturday: Legs B (lighter) + abs",
            [
                ("Leg press (lighter)", "3 × 10–12", "Higher foot placement for glutes/hams"),
                ("Smith Bulgarian split squat", "3 × 10 / leg", "Rear foot elevated; control descent"),
                ("Leg extension", "3 × 12", "Squeeze quads at top; don’t slam the stack"),
                ("Seated calf raises", "4 × 15", "Pause stretch at bottom"),
                ("Cable crunch or hanging leg raise", "3 × 12–15", "Curl ribs to pelvis; don’t yank with arms"),
                ("Bicycle crunch", "3 × 12 / side", "Slow — elbow to opposite knee"),
            ],
        )
    )

    story.append(p("Machine form checklist", s["h2"]))
    story.append(
        p(
            "1. Adjust seat so joints line up with the machine’s pivot (elbows with press pads, knees with leg-curl cam).<br/>"
            "2. Use a full controlled range — stretch under load, squeeze at peak.<br/>"
            "3. Prefer chest-supported and guided machines when tired; they protect form while cutting.<br/>"
            "4. Same sets/reps as listed. Add weight when you hit the top of the range on all sets.<br/>"
            "5. Machines won’t slow fat loss. Diet, protein, steps and sleep still do 80% of the work.",
            s["body"],
        )
    )

    story.append(p("50-day timeline", s["h1"]))
    story.append(
        table(
            [
                [p("<b>Days</b>", s["cell_b"]), p("<b>Focus</b>", s["cell_b"])],
                [
                    p("1–14", s["cell"]),
                    p("Build the habit. Front/side/back photos. Weigh 3× a week in the morning.", s["cell"]),
                ],
                [
                    p("15–35", s["cell"]),
                    p(
                        "Main fat loss: ~0.5–0.8 kg/week. Flat weight 10+ days → cut ~200 kcal "
                        "(smaller rice) or add 2 incline walks.",
                        s["cell"],
                    ),
                ],
                [p("36–43", s["cell"]), p("Stay consistent, keep protein high, sleep 7–8 hours.", s["cell"])],
                [
                    p("44–50 (wedding week)", s["cell"]),
                    p(
                        "No crash dieting. Train Mon–Thu, then light or rest. Plenty of water. "
                        "No new foods/supplements. Final suit fitting ~1 week before.",
                        s["cell"],
                    ),
                ],
            ],
            [40 * mm, usable - 40 * mm],
        )
    )

    story.append(p("Daily checklist", s["h1"]))
    checks = [
        "180 g protein",
        "~2,200–2,300 kcal (2,000 on Sunday)",
        "Coffee with milk, no sugar, max 3 cups, none after 5 pm",
        "3+ litres of water",
        "Max 1 serving protein cookie dough (measured)",
        "Nuts max 20 g · dates max 3 · fruit 2–3 servings",
        "Gym session done (machines OK)",
        "8,000+ steps",
        "7–8 hours of sleep",
    ]
    for c in checks:
        story.append(p(f"☐  {c}", s["body"]))

    story.append(Spacer(1, 8))
    story.append(
        p(
            "Calorie and protein values are estimates. Track with MyFitnessPal or HealthifyMe for the first 2 weeks. "
            "If you have a medical condition, check with a doctor before starting a diet.",
            s["small"],
        )
    )

    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=A4,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=12 * mm,
        bottomMargin=10 * mm,
        title="50-Day Wedding Lean Plan — Machine Gym Edition",
        author="Wedding Lean Plan",
    )
    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    print(OUTPUT)


if __name__ == "__main__":
    build()
