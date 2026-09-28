from helpers import *


def units():
    s = SVG(760, 200, "Units of digital data from bit to terabyte")
    items = [("bit", "0 or 1"), ("nibble", "4 bits"), ("byte", "8 bits"), ("kilobyte", "1,000 bytes"), ("megabyte", "1,000 kB"), ("gigabyte", "1,000 MB"), ("terabyte", "1,000 GB")]
    for i, (a, b) in enumerate(items):
        x = 20 + i * 104
        s.box(x, 40, 92, 56, a, b, size=13, fill=["#f4f9fc", "#edf5fb", "#e6f1f9", "#dfedf8", "#d7e8f6", "#cfe3f4", "#c4dcf1"][i])
        if i:
            s.arrow(x - 12, 68, x - 1, 68, width=1.8)
    s.text(380, 135, "Storage makers use powers of 10 (1 kB = 1,000 bytes). Operating systems often use powers of 2:", size=12)
    s.text(380, 155, "1 KiB (kibibyte) = 1,024 bytes, 1 MiB = 1,024 KiB, 1 GiB = 1,024 MiB.", size=12, bold=True)
    s.text(380, 180, "That is why a “500 GB” drive shows as about 465 GiB on a computer: same bytes, different unit.", size=12, color=WARN)
    return s.render("Units of data. Read the question carefully to see whether it means 1,000 or 1,024.")


def place_values():
    s = SVG(760, 230, "Converting a byte between binary, hexadecimal and denary")
    vals = ["128", "64", "32", "16", "8", "4", "2", "1"]
    bits = ["1", "0", "1", "1", "0", "1", "1", "0"]
    s.grid(100, 30, 8, 1, 60, 34, [vals], [["#eaf2f9"] * 8], size=13, mono=False)
    s.grid(100, 64, 8, 1, 60, 40, [bits], [["#dcebf6" if b == "1" else "white" for b in bits]], size=18)
    s.text(60, 90, "binary", size=12, anchor="end")
    s.add(f'<path d="M100 115 L100 128 L340 128 L340 115" stroke="{ACCENT}" stroke-width="2" fill="none"/>')
    s.add(f'<path d="M340 115 L340 128 L580 128 L580 115" stroke="{WARN}" stroke-width="2" fill="none"/>')
    s.text(220, 150, "1011 = 8+2+1 = 11 = B", size=14, color=ACCENT, bold=True)
    s.text(460, 150, "0110 = 4+2 = 6", size=14, color=WARN, bold=True)
    s.text(340, 190, "Hexadecimal: B6        Denary: 128 + 32 + 16 + 4 + 2 = 182", size=15, bold=True)
    s.text(680, 60, "Hex digits:", size=12)
    s.text(680, 80, "0–9, then", size=12)
    s.text(680, 100, "A=10 B=11 C=12", size=12)
    s.text(680, 120, "D=13 E=14 F=15", size=12)
    return s.render("Each hexadecimal digit stands for exactly one nibble (4 bits), so a byte is always two hex digits: 00 to FF.")


def column_sum(title, rows, carries, answer_note):
    s = SVG(760, 210, title)
    x0 = 220
    for r, (lab, bits) in enumerate(rows):
        y = 55 + r * 38
        s.text(x0 - 20, y, lab, size=13, anchor="end")
        for i, b in enumerate(bits):
            s.text(x0 + i * 38, y, b, size=20, mono=True)
    if carries:
        for i, c in enumerate(carries):
            if c.strip():
                s.text(x0 + i * 38, 22, c, size=13, color=WARN, mono=True)
    s.line(x0 - 20, 55 + (len(rows) - 1) * 38 - 26, x0 + 8 * 38, 55 + (len(rows) - 1) * 38 - 26, color=INK, width=1.5)
    s.text(380, 195, answer_note, size=12, color=ACCENT)
    return s


def addition():
    s = column_sum("Adding two binary bytes", [("92", "01011100"), ("+ 58", "00111010"), ("= 150", "10010110")], "1111    ", "")
    s.text(560, 60, "Rules for each column:", size=13, anchor="start", bold=True)
    for i, t in enumerate(["0 + 0 = 0", "0 + 1 = 1", "1 + 1 = 0, carry 1", "1 + 1 + 1 = 1, carry 1"]):
        s.text(560, 84 + i * 20, t, size=13, anchor="start", mono=True)
    s.text(380, 195, "Carries (orange) move one column to the left, just like carrying 10 in denary.", size=12, color=ACCENT)
    return s.render("Binary addition, worked from right to left. Check it: 92 + 58 = 150.")


