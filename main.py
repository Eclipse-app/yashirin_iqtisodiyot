import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Sahifa konfiguratsiyasi
st.set_page_config(
    page_title="Yashirin Iqtisodiyot Tahlili",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    h1, h2, h3 {
        color: #1e3a8a;
        font-weight: 700;
    }
    .metric-card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 10px 0;
    }
    .highlight {
        background: linear-gradient(120deg, #84fab0 0%, #8fd3f4 100%);
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Sarlavha
st.title("🌍 Jahon va O'zbekiston Yashirin Iqtisodiyoti Tahlili")
st.markdown("### 📈 2020-2025 Yillar Dinamikasi")

# Sidebar
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/8/84/Flag_of_Uzbekistan.svg", width=100)
    st.header("⚙️ Sozlamalar")
    
    analysis_type = st.selectbox(
        "Tahlil turini tanlang:",
        ["Umumiy Ko'rinish", "Yashirin Iqtisodiyot Nima?", "Usullar va Turlar", 
         "Mamlakatlar Taqqoslash", "O'zbekiston Tahlili", "Yillar Dinamikasi"]
    )
    
    st.markdown("---")
    st.markdown("### 📊 Asosiy Ko'rsatkichlar")
    st.info("**Yashirin iqtisodiyot** - bu soliq va nazoratdan yashiringan iqtisodiy faoliyat")

# Ma'lumotlar
# Jahon yashirin iqtisodiyoti (% YaIM)
global_data = {
    'Yil': [2000, 2010, 2015, 2020, 2021, 2022, 2023, 2024, 2025],
    'Jahon_foiz': [17.7, 15.2, 14.1, 13.2, 12.5, 12.1, 11.8, 11.5, 11.3],
    'OECD_foiz': [14.5, 12.8, 11.9, 16.48, 16.07, 15.96, 15.2, 14.8, 14.5],
    'Jahon_trillion': [3.5, 6.8, 9.2, 10.5, 11.2, 11.5, 12.0, 12.3, 12.5]
}

# Eng yirik yashirin iqtisodiyotlar (2023-2025)
top_countries = {
    'Mamlakat': ['Xitoy', 'AQSH', 'Hindiston', 'Braziliya', 'Indoneziya', 
                 'Meksika', 'Rossiya', 'Turkiya', 'Germaniya', 'Yaponiya'],
    'Yashirin_trillion': [3.7, 1.4, 0.951, 0.448, 0.380, 0.310, 0.285, 0.245, 0.195, 0.165],
    'Foiz_YaIM': [20.0, 5.0, 26.0, 20.6, 23.8, 17.9, 15.2, 18.5, 8.2, 6.8],
    'YaIM_trillion': [19.0, 28.0, 3.66, 2.17, 1.60, 1.73, 1.87, 1.33, 2.38, 2.42]
}

# O'zbekiston ma'lumotlari
uzbekistan_data = {
    'Yil': [2020, 2021, 2022, 2023, 2024, '2025 (6 oy)', '2025 (9 oy)', '2025 (Prognoz)'],
    'Yashirin_foiz': [None, None, None, 8.4, 8.4, 8.0, 7.7, 7.5],
    'Norasmiy_foiz': [None, None, None, None, 26.4, 24.9, 25.6, 25.0],
    'Jami_kuzatilmagan': [None, None, 45.0, 40.0, 34.8, 32.9, 33.3, 32.5],
    'YaIM_mlrd': [57.7, 69.2, 80.4, 90.0, 115.0, 64.5, 108.7, 130.0]
}

# Sektorlar bo'yicha (O'zbekiston 2024-2025)
sectors_data = {
    'Sektor': ['Qishloq xo\'jalik', 'Xizmatlar', 'Qurilish', 'Sanoat'],
    '2024_foiz': [69.4, 36.2, 35.0, 10.2],
    '2025_foiz': [68.8, 35.5, 34.2, 10.0]
}

# DataFrames
df_global = pd.DataFrame(global_data)
df_countries = pd.DataFrame(top_countries)
df_uzbekistan = pd.DataFrame(uzbekistan_data)
df_sectors = pd.DataFrame(sectors_data)

# Asosiy metrikalar
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("🌐 Jahon (2023)", "11.8% YaIM", "-5.9% (2000 yildan)")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("💰 Jahon qiymati", "$12 trillion", "+$8.5T (2000 yildan)")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("🇺🇿 O'zbekiston (2025)", "7.7% YaIM", "-0.7% (2024 yildan)")
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("📊 O'zbekiston jami", "33.3% YaIM", "Yashirin + Norasmiy")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# Tahlil turiga qarab ko'rsatish
if analysis_type == "Yashirin Iqtisodiyot Nima?":
    st.header("💡 Yashirin Iqtisodiyot: Ta'rif va Tushuncha")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="highlight">', unsafe_allow_html=True)
        st.markdown("""
        ### 📖 Asosiy Ta'rif
        
        **Yashirin iqtisodiyot** (Shadow Economy, Underground Economy, Black Market, Informal Economy) - bu 
        davlat nazoratidan va soliqqa tortishdan yashiringan barcha iqtisodiy faoliyatlarni o'z ichiga oladi.
        
        Bu iqtisodiyot quyidagilarni qamrab oladi:
        - 🔴 **Noqonuniy faoliyat:** Giyohvand moddalar savdosi, qaroqchilik
        - 🟡 **Qonuniy, lekin e'lon qilinmagan:** Naqd pul bilan to'lovlar, soliq to'lamaslik
        - 🟢 **Norasmiy sektor:** Ro'yxatdan o'tmagan biznes, rasmiylashtirmagan ish
        
        ### 🎯 Asosiy Xususiyatlar:
        
        1. **Yashirinlik**: Davlat statistikasida ko'rinmaydi
        2. **Soliq to'lamaslik**: Byudjet daromadlarini kamaytiradi
        3. **Tartibga solinmagan**: Mehnat va sog'liqni saqlash standartlari buziladi
        4. **Naqd pul ustunligi**: Ko'pchilik operatsiyalar naqd pul bilan amalga oshadi
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        # Yashirin iqtisodiyot komponentlari
        components = {
            'Komponent': ['Noqonuniy', 'Qonuniy norasmiy', 'Soliq yashirish', 'Barter savdo'],
            'Ulush_%': [15, 45, 30, 10]
        }
        df_comp = pd.DataFrame(components)
        
        fig_comp = px.pie(
            df_comp,
            values='Ulush_%',
            names='Komponent',
            title="Yashirin Iqtisodiyot Tarkibi",
            color_discrete_sequence=px.colors.sequential.RdBu
        )
        st.plotly_chart(fig_comp, use_container_width=True)
        
        st.metric("🌍 Jahon o'rtacha", "11.8% YaIM", "2023")
        st.metric("🇺🇿 O'zbekiston", "33.3% YaIM", "2025 (9 oy)")
        st.metric("💰 Jahon qiymati", "$12 trillion", "2023")
    
    # Sabablari
    st.subheader("🔍 Yashirin Iqtisodiyot Sabablari")
    
    causes_data = {
        'Sabab': ['Yuqori soliqlar', 'Og\'ir tartibga solish', 'Korrupsiya', 
                  'Iqtisodiy inqiroz', 'Past ish haqi', 'Davlatga ishonchsizlik',
                  'Murakkab soliq tizimi', 'Zaif nazorat'],
        'Ta\'sir_darajasi': [85, 75, 80, 70, 65, 60, 70, 55],
        'Kategoriya': ['Moliyaviy', 'Tartibga solish', 'Institusional', 'Iqtisodiy',
                       'Ijtimoiy', 'Institusional', 'Moliyaviy', 'Institusional']
    }
    df_causes = pd.DataFrame(causes_data)
    
    fig_causes = px.bar(
        df_causes.sort_values('Ta\'sir_darajasi', ascending=True),
        y='Sabab',
        x='Ta\'sir_darajasi',
        orientation='h',
        color='Kategoriya',
        title="Yashirin Iqtisodiyotning Asosiy Sabablari",
        labels={'Ta\'sir_darajasi': 'Ta\'sir darajasi (%)'},
        color_discrete_map={
            'Moliyaviy': '#ef4444',
            'Tartibga solish': '#f59e0b',
            'Institusional': '#3b82f6',
            'Iqtisodiy': '#10b981',
            'Ijtimoiy': '#8b5cf6'
        }
    )
    fig_causes.update_traces(texttemplate='%{x:.0f}%', textposition='outside')
    st.plotly_chart(fig_causes, use_container_width=True)
    
    # Oqibatlari
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="highlight">', unsafe_allow_html=True)
        st.markdown("""
        ### ⚠️ Salbiy Oqibatlar:
        
        1. **Byudjet yo'qotishlari** 
           - Soliq tushumlarining kamayishi
           - Ijtimoiy dasturlar uchun mablag' yetishmasligi
        
        2. **Ishchilarni himoyasizligi**
           - Minimal ish haqi kafolati yo'q
           - Sog'liqni saqlash standartlari buziladi
           - Ijtimoiy ta'minot yo'q
        
        3. **Noto'g'ri raqobat**
           - Rasmiy bizneslar zarar ko'radi
           - Bozor noto'g'ri shakllanadi
        
        4. **Statistik buzilish**
           - YaIM noto'g'ri hisoblanadi
           - Iqtisodiy qarorlar noto'g'ri qabul qilinadi
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="highlight">', unsafe_allow_html=True)
        st.markdown("""
        ### ✅ Ijobiy Jihatlar:
        
        1. **Ish o'rinlari**
           - Ishsizlar uchun daromad manbai
           - Kambag'allikni kamaytirish
        
        2. **Moslashuvchanlik**
           - Kirishda pastroq to'siqlar
           - Ixtiyoriy ish tartibi
        
        3. **Iqtisodiy amortizator**
           - Inqiroz paytida yordam
           - Ijtimoiy himoya tarmog'i
        
        4. **Tadbirkorlik**
           - Kichik biznes imkoniyatlari
           - Innovatsiyalar sinovdan o'tkazish
        """)
        st.markdown('</div>', unsafe_allow_html=True)

elif analysis_type == "Usullar va Turlar":
    st.header("🛠️ Yashirin Iqtisodiyot Usullari va Turlari")
    
    # Asosiy usullar
    st.subheader("💼 Amalga Oshirish Usullari")
    
    methods_data = {
        'Usul': ['Naqd to\'lovlar', 'Stol ostida to\'lov', 'Daromadni yashirish', 
                 'Barter savdo', 'Soxta hujjatlar', 'Offshore hisoblar',
                 'Cryptocurrency', 'Qonuniy biznes niqobi'],
        'Keng_tarqalgan_%': [90, 75, 70, 45, 40, 35, 25, 60],
        'Aniqlash_qiyinligi': [3, 4, 5, 2, 7, 8, 9, 6]
    }
    df_methods = pd.DataFrame(methods_data)
    
    fig_methods = make_subplots(
        rows=1, cols=2,
        subplot_titles=('Keng Tarqalganlik', 'Aniqlash Qiyinligi'),
        specs=[[{"type": "bar"}, {"type": "bar"}]]
    )
    
    fig_methods.add_trace(
        go.Bar(
            y=df_methods['Usul'],
            x=df_methods['Keng_tarqalgan_%'],
            orientation='h',
            name='Keng tarqalganlik',
            marker_color='#3b82f6',
            text=df_methods['Keng_tarqalgan_%'],
            texttemplate='%{text}%',
            textposition='outside'
        ),
        row=1, col=1
    )
    
    fig_methods.add_trace(
        go.Bar(
            y=df_methods['Usul'],
            x=df_methods['Aniqlash_qiyinligi'],
            orientation='h',
            name='Qiyinlik',
            marker_color='#ef4444',
            text=df_methods['Aniqlash_qiyinligi'],
            texttemplate='%{text}/10',
            textposition='outside'
        ),
        row=1, col=2
    )
    
    fig_methods.update_layout(height=500, showlegend=False)
    st.plotly_chart(fig_methods, use_container_width=True)
    
    # Sektorlar bo'yicha
    st.subheader("🏭 Sektorlar Bo'yicha Yashirin Iqtisodiyot")
    
    sectors_shadow = {
        'Sektor': ['Qurilish', 'Savdo (chakana)', 'Qishloq xo\'jalik', 
                   'Xizmatlar (restoran)', 'Transport', 'San\'at va ko\'ngilochar',
                   'Moliya', 'Sanoat', 'IT va texnologiya'],
        'Yashirin_foiz': [28, 12, 69, 12, 18, 14, 5, 10, 8],
        'Xodimlar_ming': [450, 320, 890, 280, 195, 125, 45, 280, 85]
    }
    df_sectors = pd.DataFrame(sectors_shadow)
    
    fig_sectors = px.scatter(
        df_sectors,
        x='Yashirin_foiz',
        y='Xodimlar_ming',
        size='Yashirin_foiz',
        color='Yashirin_foiz',
        hover_data=['Sektor'],
        text='Sektor',
        title="Sektorlar: Yashirin Iqtisodiyot Ulushi va Xodimlar Soni",
        labels={'Yashirin_foiz': 'Yashirin faoliyat (%)', 'Xodimlar_ming': 'Xodimlar (ming)'},
        color_continuous_scale='Reds'
    )
    fig_sectors.update_traces(textposition='top center')
    fig_sectors.update_layout(height=500)
    st.plotly_chart(fig_sectors, use_container_width=True)
    
    # Konkret misollar
    st.subheader("📋 Real Hayotdan Misollar")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="highlight">', unsafe_allow_html=True)
        st.markdown("""
        ### 🏗️ Qurilish Sektori
        
        **Klassik sxema:**
        1. Ish beruvchi ishchilarni "stol ostida" yollaydi
        2. Ish haqi naqd pul bilan beriladi
        3. Hech qanday shartnoma imzolanmaydi
        4. Soliq e'lon qilinmaydi
        5. Ijtimoiy sug'urta to'lanmaydi
        
        **Natija:** 
        - Ish beruvchi: Soliq va sug'urta to'lamaydi (30-40% tejash)
        - Ishchi: Yuqori ish haqi oladi, lekin himoyasiz
        - Davlat: Yiliga $450 milliard yo'qotadi (jahon bo'yicha)
        
        ---
        
        ### 🍔 Restoran va Xizmatlar
        
        **Klassik sxema:**
        1. Tushumning bir qismini naqd qabul qilish
        2. Chek bermaslik yoki soxta chek berish
        3. Mahsulotlarni norasmiy sotib olish
        4. Xodimlarni qisman rasmiylashtirish
        
        **Misol:** 
        - Kunlik $1000 tushum: $600 rasmiy, $400 yashirin
        - Yiliga ~$145,000 soliq to'lanmaydi
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="highlight">', unsafe_allow_html=True)
        st.markdown("""
        ### 👨‍🌾 Qishloq Xo'jaligi
        
        **Klassik sxema:**
        1. Mahsulotni to'g'ridan-to'g'ri bozorda sotish
        2. Hech qanday hisob-kitob yuritmaslik
        3. Daromadni e'lon qilmaslik
        4. Ishchilarni rasmiylashtirmaslik
        
        **O'zbekistonda:**
        - 68.8% fermer xo'jaliklari norasmiy (2025)
        - Dehqon bozorlarida ~$5 mlrd/yil aylanma
        - Ko'pchilik operatsiyalar naqd pul bilan
        
        ---
        
        ### 🚕 Transport va Taksi
        
        **Klassik sxema:**
        1. Norasmiy taksi xizmati
        2. Naqd to'lovlar, cheksiz
        3. Ro'yxatdan o'tmaslik
        4. Soliq to'lamaslik
        
        **Misol:**
        - Kunlik 20 yo'lovchi × $3 = $60
        - Oylik $1,800, yilik $21,600
        - 0% soliq to'lanadi (bo'lishi kerak: ~$4,300)
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # O'lchash usullari
    st.subheader("📐 Yashirin Iqtisodiyotni O'lchash Usullari")
    
    measurement_methods = {
        'Usul': ['To\'g\'ridan-to\'g\'ri (so\'rovnoma)', 'Valyuta talabi', 
                 'Elektr energiya iste\'moli', 'Mehnat bozori', 
                 'MIMIC modeli', 'Milliy hisob farqlari'],
        'Aniqlik': [75, 60, 55, 50, 70, 65],
        'Xarajat': [8, 4, 3, 5, 6, 7],
        'Qo\'llanilishi': [65, 85, 70, 60, 80, 55]
    }
    df_measure = pd.DataFrame(measurement_methods)
    
    fig_measure = go.Figure()
    
    fig_measure.add_trace(go.Scatterpolar(
        r=df_measure['Aniqlik'],
        theta=df_measure['Usul'],
        fill='toself',
        name='Aniqlik',
        line_color='#3b82f6'
    ))
    
    fig_measure.add_trace(go.Scatterpolar(
        r=df_measure['Qo\'llanilishi'],
        theta=df_measure['Usul'],
        fill='toself',
        name='Qo\'llanilishi',
        line_color='#10b981'
    ))
    
    fig_measure.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=True,
        title="O'lchash Usullarining Samaradorligi",
        height=500
    )
    st.plotly_chart(fig_measure, use_container_width=True)
    
    st.markdown('<div class="highlight">', unsafe_allow_html=True)
    st.markdown("""
    ### 🔬 O'lchash Usullari Tavsifi:
    
    1. **To'g'ridan-to'g'ri (So'rovnoma):**
       - Uy xo'jaliklari va biznes so'rovlari
       - ✅ Batafsil ma'lumot
       - ❌ Kichik tanlov, xato ehtimolidir
    
    2. **Valyuta Talabi Yondashuvi:**
       - Naqd pul talabi va soliq yuki o'rtasidagi bog'liqlik
       - ✅ Keng qo'llaniladi
       - ❌ Barcha operatsiyalar naqd emas
    
    3. **Elektr Energiya Iste'moli:**
       - Energiya va YaIM o'rtasidagi farq
       - ✅ Oson ma'lumot
       - ❌ Boshqa omillar ta'sir qilishi mumkin
    
    4. **MIMIC Modeli:**
       - Ko'p ko'rsatkichlar va ko'p sabablar modeli
       - ✅ Keng qamrovli
       - ❌ Murakkab, xato ehtimolidir
    """)
    st.markdown('</div>', unsafe_allow_html=True)

elif analysis_type == "Umumiy Ko'rinish":
    st.header("🌍 Jahon Yashirin Iqtisodiyoti Dinamikasi")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Jahon tendentsiyasi
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(
            x=df_global['Yil'],
            y=df_global['Jahon_foiz'],
            mode='lines+markers',
            name='Jahon',
            line=dict(color='#3b82f6', width=3),
            marker=dict(size=10)
        ))
        fig1.add_trace(go.Scatter(
            x=df_global['Yil'],
            y=df_global['OECD_foiz'],
            mode='lines+markers',
            name='OECD',
            line=dict(color='#10b981', width=3),
            marker=dict(size=10)
        ))
        fig1.update_layout(
            title="Yashirin Iqtisodiyot Dinamikasi (% YaIM)",
            xaxis_title="Yil",
            yaxis_title="% YaIM",
            template="plotly_white",
            hovermode='x unified',
            height=400
        )
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        # Hajmi bo'yicha
        fig2 = go.Figure()
        fig2.add_trace(go.Bar(
            x=df_global['Yil'],
            y=df_global['Jahon_trillion'],
            name='Jahon hajmi',
            marker_color='#8b5cf6',
            text=df_global['Jahon_trillion'],
            texttemplate='$%{text:.1f}T',
            textposition='outside'
        ))
        fig2.update_layout(
            title="Yashirin Iqtisodiyot Hajmi (trillion $)",
            xaxis_title="Yil",
            yaxis_title="Trillion $",
            template="plotly_white",
            height=400
        )
        st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown('<div class="highlight">', unsafe_allow_html=True)
    st.markdown("""
    ### 🔍 Asosiy Xulosalar:
    - **2000-2023:** Yashirin iqtisodiyot 119 mamlakatda kamaydi (17.7% → 11.8%)
    - **Sabablari:** Raqamlashtirish, soliq islohotlari, davlat nazoratining kuchayishi
    - **2025 Prognoz:** 11.3% YaIM atrofida barqarorlashtirish kutilmoqda
    - **O'rtacha kamayish:** 6.7% YaIM (23 yil davomida)
    """)
    st.markdown('</div>', unsafe_allow_html=True)

elif analysis_type == "Mamlakatlar Taqqoslash":
    st.header("🗺️ Eng Yirik Yashirin Iqtisodiyotlar (2023-2025)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Hajm bo'yicha top-10
        fig3 = px.bar(
            df_countries.sort_values('Yashirin_trillion', ascending=True),
            y='Mamlakat',
            x='Yashirin_trillion',
            orientation='h',
            title="Yashirin Iqtisodiyot Hajmi (trillion $)",
            color='Yashirin_trillion',
            color_continuous_scale='Viridis',
            text='Yashirin_trillion'
        )
        fig3.update_traces(texttemplate='$%{text:.2f}T', textposition='outside')
        fig3.update_layout(height=500, showlegend=False)
        st.plotly_chart(fig3, use_container_width=True)
    
    with col2:
        # Foiz bo'yicha
        fig4 = px.bar(
            df_countries.sort_values('Foiz_YaIM', ascending=True),
            y='Mamlakat',
            x='Foiz_YaIM',
            orientation='h',
            title="Yashirin Iqtisodiyot Ulushi (% YaIM)",
            color='Foiz_YaIM',
            color_continuous_scale='RdYlGn_r',
            text='Foiz_YaIM'
        )
        fig4.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
        fig4.update_layout(height=500, showlegend=False)
        st.plotly_chart(fig4, use_container_width=True)
    
    # Jadval
    st.subheader("📋 Batafsil Ma'lumotlar")
    df_display = df_countries.copy()
    df_display['Yashirin_trillion'] = df_display['Yashirin_trillion'].apply(lambda x: f"${x:.2f}T")
    df_display['Foiz_YaIM'] = df_display['Foiz_YaIM'].apply(lambda x: f"{x:.1f}%")
    df_display['YaIM_trillion'] = df_display['YaIM_trillion'].apply(lambda x: f"${x:.2f}T")
    df_display.columns = ['Mamlakat', 'Yashirin Hajmi', 'YaIM %', 'Umumiy YaIM']
    st.dataframe(df_display, use_container_width=True, height=400)
    
    st.markdown('<div class="highlight">', unsafe_allow_html=True)
    st.markdown("""
    ### 💡 Tahlil:
    - **Xitoy:** $3.7T - dunyodagi eng katta (20% YaIM)
    - **AQSH:** $1.4T - ikkinchi o'rinda, lekin faqat 5% YaIM
    - **Hindiston:** 26% YaIM bilan eng yuqori nisbatga ega
    - **Rivojlangan mamlakatlar:** Germaniya (8.2%), Yaponiya (6.8%) - past ko'rsatkichlar
    """)
    st.markdown('</div>', unsafe_allow_html=True)

elif analysis_type == "O'zbekiston Tahlili":
    st.header("🇺🇿 O'zbekiston Yashirin Iqtisodiyoti")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # O'zbekiston dinamikasi
        fig5 = go.Figure()
        
        # Jami kuzatilmagan
        fig5.add_trace(go.Scatter(
            x=df_uzbekistan['Yil'],
            y=df_uzbekistan['Jami_kuzatilmagan'],
            mode='lines+markers',
            name='Jami Kuzatilmagan',
            line=dict(color='#ef4444', width=3),
            marker=dict(size=12)
        ))
        
        fig5.update_layout(
            title="O'zbekiston: Kuzatilmagan Iqtisodiyot Dinamikasi",
            xaxis_title="Yil",
            yaxis_title="% YaIM",
            template="plotly_white",
            hovermode='x unified',
            height=400
        )
        st.plotly_chart(fig5, use_container_width=True)
    
    with col2:
        # 2024-2025 tarkibi
        fig6 = go.Figure()
        
        years = ['2024', '2025 (9 oy)']
        shadow = [8.4, 7.7]
        informal = [26.4, 25.6]
        
        fig6.add_trace(go.Bar(name='Yashirin', x=years, y=shadow, marker_color='#f59e0b'))
        fig6.add_trace(go.Bar(name='Norasmiy', x=years, y=informal, marker_color='#06b6d4'))
        
        fig6.update_layout(
            title="Yashirin vs Norasmiy Iqtisodiyot",
            yaxis_title="% YaIM",
            barmode='stack',
            template="plotly_white",
            height=400
        )
        st.plotly_chart(fig6, use_container_width=True)
    
    # Sektorlar tahlili
    st.subheader("🏭 Sektorlar bo'yicha Kuzatilmagan Iqtisodiyot (2024-2025)")
    
    fig7 = go.Figure()
    
    fig7.add_trace(go.Bar(
        name='2024',
        x=df_sectors['Sektor'],
        y=df_sectors['2024_foiz'],
        marker_color='#8b5cf6',
        text=df_sectors['2024_foiz'],
        texttemplate='%{text:.1f}%',
        textposition='outside'
    ))
    
    fig7.add_trace(go.Bar(
        name='2025',
        x=df_sectors['Sektor'],
        y=df_sectors['2025_foiz'],
        marker_color='#10b981',
        text=df_sectors['2025_foiz'],
        texttemplate='%{text:.1f}%',
        textposition='outside'
    ))
    
    fig7.update_layout(
        barmode='group',
        yaxis_title="% YaIM qo'shilgan qiymatidan",
        template="plotly_white",
        height=400
    )
    st.plotly_chart(fig7, use_container_width=True)
    
    st.markdown('<div class="highlight">', unsafe_allow_html=True)
    st.markdown("""
    ### 📊 O'zbekiston: Asosiy Ko'rsatkichlar
    
    **2025 yil (9 oy) natijalari:**
    - Yashirin iqtisodiyot: **7.7% YaIM** (2024: 8.4%)
    - Norasmiy sektor: **25.6% YaIM** (2024: 26.4%)
    - Jami kuzatilmagan: **33.3% YaIM** (~$36.2 mlrd)
    
    **Yuqori nisbatlar:**
    - 🌾 Qishloq xo'jalik: 68.8%
    - 🏗️ Qurilish: 34.2%
    - 🛍️ Xizmatlar: 35.5%
    
    **Davlat choralari:**
    - 2024 yilda 16 trillion so'm "soyadan chiqarildi"
    - 15,000+ ish o'rni rasmiylashtirildi
    - 9,000+ tadbirkor ro'yxatdan o'tkazildi
    - **Maqsad:** 2030 yilga qadar yashirin iqtisodiyotni 2 baravarga kamaytirish
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Qo'shimcha metrikalar
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("🇺🇿 YaIM 2025 (9 oy)", "$108.7 mlrd", "+7.6%")
    
    with col2:
        st.metric("👥 Norasmiy bandlik", "~60% (2018-2019)", "Hozir kamaymoqda")
    
    with col3:
        st.metric("💼 Soliq to'lovchilar", "4.9M / 13.5M", "36% bandlardan")

elif analysis_type == "Yillar Dinamikasi":
    st.header("📈 Yillar Kesimida Qiyosiy Tahlil")
    
    # Global vs Uzbekistan
    fig8 = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Jahon Tendentsiyasi', 'OECD Mamlakatlari', 
                       'O\'zbekiston Jami', 'O\'zbekiston Yashirin'),
        specs=[[{"secondary_y": False}, {"secondary_y": False}],
               [{"secondary_y": False}, {"secondary_y": False}]]
    )
    
    # Jahon
    fig8.add_trace(
        go.Scatter(x=df_global['Yil'], y=df_global['Jahon_foiz'], 
                  name='Jahon', line=dict(color='#3b82f6', width=3)),
        row=1, col=1
    )
    
    # OECD
    fig8.add_trace(
        go.Scatter(x=df_global['Yil'], y=df_global['OECD_foiz'], 
                  name='OECD', line=dict(color='#10b981', width=3)),
        row=1, col=2
    )
    
    # O'zbekiston jami
    uz_years = [2022, 2023, 2024, 2025]
    uz_total = [45, 40, 34.8, 33.3]
    fig8.add_trace(
        go.Scatter(x=uz_years, y=uz_total, 
                  name='UZ Jami', line=dict(color='#ef4444', width=3)),
        row=2, col=1
    )
    
    # O'zbekiston yashirin
    uz_shadow_years = [2023, 2024, 2025]
    uz_shadow = [8.4, 8.4, 7.7]
    fig8.add_trace(
        go.Scatter(x=uz_shadow_years, y=uz_shadow, 
                  name='UZ Yashirin', line=dict(color='#f59e0b', width=3)),
        row=2, col=2
    )
    
    fig8.update_xaxes(title_text="Yil", row=1, col=1)
    fig8.update_xaxes(title_text="Yil", row=1, col=2)
    fig8.update_xaxes(title_text="Yil", row=2, col=1)
    fig8.update_xaxes(title_text="Yil", row=2, col=2)
    
    fig8.update_yaxes(title_text="% YaIM", row=1, col=1)
    fig8.update_yaxes(title_text="% YaIM", row=1, col=2)
    fig8.update_yaxes(title_text="% YaIM", row=2, col=1)
    fig8.update_yaxes(title_text="% YaIM", row=2, col=2)
    
    fig8.update_layout(height=700, showlegend=True, template="plotly_white")
    st.plotly_chart(fig8, use_container_width=True)
    
    # Yillik o'zgarishlar taqqoslash
    st.subheader("📊 Yillik O'zgarishlar Taqqoslash")
    
    comparison_data = {
        'Ko\'rsatkich': ['Jahon o\'rtacha', 'OECD o\'rtacha', 'Xitoy', 'AQSH', 'Hindiston', 'O\'zbekiston'],
        '2020': [13.2, 16.48, 20.5, 5.2, 27.0, None],
        '2021': [12.5, 16.07, 20.3, 5.1, 26.5, None],
        '2023': [11.8, 15.2, 20.0, 5.0, 26.0, 40.0],
        '2024': [11.5, 14.8, 19.8, 4.9, 25.8, 34.8],
        '2025': [11.3, 14.5, 19.5, 4.8, 25.5, 33.3]
    }
    
    df_comparison = pd.DataFrame(comparison_data)
    
    st.dataframe(
        df_comparison.style.background_gradient(cmap='RdYlGn_r', subset=['2020', '2021', '2023', '2024', '2025']),
        use_container_width=True,
        height=300
    )
    
    st.markdown('<div class="highlight">', unsafe_allow_html=True)
    st.markdown("""
    ### 🎯 Asosiy Xulosalar va Kelajak Prognozlari:
    
    **Jahon tendentsiyasi:**
    - 2000-2025: Yashirin iqtisodiyot 17.7% → 11.3% (36% kamayish)
    - Eng katta kamayish: Kam daromadli mamlakatlarda (-6.7% o'rtacha)
    - Barqaror davlatlar: 6-8% darajasida stabillashtirish
    
    **O'zbekiston:**
    - 2022-2025: Dramatik kamayish (45% → 33.3%)
    - Yashirin sektor: 8.4% → 7.7% (2024-2025)
    - **2030 Maqsad:** Yashirin iqtisodiyotni 2 baravarga kamaytirish
    
    **Sabablari:**
    - ✅ Raqamlashtirish va elektron to'lovlar
    - ✅ Soliq islohotlari va soddalashtirilgan tizim
    - ✅ Davlat nazoratining oshishi
    - ✅ Biznesni rasmiylashtirish dasturlari
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #64748b; padding: 20px;'>
    <p><strong>Ma'lumot manbalari:</strong></p>
    <p>EY Global Shadow Economy Report 2025 | O'zbekiston Davlat Statistika Qo'mitasi | 
    IMF Working Papers | World Bank | Eurasianet</p>
    <p style='margin-top: 10px;'>📅 Yangilangan: Dekabr 2025</p>
</div>
""", unsafe_allow_html=True)