import streamlit as st
import requests

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Fraud Detection System",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# API
# =========================================================

API_URL = "https://fraud-detection-api-29f55a6c.fastapicloud.dev/predict"

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
}

.hero {
    padding: 25px 30px;
    border-radius: 18px;
    margin-bottom: 25px;
    border: 1px solid rgba(128,128,128,0.25);
}

.hero h1 {
    margin-bottom: 5px;
    font-size: 38px;
}

.hero p {
    margin-top: 0;
    font-size: 17px;
    opacity: 0.75;
}

.section-title {
    font-size: 22px;
    font-weight: 700;
    margin-top: 15px;
    margin-bottom: 15px;
}

.result-box {
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    margin-top: 20px;
    border: 1px solid rgba(128,128,128,0.25);
}

.result-box h2 {
    font-size: 30px;
    margin-bottom: 8px;
}

.risk-text {
    font-size: 18px;
    margin-top: 8px;
}

.footer {
    text-align: center;
    margin-top: 40px;
    padding: 20px;
    opacity: 0.55;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="hero">
    <h1>🛡️ Fraud Detection System</h1>
    <p>AI-powered transaction risk analysis using a Machine Learning model</p>
</div>
""", unsafe_allow_html=True)

# =========================================================
# TRANSACTION INFORMATION
# =========================================================

st.markdown(
    '<div class="section-title">💳 Transaction Information</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:

    amount = st.number_input(
        "Transaction Amount",
        min_value=0.0,
        value=100.0,
        step=10.0
    )

    account_age_days = st.number_input(
        "Account Age (Days)",
        min_value=0,
        value=365
    )

    total_transactions_user = st.number_input(
        "Total User Transactions",
        min_value=0,
        value=50
    )

with col2:

    avg_amount_user = st.number_input(
        "User Average Amount",
        min_value=0.0,
        value=150.0,
        step=10.0
    )

    shipping_distance_km = st.number_input(
        "Shipping Distance (km)",
        min_value=0.0,
        value=10.0,
        step=10.0
    )

    country = st.selectbox(
        "Country",
        ["US", "GB", "FR", "DE", "IT", "ES", "NL", "PL", "RO", "TR"]
    )

with col3:

    bin_country = st.selectbox(
        "BIN Country",
        ["US", "GB", "FR", "DE", "IT", "ES", "NL", "PL", "RO", "TR"]
    )

    channel = st.selectbox(
        "Channel",
        ["online", "offline"]
    )

    merchant_category = st.selectbox(
        "Merchant Category",
        ["electronics", "fashion", "grocery", "travel", "other"]
    )

# =========================================================
# SECURITY INFORMATION
# =========================================================

st.divider()

st.markdown(
    '<div class="section-title">🔐 Security Information</div>',
    unsafe_allow_html=True
)

col4, col5, col6, col7 = st.columns(4)

with col4:
    promo_used = st.selectbox(
        "Promo Used",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

with col5:
    avs_match = st.selectbox(
        "AVS Match",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

with col6:
    cvv_result = st.selectbox(
        "CVV Result",
        [0, 1],
        format_func=lambda x: "Valid" if x == 1 else "Invalid"
    )

with col7:
    three_ds_flag = st.selectbox(
        "3D Secure",
        [0, 1],
        format_func=lambda x: "Enabled" if x == 1 else "Disabled"
    )

# =========================================================
# TRANSACTION TIME
# =========================================================

st.divider()

st.markdown(
    '<div class="section-title">🕒 Transaction Time</div>',
    unsafe_allow_html=True
)

col8, col9, col10, col11 = st.columns(4)

with col8:
    transaction_hour = st.number_input(
        "Transaction Hour",
        min_value=0,
        max_value=23,
        value=12
    )

with col9:
    transaction_dayofweek = st.number_input(
        "Day of Week",
        min_value=0,
        max_value=6,
        value=1
    )

with col10:
    transaction_month = st.number_input(
        "Transaction Month",
        min_value=1,
        max_value=12,
        value=8
    )

with col11:
    is_weekend = st.selectbox(
        "Is Weekend",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

# =========================================================
# PREDICTION
# =========================================================

st.divider()

if st.button(
    "🔍 Analyze Transaction",
    use_container_width=True,
    type="primary"
):

    payload = {

        "account_age_days": account_age_days,
        "total_transactions_user": total_transactions_user,
        "avg_amount_user": avg_amount_user,
        "amount": amount,

        "country": country,
        "bin_country": bin_country,
        "channel": channel,
        "merchant_category": merchant_category,

        "shipping_distance_km": shipping_distance_km,

        "promo_used": promo_used,
        "avs_match": avs_match,
        "cvv_result": cvv_result,
        "three_ds_flag": three_ds_flag,

        "transaction_hour": transaction_hour,
        "transaction_dayofweek": transaction_dayofweek,
        "transaction_month": transaction_month,
        "is_weekend": is_weekend
    }

    with st.spinner("Analyzing transaction..."):

        try:

            response = requests.post(
                API_URL,
                json=payload,
                timeout=30
            )

            if response.status_code == 200:

                result = response.json()

                prediction = result.get("prediction")
                risk_probability = result.get("risk_probability")

                risk_percent = risk_probability * 100

                st.divider()

                st.markdown(
                    '<div class="section-title">📊 Analysis Result</div>',
                    unsafe_allow_html=True
                )

                # -----------------------------------------
                # FRAUD
                # -----------------------------------------

                if prediction == 1:

                    st.markdown(
                        f"""
                        <div class="result-box">
                            <h2>🚨 FRAUD DETECTED</h2>
                            <div class="risk-text">
                                High Risk Transaction
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    st.metric(
                        "Risk Probability",
                        f"{risk_percent:.2f}%"
                    )

                    st.progress(
                        min(risk_probability, 1.0)
                    )

                    st.error(
                        "This transaction has been classified as potentially fraudulent."
                    )

                # -----------------------------------------
                # NOT FRAUD
                # -----------------------------------------

                else:

                    if risk_percent >= 50:
                        risk_level = "Medium Risk"
                    else:
                        risk_level = "Low Risk"

                    st.markdown(
                        f"""
                        <div class="result-box">
                            <h2>✅ NOT FRAUD</h2>
                            <div class="risk-text">
                                {risk_level} Transaction
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    st.metric(
                        "Risk Probability",
                        f"{risk_percent:.2f}%"
                    )

                    st.progress(
                        min(risk_probability, 1.0)
                    )

                    if risk_percent >= 50:
                        st.warning(
                            "The transaction is classified as not fraud, "
                            "but the risk probability is relatively high."
                        )
                    else:
                        st.success(
                            "The transaction appears to have a low fraud risk."
                        )

                # -----------------------------------------
                # SUMMARY
                # -----------------------------------------

                st.divider()

                st.markdown(
                    '<div class="section-title">📋 Transaction Summary</div>',
                    unsafe_allow_html=True
                )

                s1, s2, s3, s4 = st.columns(4)

                s1.metric(
                    "Amount",
                    f"{amount:.2f}"
                )

                s2.metric(
                    "Country",
                    country
                )

                s3.metric(
                    "Channel",
                    channel
                )

                s4.metric(
                    "Distance",
                    f"{shipping_distance_km:.0f} km"
                )

            else:

                st.error(
                    f"API Error: {response.status_code}"
                )

                st.code(
                    response.text
                )

        except requests.exceptions.RequestException as e:

            st.error(
                "Unable to connect to the Fraud Detection API."
            )

            st.write(str(e))

# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        🛡️ Fraud Detection System • Machine Learning + FastAPI + Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