def twos_line():
    s = SVG(760, 200, "Eight-bit two's complement place values and range")
    vals = ["−128", "64", "32", "16", "8", "4", "2", "1"]
    s.grid(140, 25, 8, 1, 60, 32, [vals], [["#fbe3d4"] + ["#eaf2f9"] * 7], size=13, mono=False)
    s.grid(140, 57, 8, 1, 60, 36, [list("11101100")], None, size=18)
    s.text(130, 81, "−20 =", size=14, anchor="end")
    s.text(380, 120, "−128 + 64 + 32 + 8 + 4 = −20", size=15, bold=True)
    s.line(60, 160, 700, 160, color=INK, width=2)
    for x, t in [(60, "−128"), (380, "0"), (700, "+127")]:
        s.line(x, 152, x, 168, color=INK, width=2)
        s.text(x, 188, t, size=13)
    s.text(220, 150, "negative numbers start with 1", size=12, color=WARN)
    s.text(540, 150, "positive numbers start with 0", size=12, color=ACCENT)
    return s.render("In two’s complement the leftmost bit is worth −128, so eight bits store −128 to +127.")


def float_fig():
    s = SVG(760, 200, "A floating point number made of a mantissa and an exponent")
    s.text(90, 40, "Mantissa (the digits)", size=13, anchor="start", bold=True)
    s.grid(90, 50, 8, 1, 44, 40, [list("01101000")], [["#fbe3d4"] + ["#dcebf6"] * 7], size=17)
    s.text(90, 112, "sign bit, then binary point: 0.1101000", size=12, anchor="start")
    s.text(520, 40, "Exponent (the scale)", size=13, anchor="start", bold=True)
    s.grid(520, 50, 4, 1, 44, 40, [list("0011")], [["#e8f1e4"] * 4], size=17)
    s.text(520, 112, "0011 = +3: move the point 3 right", size=12, anchor="start")
    s.text(380, 150, "0.1101 × 2³  →  110.1  =  4 + 2 + 0.5  =  6.5", size=16, bold=True)
    s.text(380, 182, "More mantissa bits = more precision (accuracy). More exponent bits = bigger range of sizes.", size=12, color=ACCENT)
    return s.render("Floating point works like scientific notation in binary. Most fractions (such as 0.1) cannot be stored exactly, so they are rounded.")


C1 = deeper("C1",
    h3("Units, and why 1,000 is not always 1,000"),
    units(),
    h3("Hexadecimal: a short way to write binary"),
    place_values(),
    p("Programmers and technicians use <strong>hexadecimal</strong> (base 16) because it is much easier to read than long binary strings but converts to binary instantly. You will see it in colour codes such as <code>#FF8000</code>, network MAC addresses such as <code>3C:22:FB:19:A0:7E</code>, and memory addresses in error messages."),
    table(["Denary", "Binary", "Hex", "", "Denary", "Binary", "Hex"], [
        [str(i), format(i, "04b"), format(i, "X"), "", str(i + 8), format(i + 8, "04b"), format(i + 8, "X")] for i in range(8)
    ], caption="The 16 nibbles"),
    h3("Binary arithmetic"),
    addition(),
    worked("Subtraction by adding a negative (35 − 12)", [
        "Write 12 in binary: <code>0000 1100</code>.",
        "Make it negative with two’s complement: flip every bit <code>1111 0011</code>, then add 1 → <code>1111 0100</code> (−12).",
        "Add 35 (<code>0010 0011</code>) + (−12) (<code>1111 0100</code>) = <code>1 0001 0111</code>.",
        "Throw away the carry that falls off the left of the 8 bits: <code>0001 0111</code> = 16 + 4 + 2 + 1 = 23.",
    ], "Computers subtract by adding a negative number, so the same adder circuit does both jobs."),
    worked("Multiplying and dividing with shifts", [
        "Shifting left one place doubles a number: <code>0000 0110</code> (6) becomes <code>0000 1100</code> (12).",
        "To multiply 6 × 5, write 5 as 4 + 1: (6 shifted left twice) + 6 = 24 + 6 = 30, which is <code>0001 1110</code>.",
        "Shifting right one place halves a whole number: <code>0010 1100</code> (44) shifted right twice is <code>0000 1011</code> (11), so 44 ÷ 4 = 11.",
        "Longer divisions use the same ‘bus stop’ method as denary, but each step only asks: does it go in once, or not at all?",
    ]),
    h3("Negative numbers and fractions"),
    twos_line(),
    float_fig(),
    p("<strong>Binary coded decimal (BCD)</strong> stores each denary digit in its own nibble. It is less efficient than pure binary but converts easily to the digits on a display, which is why calculators, digital clocks and some financial systems use it. When a BCD digit adds up to more than 9, add <code>0110</code> (6) to correct it and carry into the next digit."),
    terms([
        ("Nibble", "four bits; one hexadecimal digit."),
        ("Hexadecimal", "base 16, using 0–9 and A–F."),
        ("Two’s complement", "a way to store negative whole numbers where the leftmost bit has a negative place value."),
        ("Overflow", "when a result is too big for the number of bits available."),
        ("Mantissa", "the part of a floating point number that holds its digits."),
        ("Exponent", "the part of a floating point number that says where the binary point goes."),
    ]),
    think([
        ("Convert <code>0100 1111</code> to hexadecimal and denary.", "0100 = 4 and 1111 = F, so it is 4F. In denary, 64 + 8 + 4 + 2 + 1 = 79."),
        ("What is the largest number an unsigned byte can hold, and the largest in two’s complement?", "Unsigned: 255 (1111 1111). Two’s complement: +127 (0111 1111)."),
        ("Why can a bank not simply store £0.10 as a floating point number?", "0.1 has no exact binary form, so it would be stored as a tiny bit more or less. Over millions of transactions those rounding errors add up, so money is stored as whole pence (or in BCD/decimal types)."),
    ]),
)


