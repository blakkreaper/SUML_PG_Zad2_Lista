import streamlit as st
import uuid

# Tytuł aplikacji
st.title('Lista Zakupów')

# Inicjalizacja sesji (do przechowywania listy zakupów)
if 'shopping_list' not in st.session_state:
    st.session_state.shopping_list = []

# Funkcja do dodawania nowego produktu z ilością i jednostką
def add_product(name, quantity, unit):
    st.session_state.shopping_list.append({
        "id": str(uuid.uuid4()),  # Generowanie unikalnego ID
        "name": name,
        "quantity": quantity,
        "unit": unit
    })

# Funkcja do usuwania produktu
def remove_product(product_id):
    st.session_state.shopping_list = [product for product in st.session_state.shopping_list if product["id"] != product_id]

# Pola do wprowadzania nowego produktu, jego ilości i wyboru jednostki
new_product_name = st.text_input('Nazwa produktu', '')
new_product_quantity = st.number_input('Ilość', min_value=0.01, step=0.01, format="%.2f")
new_product_unit = st.selectbox('Jednostka', ('kg', 'l', 'ml', 'g', 'sztuk'))

# Przycisk do dodawania produktu
if st.button('Dodaj do listy'):
    if new_product_name:
        add_product(new_product_name, new_product_quantity, new_product_unit)
        st.success(f'Dodano "{new_product_name}" do listy zakupów.')
    else:
        st.error('Wpisz nazwę produktu.')

# Wyświetlanie aktualnej listy zakupów z przyciskami do usuwania
st.write('Twoja aktualna lista zakupów:')
for product in st.session_state.shopping_list:
    col1, col2 = st.columns([4, 1])
    with col1:
        st.write(f"- {product['name']} ({product['quantity']} {product['unit']})")
    with col2:
        remove_button = st.button("Usuń", key=product["id"])
    if remove_button:
        remove_product(product["id"])
        st.experimental_rerun()
