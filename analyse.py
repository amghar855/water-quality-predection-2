# analyse.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# لتحسين المظهر داخل ستريملت
sns.set_style('whitegrid')

@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    return df

def show_overview(df):
    st.subheader(" Aperçu des données")
    st.dataframe(df.head())

    st.subheader(" Description statistique")
    st.dataframe(df.describe())

    st.subheader(" Valeurs manquantes")
    st.dataframe(df.isnull().sum())

def plot_distributions(df):
    st.subheader(" Distribution des variables")
    num_cols = df.select_dtypes(include='number').columns

    for col in num_cols:
        fig, ax = plt.subplots()
        sns.histplot(df[col], kde=True, ax=ax, bins=30, color='skyblue')
        ax.set_title(f'Distribution de {col}')
        st.pyplot(fig)

def plot_correlation_heatmap(df):
    st.subheader(" Heatmap de corrélation")
    corr = df.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', ax=ax)
    st.pyplot(fig)

def plot_boxplots(df):
    st.subheader(" Boxplots selon la variable cible")
    target_col = "is_safe"
    
    if target_col in df.columns:
        features = df.drop(columns=[target_col]).select_dtypes(include='number').columns
        for col in features:
            fig, ax = plt.subplots()
            sns.boxplot(data=df, x=target_col, y=col, palette='Set2', ax=ax)
            ax.set_title(f'Boxplot de {col} par {target_col}')
            st.pyplot(fig)
    else:
        st.warning(f"La colonne cible '{target_col}' n'existe pas dans le DataFrame.")

def run_analysis_app():
    st.title(" Analyse des données de qualité de l'eau")

    data_path = "waterQuality1.csv"
    df = load_data(data_path)

    show_overview(df)
    plot_distributions(df)
    plot_correlation_heatmap(df)
    plot_boxplots(df)