def ascii_mask():
    s = SVG(760, 250, "Upper and lower case letters differ by one bit")
    s.text(160, 30, "Character", size=13, bold=True)
    s.text(300, 30, "Denary", size=13, bold=True)
    s.text(500, 30, "Binary", size=13, bold=True)
    rows = [("A", "65", "0100 0001"), ("a", "97", "0110 0001"), ("7", "55", "0011 0111")]
    for i, (c, d, b) in enumerate(rows):
        y = 60 + i * 34
        s.text(160, y, c, size=18, mono=True)
        s.text(300, y, d, size=16)
        s.text(500, y, b, size=18, mono=True)
    s.add(f'<rect x="470" y="72" width="16" height="46" rx="4" fill="none" stroke="{WARN}" stroke-width="2"/>')
    s.text(600, 88, "only this bit (worth 32)", size=12, color=WARN, anchor="start")
    s.text(600, 104, "is different", size=12, color=WARN, anchor="start")
    s.text(380, 180, "Mask to upper case:  0110 0001 (a)  AND  1101 1111  =  0100 0001 (A)", size=14, mono=True)
    s.text(380, 206, "Mask to lower case:  0100 0001 (A)  OR   0010 0000  =  0110 0001 (a)", size=14, mono=True)
    s.text(380, 232, "Digit character to number:  0011 0111 ('7')  AND  0000 1111  =  0000 0111 (7)", size=14, mono=True)
    return s.render("ASCII was designed so that simple bit masks change letter case or turn a digit character into its value.")


def utf8():
    s = SVG(760, 220, "Unicode characters and how many UTF-8 bytes they need")
    rows = [("A", "U+0041", "Latin capital A", "1 byte", "41"), ("é", "U+00E9", "e with acute accent", "2 bytes", "C3 A9"), ("中", "U+4E2D", "Chinese ‘middle’", "3 bytes", "E4 B8 AD"), ("😀", "U+1F600", "grinning face emoji", "4 bytes", "F0 9F 98 80")]
    heads = ["Char", "Code point", "Name", "UTF-8 size", "Bytes (hex)"]
    xs = [60, 170, 320, 500, 640]
    for x, h in zip(xs, heads):
        s.text(x, 30, h, size=13, bold=True)
    for i, r in enumerate(rows):
        y = 64 + i * 36
        for j, (x, v) in enumerate(zip(xs, r)):
            s.text(x, y, v, size=18 if j == 0 else 13, mono=j in (1, 4))
    s.text(380, 208, "ASCII characters keep the same single byte in UTF-8, so old English text is still valid.", size=12, color=ACCENT)
    return s.render("Unicode gives every character a code point; UTF-8 stores common characters in 1 byte and others in 2–4 bytes.")


