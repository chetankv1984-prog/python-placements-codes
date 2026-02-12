import streamlit as st

st.title("Password Validation and Encryption")

password = st.text_input("Enter the password", type="password")

if st.button("Validate and encrypt"):

    if password == "":
        st.warning("Please enter password")

    elif len(password) < 8:
        st.error("Password must be at least 8 characters")

    elif password[0] not in "12345":
        st.error("The first character must be in 1-5 range")

    elif not password.isalnum():
        st.error("Password must contain only alphabets and numbers")

    else:
        has_upper = any(i.isupper() for i in password)
        has_lower = any(i.islower() for i in password)

        if not (has_upper and has_lower):
            st.error("Must contain at least 1 uppercase and 1 lowercase letter")

        else:
            encrypted_password = (
                password.replace("A", "@")
                        .replace("a", "B")
                        .replace("b", "1")
            )

            st.success("Thank you for entering valid password ✅")
            st.write("The encrypted Password:")
            st.code(encrypted_password)