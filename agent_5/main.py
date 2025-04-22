import streamlit as st
import requests
from presentation import PresentationGenerator
from get_info import ContentCreatorStats

st.title("AI Agent for YouTubers and TikTokers")

youtube_name = st.text_input("Enter YouTube Username")
tiktok_name = st.text_input("Enter TikTok Username")

# Use fixed SlidesGPT API Key for all queries
api_key = "fta7mccn1iyq2za998rnv7uj83e7pnvz"

if "analysis_results" not in st.session_state:
    st.session_state.analysis_results = {}

creator_name = youtube_name or tiktok_name

if creator_name:
    st.write(f"Creating content for: {creator_name}")

if st.button("Generate Presentation", type="secondary"):
    with st.spinner("Gathering data and generating presentation via SlidesGPT API..."):
        # Step 1: Pull info from get_info.py
        stats = ContentCreatorStats()
        analysis_results = stats.analyze_content_creator(youtube_name=youtube_name, tiktok_name=tiktok_name)
        st.session_state.analysis_results = analysis_results

        # Step 2: Prepare SlidesGPT prompt
        prompt = f"""
Create a visually appealing presentation for a content creator.

Creator Name: {creator_name}\n\n"""
        if analysis_results.get('youtube'):
            prompt += f"YouTube Stats:\n"
            for k, v in analysis_results['youtube'].items():
                prompt += f"- {k.replace('_', ' ').title()}: {v}\n"
        if analysis_results.get('tiktok'):
            prompt += f"\nTikTok Stats:\n"
            for k, v in analysis_results['tiktok'].items():
                prompt += f"- {k.replace('_', ' ').title()}: {v}\n"
        if analysis_results.get('suggestions'):
            prompt += f"\nSuggestions:\n"
            for s in analysis_results['suggestions']:
                prompt += f"- {s}\n"
        prompt += "\nMake the slides modern, clean, and visually engaging. Include a summary, detailed stats, suggestions, and a next steps slide."

        # Step 3: Call SlidesGPT API
        try:
            response = requests.post(
                "https://api.slidesgpt.com/v1/presentations/generate",
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json"
                },
                json={"prompt": prompt},
                timeout=20  # Reduced timeout
            )
            st.write(f"SlidesGPT API status code: {response.status_code}")
            if response.status_code == 200:
                data = response.json()
                embed_url = data.get("embed")
                download_url = data.get("download")
                pres_id = data.get("id")

                st.success("Presentation generated!")
                if embed_url:
                    st.markdown(f"[Preview Presentation]({embed_url})", unsafe_allow_html=True)
                    st.components.v1.iframe(embed_url, height=400)
                if download_url:
                    st.markdown(f"[Download PPTX]({download_url})", unsafe_allow_html=True)
                else:
                    st.info("Download link not available.")
            else:
                st.error(f"SlidesGPT API error: {response.status_code} {response.text}")
                st.write(f"Response content: {response.content}")
        except requests.Timeout:
            st.error("SlidesGPT API timed out. Please try again later or check your network connection.")
        except Exception as e:
            st.error(f"Error calling SlidesGPT API: {e}")

        # (Optional) Still allow download of pptx via PresentationGenerator if user wants
        presentation_generator = PresentationGenerator()
        presentation_bytes = presentation_generator.create_content_creator_presentation(
            analysis_results,
            creator_name=creator_name
        )
        if not (isinstance(presentation_bytes, dict) and "error" in presentation_bytes):
            st.download_button(
                label="Download PowerPoint (Local Generation)",
                data=presentation_bytes,
                file_name=f"content_analysis_{creator_name.replace('@', '')}.pptx" if creator_name else "content_analysis.pptx",
                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
            )
        else:
            st.info("You can also generate a PowerPoint using the SlidesGPT API above.")