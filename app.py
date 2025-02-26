import streamlit as st

def bayes_theorem(prior, sensitivity, specificity):
    false_positive_rate = 1 - specificity  # Correct interpretation
    p_positive = (sensitivity * prior) + (false_positive_rate * (1 - prior))
    posterior = (sensitivity * prior) / p_positive
    return posterior

st.title("COVID-19 Test Bayesian Calculator")

# User Inputs with Sliders and Number Inputs
prior = st.number_input("Prevalence of COVID-19 in the community (Prior Probability)", 0.0, 1.0, 0.04, 0.01)
prior = st.slider("Adjust Prevalence", 0.0, 1.0, prior, 0.01)

sensitivity = st.number_input("Test Sensitivity (True Positive Rate)", 0.0, 1.0, 0.73, 0.01)
sensitivity = st.slider("Adjust Sensitivity", 0.0, 1.0, sensitivity, 0.01)

specificity = st.number_input("Test Specificity (True Negative Rate)", 0.0, 1.0, 0.95, 0.01)
specificity = st.slider("Adjust Specificity", 0.0, 1.0, specificity, 0.01)

false_positive_rate = 1 - specificity  # Clarify dependency

if specificity == 0:
    st.error("Specificity cannot be zero.")
else:
    posterior = bayes_theorem(prior, sensitivity, specificity)
    st.write(f"# The probability of having COVID-19 given a positive test result is: {posterior:.4f} ({posterior*100:.2f}%)")