# mis_app.py

import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="AP Solutions", layout="centered")

st.markdown("<h1 style='text-align: center;'>AP Solutions</h1>", unsafe_allow_html=True)

# Upload Excel File
uploaded_file = st.file_uploader("📁 Upload Excel file", type=["xlsx", "xls"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)
        st.success("✅ File uploaded successfully!")

        # Show column names and shape
        st.markdown("### 📊 File Info:")
        st.write(f"**Columns:** {', '.join(df.columns)}")
        st.write(f"**Shape:** {df.shape[0]} rows x {df.shape[1]} columns")

        # Chat-style box for info
        with st.expander("🔍 View Data"):
            st.dataframe(df)

        # Text area for prompt
        prompt = st.text_area("📝 Add prompt (Steps to generate MIS or report)")

        if prompt:
            st.markdown("### ⚙️ Generated Script (simulated):")
            script = f"# This is a simulated Python script for:\n# {prompt}\n\n# Example: Filter or group data\n# final_df = df.groupby('Column').sum()"
            st.code(script, language='python')

            confirm = st.button("✅ Confirm & Run Script")

            if confirm:
                try:
                    # Simulate some output (you can replace with actual logic later)
                    output_df = df.copy()
                    output_df["DummyColumn"] = "Processed"

                    # Generate downloadable Excel
                    output = io.BytesIO()
                    with pd.ExcelWriter(output, engine='openpyxl') as writer:
                        output_df.to_excel(writer, index=False, sheet_name='MIS Report')

                    st.success("✅ MIS Report Generated!")

                    st.download_button(
                        label="📥 Download MIS Report",
                        data=output.getvalue(),
                        file_name="MIS_Report.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )

                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")

    except Exception as e:
        st.error(f"❌ Failed to read the Excel file: {str(e)}")