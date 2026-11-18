
import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io
import html

# =====================================================
# 1. PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="BrandCraft AI",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =====================================================
# 2. PREMIUM CUSTOM CSS - BRANDCRAFT AI
# =====================================================

st.html("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700&display=swap');

/* =================================
   GLOBAL BACKGROUND
================================= */

.stApp {
    background:
        radial-gradient(circle at 10% 10%,
        rgba(142, 88, 220, 0.24), transparent 35%),
        radial-gradient(circle at 90% 85%,
        rgba(105, 66, 180, 0.20), transparent 35%),
        linear-gradient(135deg, #0D0918, #19102B, #100B1C);

    color: #FFFFFF;
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* =================================
   PREMIUM COMPACT SIDEBAR
================================= */

[data-testid="stSidebar"] {
    background:
        radial-gradient(circle at 15% 0%, rgba(166, 117, 232, 0.18), transparent 32%),
        linear-gradient(180deg, #211431 0%, #171024 55%, #100B1D 100%);
    border-right: 1px solid rgba(214, 188, 255, 0.22);
}

[data-testid="stSidebar"] > div:first-child {
    padding-top: 1.25rem;
}

[data-testid="stSidebar"] * {
    color: #F8F3FF;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    font-family: 'Playfair Display', serif;
}

.sidebar-brand {
    text-align: center;
    padding: 15px 10px 18px;
    margin: 0 0 16px;
    border: 1px solid rgba(214, 188, 255, 0.22);
    border-radius: 18px;
    background: linear-gradient(145deg, rgba(112, 70, 175, 0.28), rgba(255,255,255,0.035));
    box-shadow: 0 10px 28px rgba(0,0,0,0.18);
}

.sidebar-brand-icon {
    width: 54px;
    height: 54px;
    margin: 0 auto 9px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 16px;
    font-size: 28px;
    background: linear-gradient(135deg, #E7C98D, #B68AFF);
    box-shadow: 0 6px 18px rgba(182,138,255,0.22);
}

.sidebar-brand-name {
    color: #FFFFFF;
    font-family: 'Playfair Display', serif;
    font-size: 23px;
    font-weight: 700;
    letter-spacing: 0.2px;
}

.sidebar-brand-tagline {
    color: #CDBCE5;
    font-size: 11px;
    margin-top: 4px;
    letter-spacing: 0.7px;
}

.sidebar-group-label {
    color: #BDA7D8;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 2px;
    margin: 17px 3px 8px;
    text-transform: uppercase;
}

.sidebar-note {
    color: #AFA0C5;
    font-size: 11px;
    line-height: 1.6;
    text-align: center;
    padding: 12px 8px 4px;
}

/* Compact, separate feature tabs */
[data-testid="stSidebar"] [role="radiogroup"] {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 7px;
    width: 100%;
}

[data-testid="stSidebar"] [role="radiogroup"] > label {
    min-height: 67px;
    box-sizing: border-box;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 8px 5px;
    margin: 0;
    border: 1px solid rgba(210, 187, 238, 0.13);
    border-radius: 12px;
    background: rgba(255,255,255,0.045);
    transition: background 0.2s ease, border-color 0.2s ease, transform 0.2s ease;
}

[data-testid="stSidebar"] [role="radiogroup"] > label:hover {
    background: rgba(167,123,255,0.16);
    border-color: rgba(196, 160, 255, 0.65);
    transform: translateY(-1px);
}

[data-testid="stSidebar"] [role="radiogroup"] > label:has(input:checked) {
    background: linear-gradient(145deg, rgba(137, 91, 194, 0.42), rgba(73, 48, 104, 0.55));
    border: 1px solid #C6A0FF;
    box-shadow: inset 0 0 0 1px rgba(255,255,255,0.035), 0 5px 14px rgba(0,0,0,0.15);
}

[data-testid="stSidebar"] [role="radiogroup"] > label p {
    font-size: 11px;
    line-height: 1.25;
    font-weight: 650;
    margin: 0;
}

[data-testid="stSidebar"] [role="radiogroup"] > label [data-testid="stMarkdownContainer"] {
    justify-content: center;
}

[data-testid="stSidebar"] [role="radiogroup"] input {
    accent-color: #D6BCFF;
}

/* Hide the radio group label while keeping the controls accessible */
[data-testid="stSidebar"] [data-testid="stWidgetLabel"] {
    display: none;
}

/* =================================
   MAIN TITLE
================================= */

.main-title {
    font-family: 'Playfair Display', serif;
    font-size: 48px;
    font-weight: 700;
    color: #FFFFFF !important;

    background:
        linear-gradient(120deg,
        rgba(112,70,175,0.55),
        rgba(39,25,62,0.90));

    border: 1px solid rgba(190,155,255,0.35);
    border-radius: 22px;

    padding: 28px 30px;
    margin-bottom: 15px;

    box-shadow: 0 12px 35px rgba(0,0,0,0.25);
}

.subtitle {
    color: #C9B9E5 !important;
    font-size: 15px;
    margin: 12px 0 28px 4px;
}

/* =================================
   SECTION HEADINGS
================================= */

.section-heading-box {
    background: linear-gradient(
        120deg,
        rgba(101,65,155,0.35),
        rgba(35,24,53,0.92)
    );

    border: 1px solid rgba(190,155,255,0.28);
    border-left: 5px solid #B68AFF;
    border-radius: 17px;

    padding: 22px 25px;
    margin: 22px 0;

    box-shadow: 0 8px 25px rgba(0,0,0,0.18);
}

.section-category {
    color: #D8C2FF;
    font-size: 11px;
    letter-spacing: 3px;
    font-weight: 800;
    margin-bottom: 8px;
}

.section-heading {
    color: #FFFFFF;
    font-family: 'Playfair Display', serif;
    font-size: 31px;
    font-weight: 700;
    margin-bottom: 8px;
}

.section-description {
    color: #C9B9E5;
    font-size: 14px;
}

/* =================================
   HERO SECTION
================================= */

.hero {
    background:
        radial-gradient(circle at 85% 20%,
        rgba(192,153,255,0.25), transparent 35%),
        linear-gradient(120deg, #543578, #211531);

    border: 1px solid rgba(195,165,255,0.35);
    border-radius: 23px;

    padding: 38px;
    margin: 20px 0 28px;

    box-shadow: 0 12px 35px rgba(0,0,0,0.22);
}

.hero h2 {
    color: #FFFFFF !important;
    font-family: 'Playfair Display', serif;
    font-size: 33px;

    background: transparent;
    border: none;
    padding: 0;
    margin: 0 0 12px;
    box-shadow: none;
}

.hero p {
    color: #E5D9F5 !important;
    font-size: 15px;
    line-height: 1.8;
}

/* =================================
   CONTENT CARDS
================================= */

.content-card,
.feature-card,
.metric-card {

    background: linear-gradient(
        145deg,
        rgba(57,40,82,0.90),
        rgba(29,21,45,0.96)
    );

    border: 1px solid rgba(190,155,255,0.25);
    border-radius: 17px;

    padding: 23px;
    margin-bottom: 16px;

    box-shadow: 0 8px 25px rgba(0,0,0,0.17);
}

.feature-card {
    min-height: 150px;
    transition: all 0.3s ease;
}

.feature-card:hover {
    transform: translateY(-5px);
    border-color: #C9A8FF;
    box-shadow: 0 12px 30px rgba(155,105,225,0.20);
}

.feature-title {
    color: #FFFFFF !important;
    font-size: 19px;
    font-weight: 700;
    margin: 10px 0;
}

.feature-copy {
    color: #C9B9E5 !important;
    font-size: 14px;
    line-height: 1.7;
}

/* =================================
   METRIC CARDS
================================= */

.metric-card {
    text-align: center;
    background: linear-gradient(135deg, #42295E, #241832);
}

.metric-number {
    color: #D6BCFF !important;
    font-size: 35px;
    font-weight: 800;
}

.metric-label {
    color: #C9B9E5 !important;
    font-size: 13px;
    margin-top: 6px;
}

/* =================================
   SUBHEADINGS
================================= */

.subheading-box {
    background: rgba(125,85,180,0.15);
    border-left: 4px solid #B68AFF;
    border-radius: 11px;

    padding: 13px 18px;
    margin: 23px 0 15px;
}

.subheading-text {
    color: #FFFFFF !important;
    font-size: 19px;
    font-weight: 700;
}

/* =================================
   MARKDOWN HEADINGS
================================= */

.stMarkdown h1,
.stMarkdown h2,
.stMarkdown h3,
.stMarkdown h4,
.stMarkdown h5,
.stMarkdown h6 {
    color: #F8F3FF !important;
}

/* =================================
   BUTTONS
================================= */

.stButton > button,
.stDownloadButton > button,
.stFormSubmitButton > button {

    background: linear-gradient(110deg, #8050C8, #B18AFF);

    color: #FFFFFF !important;
    border: 1px solid rgba(218,194,255,0.5);

    border-radius: 11px;
    padding: 11px 20px;

    font-weight: 700;
    transition: all 0.25s ease;
}

.stButton > button:hover,
.stDownloadButton > button:hover,
.stFormSubmitButton > button:hover {

    background: linear-gradient(110deg, #A474EC, #C6A9FF);

    color: #FFFFFF !important;
    transform: translateY(-2px);

    box-shadow: 0 8px 22px rgba(161,112,232,0.30);
}

/* =================================
   INPUT FIELDS
================================= */

.stTextInput input,
.stTextArea textarea,
.stNumberInput input {

    background: #211831 !important;
    color: #FFFFFF !important;

    border: 1px solid rgba(190,155,255,0.3) !important;
    border-radius: 10px;
}

.stSelectbox div[data-baseweb="select"] {
    background: #211831 !important;
    color: #FFFFFF !important;
    border-radius: 10px;
}

.stTextInput label,
.stTextArea label,
.stSelectbox label,
.stFileUploader label,
.stColorPicker label,
.stRadio label,
.stNumberInput label {
    color: #E9DFFF !important;
    font-weight: 600;
}

/* =================================
   FILE UPLOADER
================================= */

[data-testid="stFileUploader"] {

    background: rgba(95,66,133,0.15);

    border: 1px dashed #B68AFF;
    border-radius: 15px;

    padding: 17px;
    transition: 0.3s ease;
}

[data-testid="stFileUploader"]:hover {
    border-color: #E0CAFF;
    background: rgba(125,85,180,0.22);
}

/* =================================
   METRICS
================================= */

[data-testid="stMetric"] {
    background: rgba(62,43,88,0.45);
    border: 1px solid rgba(190,155,255,0.25);
    border-radius: 13px;
    padding: 15px;
}

[data-testid="stMetricValue"] {
    color: #D6BCFF !important;
}

[data-testid="stMetricLabel"] {
    color: #C9B9E5 !important;
}

/* =================================
   CAPTIONS AND ALERTS
================================= */

.stCaption,
[data-testid="stCaptionContainer"] {
    color: #C9B9E5 !important;
}

.stAlert {
    border-radius: 12px;
}

/* =================================
   DIVIDERS
================================= */

hr {
    border-color: rgba(190,155,255,0.25);
}

/* =================================
   FOOTER
================================= */

.footer {
    text-align: center;
    color: #C9B9E5 !important;
    padding: 30px 0;
    font-size: 13px;
    line-height: 1.8;
}

/* =================================
   RESPONSIVE DESIGN
================================= */

@media(max-width: 768px) {

    .main-title {
        font-size: 32px;
        padding: 20px;
    }

    .section-heading {
        font-size: 24px;
    }

    .hero {
        padding: 23px;
    }

    .hero h2 {
        font-size: 25px;
    }
}

</style>
""")

# =====================================================
# 3. HELPER FUNCTIONS
# =====================================================

def section_header(category, title, description):
    st.markdown(
        f"""
        <div class="section-heading-box">
            <div class="section-category">
                {html.escape(category)}
            </div>
            <div class="section-heading">
                {html.escape(title)}
            </div>
            <p class="section-description">
                {html.escape(description)}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


def subheading(title):
    st.markdown(
        f"""
        <div class="subheading-box">
            <div class="subheading-text">
                {html.escape(title)}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def feature_card(title, description, symbol):
    st.markdown(
        f"""
        <div class="feature-card">
            <div style="font-size:29px;">{symbol}</div>
            <div class="feature-title">{html.escape(title)}</div>
            <div class="feature-copy">{html.escape(description)}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def extract_colors(image, number=6):
    image = image.convert("RGB")
    image.thumbnail((200, 200))

    quantized = image.quantize(colors=number)
    palette = quantized.getpalette()
    color_counts = quantized.getcolors()

    if not color_counts:
        return []

    color_counts.sort(reverse=True)
    colors = []

    for count, index in color_counts[:number]:
        position = index * 3
        rgb = tuple(palette[position:position + 3])
        colors.append(rgb)

    return colors


def get_font(size, bold=False, symbol=False):
    if symbol:
        paths = [
            "C:/Windows/Fonts/seguisym.ttf",
            "C:/Windows/Fonts/arial.ttf"
        ]
    elif bold:
        paths = [
            "C:/Windows/Fonts/arialbd.ttf",
            "C:/Windows/Fonts/segoeuib.ttf"
        ]
    else:
        paths = [
            "C:/Windows/Fonts/arial.ttf",
            "C:/Windows/Fonts/segoeui.ttf"
        ]

    for path in paths:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue

    return ImageFont.load_default()


def create_logo_image(
    brand_name,
    tagline,
    symbol,
    layout,
    logo_style,
    bg_color,
    logo_color,
    text_color
):
    image = Image.new("RGB", (900, 600), bg_color)
    draw = ImageDraw.Draw(image)

    brand_font = get_font(
        55,
        bold=logo_style in ["Modern", "Abstract", "Lettermark"]
    )

    tagline_font = get_font(25)
    icon_font = get_font(105, symbol=True)

    if logo_style == "Luxury":
        draw.rounded_rectangle(
            (35, 35, 865, 565),
            radius=25,
            outline=logo_color,
            width=4
        )

    elif logo_style == "Abstract":
        draw.ellipse(
            (330, 55, 570, 295),
            outline=logo_color,
            width=8
        )
        draw.line(
            (280, 175, 620, 175),
            fill=logo_color,
            width=5
        )

    if logo_style == "Lettermark":
        initials = "".join(
            word[0] for word in brand_name.split() if word
        ).upper()

        draw.text(
            (450, 220),
            initials,
            fill=logo_color,
            font=get_font(150, bold=True),
            anchor="mm"
        )

        draw.text(
            (450, 355),
            brand_name,
            fill=text_color,
            font=get_font(38, bold=True),
            anchor="mm"
        )

        if tagline:
            draw.text(
                (450, 420),
                tagline,
                fill=text_color,
                font=tagline_font,
                anchor="mm"
            )

    elif layout == "Icon Above Text":
        draw.text(
            (450, 160),
            symbol,
            fill=logo_color,
            font=icon_font,
            anchor="mm"
        )

        draw.text(
            (450, 300),
            brand_name,
            fill=text_color,
            font=brand_font,
            anchor="mm"
        )

        if tagline:
            draw.text(
                (450, 375),
                tagline,
                fill=text_color,
                font=tagline_font,
                anchor="mm"
            )

    elif layout == "Icon Beside Text":
        draw.text(
            (180, 290),
            symbol,
            fill=logo_color,
            font=icon_font,
            anchor="mm"
        )

        draw.text(
            (590, 260),
            brand_name,
            fill=text_color,
            font=brand_font,
            anchor="mm"
        )

        if tagline:
            draw.text(
                (590, 345),
                tagline,
                fill=text_color,
                font=tagline_font,
                anchor="mm"
            )

    else:
        draw.text(
            (450, 300),
            symbol,
            fill=logo_color,
            font=get_font(180, symbol=True),
            anchor="mm"
        )

    return image


def create_logo_svg(
    brand_name,
    tagline,
    symbol,
    layout,
    logo_style,
    bg_color,
    logo_color,
    text_color
):
    safe_brand = html.escape(brand_name)
    safe_tagline = html.escape(tagline)
    safe_symbol = html.escape(symbol)

    if logo_style == "Lettermark":
        initials = "".join(
            word[0] for word in brand_name.split() if word
        ).upper()

        artwork = f"""
        <text x="450" y="250" font-size="150"
        font-weight="bold" text-anchor="middle"
        fill="{logo_color}">{html.escape(initials)}</text>
        <text x="450" y="355" font-size="38"
        text-anchor="middle" fill="{text_color}">{safe_brand}</text>
        <text x="450" y="420" font-size="25"
        text-anchor="middle" fill="{text_color}">{safe_tagline}</text>
        """

    elif layout == "Icon Beside Text":
        artwork = f"""
        <text x="180" y="320" font-size="105"
        text-anchor="middle" fill="{logo_color}">{safe_symbol}</text>
        <text x="590" y="270" font-size="55"
        text-anchor="middle" fill="{text_color}">{safe_brand}</text>
        <text x="590" y="345" font-size="25"
        text-anchor="middle" fill="{text_color}">{safe_tagline}</text>
        """

    elif layout == "Icon Only":
        artwork = f"""
        <text x="450" y="355" font-size="180"
        text-anchor="middle" fill="{logo_color}">{safe_symbol}</text>
        """

    else:
        artwork = f"""
        <text x="450" y="210" font-size="105"
        text-anchor="middle" fill="{logo_color}">{safe_symbol}</text>
        <text x="450" y="340" font-size="55"
        text-anchor="middle" fill="{text_color}">{safe_brand}</text>
        <text x="450" y="415" font-size="25"
        text-anchor="middle" fill="{text_color}">{safe_tagline}</text>
        """

    decoration = ""

    if logo_style == "Luxury":
        decoration = f"""
        <rect x="35" y="35" width="830" height="530"
        rx="25" fill="none" stroke="{logo_color}" stroke-width="4"/>
        """

    elif logo_style == "Abstract":
        decoration = f"""
        <circle cx="450" cy="175" r="120"
        fill="none" stroke="{logo_color}" stroke-width="8"/>
        <line x1="280" y1="175" x2="620" y2="175"
        stroke="{logo_color}" stroke-width="5"/>
        """

    return f"""
    <svg xmlns="http://www.w3.org/2000/svg"
    width="900" height="600" viewBox="0 0 900 600">
        <rect width="900" height="600" fill="{bg_color}"/>
        {decoration}
        {artwork}
    </svg>
    """



# =====================================================
# 4. SIDEBAR NAVIGATION - FIXED
# =====================================================

with st.sidebar:

    # Brand header
    st.markdown(
        '''
        <div class="sidebar-brand">
            <div class="sidebar-brand-icon">🎨</div>
            <div class="sidebar-brand-name">BrandCraft AI</div>
            <div class="sidebar-brand-tagline">EMPOWERING CREATIVE ARTISTS</div>
        </div>
        ''',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-group-label">Workspace</div>',
        unsafe_allow_html=True
    )

    menu = st.radio(
        "Navigate to a workspace",
        [
            "Dashboard",
            "ArtSense AI",
            "Logo Studio",
            "Color Studio",
            "Creative DNA",
            "Marketing Studio",
            "Portfolio Studio"
        ],
        format_func=lambda item: {
            "Dashboard": "🏠  Dashboard",
            "ArtSense AI": "🧠  ArtSense AI",
            "Logo Studio": "✦  Logo Studio",
            "Color Studio": "🎨  Color Studio",
            "Creative DNA": "🧬  Creative DNA",
            "Marketing Studio": "📣  Marketing",
            "Portfolio Studio": "🖼️  Portfolio"
        }[item],
        key="main_navigation",
        label_visibility="collapsed"
    )

    st.markdown("---")

    st.markdown(
        '''
        <div class="sidebar-note">
            ✨ Your creativity. Your identity. Your brand.<br>
            <span style="color:#D6BCFF;">Create something remarkable.</span>
        </div>
        ''',
        unsafe_allow_html=True
    )



# =====================================================
# 5. DASHBOARD
# =====================================================

if menu == "Dashboard":

    st.markdown(
        '<div class="main-title">BrandCraft AI ✦</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Your creative journey starts here. '
        'Turn imagination into identity.</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="hero">
        <h2>Welcome to your Creative Space ✨</h2>
        <p>
            Explore your artistic identity, create visual concepts,
            discover colors and build your personal creative brand.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">07</div>
            <div class="metric-label">Creative Studios</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">∞</div>
            <div class="metric-label">Creative Possibilities</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">100%</div>
            <div class="metric-label">Artist First</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    section_header(
        "EXPLORE",
        "Your Creative Studios",
        "Choose a space and start creating."
    )

    col1, col2 = st.columns(2)

    with col1:
        feature_card(
            "ArtSense AI",
            "Explore your artwork through image insights.",
            "🖼️"
        )
        feature_card(
            "Logo Studio",
            "Create a visual identity for your brand.",
            "✦"
        )
        feature_card(
            "Color Studio",
            "Discover beautiful palettes from your artwork.",
            "🎨"
        )

    with col2:
        feature_card(
            "Creative DNA",
            "Explore your artistic personality.",
            "🧬"
        )
        feature_card(
            "Marketing Studio",
            "Create promotional captions for your artwork.",
            "📢"
        )
        feature_card(
            "Portfolio Studio",
            "Organize and showcase your creative work.",
            "📁"
        )

    st.markdown("---")

    section_header(
        "GET STARTED",
        "Tell Us About Yourself",
        "Add your creative identity."
    )

    artist_name = st.text_input("Your Artist Name")

    art_type = st.selectbox(
        "Your Creative Field",
        [
            "Digital Art",
            "Painting",
            "Photography",
            "Graphic Design",
            "Illustration",
            "Craft",
            "Other"
        ]
    )

    if st.button("Save Artist Profile"):
        if artist_name.strip():
            st.session_state["artist_name"] = artist_name
            st.session_state["art_type"] = art_type
            st.success("Your artist profile has been saved!")
        else:
            st.warning("Please enter your artist name.")


# =====================================================
# 6. ARTSENSE AI
# =====================================================


elif menu == "ArtSense AI":

    from PIL import ImageStat, ImageFilter

    st.header("🎨 ArtSense AI")

    st.markdown(
        "Upload your artwork and discover its visual characteristics "
        "with our local artwork intelligence engine."
    )

    st.markdown("---")

    uploaded_file = st.file_uploader(
        "Upload your artwork",
        type=["png", "jpg", "jpeg", "webp"],
        key="artsense_upload"
    )

    if uploaded_file is not None:

        try:
            image = Image.open(uploaded_file).convert("RGB")

            # Resize image for faster analysis
            image.thumbnail((900, 900))

            st.markdown("### 🖼️ Your Artwork")

            col1, col2 = st.columns([1.2, 1])

            with col1:
                st.image(image, use_container_width=True)

            # Prepare a smaller image for analysis
            sample = image.resize((256, 256))
            hsv_image = sample.convert("HSV")
            gray_image = sample.convert("L")

            # Calculate image statistics
            hsv_stats = ImageStat.Stat(hsv_image)
            gray_stats = ImageStat.Stat(gray_image)

            brightness = hsv_stats.mean[2]
            saturation = hsv_stats.mean[1]
            contrast = gray_stats.stddev[0]

            # Edge detection
            edge_image = gray_image.filter(ImageFilter.FIND_EDGES)
            edge_histogram = edge_image.histogram()

            edge_pixels = sum(edge_histogram[36:])
            edge_density = (edge_pixels / (256 * 256)) * 100

            # Extract dominant colors
            quantized = sample.quantize(colors=6).convert("RGB")
            color_data = quantized.getcolors(256 * 256)
            color_data = sorted(
                color_data,
                reverse=True,
                key=lambda item: item[0]
            )[:6]

            palette = [
                (count, color)
                for count, color in color_data
            ]

            # Approximate visual mood
            if saturation > 145 and brightness > 145:
                mood = "Energetic & Vibrant"
                mood_detail = "Your artwork uses vivid colours and has a lively visual impression."

            elif brightness < 90 and contrast > 55:
                mood = "Dramatic & Intense"
                mood_detail = "Dark tones and strong contrast create a dramatic impression."

            elif saturation < 65:
                mood = "Calm & Minimal"
                mood_detail = "Muted colours create a subtle and peaceful visual impression."

            elif brightness > 175:
                mood = "Soft & Cheerful"
                mood_detail = "The brighter tones give your artwork a light visual impression."

            else:
                mood = "Balanced & Expressive"
                mood_detail = "Your artwork has a balanced combination of tones and colours."

            # Approximate style signals
            if edge_density > 18 and saturation > 110:
                style_hint = "Bold / Graphic appearance"
            elif edge_density < 8 and saturation < 100:
                style_hint = "Soft / Minimal appearance"
            elif edge_density > 18:
                style_hint = "Detailed / High-texture appearance"
            else:
                style_hint = "Balanced visual appearance"

            # Composition analysis
            left = gray_image.crop((0, 0, 128, 256))
            right = gray_image.crop((128, 0, 256, 256))

            top = gray_image.crop((0, 0, 256, 128))
            bottom = gray_image.crop((0, 128, 256, 256))

            left_brightness = ImageStat.Stat(left).mean[0]
            right_brightness = ImageStat.Stat(right).mean[0]

            top_brightness = ImageStat.Stat(top).mean[0]
            bottom_brightness = ImageStat.Stat(bottom).mean[0]

            horizontal_difference = abs(
                left_brightness - right_brightness
            )

            vertical_difference = abs(
                top_brightness - bottom_brightness
            )

            if horizontal_difference < 15 and vertical_difference < 15:
                composition = "Visually Balanced"
                composition_detail = "The brightness is distributed relatively evenly across the image."

            elif horizontal_difference > vertical_difference:
                composition = "Horizontal Visual Variation"
                composition_detail = "The left and right sides have noticeably different brightness levels."

            else:
                composition = "Vertical Visual Variation"
                composition_detail = "The upper and lower areas have noticeably different brightness levels."

            # Creative suggestions
            suggestions = []

            if saturation < 75:
                suggestions.append(
                    "Try adding one accent colour to create a stronger focal point."
                )
            else:
                suggestions.append(
                    "Your colour intensity is noticeable. Maintain a consistent colour balance."
                )

            if contrast < 40:
                suggestions.append(
                    "Experiment with light and shadow to create more depth."
                )
            else:
                suggestions.append(
                    "Your tonal contrast is noticeable. Use it carefully to guide attention."
                )

            if edge_density > 18:
                suggestions.append(
                    "Consider keeping some areas less detailed so the main subject can stand out."
                )
            else:
                suggestions.append(
                    "You can experiment with additional textures or fine details."
                )

            # Show results
            with col2:

                st.markdown("### ✨ Artwork Insights")

                st.metric(
                    "Visual Mood",
                    mood
                )

                st.metric(
                    "Brightness",
                    f"{brightness:.1f}/255"
                )

                st.metric(
                    "Colour Saturation",
                    f"{saturation:.1f}/255"
                )

                st.metric(
                    "Contrast",
                    f"{contrast:.1f}"
                )

                st.markdown("---")

                st.markdown("### 💜 Mood Analysis")
                st.write(f"**{mood}**")
                st.write(mood_detail)

                st.markdown("### 🖌️ Style Signals")
                st.write(style_hint)

                st.markdown("### 📐 Composition")
                st.write(f"**{composition}**")
                st.write(composition_detail)

            st.markdown("---")

            # Display colour palette
            st.markdown("### 🎨 Dominant Colour Palette")

            palette_columns = st.columns(len(palette))

            for index, (count, color) in enumerate(palette):

                hex_color = "#{:02X}{:02X}{:02X}".format(*color)

                with palette_columns[index]:
                    st.markdown(
                        f"""
                        <div style="
                            background:{hex_color};
                            height:75px;
                            border-radius:12px;
                            border:1px solid #777;
                        "></div>
                        <p style="text-align:center;color:white;">
                            <b>{hex_color}</b>
                        </p>
                        """,
                        unsafe_allow_html=True
                    )

            st.markdown("---")

            # Creative feedback
            st.markdown("### 🚀 Creative Improvement Suggestions")

            for suggestion in suggestions:
                st.markdown(f"- {suggestion}")

            # Generate artwork description
            st.markdown("---")
            st.markdown("### ✍️ Artwork Description")

            description = (
                f"This artwork presents a {mood.lower()} visual impression, "
                f"with a {style_hint.lower()}. "
                f"Its composition is {composition.lower()}, "
                f"supported by a brightness level of {brightness:.0f}/255 "
                f"and colour saturation of {saturation:.0f}/255."
            )

            st.write(description)

            st.download_button(
                "📥 Download Artwork Analysis",
                data=(
                    "BRANDCRAFT AI - ARTWORK ANALYSIS\n\n"
                    f"Visual Mood: {mood}\n"
                    f"Style Signals: {style_hint}\n"
                    f"Composition: {composition}\n"
                    f"Brightness: {brightness:.1f}/255\n"
                    f"Saturation: {saturation:.1f}/255\n"
                    f"Contrast: {contrast:.1f}\n\n"
                    f"Description:\n{description}\n\n"
                    "Creative Suggestions:\n"
                    + "\n".join(suggestions)
                ),
                file_name="BrandCraft_Artwork_Analysis.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"Unable to analyse this image: {e}")

    else:
        st.info(
            "Upload an artwork to discover its colours, mood, "
            "composition and creative improvement suggestions."
        )


    st.markdown("""
    <div class="content-card">
        <div class="feature-title">Every artwork tells a story.</div>
        <div class="feature-copy">
            Upload your artwork to explore its dimensions,
            dominant colors and basic visual characteristics.
            Your original artwork remains yours.
        </div>
    </div>
    """, unsafe_allow_html=True)

    artwork_file = st.file_uploader(
    "Upload your artwork",
    type=["png", "jpg", "jpeg"],
    key="artsense_upload_main"
)

    if artwork_file:

        image = Image.open(artwork_file).convert("RGB")

        st.image(
            image,
            caption="Your Uploaded Artwork",
            use_container_width=True
        )

        width, height = image.size
        colors = extract_colors(image, 5)

        subheading("Artwork Insights")

        col1, col2, col3 = st.columns(3)

        col1.metric("Width", f"{width} px")
        col2.metric("Height", f"{height} px")
        col3.metric("Aspect Ratio", f"{width / height:.2f}")

        subheading("Dominant Colors")

        if colors:
            color_columns = st.columns(len(colors))

            for i, color in enumerate(colors):
                hex_color = "#{:02X}{:02X}{:02X}".format(*color)

                with color_columns[i]:
                    st.markdown(
                        f"""
                        <div style="background:{hex_color};
                        height:65px;border-radius:10px;
                        border:1px solid #806b99;"></div>
                        <p style="text-align:center;color:#FFFFFF;">
                        {hex_color}</p>
                        """,
                        unsafe_allow_html=True
                    )

        st.info(
            "These are basic image insights, not an AI-generated "
            "interpretation of the artwork."
        )


# =====================================================
# 7. LOGO STUDIO
# =====================================================

elif menu == "Logo Studio":

    section_header(
        "VISUAL IDENTITY",
        "Logo Studio ✦",
        "Create a visual identity for your creative brand."
    )

    st.markdown("""
    <div class="content-card">
        <div class="feature-title">Give your ideas a symbol.</div>
        <div class="feature-copy">
            Experiment with symbols, typography, layouts and colors.
            Create and download your own logo without an API key.
        </div>
    </div>
    """, unsafe_allow_html=True)

    subheading("✨ Brand Details")

    col1, col2 = st.columns(2)

    with col1:
        brand_name = st.text_input(
            "Brand Name",
            value="Creative Studio"
        )

        tagline = st.text_input(
            "Tagline",
            value="Create Without Limits"
        )

        symbol = st.selectbox(
            "Choose Logo Symbol",
            ["✦", "★", "♥", "◆", "●", "✿", "⚡", "✧", "▲"]
        )

    with col2:
        layout = st.selectbox(
            "Logo Layout",
            [
                "Icon Above Text",
                "Icon Beside Text",
                "Icon Only"
            ]
        )

        logo_style = st.selectbox(
            "Logo Style",
            [
                "Minimalist",
                "Luxury",
                "Modern",
                "Abstract",
                "Lettermark"
            ]
        )

        bg_choice = st.selectbox(
            "Background",
            ["Dark Purple", "White", "Lavender", "Black"]
        )

        logo_color = st.color_picker(
            "Logo Color",
            "#B99AFF"
        )

        text_color = st.color_picker(
            "Text Color",
            "#FFFFFF"
        )

    backgrounds = {
        "Dark Purple": "#211638",
        "White": "#FFFFFF",
        "Lavender": "#E9DFFF",
        "Black": "#111111"
    }

    bg_color = backgrounds[bg_choice]

    st.markdown("---")
    subheading("🎨 Your Logo Preview")

    if not brand_name.strip():
        st.warning("Please enter a brand name.")

    else:
        logo_image = create_logo_image(
            brand_name,
            tagline,
            symbol,
            layout,
            logo_style,
            bg_color,
            logo_color,
            text_color
        )

        st.image(
            logo_image,
            caption="Your BrandCraft Logo",
            use_container_width=True
        )

        png_buffer = io.BytesIO()
        logo_image.save(png_buffer, format="PNG")

        svg_content = create_logo_svg(
            brand_name,
            tagline,
            symbol,
            layout,
            logo_style,
            bg_color,
            logo_color,
            text_color
        )

        subheading("📥 Download Your Logo")

        download_col1, download_col2 = st.columns(2)

        with download_col1:
            st.download_button(
                "⬇️ Download PNG",
                data=png_buffer.getvalue(),
                file_name="brandcraft_logo.png",
                mime="image/png",
                use_container_width=True
            )

        with download_col2:
            st.download_button(
                "⬇️ Download SVG",
                data=svg_content.encode("utf-8"),
                file_name="brandcraft_logo.svg",
                mime="image/svg+xml",
                use_container_width=True
            )


# =====================================================
# 8. COLOR STUDIO
# =====================================================

elif menu == "Color Studio":

    section_header(
        "COLOR EXPLORATION",
        "Color Studio 🎨",
        "Discover beautiful color palettes from your artwork."
    )

    st.markdown("""
    <div class="content-card">
        <div class="feature-title">Find the colors of your imagination.</div>
        <div class="feature-copy">
            Upload an image and extract its dominant colors.
            Use these colors as inspiration for your next creation.
        </div>
    </div>
    """, unsafe_allow_html=True)

    color_file = st.file_uploader(
        "Upload an image",
        type=["png", "jpg", "jpeg"],
        key="color_upload"
    )

    if color_file:

        image = Image.open(color_file).convert("RGB")

        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )

        colors = extract_colors(image, 6)

        subheading("🎨 Your Color Palette")

        if colors:
            palette_columns = st.columns(len(colors))
            hex_codes = []

            for i, color in enumerate(colors):
                hex_color = "#{:02X}{:02X}{:02X}".format(*color)
                hex_codes.append(hex_color)

                with palette_columns[i]:
                    st.markdown(
                        f"""
                        <div style="background:{hex_color};
                        height:100px;border-radius:12px;
                        border:1px solid #806b99;"></div>
                        <p style="text-align:center;
                        color:#FFFFFF;font-weight:600;">
                        {hex_color}</p>
                        """,
                        unsafe_allow_html=True
                    )

            palette_text = "BrandCraft AI Color Palette\n\n"
            palette_text += "\n".join(hex_codes)

            st.download_button(
                "⬇️ Download Color Palette",
                data=palette_text,
                file_name="brandcraft_color_palette.txt",
                mime="text/plain"
            )


# =====================================================
# 9. CREATIVE DNA
# =====================================================

elif menu == "Creative DNA":

    section_header(
        "ARTIST PERSONALITY",
        "Creative DNA 🧬",
        "Discover your creative preferences and artistic style."
    )

    st.markdown("""
    <div class="content-card">
        <div class="feature-title">What makes your creativity unique?</div>
        <div class="feature-copy">
            Answer a few questions to create your personal
            creative identity profile.
        </div>
    </div>
    """, unsafe_allow_html=True)

    subheading("✨ Explore Your Creative Preferences")

    with st.form("creative_dna_form"):

        art_style = st.selectbox(
            "Which artistic style do you prefer?",
            [
                "Minimalist",
                "Abstract",
                "Realistic",
                "Traditional",
                "Modern",
                "Experimental"
            ]
        )

        favorite_colors = st.selectbox(
            "Which colors attract you most?",
            [
                "Pastel Colors",
                "Bold and Bright",
                "Dark and Moody",
                "Earthy Colors",
                "Monochrome"
            ]
        )

        inspiration = st.selectbox(
            "What inspires your creativity?",
            [
                "Nature",
                "People and Emotions",
                "Culture and Traditions",
                "Technology",
                "Everyday Life",
                "Imagination"
            ]
        )

        working_style = st.selectbox(
            "How do you usually create?",
            [
                "Carefully Planned",
                "Spontaneously",
                "Experimenting",
                "Following a Reference"
            ]
        )

        submitted = st.form_submit_button(
            "Discover My Creative DNA"
        )

    if submitted:
        st.session_state["creative_profile"] = {
            "style": art_style,
            "colors": favorite_colors,
            "inspiration": inspiration,
            "working": working_style
        }

    if "creative_profile" in st.session_state:

        profile = st.session_state["creative_profile"]

        subheading("✨ Your Creative Identity")

        st.markdown(
            f"""
            <div class="content-card">
                <div style="
                    color:#FFFFFF;
                    font-family:'Playfair Display',serif;
                    font-size:25px;
                    font-weight:700;
                    margin-bottom:12px;
                ">
                    The {html.escape(profile['style'])} Creator
                </div>

                <p style="color:#FFFFFF;line-height:1.8;">
                    Your preferred artistic style is
                    <b>{html.escape(profile['style'])}</b>.
                    You are drawn towards
                    <b>{html.escape(profile['colors'])}</b>
                    and find inspiration in
                    <b>{html.escape(profile['inspiration'])}</b>.
                    Your working approach is
                    <b>{html.escape(profile['working'])}</b>.
                </p>

                <p style="color:#FFFFFF;font-size:13px;">
                    This profile reflects your selected preferences.
                    It is a creative reflection, not a psychological test.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )


# =====================================================
# 10. MARKETING STUDIO
# =====================================================

elif menu == "Marketing Studio":

    section_header(
        "CREATIVE PROMOTION",
        "Marketing Studio 📢",
        "Create promotional captions for your artwork."
    )

    st.markdown("""
    <div class="content-card">
        <div class="feature-title">Let your artwork reach more people.</div>
        <div class="feature-copy">
            Create a caption idea for your social media posts.
            Edit it to make it sound like your own voice.
        </div>
    </div>
    """, unsafe_allow_html=True)

    artist = st.text_input(
        "Artist or Brand Name",
        value=st.session_state.get("artist_name", "")
    )

    artwork_title = st.text_input(
        "Artwork Title",
        placeholder="Example: Dreams in Colors"
    )

    artwork_type = st.selectbox(
        "Artwork Type",
        [
            "Digital Art",
            "Painting",
            "Photography",
            "Illustration",
            "Graphic Design",
            "Handmade Craft"
        ]
    )

    mood = st.selectbox(
        "Artwork Mood",
        [
            "Inspirational",
            "Peaceful",
            "Bold",
            "Dreamy",
            "Mysterious",
            "Playful"
        ]
    )

    platform = st.selectbox(
        "Choose Platform",
        ["Instagram", "Facebook", "LinkedIn"]
    )

    if st.button("Generate Caption Idea"):

        if not artwork_title.strip():
            st.warning("Please enter your artwork title.")

        else:
            artist_text = artist.strip() or "Creative Artist"

            caption = (
                f"✨ Introducing '{artwork_title}' by "
                f"{artist_text}!\n\n"
                f"A {mood.lower()} creation in "
                f"{artwork_type.lower()}, made to express "
                f"ideas beyond words.\n\n"
                f"Every detail tells a story. Every creation "
                f"has a feeling. 🎨\n\n"
                f"What does this artwork make you feel?\n\n"
                f"#CreativeArtist #OriginalArt #ArtLovers "
                f"#{artwork_type.replace(' ', '')} #BrandCraftAI"
            )

            if platform == "LinkedIn":
                caption = (
                    f"Presenting '{artwork_title}' — a creative "
                    f"work by {artist_text}.\n\n"
                    f"This {artwork_type.lower()} piece explores "
                    f"a {mood.lower()} visual direction.\n\n"
                    f"Creativity is a journey of ideas, expression "
                    f"and continuous exploration.\n\n"
                    f"#Creativity #Design #Art #CreativeJourney"
                )

            st.session_state["marketing_caption"] = caption

    if "marketing_caption" in st.session_state:

        subheading("Your Caption Idea")

        st.text_area(
            "Edit your caption",
            value=st.session_state["marketing_caption"],
            height=220,
            key="editable_caption"
        )

        st.download_button(
            "⬇️ Download Caption",
            data=st.session_state["editable_caption"],
            file_name="brandcraft_caption.txt",
            mime="text/plain"
        )

        st.caption(
            "This caption is generated using local templates, "
            "not an external AI service."
        )


# =====================================================
# 11. PORTFOLIO STUDIO
# =====================================================

elif menu == "Portfolio Studio":

    section_header(
        "YOUR CREATIVE COLLECTION",
        "Portfolio Studio 📁",
        "Upload and organize your artwork in one place."
    )

    st.markdown("""
    <div class="content-card">
        <div class="feature-title">Your work deserves to be showcased.</div>
        <div class="feature-copy">
            Build a personal artwork collection and keep
            your creative projects organized.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if "portfolio" not in st.session_state:
        st.session_state["portfolio"] = []

    subheading("➕ Add New Artwork")

    with st.form("portfolio_form", clear_on_submit=True):

        portfolio_file = st.file_uploader(
            "Upload Artwork",
            type=["png", "jpg", "jpeg"]
        )

        portfolio_title = st.text_input("Artwork Title")
        portfolio_description = st.text_area("Artwork Description")

        add_artwork = st.form_submit_button("Add to Portfolio")

    if add_artwork:

        if portfolio_file is None:
            st.warning("Please upload an artwork.")

        elif not portfolio_title.strip():
            st.warning("Please enter an artwork title.")

        else:
            artwork_data = {
                "title": portfolio_title,
                "description": portfolio_description,
                "image": portfolio_file.getvalue()
            }

            st.session_state["portfolio"].append(artwork_data)
            st.success("Artwork added to your portfolio!")

    st.markdown("---")

    subheading("🖼️ My Creative Collection")

    portfolio = st.session_state["portfolio"]

    if not portfolio:
        st.info(
            "Your portfolio is empty. Upload your first artwork above."
        )

    else:
        st.write(f"Total artworks: {len(portfolio)}")

        for index, artwork in enumerate(portfolio):

            with st.container():

                col1, col2 = st.columns([1, 2])

                with col1:
                    st.image(
                        artwork["image"],
                        use_container_width=True
                    )

                with col2:
                    subheading(artwork["title"])

                    st.write(
                        artwork["description"] or
                        "No description added."
                    )

                    if st.button(
                        "🗑️ Delete Artwork",
                        key=f"delete_artwork_{index}"
                    ):
                        st.session_state["portfolio"].pop(index)
                        st.rerun()

                st.markdown("---")

        portfolio_text = "BRANDCRAFT AI - MY PORTFOLIO\n\n"

        for index, artwork in enumerate(portfolio, start=1):
            portfolio_text += (
                f"{index}. {artwork['title']}\n"
                f"Description: {artwork['description']}\n\n"
            )

        st.download_button(
            "⬇️ Download Portfolio Details",
            data=portfolio_text,
            file_name="my_creative_portfolio.txt",
            mime="text/plain"
        )


# =====================================================
# 12. FOOTER
# =====================================================

st.markdown("---")

st.markdown("""
<div class="footer">
    <p style="font-size:19px;font-weight:700;">
        🎨 BrandCraft AI
    </p>
    <p>Empowering the Creative Artist | Built with creativity and care.</p>
    <p>Your creativity. Your identity. Your brand.</p>
</div>
""", unsafe_allow_html=True)

