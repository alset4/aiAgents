import streamlit as st

if st.button("Generate Presentation", type="secondary"):
                with st.spinner("Generating presentation..."):
                    creator_name = youtube_name or tiktok_name
                    presentation_generator = PresentationGenerator()
                    presentation_bytes = presentation_generator.create_content_creator_presentation(
                        st.session_state.analysis_results,
                        creator_name=creator_name
                    )
                    
                    if isinstance(presentation_bytes, dict) and "error" in presentation_bytes:
                        st.error(f"Failed to generate presentation: {presentation_bytes['error']}")
                    else:
                        # Generate download link
                        download_link = presentation_generator.get_download_link(presentation_bytes)
                        
                        # Display success message and download button
                        st.success("Presentation generated successfully!")
                        st.session_state.presentation_generated = True
                        
                        # Create a download button
                        st.download_button(
                            label="Download Presentation",
                            data=presentation_bytes,
                            file_name=f"content_analysis_{creator_name.replace('@', '')}.pptx" if creator_name else "content_analysis.pptx",
                            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
                        )
                        
                        # Show preview message
                        st.info("Your presentation contains detailed statistics and optimization suggestions. Click the button above to download it.")