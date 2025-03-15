import streamlit as st

# For optional charting/visuals:
import plotly.graph_objects as go

def main():
    st.title("Ethical Propensity Score Dashboard")
    st.write("""
    This dashboard calculates key metrics (Bias Index, Transparency Score, etc.) 
    and provides an overall Ethical Propensity Score (EPS) for AI-driven hiring.
    """)

    # --- Section 1: User Inputs ---
    st.header("1. Enter Your Data")

    col1, col2 = st.columns(2)
    
    with col1:
        total_decisions = st.number_input("Total AI Decisions", min_value=1, value=1)
        bias_complaints = st.number_input("Number of Bias Complaints", min_value=0, value=0)
        explainable_ai = st.number_input("Explainable AI Decisions", min_value=0, value=0)
        human_reviewed = st.number_input("Human-Reviewed Decisions", min_value=0, value=0)
        data_transactions = st.number_input("Total Data Transactions", min_value=1, value=1)
    with col2:
        policy_violations = st.number_input("Policy Violations Detected", min_value=0, value=0)
        diverse_hires = st.number_input("Number of Diverse Hires", min_value=0, value=0)
        total_hires = st.number_input("Total Hires", min_value=1, value=1)
        positive_feedback = st.number_input("Positive Feedback (count)", min_value=0, value=0)
        total_feedback = st.number_input("Total Feedback (count)", min_value=1, value=1)

    # --- Section 2: Calculations ---
    st.header("2. Calculations")

    # 1. Bias Index
    bias_index = (bias_complaints / total_decisions) * 100

    # 2. Transparency Score
    transparency_score = (explainable_ai / total_decisions) * 100

    # 3. Accountability Index
    accountability_index = (human_reviewed / total_decisions) * 100

    # 4. Privacy Compliance Score
    privacy_compliance = ((data_transactions - policy_violations) / data_transactions) * 100

    # 5. Fairness Index
    fairness_index = (diverse_hires / total_hires) * 100

    # 6. Stakeholder Sentiment
    stakeholder_sentiment = (positive_feedback / total_feedback) * 100

    # Weighted average (example weights)
    # Feel free to adjust these weights as needed
    weights_sum = 15 + 10 + 10 + 10 + 15 + 10  # 70
    eps = (
        (bias_index * 15) +
        (transparency_score * 10) +
        (accountability_index * 10) +
        (privacy_compliance * 10) +
        (fairness_index * 15) +
        (stakeholder_sentiment * 10)
    ) / weights_sum

    # --- Section 3: Display Metrics ---
    st.header("3. Metrics & EPS Result")
    st.write("Below are the individual metric results and the overall Ethical Propensity Score (EPS).")

    colA, colB, colC = st.columns(3)
    colA.metric("Bias Index (%)", f"{bias_index:.2f}")
    colA.metric("Transparency Score (%)", f"{transparency_score:.2f}")
    colB.metric("Accountability Index (%)", f"{accountability_index:.2f}")
    colB.metric("Privacy Compliance (%)", f"{privacy_compliance:.2f}")
    colC.metric("Fairness Index (%)", f"{fairness_index:.2f}")
    colC.metric("Stakeholder Sentiment (%)", f"{stakeholder_sentiment:.2f}")

    # Display EPS in a gauge chart using Plotly (optional)
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = eps,
        title = {'text': "Ethical Propensity Score (EPS)"},
        gauge = {
            'axis': {'range': [0, 100]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 40], 'color': "red"},
                {'range': [40, 70], 'color': "yellow"},
                {'range': [70, 100], 'color': "green"}
            ],
        }
    ))
    st.plotly_chart(fig, use_container_width=True)

    st.success(f"Your current Ethical Propensity Score (EPS) is: {eps:.2f} / 100")

    # --- Section 4: Recommendations (example logic) ---
    st.header("4. Recommendations")
    if eps < 40:
        st.error("Your EPS is critically low. Consider immediate bias audits and compliance checks.")
    elif eps < 70:
        st.warning("Your EPS is moderate. You may need to refine data collection, improve oversight, and enhance transparency.")
    else:
        st.info("Your EPS is strong! Maintain best practices to ensure ongoing fairness and compliance.")

if __name__ == "__main__":
    main()
