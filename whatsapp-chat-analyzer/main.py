import streamlit as st
import chat_state
import utils
import matplotlib.pyplot as plt

st.sidebar.title("WhatsApp Chat Analyzer")

# File Upload Mechanism
uploaded_file = st.sidebar.file_uploader("Upload an exported WhatsApp Chat (.txt)", type=["txt"])

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    
    # Using the new chat_state module
    df = chat_state.preprocess(data)
    
    user_list = df['user'].unique().tolist()
    if 'group_notification' in user_list:
        user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, "Overall")
    
    selected_user = st.sidebar.selectbox("Show Analysis for", user_list)
    
    if st.sidebar.button("Show Analysis"):
        
        # Using the new utils module
        num_messages, words, num_media_messages, num_links = utils.fetch_stats(selected_user, df)
        st.title("Top Statistics")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(words)
        with col3:
            st.header("Media Shared")
            st.title(num_media_messages)
        with col4:
            st.header("Links Shared")
            st.title(num_links)

        if selected_user == 'Overall':
            st.title('Most Active Users')
            x, new_df = utils.most_busy_users(df)
            fig, ax = plt.subplots()
            
            col1, col2 = st.columns(2)
            with col1:
                ax.bar(x.index, x.values, color='red')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)

        st.title('Most Common Words')
        most_common_df = utils.most_common_words(selected_user, df)
        
        fig, ax = plt.subplots()
        ax.barh(most_common_df[0], most_common_df[1])
        plt.xticks(rotation='vertical')
        st.pyplot(fig)