C2 = deeper("C2",
    h3("Inside the ASCII code"),
    ascii_mask(),
    p("<strong>ASCII</strong> uses 7 bits, giving 128 codes: control codes (such as new line), the space, digits, punctuation and the English upper and lower case letters. Many systems use an 8-bit extended ASCII with 256 codes, but different countries filled the extra 128 codes differently, so a file could show the wrong symbols on another computer."),
    utf8(),
    p("<strong>Unicode</strong> solves this by giving one agreed number, a <strong>code point</strong>, to more than 150,000 characters from almost every writing system, plus symbols and emoji. UTF-8 is the most common way to store those code points as bytes. The first 128 Unicode code points are the same as ASCII, which made the change-over much easier."),
    table(["", "ASCII", "Unicode (UTF-8)"], [
        ["Characters", "128 (7-bit)", "over 150,000"],
        ["Bytes per character", "1", "1 to 4"],
        ["Languages", "English only", "almost every language, maths symbols and emoji"],
        ["Implications", "small files, very simple", "names and text from any country display correctly; some characters take more space"],
    ], caption="ASCII and Unicode compared"),
    terms([
        ("Character set", "the list of characters a system can represent, and the code for each one."),
        ("Code point", "the unique number Unicode gives to a character, written like U+0041."),
        ("UTF-8", "a variable-length encoding that stores Unicode code points in 1–4 bytes."),
        ("Bit mask", "a pattern used with AND, OR or XOR to change or test chosen bits."),
    ]),
    think([
        ("The ASCII code for ‘D’ is 68. What is the code for ‘d’?", "Lower case letters are 32 more than upper case: 68 + 32 = 100."),
        ("A website shows ‘cafÃ©’ instead of ‘café’. What has gone wrong?", "The text was saved as UTF-8 (é is two bytes) but read as an older 1-byte character set, so each of the two bytes appears as a separate wrong symbol."),
        ("How many bytes does the word ‘naïve’ take in UTF-8?", "Five characters: n, a, v and e take 1 byte each and ï takes 2, so 6 bytes."),
    ]),
)


SMILE = ["00111100", "01000010", "10100101", "10000001", "10100101", "10011001", "01000010", "00111100"]


def pixels():
    s = SVG(760, 300, "A tiny black and white image stored as bits")
    fills = [["#17374f" if b == "1" else "white" for b in row] for row in SMILE]
    s.grid(40, 40, 8, 8, 28, 28, None, fills)
    s.text(152, 290, "8 × 8 pixels, 1 bit each", size=12)
    for i, row in enumerate(SMILE):
        s.text(300, 60 + i * 28, row, size=16, mono=True, anchor="start")
    s.text(360, 30, "stored row by row", size=12)
    s.text(520, 60, "1-bit depth: 2 colours", size=13, anchor="start", bold=True)
    s.text(520, 84, "8-bit: 256 colours", size=13, anchor="start")
    s.text(520, 108, "24-bit: about 16.7 million", size=13, anchor="start")
    s.text(520, 150, "A 24-bit pixel is 3 bytes:", size=13, anchor="start", bold=True)
    for k, (c, v, col) in enumerate([("Red", "255", "#e34b4b"), ("Green", "128", "#4aa05a"), ("Blue", "0", "#4a73d9")]):
        s.box(520 + k * 72, 165, 66, 50, c, v, size=12, fill="white", stroke=col)
    s.add('<rect x="520" y="228" width="210" height="34" rx="6" fill="#ff8000" stroke="#b35a00" stroke-width="2"/>')
    s.text(625, 250, "= orange, hex #FF8000", size=13, color="white", bold=True)
    return s.render("A bitmap is a grid of pixels. Each pixel is stored as a number; the bit depth decides how many colours that number can describe.")


def resolution():
    s = SVG(760, 230, "The same circle at low and high resolution")
    import math

    def disc(x0, n, size, label):
        cell = size / n
        for r in range(n):
            for c in range(n):
                cx, cy = (c + .5) / n - .5, (r + .5) / n - .5
                if math.hypot(cx, cy) <= .42:
                    s.add(f'<rect x="{x0 + c * cell:.1f}" y="{30 + r * cell:.1f}" width="{cell:.1f}" height="{cell:.1f}" fill="#245d83"/>')
        s.add(f'<rect x="{x0}" y="30" width="{size}" height="{size}" fill="none" stroke="{LINE}" stroke-width="1.5"/>')
        s.text(x0 + size / 2, 30 + size + 22, label, size=12)
    disc(60, 8, 150, "8 × 8 = 64 pixels")
    disc(300, 16, 150, "16 × 16 = 256 pixels")
    disc(540, 40, 150, "40 × 40 = 1,600 pixels")
    return s.render("Higher resolution means more, smaller pixels: smoother edges and more detail, but a bigger file.")


