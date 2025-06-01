# app.py
import streamlit as st
from bank import Bank

Bank.load_data()

st.set_page_config(page_title="Sunrise Bank Limited", page_icon="🏦")

st.title("🏦 Sunrise Bank Limited")
menu = [
    "Create Account", "Deposit Money", "Withdraw Money", 
    "Check Details", "Update Details", "Delete Account"
]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Create Account":
    st.header("Create a New Account")
    with st.form("create_account"):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0, step=1)
        email = st.text_input("Email")
        address = st.text_input("Address")
        tpin = st.text_input("Set 4-digit Transaction Pin", max_chars=4)
        submit = st.form_submit_button("Create Account")
    if submit:
        if not (name and email and address and tpin):
            st.error("All fields are required!")
        elif not tpin.isdigit() or len(tpin) != 4:
            st.error("TPin must be 4 digits.")
        else:
            ok, result = Bank.create_account(name, int(age), email, address, int(tpin))
            if ok:
                st.success(f"Account Created! Your Account Number: {result}")
            else:
                st.error(result)

elif choice == "Deposit Money":
    st.header("Deposit Money")
    acc = st.text_input("Account Number")
    tpin = st.text_input("Transaction Pin", type="password", max_chars=4)
    amount = st.number_input("Amount to Deposit", min_value=1, max_value=10000)
    if st.button("Deposit"):
        ok, msg = Bank.deposit_money(acc, int(tpin), amount)
        st.success(msg) if ok else st.error(msg)

elif choice == "Withdraw Money":
    st.header("Withdraw Money")
    acc = st.text_input("Account Number")
    tpin = st.text_input("Transaction Pin", type="password", max_chars=4)
    amount = st.number_input("Amount to Withdraw", min_value=1, max_value=10000)
    if st.button("Withdraw"):
        ok, msg = Bank.withdraw_money(acc, int(tpin), amount)
        st.success(msg) if ok else st.error(msg)

elif choice == "Check Details":
    st.header("Account Details")
    acc = st.text_input("Account Number")
    tpin = st.text_input("Transaction Pin", type="password", max_chars=4)
    if st.button("Show Details"):
        details = Bank.get_details(acc, int(tpin))
        if details:
            st.json(details)
        else:
            st.error("Account not found or wrong credentials.")

elif choice == "Update Details":
    st.header("Update Account Details")
    acc = st.text_input("Account Number")
    tpin = st.text_input("Transaction Pin", type="password", max_chars=4)
    if st.button("Fetch Details"):
        user = Bank.get_details(acc, int(tpin))
        if not user:
            st.error("Account not found or wrong credentials.")
        else:
            st.session_state["user_update"] = user

    if "user_update" in st.session_state:
        user = st.session_state["user_update"]
        with st.form("update_details"):
            name = st.text_input("New Name", value=user['name'])
            email = st.text_input("New Email", value=user['Email'])
            address = st.text_input("New Address", value=user['Address'])
            tpin_new = st.text_input("New TPin (4 digits)", value=str(user['Transaction_Pin']))
            submit = st.form_submit_button("Update")
        if submit:
            ok, msg = Bank.update_details(
                acc, int(tpin),
                name=name,
                Email=email,
                Address=address,
                Transaction_Pin=int(tpin_new) if tpin_new.isdigit() and len(tpin_new)==4 else None
            )
            st.success(msg) if ok else st.error(msg)

elif choice == "Delete Account":
    st.header("Delete Account")
    acc = st.text_input("Account Number")
    tpin = st.text_input("Transaction Pin", type="password", max_chars=4)
    if st.button("Delete Account"):
        ok, msg = Bank.delete_account(acc, int(tpin))
        st.success(msg) if ok else st.error(msg)