def vector_vs_bitmap():
    s = SVG(760, 220, "Enlarging a vector image and a bitmap image")
    s.text(190, 28, "Vector: stores shapes", size=14, bold=True)
    s.box(40, 45, 300, 110, fill="white")
    s.circle(110, 100, 40, fill="#dcebf6")
    s.text(245, 85, "circle: centre (70,55)", size=12, mono=True)
    s.text(245, 105, "radius 40, fill blue", size=12, mono=True)
    s.text(190, 185, "Redrawn from the formula at any size: always sharp", size=12, color=ACCENT)
    s.text(570, 28, "Bitmap: stores pixels", size=14, bold=True)
    s.box(420, 45, 300, 110, fill="white")
    for (x, y) in [(0, 1), (0, 2), (1, 0), (1, 3), (2, 0), (2, 3), (3, 1), (3, 2), (1, 1), (1, 2), (2, 1), (2, 2)]:
        s.add(f'<rect x="{530 + x * 20}" y="{60 + y * 20}" width="20" height="20" fill="#245d83"/>')
    s.text(570, 185, "Enlarged pixels show jagged ‘stair steps’", size=12, color=WARN)
    s.text(380, 212, "Vectors suit logos, diagrams and fonts; bitmaps suit photographs.", size=12)
    return s.render("Vector graphics store instructions for shapes; bitmaps store every pixel.")


def rle():
    s = SVG(760, 170, "Run-length encoding of one row of pixels")
    row = "WWWWWBBBWWWWWWWW"
    for i, ch in enumerate(row):
        s.add(f'<rect x="{60 + i * 30}" y="30" width="30" height="30" fill="{"#17374f" if ch == "B" else "white"}" stroke="{LINE}"/>')
    s.text(380, 85, "Stored pixel by pixel: 16 values", size=13)
    s.text(380, 120, "Run-length encoded: 5 white, 3 black, 8 white  →  3 pairs", size=15, bold=True)
    s.text(380, 150, "Lossless: the row can be rebuilt exactly. Works best on large areas of one colour.", size=12, color=ACCENT)
    return s.render("Run-length encoding (RLE) is a simple lossless compression method.")


C3 = deeper("C3",
    h3("From pixels to bits"),
    pixels(),
    resolution(),
    worked("How big is an uncompressed photo?", [
        "A photo is 1,200 × 800 pixels with 24-bit colour.",
        "Number of pixels = 1,200 × 800 = 960,000.",
        "Bits = 960,000 × 24 = 23,040,000 bits.",
        "Bytes = 23,040,000 ÷ 8 = 2,880,000 bytes ≈ 2.88 MB (using 1 MB = 1,000,000 bytes).",
        "The real file is a little bigger, because a header stores the width, height and bit depth, plus metadata such as the date and camera.",
    ], "File size = width × height × bit depth ÷ 8 bytes."),
    vector_vs_bitmap(),
    h3("Compression"),
    rle(),
    table(["Format", "Compression", "Best for"], [
        ["JPEG", "lossy: removes detail the eye notices least", "photographs on web pages and phones"],
        ["PNG", "lossless", "screenshots, logos and images with sharp edges or transparency"],
        ["GIF", "lossless, but only 256 colours", "simple animations and icons"],
        ["RAW / TIFF", "none or lossless", "original photos that will be edited or printed"],
        ["SVG", "vector (not pixels)", "logos, diagrams and icons that must scale"],
    ], caption="Common image formats"),
    p("Screens make colours by adding red, green and blue light (RGB). Printers work the other way, mixing cyan, magenta, yellow and black ink (CMYK) that absorbs light. Images for print are therefore often converted, and a colour that looks bright on screen may print duller."),
    terms([
        ("Pixel", "the smallest dot of colour in a bitmap image."),
        ("Resolution", "the number of pixels in an image, given as width × height."),
        ("Bit depth (colour depth)", "the number of bits used for each pixel; n bits give 2ⁿ colours."),
        ("Metadata", "data about the image, such as its size, date and camera settings."),
        ("Lossless", "compression that can rebuild the original exactly."),
        ("Lossy", "compression that permanently removes some data to make a much smaller file."),
    ]),
    think([
        ("How many colours can a 4-bit image show?", "2⁴ = 16 colours."),
        ("Why does a logo look blurry when a small JPEG of it is enlarged on a poster?", "The JPEG is a bitmap with a fixed number of pixels. Enlarging it makes each pixel bigger, and JPEG compression has already removed sharp-edge detail. A vector (SVG) logo would stay sharp."),
        ("An image doubles its resolution in both directions. What happens to the uncompressed file size?", "It becomes four times bigger, because there are twice as many pixels across and twice as many down."),
    ]),
)

SECTIONS = {"C1": C1, "C2": C2, "C3": C3}
